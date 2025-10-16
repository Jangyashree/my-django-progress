from django.urls import path
from bca.views import *
app_name='abc'
urlpatterns=[
    path('studentbranch/',studentbranch,name='studentbranch')
]