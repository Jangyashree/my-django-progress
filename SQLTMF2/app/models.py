from django.db import models
# Create your models here.

class Dept(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=50,unique=True)
    loc=models.CharField(max_length=20)   
 

class Emp(models.Model):
    Ename=models.CharField(max_length=50)
    Empno=models.IntegerField()
    Job=models.CharField(max_length=50)
    dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)