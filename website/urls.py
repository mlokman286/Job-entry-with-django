from django.urls import path
from website import views


urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('dashboard',views.dashboard,name='dashboard'),
]
