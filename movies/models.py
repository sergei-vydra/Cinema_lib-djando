import datetime

from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Category(models.Model):
    """Catalog data object."""

    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Catalog"
        verbose_name_plural = "Catalogs"


class Actor(models.Model):
    """Actor data object."""

    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Actors and Director"
        verbose_name_plural = "Actors and Directors"


class Genre(models.Model):
    """Genre data object."""

    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Movie(models.Model):
    """Movie data object."""

    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100, default="")
    description = models.TextField()
    poster = models.ImageField(upload_to="movies/")
    year = models.PositiveSmallIntegerField(default=datetime.datetime.now().year)
    country = models.CharField(max_length=100)
    directors = models.ManyToManyField(Actor, verbose_name="directors", related_name="movie_director")
    actors = models.ManyToManyField(Actor, verbose_name="actors", related_name="movie_actor")
    genres = models.ManyToManyField(Genre, verbose_name="genres", related_name="movie_genre")
    world_premiere = models.DateField(default=now)
    budget = models.PositiveIntegerField(default=0, help_text="USD")
    fees_in_usa = models.PositiveIntegerField(default=0, help_text="USD")
    fees_in_world = models.PositiveIntegerField(default=0, help_text="USD")
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class MovieShot(models.Model):
    """MovieShots date object."""

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "MovieShot"
        verbose_name_plural = "MovieShots"


class RatingStar(models.Model):
    """RatingStar date object."""

    value = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "RatingStar"
        verbose_name_plural = "RatingStars"


class Rating(models.Model):
    """Rating data object."""

    ip = models.CharField(max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Star")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Movie", null=True)

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class Review(models.Model):
    """Review data object."""

    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey("self", verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
