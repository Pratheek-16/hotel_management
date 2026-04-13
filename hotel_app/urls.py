from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
     path('logout/', views.logout),  
    path('dashboard/', views.dashboard),
    path('customers/', views.customers),
    path('hotels/', views.hotels),
    path('rooms/', views.rooms),
    path('reservation/', views.reservation),
    path('payment/', views.payment),
]