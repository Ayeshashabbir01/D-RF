from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)  # Corrected 'max_Length' to 'max_length'
    roll = models.IntegerField()
    city = models.CharField(max_length=100)  # Corrected 'max_Length' to 'max_length'
