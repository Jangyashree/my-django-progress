from django.db import models

# Create your models here.

class Dept(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=20, unique=True)
    loc=models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.dept_no)+self.dname
        
class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=10)
    job=models.CharField(max_length=10)
    mgr=models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    hiredate=models.DateField(null=False)
    sal=models.DecimalField(max_digits=10, decimal_places=2)
    comm=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename
    