from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=30, primary_key=True)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()

class Exercise(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    set = models.ManyToManyField(User, through='User_Exercise')

class User_Exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    repitions = models.IntegerField(null = True)
    weight = models.IntegerField(null = True)
    time = models.IntegerField(null = True)
    distance = models.IntegerField(null = True)

    date = models.DateField()
