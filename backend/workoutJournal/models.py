from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager







# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(default=timezone.now)
    user_height = models.IntegerField(default=60)
    user_weight = models.IntegerField(default=150)
    image = models.ImageField(upload_to='images/')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Exercise(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Workout(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    exercises = models.ManyToManyField(
        Exercise,
        through='Count',
        through_fields=('workout', 'exercise')
        )
    
    def __str__(self):
        return self.name

class Count(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.IntegerField()
    sets = models.IntegerField()

    def __str__(self):
        return (self.workout+":"+self.exercise)