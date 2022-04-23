from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, ExerciseSerializer, WorkoutSerializer
from .models import User, Exercise, Workout

# Create your views here.

class ExerciseView(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()

class WorkoutView(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    queryset = Workout.objects.all()