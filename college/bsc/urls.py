from django.urls import path
from bsc.views import *
app_name='abcdef'
urlpatterns=[
    path('studentbranch/',studentbranch,name='studentbranch')
]