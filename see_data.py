import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_project.settings')
django.setup()

from hotel_app.models import RoomCategory, Hotel, Room, Customer, Reservation, Payment

# ── Room Categories ──
cat1, _ = RoomCategory.objects.get_or_create(Category_ID=1, defaults={'Category_Name': 'Standard', 'Price': 1500.00})
cat2, _ = RoomCategory.objects.get_or_create(Category_ID=2, defaults={'Category_Name': 'Deluxe',   'Price': 2500.00})
cat3, _ = RoomCategory.objects.get_or_create(Category_ID=3, defaults={'Category_Name': 'Suite',    'Price': 5000.00})
print("✅ Room Categories loaded")

# ── Hotels ──
Hotel.objects.get_or_create(Hotel_ID=1, defaults={'Name': 'Hotel Aurum Chennai', 'Location': 'Chennai'})
Hotel.objects.get_or_create(Hotel_ID=2, defaults={'Name': 'Hotel Aurum Mumbai',  'Location': 'Mumbai'})
Hotel.objects.get_or_create(Hotel_ID=3, defaults={'Name': 'Hotel Aurum Delhi',   'Location': 'Delhi'})
print("✅ Hotels loaded")

# ── Rooms ──
Room.objects.get_or_create(Room_ID=101, defaults={'Hotel_ID': 1, 'Category_ID': 1, 'Status': 'Available'})
Room.objects.get_or_create(Room_ID=102, defaults={'Hotel_ID': 1, 'Category_ID': 2, 'Status': 'Available'})
Room.objects.get_or_create(Room_ID=103, defaults={'Hotel_ID': 1, 'Category_ID': 3, 'Status': 'Available'})
Room.objects.get_or_create(Room_ID=104, defaults={'Hotel_ID': 1, 'Category_ID': 1, 'Status': 'Available'})
Room.objects.get_or_create(Room_ID=105, defaults={'Hotel_ID': 1, 'Category_ID': 2, 'Status': 'Available'})
Room.objects.get_or_create(Room_ID=201, defaults={'Hotel_ID': 2, 'Category_ID': 1, 'Status': 'Available'})
Room.objects.get_or_create(Room_ID=202, defaults={'Hotel_ID': 2, 'Category_ID': 2, 'Status': 'Available'})
Room.objects.get_or_create(Room_ID=203, defaults={'Hotel_ID': 2, 'Category_ID': 3, 'Status': 'Available'})
Room.objects.get_or_create(Room_ID=301, defaults={'Hotel_ID': 3, 'Category_ID': 1, 'Status': 'Available'})
Room.objects.get_or_create(Room_ID=302, defaults={'Hotel_ID': 3, 'Category_ID': 2, 'Status': 'Available'})
print("✅ Rooms loaded")

# ── Customers ──
Customer.objects.get_or_create(Cus_ID=1,  defaults={'Name': 'Ravi Kumar',    'Email': 'ravi@gmail.com',    'Phone': '9876543210', 'Country': 'India'})
Customer.objects.get_or_create(Cus_ID=2,  defaults={'Name': 'Priya Singh',   'Email': 'priya@gmail.com',   'Phone': '9123456789', 'Country': 'India'})
Customer.objects.get_or_create(Cus_ID=3,  defaults={'Name': 'Arjun Mehta',   'Email': 'arjun@gmail.com',   'Phone': '9988776655', 'Country': 'India'})
Customer.objects.get_or_create(Cus_ID=4,  defaults={'Name': 'Sneha Nair',    'Email': 'sneha@gmail.com',   'Phone': '9870001234', 'Country': 'India'})
Customer.objects.get_or_create(Cus_ID=5,  defaults={'Name': 'Karthik Raja',  'Email': 'karthik@gmail.com', 'Phone': '9765432100', 'Country': 'India'})
Customer.objects.get_or_create(Cus_ID=6,  defaults={'Name': 'Divya Sharma',  'Email': 'divya@gmail.com',   'Phone': '9654321098', 'Country': 'India'})
Customer.objects.get_or_create(Cus_ID=7,  defaults={'Name': 'Rahul Verma',   'Email': 'rahul@gmail.com',   'Phone': '9543210987', 'Country': 'India'})
Customer.objects.get_or_create(Cus_ID=8,  defaults={'Name': 'Anita Joshi',   'Email': 'anita@gmail.com',   'Phone': '9432109876', 'Country': 'India'})
Customer.objects.get_or_create(Cus_ID=9,  defaults={'Name': 'Vikram Patel',  'Email': 'vikram@gmail.com',  'Phone': '9321098765', 'Country': 'India'})
Customer.objects.get_or_create(Cus_ID=10, defaults={'Name': 'Meena Iyer',    'Email': 'meena@gmail.com',   'Phone': '9210987654', 'Country': 'India'})
print("✅ Customers loaded")

# ── Reservations ──
# Past reservations (for chart data to show)
Reservation.objects.get_or_create(Reservation_ID=1, defaults={
    'Cus_ID': 1, 'Room_ID': 101,
    'Check_In_Date':  datetime.date(2025, 11, 1),
    'Check_Out_Date': datetime.date(2025, 11, 4),
    'Status': 'Checked Out'
})
Reservation.objects.get_or_create(Reservation_ID=2, defaults={
    'Cus_ID': 2, 'Room_ID': 102,
    'Check_In_Date':  datetime.date(2025, 11, 10),
    'Check_Out_Date': datetime.date(2025, 11, 13),
    'Status': 'Checked Out'
})
Reservation.objects.get_or_create(Reservation_ID=3, defaults={
    'Cus_ID': 3, 'Room_ID': 201,
    'Check_In_Date':  datetime.date(2025, 12, 5),
    'Check_Out_Date': datetime.date(2025, 12, 8),
    'Status': 'Checked Out'
})
Reservation.objects.get_or_create(Reservation_ID=4, defaults={
    'Cus_ID': 4, 'Room_ID': 202,
    'Check_In_Date':  datetime.date(2025, 12, 15),
    'Check_Out_Date': datetime.date(2025, 12, 18),
    'Status': 'Checked Out'
})
Reservation.objects.get_or_create(Reservation_ID=5, defaults={
    'Cus_ID': 5, 'Room_ID': 301,
    'Check_In_Date':  datetime.date(2026, 1, 3),
    'Check_Out_Date': datetime.date(2026, 1, 6),
    'Status': 'Checked Out'
})
Reservation.objects.get_or_create(Reservation_ID=6, defaults={
    'Cus_ID': 6, 'Room_ID': 103,
    'Check_In_Date':  datetime.date(2026, 1, 20),
    'Check_Out_Date': datetime.date(2026, 1, 23),
    'Status': 'Checked Out'
})
Reservation.objects.get_or_create(Reservation_ID=7, defaults={
    'Cus_ID': 7, 'Room_ID': 302,
    'Check_In_Date':  datetime.date(2026, 2, 5),
    'Check_Out_Date': datetime.date(2026, 2, 8),
    'Status': 'Checked Out'
})
Reservation.objects.get_or_create(Reservation_ID=8, defaults={
    'Cus_ID': 8, 'Room_ID': 203,
    'Check_In_Date':  datetime.date(2026, 2, 14),
    'Check_Out_Date': datetime.date(2026, 2, 17),
    'Status': 'Checked Out'
})
Reservation.objects.get_or_create(Reservation_ID=9, defaults={
    'Cus_ID': 9, 'Room_ID': 104,
    'Check_In_Date':  datetime.date(2026, 3, 1),
    'Check_Out_Date': datetime.date(2026, 3, 4),
    'Status': 'Confirmed'
})
Reservation.objects.get_or_create(Reservation_ID=10, defaults={
    'Cus_ID': 10, 'Room_ID': 105,
    'Check_In_Date':  datetime.date(2026, 3, 10),
    'Check_Out_Date': datetime.date(2026, 3, 13),
    'Status': 'Confirmed'
})
# Current / upcoming reservations
Reservation.objects.get_or_create(Reservation_ID=11, defaults={
    'Cus_ID': 1, 'Room_ID': 201,
    'Check_In_Date':  datetime.date(2026, 4, 15),
    'Check_Out_Date': datetime.date(2026, 4, 18),
    'Status': 'Confirmed'
})
Reservation.objects.get_or_create(Reservation_ID=12, defaults={
    'Cus_ID': 3, 'Room_ID': 301,
    'Check_In_Date':  datetime.date(2026, 4, 20),
    'Check_Out_Date': datetime.date(2026, 4, 23),
    'Status': 'Pending'
})
print("✅ Reservations loaded")

# ── Payments ──
# Standard = ₹1500/night, Deluxe = ₹2500/night, Suite = ₹5000/night
Payment.objects.get_or_create(Payment_ID=1,  defaults={'Reservation_ID': 1,  'Amount': 4500.00,  'Payment_Method': 'Cash',          'Payment_Date': datetime.date(2025, 11, 1)})
Payment.objects.get_or_create(Payment_ID=2,  defaults={'Reservation_ID': 2,  'Amount': 7500.00,  'Payment_Method': 'Card',          'Payment_Date': datetime.date(2025, 11, 10)})
Payment.objects.get_or_create(Payment_ID=3,  defaults={'Reservation_ID': 3,  'Amount': 4500.00,  'Payment_Method': 'UPI',           'Payment_Date': datetime.date(2025, 12, 5)})
Payment.objects.get_or_create(Payment_ID=4,  defaults={'Reservation_ID': 4,  'Amount': 7500.00,  'Payment_Method': 'Card',          'Payment_Date': datetime.date(2025, 12, 15)})
Payment.objects.get_or_create(Payment_ID=5,  defaults={'Reservation_ID': 5,  'Amount': 4500.00,  'Payment_Method': 'Cash',          'Payment_Date': datetime.date(2026, 1, 3)})
Payment.objects.get_or_create(Payment_ID=6,  defaults={'Reservation_ID': 6,  'Amount': 15000.00, 'Payment_Method': 'Card',          'Payment_Date': datetime.date(2026, 1, 20)})
Payment.objects.get_or_create(Payment_ID=7,  defaults={'Reservation_ID': 7,  'Amount': 7500.00,  'Payment_Method': 'UPI',           'Payment_Date': datetime.date(2026, 2, 5)})
Payment.objects.get_or_create(Payment_ID=8,  defaults={'Reservation_ID': 8,  'Amount': 15000.00, 'Payment_Method': 'Net Banking',   'Payment_Date': datetime.date(2026, 2, 14)})
Payment.objects.get_or_create(Payment_ID=9,  defaults={'Reservation_ID': 9,  'Amount': 4500.00,  'Payment_Method': 'UPI',           'Payment_Date': datetime.date(2026, 3, 1)})
Payment.objects.get_or_create(Payment_ID=10, defaults={'Reservation_ID': 10, 'Amount': 7500.00,  'Payment_Method': 'Card',          'Payment_Date': datetime.date(2026, 3, 10)})
print("✅ Payments loaded")

print("")
print("🎉 All data loaded successfully!")
print("   Customers   : 10")
print("   Hotels      : 3")
print("   Rooms       : 10")
print("   Reservations: 12")
print("   Payments    : 10")