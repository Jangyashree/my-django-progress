from django.db import models

# Create your models here.
class Author(models.Model):
    Aid=models.IntegerField(primary_key=True)
    Aname=models.CharField(max_length=100)
    Amobile_no=models.CharField(unique=True)
    
class Books(models.Model):
    Bid=models.IntegerField(primary_key=True)
    Bname=models.CharField(max_length=100)
    Publish_date=models.DateField(auto_now_add=True)
    Aid=models.ForeignKey(Author,on_delete=models.CASCADE)