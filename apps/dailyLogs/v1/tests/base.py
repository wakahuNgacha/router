# apps/logs/v1/tests/base.py

from django.test import TestCase
from rest_framework.test import APIClient
from datetime import date
from django.utils import timezone
from datetime import timedelta

from apps.companies.v1.models import Company
from apps.trucks.v1.models import Truck
from apps.routes.v1.models import Route
from apps.users.v1.models import User,Driver
from apps.dailyLogs.v1.models import DailyLog


class BaseLogTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.company = Company.objects.create(
            name="Test Company"
        )

        self.user = User.objects.create_user(
            email="driver@test.com",
            username="testdriver",
            password="testpass123",
            role="driver"
        )


        self.driver = Driver.objects.create(
            user=self.user,
            license_number="LIC12345"
        )

        self.truck = Truck.objects.create(
            license_plate="ABC123",
            model="Volvo",
            consumption=8.5,
            max_range=500,
            capacity=10,
            company_id=1,
            total_truck_milage=10000
        )

        self.route = Route.objects.create(
            origin_lat=1.2345,
            origin_lng=36.7890,
            destination_lat=1.3456,
            destination_lng=36.8901,
            routees=None
        )

        self.daily_log = DailyLog.objects.create(
            date=date.today(),
            driver=self.driver,
            truck=self.truck,
            route=self.route,
            total_driving_milage=100
        )

        self.now = timezone.now()
        self.later = self.now + timedelta(hours=2)
