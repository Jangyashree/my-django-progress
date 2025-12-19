from django.db import models

# Create your models here.
class School(models.Model):
    scname=models.CharField()
    scloaction=models.CharField()
    scprincipal=models.CharField()