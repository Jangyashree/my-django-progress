from django.urls import path
from btech.views import *
app_name='abcdefg'
urlpatterns=[
    path('studentbranch/',studentbranch,name='studentbranch')
]