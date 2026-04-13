from django.core.mail import send_mail
from django.conf import settings


def send_registration_email(customer_name, customer_email, customer_phone, country):
    subject = "Welcome to Hotel Aurum – Registration Confirmed"
    message = f"""
Dear {customer_name},

Thank you for registering with Hotel Aurum! Your guest profile has been successfully created.

──────────────────────────────
 YOUR REGISTRATION DETAILS
──────────────────────────────
Name    : {customer_name}
Email   : {customer_email}
Phone   : {customer_phone}
Country : {country}
──────────────────────────────

You can now make reservations and enjoy our premium services.

Warm regards,
Hotel Aurum Management Team
📧 support@hotelaurum.com
📞 +91-9876543210
"""
    try:
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [customer_email], fail_silently=False)
        return True
    except Exception as e:
        print(f"[EMAIL ERROR] Registration email failed for {customer_email}: {e}")
        return False


def send_reservation_email(customer_name, customer_email, reservation_id,
                           room_id, room_category, checkin, checkout, nights, total_amount):
    subject = f"Reservation Confirmed – Hotel Aurum (Booking #{reservation_id})"
    message = f"""
Dear {customer_name},

Your reservation at Hotel Aurum has been confirmed!

──────────────────────────────────────
 RESERVATION CONFIRMATION
──────────────────────────────────────
Booking ID      : #{reservation_id}
Room            : Room #{room_id} ({room_category})
Check-In Date   : {checkin.strftime('%d %B %Y')}
Check-Out Date  : {checkout.strftime('%d %B %Y')}
Duration        : {nights} night(s)
Estimated Total : ₹{total_amount:,.2f}
Status          : ✅ Confirmed
──────────────────────────────────────

IMPORTANT NOTES:
• Please present this email at check-in.
• Check-in time: 2:00 PM | Check-out time: 11:00 AM
• For changes or cancellations, contact us 24 hours in advance.

We look forward to welcoming you!

Warm regards,
Hotel Aurum Management Team
📧 support@hotelaurum.com
📞 +91-9876543210
"""
    try:
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [customer_email], fail_silently=False)
        return True
    except Exception as e:
        print(f"[EMAIL ERROR] Reservation email failed for {customer_email}: {e}")
        return False


def send_status_update_email(customer_name, customer_email, reservation_id, new_status, checkin, checkout, room_id):
    """Send email when reservation status is updated."""
    status_icons = {
        'Pending': '🕐',
        'Confirmed': '✅',
        'Checked In': '🏨',
        'Checked Out': '👋',
        'Cancelled': '❌',
    }
    icon = status_icons.get(new_status, '📋')
    subject = f"Reservation #{reservation_id} Status Update – Hotel Aurum"
    message = f"""
Dear {customer_name},

Your reservation status has been updated.

──────────────────────────────────────
 RESERVATION STATUS UPDATE
──────────────────────────────────────
Booking ID      : #{reservation_id}
Room            : Room #{room_id}
Check-In Date   : {checkin.strftime('%d %B %Y')}
Check-Out Date  : {checkout.strftime('%d %B %Y')}
New Status      : {icon} {new_status}
──────────────────────────────────────

{'We look forward to welcoming you!' if new_status == 'Confirmed' else ''}
{'Welcome! We hope you enjoy your stay.' if new_status == 'Checked In' else ''}
{'Thank you for staying with us. We hope to see you again!' if new_status == 'Checked Out' else ''}

For any queries, contact us at support@hotelaurum.com.

Warm regards,
Hotel Aurum Management Team
📧 support@hotelaurum.com
📞 +91-9876543210
"""
    try:
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [customer_email], fail_silently=False)
        return True
    except Exception as e:
        print(f"[EMAIL ERROR] Status update email failed for {customer_email}: {e}")
        return False


def send_cancellation_email(customer_name, customer_email, reservation_id,
                            room_id, checkin, checkout, reason, cancelled_at):
    """Send cancellation confirmation email to the customer."""
    subject = f"Reservation #{reservation_id} Cancelled – Hotel Aurum"
    message = f"""
Dear {customer_name},

We're sorry to inform you that your reservation has been cancelled.

──────────────────────────────────────
 CANCELLATION CONFIRMATION
──────────────────────────────────────
Booking ID      : #{reservation_id}
Room            : Room #{room_id}
Check-In Date   : {checkin.strftime('%d %B %Y')}
Check-Out Date  : {checkout.strftime('%d %B %Y')}
Cancelled On    : {cancelled_at.strftime('%d %B %Y, %I:%M %p')}
Reason          : {reason if reason else 'Not specified'}
Status          : ❌ Cancelled
──────────────────────────────────────

If this cancellation was made in error or you have any concerns,
please contact us immediately at support@hotelaurum.com.

We hope to welcome you at Hotel Aurum in the future!

Warm regards,
Hotel Aurum Management Team
📧 support@hotelaurum.com
📞 +91-9876543210
"""
    try:
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [customer_email], fail_silently=False)
        return True
    except Exception as e:
        print(f"[EMAIL ERROR] Cancellation email failed for {customer_email}: {e}")
        return False


def send_payment_email(customer_name, customer_email, payment_id,
                       reservation_id, amount, payment_method, payment_date,
                       room_id, checkin, checkout):
    subject = f"Payment Receipt – Hotel Aurum (Payment #{payment_id})"
    message = f"""
Dear {customer_name},

We have successfully received your payment. Thank you!

──────────────────────────────────────
 PAYMENT RECEIPT
──────────────────────────────────────
Receipt No.     : PAY-{payment_id:05d}
Booking ID      : #{reservation_id}
Room            : Room #{room_id}
Check-In        : {checkin.strftime('%d %B %Y')}
Check-Out       : {checkout.strftime('%d %B %Y')}
──────────────────────────────────────
Amount Paid     : ₹{float(amount):,.2f}
Payment Method  : {payment_method}
Payment Date    : {payment_date.strftime('%d %B %Y')}
──────────────────────────────────────
Status          : ✅ PAID
──────────────────────────────────────

Please keep this receipt for your records.

Warm regards,
Hotel Aurum Management Team
📧 support@hotelaurum.com
📞 +91-9876543210
"""
    try:
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [customer_email], fail_silently=False)
        return True
    except Exception as e:
        print(f"[EMAIL ERROR] Payment email failed for {customer_email}: {e}")
        return False