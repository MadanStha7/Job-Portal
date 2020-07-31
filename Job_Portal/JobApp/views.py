from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homePage(request):
    return render(request, "JobApp/dashboard.html")


def loginPage(request):
    return render(request, "JobApp/login.html")


def jobseeker_registerPage(request):
    return render(request, "JobApp/register.html")

def company_registerPage(request):
    return render(request, "JobApp/company_register.html")


def companyPage(request):
    return render(request, "JobApp/company.html")


def jobPage(request):
    return render(request, "JobApp/jobs.html")
