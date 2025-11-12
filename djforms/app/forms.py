from django import forms
from app.models import *


def check_for_s(value):
    if value[0].lower()=='s':
        raise forms.ValidationError('Name should not starts with s')
def check_for_len(value):
    if len(str(value))<=5:
        raise forms.ValidationError('length is too small')
    
     
g=[('MALE','male'),('FEMALE','female')]
c=[('Python','python'),('Django','django'),('Sql','sql')]

class StudentdjForm(forms.Form):
    stname=forms.CharField(validators=[check_for_s,check_for_len])
    stage=forms.IntegerField()
    #gender=forms.ChoiceField(choices=g)
    #gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #course=forms.MultipleChoiceField(choices=c)
    #course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    password=forms.CharField(widget=forms.PasswordInput)
    #repassword=forms.CharField()
    address=forms.CharField(widget=forms.Textarea(attrs={'rows':10,'cols':20}))
    semail=forms.EmailField()
    reemail=forms.EmailField()
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)
    

    def clean(self):
        print(str(self.cleaned_data))
        se=self.cleaned_data['semail']
        re=self.cleaned_data['reemail']
        if se!=re:
            raise forms.ValidationError('emails NOT Matched')

    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot')
