from django import forms
from app.models import *

class TopicDjForm(forms.Form):
    topic_name=forms.CharField()

class WebpageDjForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField()
    url=forms.URLField()

class AccessDjForm(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    author=forms.CharField()
    date=forms.DateField()