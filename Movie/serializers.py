from rest_framework import serializers 
from .models import Profile,Category,Movie,Rate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from drf_extra_fields.fields import Base64ImageField

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        profile =  Profile.objects.create(user=user,id=user.id)
        return user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email','is_superuser')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

class LoginAdminSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
    
        if user and user.is_active and  user.is_superuser:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
class profileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model= Profile
        fields = '__all__'
    # def validate(self, data):
    #     model = Profile
    #     print ("manhasdada",model.deleted)
    #     if model and not model.deleted :
    #         return model
    #     raise serializers.ValidationError("Incorrect Credentials")

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =  Category
        fields = '__all__'
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Movie
        fields = '__all__'
    def validate(self, data):
        model = authenticate(**data)
    
        if model and not model.deleted :
            return model
        raise serializers.ValidationError("Incorrect Credentials")

class RateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Rate
        fields = '__all__'


