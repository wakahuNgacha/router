from django.db import models
from apps.trucks.v1.models import Truck
from apps.routs.v1.models import Rout
from apps.users.v1.models import Driver

# Create your models here.
class DailyLog(models.Model):
    date = models.DateField()    
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='daily_logs')
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, related_name='daily_logs')
    rout = models.ForeignKey(Rout, on_delete=models.CASCADE, related_name='daily_logs')
    total_driving_milage = models.FloatField(help_text="Total mileage driven in miles")

    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Daily Log for {self.truck} on {self.date}"
    
class OffDuty(models.Model):
    daily_log = models.ForeignKey(DailyLog, on_delete=models.CASCADE, related_name='off_duties')
    start = models.DateTimeField()
    stop = models.DateTimeField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='off_duties')
    location = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Off Duty for {self.driver} on {self.start}"
    
class SleeperBerth(models.Model):
    daily_log = models.ForeignKey(DailyLog, on_delete=models.CASCADE, related_name='sleeper_berths')
    start = models.DateTimeField()
    stop = models.DateTimeField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='sleeper_berths')

    def __str__(self):
        return f"Sleeper Berth for {self.driver} on {self.start}"

class Driving(models.Model):
    daily_log = models.ForeignKey(DailyLog, on_delete=models.CASCADE, related_name='drivings')
    start = models.DateTimeField()
    stop = models.DateTimeField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='drivings')

    def __str__(self):
        return f"Driving for {self.driver} on {self.start}"

class OnDuty(models.Model):
    daily_log = models.ForeignKey(DailyLog, on_delete=models.CASCADE, related_name='on_duties')
    start = models.DateTimeField()
    stop = models.DateTimeField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='on_duties')
    location = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"On Duty for {self.driver} on {self.start}"
