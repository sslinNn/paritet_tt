from django.urls import path

from images_manager.views import ImageCreateAPIView, ImageListAPIView, ImageDeleteAPIView

urlpatterns = [
    path('upload/', ImageCreateAPIView.as_view(), name='upload-image'),
    path('list/', ImageListAPIView.as_view(), name='list-images'),
    path('<int:id>/', ImageDeleteAPIView.as_view(), name='delete-image'),
]
