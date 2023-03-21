from django.contrib import admin

# Register your models here.
from . models import Comment
# Register your models here.
@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ('truyen', 'user', 'comment')