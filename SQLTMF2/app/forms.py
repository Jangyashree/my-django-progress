from django import forms
from app.models import *

class DeptMF(forms.ModelForm):
    class Meta:
        model=Dept
        fields='__all__'

class EmpMF(forms.ModelForm):
    class Meta:
        model=Emp
        exclude=['dept_no']