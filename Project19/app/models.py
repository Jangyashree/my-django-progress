from django.db import models

# Create your models here.
class School(models.Model):
    scname=models.CharField()
    scloc=models.CharField()
    scprincipal=models.CharField()
    def __str__(self):
        return self.scname

class Student(models.Model):
    stname=models.CharField()
    stage=models.IntegerField()
    scname=models.ForeignKey(School, on_delete=models.CASCADE, related_name="School")
    def __str__(self):
        return self.stname