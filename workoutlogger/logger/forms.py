from django import forms
from logger.models import User_Exercise, Exercise
from datetime import date

class WorkoutLogForm(forms.Form):

    exercise = forms.ModelChoiceField(queryset=Exercise.objects.all())
    date = forms.DateField(label='Date', initial=date.today())
    #category = forms.CharField(label='Category')
    repititions = forms.IntegerField(label='Repititions', initial=0)
    weight = forms.FloatField(label='Weight', initial=0)
    time = forms.IntegerField(label='Time', initial=0)
    distance = forms.FloatField(label='Distance', initial=0)
