from django.urls import path
from mtech.views import *
app_name='abcdef'
urlpatterns=[
    path('studentbranch/',studentbrnach,name='studentbranch')
]