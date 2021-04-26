from rest_framework import serializers
from .models import PageFeatures



class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageFeatures
        fields = ['id', 'video_id', 'comment', 'like']