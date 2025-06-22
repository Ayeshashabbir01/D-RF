from .models import Singer, Song
from rest_framework import serializers

# 🔵 Pehle SongSerializer define karo
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'singer']

# 🔵 Phir SingerSerializer define karo
class SingerSerializer(serializers.ModelSerializer):
    sungby = SongSerializer(many=True, read_only=True)  # Make sure related_name='sungby' is in the model

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'sungby']
