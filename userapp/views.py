from django.shortcuts import redirect, render
from userapp.fomrs import CompanyForm, ResumeForm, SingupForm
from django.contrib import messages
from userapp.models import Company, JobUser, Resume
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form=SingupForm(request.POST)
            if form.is_valid():
                form.save()
                messages.info(request,'Your account has been created.')
                return redirect('login')
            else:
                messages.warning(request,'In valid fields')
                return redirect('signup')
        else:
            form= SingupForm()
            context = {'form':form}
            return render(request,'registration/signup.html',context)
    else:
        messages.info(request,'you already logged in.')
        return redirect('home')

def applicant_profile(request):
    if request.user.has_resume:
        profile= request.user.resume
        return render(request,'user/profile.html',{'profile':profile})
    else:
        messages.warning(request,"Permission Denied ! you must have to be a applicant or a resume")
        return redirect('home')

@login_required
def user_resume(request):
    if request.user.user_type == 'Applicant':
        resume, created = Resume.objects.get_or_create(user=request.user)
        if request.method == 'POST':
            form = ResumeForm(request.POST,request.FILES,instance=resume)

            if form.is_valid():
                new_form = form.save(commit=False)
                user = JobUser.objects.get(id=request.user.id)
                user.has_resume = True
                user.save()
                new_form.save()

                messages.success(request,'Resume creation successfull')
                return redirect('home')
        else:
            form = ResumeForm(instance=resume)
            return render(request,'user/resume.html',{'form':form})
    else:
        messages.warning(request,'Permission denied ! only for applicants')
        return redirect('home')
    
@login_required
def user_compay(request):
    if request.user.user_type == 'Recruiter':
        company, created = Company.objects.get_or_create(user=request.user)
        if request.method == 'POST':
            form = CompanyForm(request.POST,request.FILES,instance=company)

            if form.is_valid():
                new_form = form.save(commit=False)
                user = JobUser.objects.get(id=request.user.id)
                user.has_company = True
                user.save()
                new_form.save()

                messages.success(request,'Company info saved successfull')
                return redirect('home')
        else:
            form = CompanyForm(instance=company)
            return render(request,'user/company.html',{'form':form})
    else:
        messages.warning(request,'Permission denied ! only for recruiters')
        return redirect('home')
