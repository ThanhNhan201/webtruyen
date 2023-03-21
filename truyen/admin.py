from django.contrib import admin

# Register your models here.
from . models import Comment, Rate
# Register your models here.
@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ('truyen', 'user', 'comment')

@admin.register(Rate)
class Comment(admin.ModelAdmin):
    list_display = ('truyen', 'user', 'rate')