from django import forms

g=[('MALE','male'),('FEMALE','female')]
c=[('Python','python'),('Django','django'),('Sql','sql')]
class StudentdjForm(forms.Form):
    stname=forms.CharField()
    stage=forms.IntegerField()
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'rows':10,'cols':20}))