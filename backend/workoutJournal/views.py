from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, ExerciseSerializer
from .models import User, Exercise

# Create your views here.

class ExerciseView(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()