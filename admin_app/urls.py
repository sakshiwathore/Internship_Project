from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('home/', views.home_view, name='home'),
    path('services/', views.services_view, name='services'),
    path('workers/', views.workers_view, name='workers'),
    path('coupons/', views.coupons_view, name='coupons'),
    path('bookings/', views.bookings_view, name='bookings'),
    path('logout/', views.logout_view, name='logout'),
]
