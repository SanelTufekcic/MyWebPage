from django.shortcuts import render
from rest_framework import generics
from .models import Profile, Project
from .serializers import ProfileSerializer, ProjectSerializer

# Create your views here.

class ProfileView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProjectView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
