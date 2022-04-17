from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager







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
