from django.db import models
from djangoratings.fields import RatingField

# Create your models here.


class Truyen(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    rating = RatingField(range=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    follow_up = models.IntegerField(default=0)
    content = content = models.TextField(blank=True)
    removed = models.BooleanField(default=False)
