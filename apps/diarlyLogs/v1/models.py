from django.db import models

# Create your models here.
class DiaryLog(models.Model):
    truck = models.ForeignKey('trucks.Truck', on_delete=models.CASCADE, related_name='diary_logs')
    rout = models.ForeignKey('routs.Rout', on_delete=models.CASCADE, related_name='diary_logs')
    date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Diary Log for {self.truck} on {self.date}"