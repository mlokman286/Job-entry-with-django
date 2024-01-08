from django.urls import  path
from userapp import views


urlpatterns = [
    path('',views.signup,name='signup'),
    path('profile',views.applicant_profile,name='profile'),
    path('resume',views.user_resume,name='resume'),
    path('company',views.user_compay,name='company'),
]
