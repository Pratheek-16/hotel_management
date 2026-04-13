from django.db import models


class Customer(models.Model):
    Cus_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=15)
    Country = models.CharField(max_length=50)

    class Meta:
        db_table = "Customer"
        managed = True


class Hotel(models.Model):
    Hotel_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Location = models.CharField(max_length=100)

    class Meta:
        db_table = "Hotel"
        managed = True


class RoomCategory(models.Model):
    Category_ID = models.AutoField(primary_key=True)
    Category_Name = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "Room_Category"
        managed = True


class Room(models.Model):
    Room_ID = models.AutoField(primary_key=True)
    Hotel_ID = models.IntegerField()
    Category_ID = models.IntegerField()
    Status = models.CharField(max_length=20)

    class Meta:
        db_table = "Room"
        managed = True


class Reservation(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Checked In', 'Checked In'),
        ('Checked Out', 'Checked Out'),
        ('Cancelled', 'Cancelled'),
    ]

    Reservation_ID = models.AutoField(primary_key=True)
    Cus_ID = models.IntegerField()
    Room_ID = models.IntegerField()
    Check_In_Date = models.DateField()
    Check_Out_Date = models.DateField()
    Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    Cancelled_At = models.DateTimeField(null=True, blank=True)
    Cancel_Reason = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "Reservation"
        managed = True


class Payment(models.Model):
    Payment_ID = models.AutoField(primary_key=True)
    Reservation_ID = models.IntegerField()
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Payment_Method = models.CharField(max_length=20)
    Payment_Date = models.DateField(null=True)

    class Meta:
        db_table = "Payment"
        managed = True