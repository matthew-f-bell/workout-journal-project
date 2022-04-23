from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CountSerializer, UserSerializer, ExerciseSerializer, WorkoutSerializer
from .models import Count, User, Exercise, Workout

# Create your views here.

class ExerciseView(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()

class WorkoutView(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    queryset = Workout.objects.all()

class CountView(viewsets.ModelViewSet):
    serializer_class = CountSerializer
    queryset = Count.objects.all()

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()