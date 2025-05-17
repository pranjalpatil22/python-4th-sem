from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Flight URLs
    path('flights/', views.flight_list, name='flight_list'),
    path('flights/add/', views.flight_add, name='flight_add'),
    path('flights/edit/<int:pk>/', views.flight_edit, name='flight_edit'),
    path('flights/delete/<int:pk>/', views.flight_delete, name='flight_delete'),

    # Passenger URLs
    path('passengers/', views.passenger_list, name='passenger_list'),
    path('passengers/add/', views.passenger_add, name='passenger_add'),
    path('passengers/edit/<int:pk>/', views.passenger_edit, name='passenger_edit'),
    path('passengers/delete/<int:pk>/', views.passenger_delete, name='passenger_delete'),

    # Check-in URLs
    path('checkins/', views.checkin_list, name='checkin_list'),
    path('checkins/add/', views.checkin_add, name='checkin_add'),
    path('checkins/delete/<int:pk>/', views.checkin_delete, name='checkin_delete'),
]
