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
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'user_height', 'user_weight', 'image')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'user_height': {'required': False},
            'user_weight': {'required': False},
            'image': {'required': False},
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value


    def update(self, instance, validated_data):
        user = self.context['request'].user
        
        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})
        
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']

        instance.save()

        return instance