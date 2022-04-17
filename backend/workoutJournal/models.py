from django.db import models

# Create your models here.






class Exercises(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField()
    desription = models.CharField()

class Workouts(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(
        Exercises,
        through='Counts',
        through_fields=('workout', 'exercise')
        )

class Counts(models.Model):
    workout = models.ForeignKey(Workouts, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    reps = models.IntegerField()
    sets = models.IntegerField()