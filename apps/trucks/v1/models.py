from django.db import models

from apps.companies.v1.models import Company
from apps.users.v1.models import Driver

# Create your models here.
class Truck(models.Model):
    license_plate = models.CharField(max_length=20, unique=True)
    model = models.CharField(max_length=100)
    consumption = models.FloatField(help_text="Fuel consumption rate in miles per gallon")
    max_range = models.FloatField(help_text="Maximum range in miles")
    capacity = models.FloatField(help_text="Capacity in tons")
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, related_name='trucks')
    total_truck_milage = models.FloatField(help_text="Total mileage driven in miles")

    def __str__(self):
        return f"{self.model} ({self.license_plate})"
