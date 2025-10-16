from django.urls import path
from colddrinks.views import *

app_name='colddrinks'
urlpatterns=[
    path('sprite/',sprite,name='sprite')
]