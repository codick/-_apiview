from django.urls import path
from .views import *

urlpatterns = [
    path('films/', FilmList.as_view()),
    path('films/<int:pk>/', FilmView.as_view()),
    path('directors/', DirectorList.as_view()),
    path('directors/<int:pk>', DirectorView.as_view()),
    path('genres/', GenreList.as_view()),
    path('genres/<int:pk>/', GenreView.as_view()),
    path('posters/', PosterList.as_view()),
    path('posters/<int:pk>/', PosterView.as_view()),
]
