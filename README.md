# 🏨 Hotel Aurum — Hotel Management System

A full-stack hotel management web application built with **Python** and **Django**, featuring room management, reservations, payments, automated email notifications, and an analytics dashboard.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Database | SQLite |
| Frontend | HTML, CSS, JavaScript |
| Charts | Chart.js |
| Email | Django SMTP (Gmail) |

---

## ✨ Features

### 👤 Customer Management
- Register new guest profiles with name, email, phone, and country
- Automatic welcome email sent on registration

### 🏨 Hotel & Room Management
- Add and manage hotels and locations
- Add rooms with categories (Standard, Deluxe, Suite) and pricing
- Room status tracking (Available / Occupied)

### 📅 Reservation System
- Book available rooms for registered customers
- Real-time price calculation (nights × room rate)
- Reservation status tracking:
  ```
  Pending → Confirmed → Checked In → Checked Out
                                    ↘ Cancelled
  ```
- Update status with one click — customer gets email on every change
- Cancel reservation with optional reason — room freed automatically

### 💳 Payment Tracking
- Record payments with method (Cash, Card, UPI, Net Banking)
- Auto-calculates amount based on room rate and nights
- Payment receipt email sent instantly to customer

### 📊 Analytics Dashboard
- **Revenue Trend** — Monthly revenue line chart (last 6 months)
- **Room Occupancy** — Live doughnut chart with occupancy %
- **Reservation Status** — Breakdown pie chart
- **Monthly Bookings** — Bar chart per month
- **Avg Revenue per Booking** — Trend line chart

### ✉️ Automated Email Notifications
| Trigger | Email Sent To |
|---|---|
| Customer registered | Customer |
| Reservation created | Customer |
| Reservation status updated | Customer |
| Reservation cancelled | Customer |
| Payment recorded | Customer |

---

## 📁 Project Structure

```
hotel_project/
├── hotel_app/
│   ├── models.py          # Database models
│   ├── views.py           # Business logic & email triggers
│   ├── email_utils.py     # All email functions
│   ├── urls.py            # URL routing
│   ├── admin.py           # Django admin registration
│   └── migrations/        # Database migrations
├── hotel_project/
│   ├── settings.py        # Project settings + email config
│   └── urls.py
├── templates/             # HTML templates
├── static/                # CSS & JS files
├── seed_data.py           # Script to load sample data
├── manage.py
└── db.sqlite3             # SQLite database
```

---

## ⚙️ Setup & Installation

### 1. Clone or extract the project
```bash
cd hotel_project
```

### 2. Install dependencies
```bash
pip install django
```

### 3. Run migrations
```bash
python manage.py migrate
```

### 4. Load sample data (optional)
```bash
python seed_data.py
```

### 5. Create admin user (for Django admin panel)
```bash
python manage.py createsuperuser
```

### 6. Configure email — open `hotel_project/settings.py`
```python
EMAIL_HOST_USER     = 'your_gmail@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'   # Gmail App Password
DEFAULT_FROM_EMAIL  = 'Hotel Aurum <your_gmail@gmail.com>'
```
> To get a Gmail App Password: Google Account → Security → 2-Step Verification → App Passwords

### 7. Run the server
```bash
python manage.py runserver
```

### 8. Open in browser
```
http://127.0.0.1:8000/
```

---

## 🔐 Login

| Field | Value |
|---|---|
| Username | `admin` |
| Password | `admin123` |

---

## 📌 Pages & URLs

| Page | URL |
|---|---|
| Home | `/` |
| Login | `/login/` |
| Dashboard | `/dashboard/` |
| Customers | `/customers/` |
| Hotels | `/hotels/` |
| Rooms | `/rooms/` |
| Reservations | `/reservation/` |
| Payments | `/payment/` |
| Django Admin | `/admin/` |

---

## 📧 Email Testing (Without Gmail)

To test locally without sending real emails, open `settings.py` and switch to:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
Emails will print directly in your terminal.

---

## 📷 Dashboard Charts

All charts are powered by **Chart.js** (CDN — no installation needed) and use live data from the database. The dark-themed analytics section features:
- Gold gradient area charts
- Smooth doughnut charts with custom legends
- Highlighted bar charts for current month
- Dark tooltips with gold accents

---

## 🗄️ Database Models

| Model | Key Fields |
|---|---|
| Customer | Name, Email, Phone, Country |
| Hotel | Name, Location |
| RoomCategory | Category Name, Price |
| Room | Hotel, Category, Status |
| Reservation | Customer, Room, Check-In, Check-Out, Status |
| Payment | Reservation, Amount, Method, Date |

---

## 🚀 Future Enhancements
- Razorpay online payment gateway
- PDF invoice generation
- Customer self-service portal
- WhatsApp/SMS notifications
- Cloud deployment (Railway / Render)
