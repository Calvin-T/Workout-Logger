from django.contrib import admin
from .models import Exercise, User_Exercise, Category, WorkoutSession, WorkoutName, WorkoutName_Exercise

admin.site.register(Exercise)
admin.site.register(User_Exercise)
admin.site.register(Category)
admin.site.register(WorkoutSession)
admin.site.register(WorkoutName)
admin.site.register(WorkoutName_Exercise)
