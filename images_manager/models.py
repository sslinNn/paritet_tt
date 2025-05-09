from django.db import models


class Image(models.Model):
    image_data = models.TextField()
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}: {self.description[:30]}"
