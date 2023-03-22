from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Films, Genre, Poster, Director
from .serializers import FilmSerializer, GenreSerializer, PosterSerializer, DirectorSerializer


class FilmList(ListCreateAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmSerializer


class FilmView(RetrieveUpdateDestroyAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmSerializer


class GenreList(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PosterList(ListCreateAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer


class PosterView(RetrieveUpdateDestroyAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer


class DirectorList(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
