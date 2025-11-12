from django.db import models

# Create your models here.
class Student(models.Model):
    stname = models.CharField()
    stage = models.IntegerField()
    address = models.CharField()
    semail=models.CharField(default='hai@gmail.com')
