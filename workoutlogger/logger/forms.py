from django import forms
from django.forms import formset_factory
from logger.models import User_Exercise, Exercise
from datetime import date

query = Exercise.objects.values()
exercise_choices = [('', '-----------')]
for exercise in query:
    exercise_choices.append((exercise['name'], exercise['name']))


class WorkoutLogForm(forms.Form):

    exercise = forms.ChoiceField(choices=exercise_choices)
    repititions = forms.IntegerField(label='Repititions')
    weight = forms.FloatField(label='Weight')


WorkoutLogFormset = formset_factory(WorkoutLogForm)

class SavedWorkoutNameForm(forms.Form):
    name = forms.CharField(max_length=50)

class SavedWorkoutLogForm(forms.Form):
    exercise = forms.ChoiceField(choices=exercise_choices)

SavedWorkoutLogFormset = formset_factory(SavedWorkoutLogForm)
