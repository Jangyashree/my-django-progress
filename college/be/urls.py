from django.urls import path
from be.views import *
app_name='abcde'
urlpatterns=[
    path('studentbranch/',studentbranch,name='studentbranch')
]