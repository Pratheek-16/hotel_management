from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum
from .models import Customer, Hotel, Room, RoomCategory, Reservation, Payment
from .email_utils import (send_registration_email, send_reservation_email,
                          send_payment_email, send_cancellation_email,
                          send_status_update_email)
import datetime
import json


# 🏠 Home Page
def home(request):
    return render(request, 'home.html')


# 🔐 Login
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "admin" and password == "admin123":
            request.session['logged_in'] = True
            return redirect('/dashboard/')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')


def logout(request):
    request.session.flush()
    return redirect('/login/')


# 🔒 Login required helper
def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('logged_in'):
            return redirect('/login/')
        return view_func(request, *args, **kwargs)
    return wrapper


# 📊 Dashboard — with Chart.js data
@login_required
def dashboard(request):
    total_customers = Customer.objects.count()
    total_rooms = Room.objects.count()
    available_rooms = Room.objects.filter(Status='Available').count()
    total_reservations = Reservation.objects.count()
    total_revenue = sum(p.Amount for p in Payment.objects.all())

    # ── Revenue by Month (last 6 months) ──
    today = datetime.date.today()
    revenue_labels = []
    revenue_data = []
    for i in range(5, -1, -1):
        month_date = today.replace(day=1) - datetime.timedelta(days=i * 30)
        label = month_date.strftime('%b %Y')
        revenue_labels.append(label)
        month_total = Payment.objects.filter(
            Payment_Date__year=month_date.year,
            Payment_Date__month=month_date.month
        ).aggregate(total=Sum('Amount'))['total'] or 0
        revenue_data.append(float(month_total))

    # ── Bookings by Month (last 6 months) ──
    bookings_labels = []
    bookings_data = []
    for i in range(5, -1, -1):
        month_date = today.replace(day=1) - datetime.timedelta(days=i * 30)
        label = month_date.strftime('%b %Y')
        bookings_labels.append(label)
        count = Reservation.objects.filter(
            Check_In_Date__year=month_date.year,
            Check_In_Date__month=month_date.month
        ).count()
        bookings_data.append(count)

    # ── Occupancy Rate ──
    occupied_rooms = Room.objects.filter(Status='Occupied').count()
    occupancy_rate = round((occupied_rooms / total_rooms * 100), 1) if total_rooms else 0

    # ── Reservation Status Breakdown ──
    status_counts = {
        'Pending': Reservation.objects.filter(Status='Pending').count(),
        'Confirmed': Reservation.objects.filter(Status='Confirmed').count(),
        'Checked In': Reservation.objects.filter(Status='Checked In').count(),
        'Checked Out': Reservation.objects.filter(Status='Checked Out').count(),
        'Cancelled': Reservation.objects.filter(Status='Cancelled').count(),
    }

    return render(request, 'dashboard.html', {
        'total_customers': total_customers,
        'total_rooms': total_rooms,
        'available_rooms': available_rooms,
        'total_reservations': total_reservations,
        'total_revenue': total_revenue,
        'occupancy_rate': occupancy_rate,
        # Chart data as JSON
        'revenue_labels': json.dumps(revenue_labels),
        'revenue_data': json.dumps(revenue_data),
        'bookings_labels': json.dumps(bookings_labels),
        'bookings_data': json.dumps(bookings_data),
        'status_labels': json.dumps(list(status_counts.keys())),
        'status_data': json.dumps(list(status_counts.values())),
        'occupancy_data': json.dumps([occupied_rooms, available_rooms]),
    })


# 👤 Customers
@login_required
def customers(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        country = request.POST.get('country', '').strip()

        if not all([name, email, phone, country]):
            messages.error(request, "All fields are required.")
        else:
            Customer.objects.create(Name=name, Email=email, Phone=phone, Country=country)
            email_sent = send_registration_email(name, email, phone, country)
            if email_sent:
                messages.success(request, f"Customer '{name}' registered! Confirmation email sent to {email}.")
            else:
                messages.warning(request, f"Customer '{name}' registered, but the confirmation email could not be sent.")

    data = Customer.objects.all()
    return render(request, 'customer.html', {'data': data})


# 🏨 Hotels
@login_required
def hotels(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        location = request.POST.get('location', '').strip()
        if not all([name, location]):
            messages.error(request, "Both fields are required.")
        else:
            Hotel.objects.create(Name=name, Location=location)
            messages.success(request, f"Hotel '{name}' added successfully!")
    data = Hotel.objects.all()
    return render(request, 'hotels.html', {'data': data})


# 🛏 Rooms
@login_required
def rooms(request):
    if request.method == "POST":
        hotel = request.POST.get('hotel')
        category = request.POST.get('category')
        status = request.POST.get('status')
        Room.objects.create(Hotel_ID=hotel, Category_ID=category, Status=status)
        messages.success(request, "Room added successfully!")
    data = Room.objects.all()
    hotels_list = Hotel.objects.all()
    categories = RoomCategory.objects.all()
    return render(request, 'rooms.html', {'data': data, 'hotels': hotels_list, 'categories': categories})


# 📅 Reservation — with Status tracking + Cancellation
@login_required
def reservation(request):
    if request.method == "POST":
        action = request.POST.get('action', 'create')

        # ── Update Status ──
        if action == 'update_status':
            res_id = request.POST.get('reservation_id')
            new_status = request.POST.get('new_status')
            try:
                res = Reservation.objects.get(Reservation_ID=res_id)
                res.Status = new_status
                res.save()

                # Send status update email
                try:
                    customer = Customer.objects.get(Cus_ID=res.Cus_ID)
                    send_status_update_email(
                        customer_name=customer.Name,
                        customer_email=customer.Email,
                        reservation_id=res.Reservation_ID,
                        new_status=new_status,
                        checkin=res.Check_In_Date,
                        checkout=res.Check_Out_Date,
                        room_id=res.Room_ID,
                    )
                except Exception:
                    pass

                messages.success(request, f"Reservation #{res_id} status updated to '{new_status}'.")
            except Reservation.DoesNotExist:
                messages.error(request, "Reservation not found.")
            return redirect('/reservation/')

        # ── Cancel Reservation ──
        if action == 'cancel':
            res_id = request.POST.get('reservation_id')
            reason = request.POST.get('cancel_reason', '').strip()
            try:
                res = Reservation.objects.get(Reservation_ID=res_id)
                cancelled_at = timezone.now()
                res.Status = 'Cancelled'
                res.Cancelled_At = cancelled_at
                res.Cancel_Reason = reason
                res.save()
                # Free up the room
                Room.objects.filter(Room_ID=res.Room_ID).update(Status='Available')

                # Send cancellation email
                try:
                    customer = Customer.objects.get(Cus_ID=res.Cus_ID)
                    send_cancellation_email(
                        customer_name=customer.Name,
                        customer_email=customer.Email,
                        reservation_id=res.Reservation_ID,
                        room_id=res.Room_ID,
                        checkin=res.Check_In_Date,
                        checkout=res.Check_Out_Date,
                        reason=reason,
                        cancelled_at=cancelled_at,
                    )
                    messages.success(request, f"Reservation #{res_id} cancelled. Notification sent to {customer.Email}.")
                except Exception:
                    messages.success(request, f"Reservation #{res_id} cancelled successfully.")
            except Reservation.DoesNotExist:
                messages.error(request, "Reservation not found.")
            return redirect('/reservation/')

        # ── Create New Reservation ──
        customer_id = request.POST.get('customer')
        room_id = request.POST.get('room')
        checkin_str = request.POST.get('checkin')
        checkout_str = request.POST.get('checkout')

        checkin = datetime.date.fromisoformat(checkin_str)
        checkout = datetime.date.fromisoformat(checkout_str)
        today = datetime.date.today()

        if checkin < today:
            messages.error(request, "Check-in date cannot be in the past.")
        elif checkout <= checkin:
            messages.error(request, "Check-out must be after check-in date.")
        else:
            res = Reservation.objects.create(
                Cus_ID=customer_id,
                Room_ID=room_id,
                Check_In_Date=checkin,
                Check_Out_Date=checkout,
                Status='Confirmed',
            )
            Room.objects.filter(Room_ID=room_id).update(Status='Occupied')

            try:
                customer = Customer.objects.get(Cus_ID=customer_id)
                room = Room.objects.get(Room_ID=room_id)
                cat = RoomCategory.objects.get(Category_ID=room.Category_ID)
                nights = (checkout - checkin).days
                total_amount = cat.Price * nights
                email_sent = send_reservation_email(
                    customer_name=customer.Name,
                    customer_email=customer.Email,
                    reservation_id=res.Reservation_ID,
                    room_id=room_id,
                    room_category=cat.Category_Name,
                    checkin=checkin,
                    checkout=checkout,
                    nights=nights,
                    total_amount=total_amount,
                )
                if email_sent:
                    messages.success(request, f"Reservation #{res.Reservation_ID} created! Confirmation sent to {customer.Email}.")
                else:
                    messages.warning(request, f"Reservation #{res.Reservation_ID} created, but the email could not be sent.")
            except Exception:
                messages.success(request, "Reservation created successfully!")

            return redirect('/reservation/')

    # ── GET: build context ──
    available_rooms_qs = Room.objects.filter(Status='Available')
    available_rooms = []
    for room in available_rooms_qs:
        try:
            cat = RoomCategory.objects.get(Category_ID=room.Category_ID)
            available_rooms.append({'Room_ID': room.Room_ID, 'category': cat.Category_Name, 'price': cat.Price})
        except RoomCategory.DoesNotExist:
            available_rooms.append({'Room_ID': room.Room_ID, 'category': 'Standard', 'price': 0})

    all_customers = Customer.objects.all()

    # Enrich reservations with customer name
    raw_data = Reservation.objects.all().order_by('-Reservation_ID')
    data = []
    for r in raw_data:
        try:
            cname = Customer.objects.get(Cus_ID=r.Cus_ID).Name
        except Customer.DoesNotExist:
            cname = f"Customer #{r.Cus_ID}"
        data.append({
            'Reservation_ID': r.Reservation_ID,
            'customer_name': cname,
            'Cus_ID': r.Cus_ID,
            'Room_ID': r.Room_ID,
            'Check_In_Date': r.Check_In_Date,
            'Check_Out_Date': r.Check_Out_Date,
            'Status': r.Status,
            'Cancel_Reason': r.Cancel_Reason,
        })

    return render(request, 'reservation.html', {
        'data': data,
        'customers': all_customers,
        'available_rooms': available_rooms,
    })


# 💳 Payment
@login_required
def payment(request):
    if request.method == "POST":
        reservation_id = request.POST.get('reservation')
        amount = request.POST.get('amount')
        method = request.POST.get('method')

        if not all([reservation_id, amount, method]):
            messages.error(request, "All payment fields are required.")
        else:
            today = datetime.date.today()
            pay = Payment.objects.create(
                Reservation_ID=reservation_id,
                Amount=amount,
                Payment_Method=method,
                Payment_Date=today
            )
            # Update reservation status to Confirmed after payment
            Reservation.objects.filter(Reservation_ID=reservation_id).update(Status='Confirmed')

            try:
                res = Reservation.objects.get(Reservation_ID=reservation_id)
                customer = Customer.objects.get(Cus_ID=res.Cus_ID)
                email_sent = send_payment_email(
                    customer_name=customer.Name,
                    customer_email=customer.Email,
                    payment_id=pay.Payment_ID,
                    reservation_id=reservation_id,
                    amount=amount,
                    payment_method=method,
                    payment_date=today,
                    room_id=res.Room_ID,
                    checkin=res.Check_In_Date,
                    checkout=res.Check_Out_Date,
                )
                if email_sent:
                    messages.success(request, f"Payment of ₹{float(amount):,.2f} recorded! Receipt sent to {customer.Email}.")
                else:
                    messages.warning(request, f"Payment recorded, but the receipt email could not be sent.")
            except Exception:
                messages.success(request, "Payment recorded successfully!")

            return redirect('/payment/')

    paid_reservation_ids = Payment.objects.values_list('Reservation_ID', flat=True)
    unpaid_qs = Reservation.objects.exclude(Reservation_ID__in=paid_reservation_ids).exclude(Status='Cancelled')

    unpaid_reservations = []
    for r in unpaid_qs:
        try:
            customer_name = Customer.objects.get(Cus_ID=r.Cus_ID).Name
        except Customer.DoesNotExist:
            customer_name = f"Customer #{r.Cus_ID}"

        nights = (r.Check_Out_Date - r.Check_In_Date).days
        try:
            room = Room.objects.get(Room_ID=r.Room_ID)
            cat = RoomCategory.objects.get(Category_ID=room.Category_ID)
            total = cat.Price * nights
        except Exception:
            total = 0

        unpaid_reservations.append({
            'Reservation_ID': r.Reservation_ID,
            'customer_name': customer_name,
            'Room_ID': r.Room_ID,
            'Check_In_Date': r.Check_In_Date,
            'Check_Out_Date': r.Check_Out_Date,
            'total_amount': total,
        })

    payments_qs = Payment.objects.all()
    payments_data = []
    for p in payments_qs:
        try:
            res = Reservation.objects.get(Reservation_ID=p.Reservation_ID)
            customer_name = Customer.objects.get(Cus_ID=res.Cus_ID).Name
        except Exception:
            customer_name = "—"
        payments_data.append({
            'Payment_ID': p.Payment_ID,
            'Reservation_ID': p.Reservation_ID,
            'customer_name': customer_name,
            'Amount': p.Amount,
            'Payment_Method': p.Payment_Method,
            'Payment_Date': p.Payment_Date,
        })

    return render(request, 'payment.html', {
        'data': payments_data,
        'unpaid_reservations': unpaid_reservations,
    })