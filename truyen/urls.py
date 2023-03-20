from django.urls import re_path as url
from django.urls import path
from .views import TruyenApiView

urlpatterns = [
    path('views/', TruyenApiView.as_view()),

]
