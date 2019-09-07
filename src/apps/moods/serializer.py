from rest_framework import serializers
from .models import Mood

class MoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mood
        exclude = ('created_at', 'updated_at',)