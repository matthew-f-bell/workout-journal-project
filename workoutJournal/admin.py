from django.contrib import admin
from .models import User, Exercise, Workout, Count

# Register your models here.
admin.site.register(User)
admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(Count)