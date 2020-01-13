from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import WorkoutLogForm
from .models import Exercise, WorkoutSession, User_Exercise, Category



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

    if request.method == 'POST':
        form = WorkoutLogForm(request.POST)
        if form.is_valid():
            #category = Category.objects.all().filter(category="Chest")
            exercise = Exercise.objects.all().filter(name=form.cleaned_data.get('exercise')).first()
            print(exercise.name)
            workout_session = WorkoutSession(user=request.user, date=form.cleaned_data.get('date'))
            workout_session.save()
            user_exercise = User_Exercise(
                exercise=exercise,
                workout_session=workout_session,
                repititions=form.cleaned_data.get('repititions'),
                weight=form.cleaned_data.get('weight'),
                time=form.cleaned_data.get('time'),
                distance=form.cleaned_data.get('distance')
            )
            user_exercise.save()
    form = WorkoutLogForm()
    return render(request, "logger/log_workout.html", {'active_page': 'Log Workout', 'form': form})

def workout_log(request):

    queryset = User_Exercise.objects.all()
    return render(request, "logger/workout_log.html", {'queryset': queryset})
