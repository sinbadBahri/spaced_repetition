from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=48, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'date_of_birth', 'language', 'company', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
