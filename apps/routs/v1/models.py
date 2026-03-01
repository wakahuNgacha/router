from django.db import models

# Create your models here.
class Rout(models.Model):
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    distance_km = models.FloatField()
    estimated_time_hours = models.FloatField()

    def __str__(self):
        return f"{self.origin} to {self.destination}"