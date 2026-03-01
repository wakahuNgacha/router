from django.db import models

# Create your models here.
class Truck(models.Model):
    license_plate = models.CharField(max_length=20, unique=True)
    model = models.CharField(max_length=100)
    capacity = models.FloatField(help_text="Capacity in tons")
    driver = models.ForeignKey('drivers.Driver', on_delete=models.SET_NULL, null=True, related_name='trucks')

    def __str__(self):
        return f"{self.model} ({self.license_plate})"