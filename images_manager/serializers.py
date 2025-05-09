from rest_framework import serializers
from images_manager.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'description', 'image_data', 'uploaded_at']
