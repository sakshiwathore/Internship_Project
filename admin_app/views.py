from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Booking, Service, Coupon
from django.db.models import Sum

def login_view(request):
    error_message = None
    if request.method == 'POST':
        login_input = request.POST.get('username')
        password = request.POST.get('password')
        
        # Try to find user by username or email
        user = authenticate(request, username=login_input, password=password)
        if user is None:
            try:
                # Check if login_input is an email and find corresponding username
                user_obj = User.objects.filter(email=login_input).first()
                if user_obj:
                    user = authenticate(request, username=user_obj.username, password=password)
            except Exception:
                user = None

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = "Invalid username or password!"
            
    return render(request, 'admin_app/login.html', {'error_message': error_message})

def register_view(request):
    success_message = None
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            error_message = "Passwords do not match!"
        elif User.objects.filter(username=username).exists():
            error_message = "Username already exists!"
        elif User.objects.filter(email=email).exists():
            error_message = "Email already registered!"
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('dashboard')
            
    return render(request, 'admin_app/register.html', {
        'success_message': success_message,
        'error_message': error_message
    })

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    total_bookings = Booking.objects.count()
    total_revenue = Booking.objects.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    active_services = Service.objects.filter(is_active=True).count()
    active_coupons = Coupon.objects.filter(is_active=True).count()
    recent_bookings = Booking.objects.all().order_by('-date')[:5]

    context = {
        'total_bookings': total_bookings,
        'total_revenue': total_revenue,
        'active_services': active_services,
        'active_coupons': active_coupons,
        'recent_bookings': recent_bookings,
    }
    return render(request, 'admin_app/dashboard.html', context)

@login_required
def home_view(request):
    return render(request, 'admin_app/home.html')

@login_required
def services_view(request):
    return render(request, 'admin_app/services.html')

@login_required
def workers_view(request):
    return render(request, 'admin_app/workers.html')

@login_required
def coupons_view(request):
    return render(request, 'admin_app/coupons.html')

@login_required
def bookings_view(request):
    return render(request, 'admin_app/bookings.html')
