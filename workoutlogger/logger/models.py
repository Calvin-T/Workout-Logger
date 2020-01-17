from django.db import models
from users.models import CustomUser as User

class Category(models.Model):
    category = models.CharField(max_length=50)



class Exercise(models.Model):
    name = models.CharField(max_length=50, primary_key=True, null=False)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)


class WorkoutSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

class User_Exercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    workout_session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE, default=None)
    repititions = models.IntegerField(null = True, blank=True)
    weight = models.IntegerField(null = True, blank=True)
    #time = models.IntegerField(null = True, blank=True)
    #distance = models.IntegerField(null = True, blank=True)
