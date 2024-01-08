from django.db import models
from ckeditor.fields import RichTextField
from userapp.models import Company, JobUser

# Create your models here.
class State(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Job(models.Model):
    JOB_Type=(
        ('Remote','Remote'),
        ('Onsite','Onsite'),
        ('Hybrid','Hybrid'),
    )
    
    JOB_STATUS=(
        ('Full time','Full time'),
        ('Half time','Half time'),
        ('Hourly','Hourly'),
    )

    user=models.ForeignKey(JobUser, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(Company, on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=500)
    job_type=models.CharField(max_length=100,choices=JOB_Type)
    job_status=models.CharField(max_length=100,choices=JOB_STATUS)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    salary=models.CharField(max_length=100)
    location=models.CharField(max_length=1000)
    state=models.ForeignKey(State, on_delete=models.CASCADE,null=True,blank=True)
    vacancy=models.CharField(max_length=100)
    responsibilities=RichTextField()  
    requirments=RichTextField()
    published=models.DateTimeField(auto_now=False, auto_now_add=True,null=True,blank=True)
    deadline=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.title
    
class ApplyJob(models.Model):
    STATUS_CHOICES = {
        ('Accepted','Accepted'),
        ('Declined','Declinned'),
        ('Pending','Pending'),
        ('sort-listed','sort-listed'),
    }
    user= models.ForeignKey(JobUser, on_delete=models.CASCADE)
    job= models.ForeignKey(Job, on_delete=models.CASCADE)
    appliedTime=models.DateTimeField(auto_now=False, auto_now_add=True)
    status=models.CharField(max_length=100,choices=STATUS_CHOICES,default='Pending')
