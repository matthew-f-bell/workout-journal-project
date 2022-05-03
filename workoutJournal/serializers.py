from rest_framework import serializers
from .models import Count, User, Exercise, Workout
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.core.exceptions import ObjectDoesNotExist

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'email', 'password','first_name', 'last_name', 'date_joined', 'user_height', 'user_weight', 'image', 'is_staff', 'is_superuser')

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('pk', 'creator', 'name', 'description')

class CountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Count
        fields = ('pk', 'workout', 'exercise', 'reps', 'sets')

class WorkoutSerializer(serializers.ModelSerializer):
    Exercises = CountSerializer(source='count_set', many=True)
    Creator = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = ('pk', 'Creator', 'name', 'Exercises')
    
    def get_Creator(self, obj):
        return {'pk': obj.creator.pk, 'first_name': obj.creator.first_name, 'last_name': obj.creator.last_name}


    


class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data

class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True, write_only=True, max_length=128)

    class Meta: 
        model = User
        fields = ['pk', 'email', 'password']

    def create(self, validated_data):
        try:
            user = User.objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:
            user = User.objects.create_user(**validated_data)
        
        return user

class UpdateUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'user_height', 'user_weight', 'image')

    def update(self, instance, validated_data):
        # We try to get profile data
        user_data = validated_data.pop('user', None)
        # If we have one
        if user_data is not None:
            # We set address, assuming that you always set address
            # if you provide user
            instance.user.first_name = user_data['first_name']
            instance.user.last_name = user_data['last_name']
            instance.user.user_height = user_data['user_height']
            instance.user.user_weight = user_data['user_weight']
            instance.user.image = user_data['image']
            instance.user.save()
        # Rest will be handled by DRF
        return super().update(instance, validated_data)
