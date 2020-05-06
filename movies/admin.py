from django.contrib import admin
from movies.models import (Category, Movie, Actor, Genre,  MovieShot, Review, RatingStar, Rating)

admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(MovieShot)
admin.site.register(Review)
admin.site.register(RatingStar)
admin.site.register(Rating)
