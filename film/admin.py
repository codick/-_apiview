from django.contrib import admin
from .models import Films, Director, Genre, Poster

admin.site.register(Films)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Poster)
