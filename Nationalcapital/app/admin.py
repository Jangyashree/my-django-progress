from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Capital)
admin.site.register(Country)