from django.urls import path
from bcom.views import *
app_name='abcd'
urlpatterns=[
    path('studentbranch/',studentbranch,name='studentbranch')
]