from django.urls import path
from diploma.views import *
app_name='abcdef'
urlpatterns=[
    path('studentbranch/',studentbranch,name='studentbranch')
]