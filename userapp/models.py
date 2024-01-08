from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.
class JobUser(AbstractUser):
    USER_TYPE = (
        ('Recruiter','Recruiter'),
        ('Applicant','Applicant'),
    )
    user_type= models.CharField(max_length = 100,choices=USER_TYPE,default='Applicant')
    has_resume= models.BooleanField(default=False)
    has_company= models.BooleanField(default=False)

class Resume(models.Model):
    user=models.OneToOneField(JobUser,on_delete=models.CASCADE,null=True,blank=True)
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profession=models.CharField(max_length=1000,null=True,blank=True)
    address=models.CharField(max_length=1000,null=True,blank=True)
    education = RichTextField()
    about_self = RichTextField(null=True,blank=True)
    skills = RichTextField(null=True,blank=True)
    profile_pic=models.FileField(upload_to='profile_pic')
    cv = models.FileField(upload_to='resume')
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Company(models.Model):
    user=models.OneToOneField(JobUser,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='company_logo',null=True,blank=True)
    address = models.CharField(max_length=100)
    details = RichTextField()
    est = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.name
    
