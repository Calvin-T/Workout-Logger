from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import WorkoutLogForm, WorkoutLogFormset
from .models import Exercise, WorkoutSession, User_Exercise, Category
from django.forms import formset_factory



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

    if request.user.is_authenticated:
        if request.method == 'POST':
            formset = WorkoutLogFormset(request.POST)
            if formset.is_valid():
                date = request.POST.get('date')
                user = request.user
                workout_session = WorkoutSession(user=user, date=date)
                workout_session.save()
                for form in formset:
                    print("==================================")
                    exercise = Exercise.objects.all().filter(name=form.cleaned_data.get('exercise')).first()
                    if exercise == None:
                        print('here')
                    # workout_session= WorkoutSession.objects.all().filter(user=user, date = date).first()
                    # if workout_session == None:
                    #     workout_session = WorkoutSession(user=user, date=date)
                    #     workout_session.save()

                    user_exercise = User_Exercise(
                        exercise=exercise,
                        workout_session=workout_session,
                        repititions=form.cleaned_data.get('repititions'),
                        weight=form.cleaned_data.get('weight'),
                    )
                    user_exercise.save()

                return redirect('logger-dashboard')

        else:
            formset = WorkoutLogFormset()
        return render(request, "logger/log_workout.html", {'active_page': 'Log Workout', 'formset': formset})
    else:
        return redirect('logger-landing-page')

def logged_sessions(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            sessions = WorkoutSession.objects.filter(user=request.user).order_by('-date')
            return render(request, "logger/log_history.html", {'active_page': 'Log History', 'sessions': sessions})
        elif request.method == 'POST':
            id = request.POST.get('id')
            session = WorkoutSession.objects.filter(id=id).first()
            sets = User_Exercise.objects.filter(workout_session=session)
            return render(request, "logger/log_history.html", {'active_page': 'Log History', 'sessions': None, 'session': session, 'sets': sets})
    else:
        return redirect('logger-landing-page')
