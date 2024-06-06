from django.contrib.auth.models import User
# Import the built-in User model provided by Django for handling users.

from rest_framework import serializers
# Import the serializers module from Django REST framework to create serializers.
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    # Define a serializer class for the User model using ModelSerializer for automatic field generation.
    class Meta:
        model = User
        # Specify the model that the serializer is for, which is the User model.
        fields = ["id", "username", "password"]
        # Define the fields from the User model that will be included in the serialized representation.
        extra_kwargs = {"password": {"write_only": True}}
        # Specify additional keyword arguments for the fields. Here, making the password write-only to ensure it's not exposed in read operations.
    def create(self, validated_data):
        # Override the create method to handle user creation with hashed passwords.
        user = User.objects.create_user(**validated_data)
        # Create a new user instance using the create_user method, which handles password hashing and other necessary steps.
        return user
        # Return the created user instance.

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note  
        fields = ["id", "title", "content", "created_at", "authr"]
        extra_kwargs = {"author": {"read_only": True}}  

