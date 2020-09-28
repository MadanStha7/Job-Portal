from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def homePage(request):
    job = Job.objects.all()
    company = Company.objects.all()
    context = {'job': job, 'company': company}
    return render(request, "JobApp/dashboard.html", context)


def companyPage(request):
    company = Company.objects.all()
    return render(request, "JobApp/company.html", {'company': company})


def jobPage(request):
    job = Job.objects.all()
    return render(request, "JobApp/jobs.html", {'job': job})


def jobseeker_profile(request):
    job_seeker = JobSeeker.objects.all()
    return render(request, "JobApp/jobseeker_profile.html", {'job_seeker': job_seeker})


def company_profile(request):
    return render(request, "JobApp/company_profile.html")


def loginPage(request):
    return render(request, "JobApp/login.html")


def jobseeker_registerPage(request):
    return render(request, "JobApp/register.html")


def company_registerPage(request):
    return render(request, "JobApp/company_register.html")


def cv_builder(request):
    return render(request, "JobApp/cv_builder.html")


def post_job(request):
    return render(request, "JobApp/Post_job.html")
