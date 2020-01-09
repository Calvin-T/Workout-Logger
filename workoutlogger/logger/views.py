from django.shortcuts import render
from django.http import HttpResponse

def landing(request):
    return render(request, "logger/landing-page.html")

def dashboard(request):
    if request.user.is_authenticated:
        print("LOGGED IN AS" + request.user.email)
        #should fix this back to dashboard.html
        return render(request, "logger/dashboard-template.html")
    else:
        return render(request, "logger/landing-page.html")
