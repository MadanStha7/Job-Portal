from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('company/', views.companyPage, name='company'),
    path('job/', views.jobPage, name='job'),

]
