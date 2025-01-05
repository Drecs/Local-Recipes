from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Recipe(models.Model):
        title = models.CharField(max_length=200)
        description = models.TextField()
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
