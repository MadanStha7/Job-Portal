from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homePage(request):
    return render(request, "JobApp/dashboard.html")


def loginPage(request):
    return render(request, "JobApp/login.html")


def registerPage(request):
    return render(request, "JobApp/register.html")


def companyPage(request):
    return render(request, "JobApp/company.html")


def jobPage(request):
    return render(request, "JobApp/jobs.html")
