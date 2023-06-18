from django.conf import settings
from django.db import models

from users.models import User


class Ad(models.Model):
    # TODO добавьте поля модели здесь
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="ad_image", blank=True, null=True)

    class Meta:
        ordering = ["-created_at"]


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
