from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ExtendUser,UserSubscripiton

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ExtendUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendUser
        fields = '__all__'

class UserSubscripitonSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscripiton
        fields = '__all__'