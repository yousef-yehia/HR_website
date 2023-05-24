from asyncio.windows_events import NULL
from this import d
from unicodedata import name
from django.db import models
from django.forms import CharField, DateField, EmailField, FloatField, IntegerField


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    phoneNumber = models.CharField(max_length=200)
    dateOfBirth = models.DateField()
    gender = models.TextField()
    maritalStatus = models.TextField()
    address = models.CharField(max_length=300)
    availableVacations = models.IntegerField()
    salary = models.FloatField()

    def __str__(self) -> str:
        return self.name

class Vacation(models.Model):
    reason = models.TextField()
    date_from = models.DateField()
    date_to = models.DateField()
    status=models.TextField()
    employee=models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,related_name='vacations')
    
    def __str__(self) -> str:
        return self.reason
