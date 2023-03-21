from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User

class Truyen(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    follow_up = models.IntegerField(default=0)
    content = content = models.TextField(blank=True)
    removed = models.BooleanField(default=False)
    number_of_rating = models.IntegerField(default=0)
    number_of_comment = models.IntegerField(default=0)

class Comment(models.Model):
    truyen = models.ForeignKey(Truyen, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    removed = models.BooleanField(default=False)
    def __str__(self):
        return str(self.truyen)