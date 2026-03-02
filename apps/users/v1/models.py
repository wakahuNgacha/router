from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.companies.v1.models import Company

# Create your models here.
class User(AbstractUser):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('driver', 'Driver'),
        ('manager', 'Manager'),
    )
    
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='driver')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50, unique=True)


    def __str__(self):
        return self.license_number
    
class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, related_name='managers')
    employee_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.employee_id
    