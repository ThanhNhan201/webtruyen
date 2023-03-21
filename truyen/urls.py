from django.urls import re_path as url
from django.urls import path
from .views import TruyenApiView, TruyenDetailView, ViewSortAPI, DateSortAPI, CommentAPI
from .views import CommentDetailAPI
urlpatterns = [
    path('views/', TruyenApiView.as_view()),
    path('views/<int:id>', TruyenDetailView.as_view()),
    path('viewsort', ViewSortAPI.as_view()),
    path('datesort', DateSortAPI.as_view()),
    path('comment/<int:id>', CommentAPI.as_view()),
    path('put_comment/<int:id>', CommentDetailAPI.as_view())
]
