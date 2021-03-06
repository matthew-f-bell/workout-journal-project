from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import CountSerializer, UpdateUserSerializer, UserSerializer, ExerciseSerializer, WorkoutSerializer, LoginSerializer, RegisterSerializer
from .models import Count, User, Exercise, Workout
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView
import json

# Create your views here.

class ExerciseView(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()

class WorkoutView(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    # serializer_classes = {
    #     'count': CountSerializer,
    #     'exercise': ExerciseSerializer,
    # }
    #default_serializer_class = WorkoutSerializer

    # def get_serializer_class(self):
    #     return self.serializer_classes.get(self.action, self.default_serializer_class)

    queryset = Workout.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        new_workout = Workout.objects.create(name=data['name'], creator=User.objects.get(id=data['creator']))
        new_workout.save()
        print("test")
        print(json.loads(request.POST.get('Exercises')))
        for exercise in json.loads(request.POST.get('Exercises')):
            exercise_obj = Exercise.objects.get(id=exercise['id'])
            new_workout.exercises.add(exercise_obj)
            count_obj = Count.objects.get(workout=new_workout.id)
            count_obj.reps = exercise['reps']
            count_obj.sets = exercise['sets']
            count_obj.save()

        serializer=WorkoutSerializer(new_workout)
        return Response(serializer.data)

class CountView(viewsets.ModelViewSet):
    serializer_class = CountSerializer
    queryset = Count.objects.all()

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = User.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj

class UserDetail(viewsets.ModelViewSet, RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdate(viewsets.ModelViewSet):
    # API endpoint that allows a User record to be updated.
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = (IsAuthenticated,)

class LoginViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class RegistrationViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response({
            "user": serializer.data,
            "refresh": res["refresh"],
            "token": res["access"]
        }, status=status.HTTP_201_CREATED)

