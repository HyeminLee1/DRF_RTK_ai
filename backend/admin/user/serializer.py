from django.contrib.auth import authenticate
from rest_framework import serializers
# pip install Django django-rest-framework
from .models import User as user

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    email = serializers.CharField()
    birth = serializers.CharField()
    address = serializers.CharField()

    class Meta:
        model = user
        fields = '__all__'

    def create(self, validated_data):
        return user.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user.objects.filter(pk=instance.username).update(**validated_data)

    def login(self, validated_data):
        user = authenticate(**validated_data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")