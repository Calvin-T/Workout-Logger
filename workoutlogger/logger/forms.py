from django import forms
from django.forms import formset_factory
from logger.models import User_Exercise, Exercise
from datetime import date

exercise_choices = (
    ("Incline Bench Press (Dumbbell)", "Incline Bench Press (Dumbbell)"),
    ("Incline Bench Press (Barbell)", "Incline Bench Press (Barbell)"),
    ("Bent Over Row (Dumbbell)", "Bent Over Row (Dumbbell)"),
    ("Bent Over Row (Barbell)", "Bent Over Row (Barbell)"),
    ("Bench Press (Dumbbell)", "Bench Press (Dumbbell)"),
    ("Bench Press (Barbell)", "Bench Press (Barbbell)"),

)

class WorkoutLogForm(forms.Form):

    exercise = forms.ChoiceField(choices=exercise_choices)
    date = forms.DateField(label='Date', initial=date.today())
    #category = forms.CharField(label='Category')
    repititions = forms.IntegerField(label='Repititions', initial=0)
    weight = forms.FloatField(label='Weight', initial=0)
#    time = forms.IntegerField(label='Time', initial=0)
#    distance = forms.FloatField(label='Distance', initial=0)

WorkoutLogFormset = formset_factory(WorkoutLogForm)
