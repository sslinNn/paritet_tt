from rest_framework import generics

from images_manager.models import Image
from images_manager.serializers import ImageSerializer


class ImageCreateAPIView(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageListAPIView(generics.ListAPIView):
    queryset = Image.objects.all().order_by('-uploaded_at')
    serializer_class = ImageSerializer


class ImageDeleteAPIView(generics.DestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'id'
