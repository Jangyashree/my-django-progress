from django.db import models

# Create your models here.

class Country(models.Model):
    country_id=models.IntegerField(primary_key=True)
    country_name=models.CharField()

    def __str__(self):
        return self.country_name

class Capital(models.Model):
    captial_id=models.IntegerField()
    captial_name=models.CharField(max_length=100)
    country_id=models.OneToOneField(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.captial_name

