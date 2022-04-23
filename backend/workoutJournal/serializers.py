from rest_framework import serializers
from .models import Count, User, Exercise, Workout

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password','first_name', 'last_name', 'date_joined', 'user_height', 'user_weight', 'image', 'is_staff', 'is_superuser')

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'creator', 'name', 'description')

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ('id', 'creator', 'name', 'exercises')

class CountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Count
        fields = ('id', 'workout', 'exercise', 'reps', 'sets')