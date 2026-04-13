from django.contrib import admin
from .models import Customer, Hotel, Room, RoomCategory, Reservation, Payment

admin.site.register(Customer)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(RoomCategory)
admin.site.register(Reservation)
admin.site.register(Payment)