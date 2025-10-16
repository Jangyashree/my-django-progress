from django.urls import path
from mca.views import *
app_name='abcdef'
urlpatterns=[
    path('studentbranch/',studentbranch,name='studentbranch')
]