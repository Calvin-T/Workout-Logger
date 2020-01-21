from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import WorkoutLogForm, WorkoutLogFormset, SavedWorkoutNameForm, SavedWorkoutLogForm, SavedWorkoutLogFormset
from .models import Exercise, WorkoutSession, User_Exercise, Category, WorkoutName, WorkoutName_Exercise
from django.forms import formset_factory
from django.urls import reverse



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

                messages.success(request, f'Successfully logged new workout!')
                return redirect('logger-logged-sessions')

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
            operation = request.POST.get('operation')
            if operation == "select":
                session = WorkoutSession.objects.filter(id=id).first()
                sets = User_Exercise.objects.filter(workout_session=session)
                return render(request, "logger/log_history.html", {'active_page': 'Log History', 'sessions': None, 'session': session, 'sets': sets})
            else:
                WorkoutSession.objects.filter(id=id).delete()
                messages.success(request, f'Successfully deleted workout!')
                return redirect('logger-logged-sessions')
    else:
        return redirect('logger-landing-page')


def save_workout(request):

    if request.user.is_authenticated:

        if request.method == 'POST':
            operation = request.POST.get('operation')

            if operation == 'redirect':
                return redirect('logger-logged-templates')

            form = SavedWorkoutNameForm(request.POST)
            formset = SavedWorkoutLogFormset(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get('name')
                workout_name = WorkoutName(
                    name=name,
                    user=request.user
                )
                workout_name.save()
            if formset.is_valid():
                for fs in formset:
                    exercise = Exercise.objects.all().filter(name=fs.cleaned_data.get('exercise')).first()
                    save_exercise = WorkoutName_Exercise(
                        name = workout_name,
                        exercise = exercise
                        )
                    save_exercise.save()
            return redirect('logger-logged-templates')
        form = SavedWorkoutNameForm()
        formset = SavedWorkoutLogFormset()
        return render(request, "logger/save_workout.html", {'active_page': 'Save Workout', 'form': form, 'formset': formset})

    else:
        return redirect('logger-landing-page')


def logged_templates(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            templates = WorkoutName.objects.filter(user=request.user)
            return render(request, "logger/create_template.html", {'active_page': 'Create Template', 'templates': templates})
        elif request.method == 'POST':
            operation = request.POST.get('operation')
            if operation == 'redirect':
                return redirect('logger-save-workout')
            elif operation == 'select':
                id = request.POST.get('id')
                print(id)
                template = WorkoutName.objects.filter(id=id).first()
                exercises = WorkoutName_Exercise.objects.filter(name=template)
                return render(request, "logger/create_template.html", {'active_page': 'Create Template', 'templates': None, 'template': template, 'exercises': exercises })
            elif operation == 'log':
                template_name = request.POST.get('template')
                print("======================")
                print(template_name)

                workout_name = WorkoutName.objects.filter(name=template_name, user=request.user).first()
                queryset = WorkoutName_Exercise.objects.filter(name=workout_name)
                print(queryset)
                list = []
                for x in queryset:
                    form = WorkoutLogForm(initial = {'exercise': x.exercise.name, 'repititions': 0, 'weight': 0})
                    list.append(x.exercise.name)
                    print(x.exercise.name)

                formset = WorkoutLogFormset(initial = [{'exercise': x}for x in list])
                return render(request, "logger/log_workout.html", {'active_page': 'Log Workout', 'formset': formset})

            elif operation == 'log_workout':
                formset = WorkoutLogFormset(request.POST)
                if formset.is_valid():
                    log(formset, request.POST.get('date'), request.user)
                    messages.success(request, f'Successfully logged new workout!')
                    return redirect('logger-logged-sessions')
            elif operation == 'delete':
                id = request.POST.get('id')
                WorkoutName.objects.filter(id=id).delete()
                messages.success(request, f'Successfully deleted workout!')
                return redirect('logger-logged-templates')
    else:
        return redirect('logger-landing-page')

def log(formset, date, user):
    workout_session = WorkoutSession(user=user, date=date)
    workout_session.save()
    for form in formset:
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
