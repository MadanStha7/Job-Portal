from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.jobseeker_registerPage, name='register'),
    path('company_register/', views.company_registerPage, name='company_register'),
    path('company/', views.companyPage, name='company'),
    path('job/', views.jobPage, name='job'),
    path('jobseeker_profile/', views.jobseeker_profile, name='jobseeker_profile'),
    path('company_profile/', views.company_profile, name='company_profile'),
    path('cv_builder/', views.cv_builder, name='cv_builder'),
    path('post_job/', views.post_job, name='post_job'),
]
