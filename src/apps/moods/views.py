from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Mood
from .serializer import MoodSerializer

# Create your views here.
class MoodViewSet(ModelViewSet):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer