from django.db import models

# Create your models here.
from django.core.validators import RegexValidator

class Student(models.Model):
    stname=models.CharField()
    stage=models.IntegerField()
    semail=models.EmailField()
    smobile=models.CharField(max_length=10,validators=[RegexValidator('[6,9]\d{9}')])