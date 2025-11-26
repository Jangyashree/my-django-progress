from django import forms
from app.models import *

class SchoolMF(forms.Form):
    class Meta:
        model=School
        fields='__all__'