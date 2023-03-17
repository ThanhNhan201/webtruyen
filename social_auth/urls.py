
from django.urls import re_path as url, include,path
from . import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', views.LoginFacebook),
]