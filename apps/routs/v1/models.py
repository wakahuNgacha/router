from django.db import models

# Create your models here.
class Rout(models.Model):
    origin_lat = models.FloatField()
    origin_lng = models.FloatField()

    destination_lat = models.FloatField()
    destination_lng = models.FloatField()
    routes = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.origin_address} to {self.destination_address}"
