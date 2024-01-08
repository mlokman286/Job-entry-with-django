from django.shortcuts import redirect, render
from job.filters import JobFilter

from job.models import ApplyJob, Category, Job, State

# Create your views here.
def home(request):
    categories=Category.objects.all()
    states=State.objects.all()

    filter=JobFilter(request.GET,queryset=Job.objects.all().order_by('-published'))
    jobs=filter.qs
    fulltimeJobs=Job.objects.filter(job_status='Full time').order_by('-published')[:5]
    parttimejobs=Job.objects.filter(job_status='Half time').order_by('-published')[:5]
    context={
        'filter':filter,
        'jobs':jobs,
        'fulltimejobs':fulltimeJobs,
        'parttimejobs':parttimejobs,
        'categories':categories,
        'states':states,
    }
    return render(request,'website/home.html',context)

def about(request):
    return render(request,'website/about.html')

def contact(request):
    return render(request,'website/contact.html')

def testimonial(request):
    return render(request,'website/testimonial.html')

def dashboard(request):
    if request.user.user_type == 'Applicant':
        jobs= ApplyJob.objects.filter(user=request.user)
        context={'jobs':jobs}
    elif request.user.user_type == 'Recruiter':
        jobs = Job.objects.filter(user=request.user,company=request.user.company)
        context={'jobs':jobs}
    return render(request,'website/dashboard.html',context)

