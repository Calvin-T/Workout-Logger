from django.shortcuts import render, redirect
from django.http import HttpResponse

def landing(request):
    if request.user.is_authenticated:
        return redirect('logger-dashboard')
    else:
        return render(request, "logger/landing-page.html")

def dashboard(request):
    if request.user.is_authenticated:
        print("LOGGED IN AS" + request.user.email)
        #should fix this back to dashboard.html
        return render(request, "logger/dashboard.html", {'active_page': 'Dashboard'})
    else:
        return redirect('logger-landing-page')

def log_workout(request):
    return render(request, "logger/log_workout.html", {'active_page': 'Log Workout'})
