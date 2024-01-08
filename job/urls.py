from django.urls import path

from job import views


urlpatterns = [
    path('',views.joblist ,name='joblist'),
    path('addjob',views.add_job ,name='addjob'),
    path('update/<str:id>',views.update_job ,name='update'),
    path('apply/<str:id>',views.apply_to_job ,name='apply'),
    path('delete/<str:id>',views.delete_job ,name='delete'),
    path('jobdetails/<str:id>',views.job_details ,name='jobdetails'),
    path('applied_applicants/<str:id>',views.applied_applicants ,name='applied_applicants'),
    path('applicant/<str:id>',views.applicant_profile ,name='applicant'),
    path('applicant_list',views.applicant_list ,name='applicant_list'),
    path('cancel/<str:id>',views.cancel_application ,name='cancel'),
    path('hired/<str:id>',views.hired_applicants ,name='hired'),
    path('sort-listed/<str:id>',views.sort_listed_applicants ,name='sort-listed'),
    path('declined/<str:id>',views.declined_applicants ,name='declined'),
]
