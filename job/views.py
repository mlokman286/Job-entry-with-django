from django.shortcuts import redirect, render
from django.contrib import messages
from job.filters import JobFilter
from job.foms import JobForm
from job.models import ApplyJob, Job
from userapp.models import JobUser, Resume
from django.contrib.auth.decorators import login_required

# Create your views here.
def joblist(request):
    # jobs=Job.objects.all().order_by('-published')
    jobs=JobFilter(request.GET,queryset=Job.objects.all().order_by('-published'))
    fulltimeJobs=Job.objects.filter(job_status='Full time').order_by('-published')
    parttimejobs=Job.objects.filter(job_status='Half time').order_by('-published')

    context={
        'jobs':jobs,
        'fulltimejobs':fulltimeJobs,
        'parttimejobs':parttimejobs,
        }
    return render(request,'job/joblist.html',context)

@login_required
def add_job(request):
    if request.user.user_type == 'Recruiter':
        if request.method == 'POST':
            form = JobForm(request.POST)

            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.user = request.user
                new_form.company= request.user.company
                new_form.save()

                messages.success(request,'Thanks for posting a job')
                return redirect('home')
        else:
            form = JobForm()
            return render(request,'job/addjob.html',{'form':form})
    else:
        messages.warning(request,'Permission denied ! only for recruiters')
        return redirect('home')


@login_required
def update_job(request,id):
    job = Job.objects.get(id=id)
    if job.user == request.user:
        if request.method == 'POST':
            form = JobForm(request.POST,instance=job)

            if form.is_valid():
                form.save()
                messages.success(request,'update Successfull')
                return redirect('dashboard')
        else:
            form = JobForm(instance=job)
            return render(request,'job/addjob.html',{'form':form})
    else:
        messages.warning(request,'Permission denied ! only for recruiters')
        return redirect('home')

@login_required 
def delete_job(request,id):
    job = Job.objects.get(id=id)
    if job.user == request.user:
        job.delete()
        return redirect('dashboard')
    else:
        print(job.user)
        messages.warning(request,'Your are not allowed to delete it')
        return redirect('dashboard')


def job_details(request,id):
    job=Job.objects.get(id=id)
    has_applied= False
    if request.user.is_authenticated:

        if ApplyJob.objects.filter(user=request.user,job=job).exists():
            has_applied = True
        else:
            has_applied= False
    
    context={
        'job':job,
        'has_applied':has_applied,
    }
    return render(request,'job/jobdetails.html',context)

@login_required
def apply_to_job(request,id):
    if request.user.has_resume and request.user.user_type=='Applicant':
        job = Job.objects.get(id=id)
        if ApplyJob.objects.filter(user=request.user,job=job).exists():
            messages.warning(request,'You already applied to this job')
            return redirect('joblist')
        else:
            ApplyJob.objects.create(
                job=job,
                user=request.user,
                status='Pending',
            )
            messages.success(request,'Applied Successfull')
            return redirect('joblist')
    else:
        messages.warning(request,'Create a Resume first')

@login_required
def applied_applicants(request,id):
    job= Job.objects.get(id=id)
    applicants = ApplyJob.objects.filter(job=job )
    context={
        'applicants':applicants,
        'job':job,
        }
    return render(request,'job/jobapplicants.html',context)

@login_required
def hired_applicants(request,id):
    applied_candidate = ApplyJob.objects.get(id=id)
    applied_candidate.status = 'Accepted'
    applied_candidate.save()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def declined_applicants(request,id):
    applied_candidate = ApplyJob.objects.get(id=id)
    applied_candidate.status = 'Declined'
    applied_candidate.save()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def sort_listed_applicants(request,id):
    applied_candidate = ApplyJob.objects.get(id=id)
    applied_candidate.status = 'sort-listed'
    applied_candidate.save()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def applicant_profile(request,id):
    applicant = Resume.objects.get(id = id)
    print('applicant',applicant)
    context={
        'profile':applicant,
    }
    return render(request,'user/profile.html',context)

@login_required
def applicant_list(request):
    if request.user.user_type =='Recruiter':
        applicants=Resume.objects.all().order_by('-id')
        return render(request,'job/applicant_list.html',{'applicants':applicants})
    else:
        messages.warning(request,'Permission denied !Ony for recruiters.')
        return redirect('home')
    
@login_required
def cancel_application(request,id):
    application = ApplyJob.objects.get(id=id,user=request.user)
    application.delete()
    return redirect(request.META.get('HTTP_REFERER'))