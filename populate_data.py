import os
import django
from datetime import datetime
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homeservice_project.settings')
django.setup()

from admin_app.models import Service, Coupon, Booking, Worker

# Clear existing data
Service.objects.all().delete()
Coupon.objects.all().delete()
Booking.objects.all().delete()
Worker.objects.all().delete()

# Create Services
s1 = Service.objects.create(name="Cleaning", price=100.00, description="Deep cleaning")
s2 = Service.objects.create(name="Repair", price=150.00, description="General repair")

# Create Coupon
c1 = Coupon.objects.create(code="WELCOME", discount_amount=10.00)

# Create Bookings
Booking.objects.create(customer_name="Alice", service=s1, date=datetime.now(), total_amount=100.00)
Booking.objects.create(customer_name="Bob", service=s2, date=datetime.now(), total_amount=150.00)
Booking.objects.create(customer_name="Charlie", service=s1, date=datetime.now(), total_amount=100.00)

print("Data populated successfully.")
