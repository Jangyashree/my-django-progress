from django.urls import path
from app2.views import *

app_name='app2'

urlpatterns=[
    path('specific2/',specific2,name='specific2')
]