from django.shortcuts import render
# Import the render shortcut to render templates, although it's not used in this view.
from django.contrib.auth.models import User
# Import the built-in User model provided by Django for handling users.
from rest_framework import generics
# Import generics from Django REST framework to create generic views.
from .serializers import UserSerializer, NoteSerializer
# Import the UserSerializer that was defined in the serializers module.
from rest_framework.permissions import IsAuthenticated, AllowAny
# Import permission classes to handle view access control.
from .models import Note


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    # Define a view class for creating a new user using the generic CreateAPIView.
    queryset = User.objects.all()
    # Specify the queryset that the view will operate on, which is all User instances.
    serializer_class = UserSerializer
    # Specify the serializer class to be used for validating and deserializing input and serializing output.
    permission_classes = [AllowAny]
    # Specify the permission classes. AllowAny means that any user, authenticated or not, can access this view.


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)    


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    