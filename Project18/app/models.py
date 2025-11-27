from django.db import models

# Create your models here.
class Student(models.Model):
    stname=models.CharField()
    stid=models.IntegerField()
    stage=models.IntegerField()