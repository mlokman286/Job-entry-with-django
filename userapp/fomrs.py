from django import forms
from django.contrib.auth.forms import UserCreationForm

from userapp.models import *

class SingupForm(UserCreationForm):
    class Meta:
        model = JobUser
        fields=['username','email','user_type','password1','password2']

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ('user',)
        widgets ={
            'education':forms.CharField()
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('user',)