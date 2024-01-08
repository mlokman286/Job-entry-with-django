from django import forms

from job.models import Job



class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['user','company']