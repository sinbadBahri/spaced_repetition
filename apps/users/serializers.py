from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    """
    A serializer class that is used to serialize and deserialize data for user registration.
    """
    password = serializers.CharField(max_length=48, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'date_of_birth', 'language', 'company', 'password')

    def create(self, validated_data):
        """
        This method is responsible for creating a new user instance based on the validated data provided.
        It uses the create_user method from the User model to create the user.
        """
        return User.objects.create_user(**validated_data)
