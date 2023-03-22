from django.db import models


class Films(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=100)
    director = models.ForeignKey("Director", on_delete=models.CASCADE)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)


class Director(models.Model):
    fullname = models.CharField(max_length=255)
    born_date = models.DateTimeField()


class Genre(models.Model):
    name = models.CharField(max_length=255, default='genre')


class Poster(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    films = models.ForeignKey("Films", on_delete=models.CASCADE)
