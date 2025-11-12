from django import forms
from app.models import *

class StudentModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

    reemail=forms.EmailField()
    bot=forms.CharField(widget=forms.HiddenInput,required=False)

    def clean(self):
        se=self.cleaned_data['semail']
        re=self.cleaned_data['reemail']
        if se!=re:
            raise forms.ValidationError('Email not Matched')

    def clean_bot(self):
         bot=self.cleaned_data['bot']
         if len(bot)>0:
            raise forms.ValidationError('bot')
        


