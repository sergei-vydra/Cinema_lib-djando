# Generated by Django 3.0.6 on 2020-05-07 19:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Actor",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("age", models.PositiveSmallIntegerField(default=0)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="actors/")),
            ],
            options={
                "verbose_name": "Actors and Directors",
                "verbose_name_plural": "Actors and Directors",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("url", models.SlugField(max_length=150, unique=True)),
            ],
            options={
                "verbose_name": "Catalogs",
                "verbose_name_plural": "Catalogs",
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("url", models.SlugField(max_length=150, unique=True)),
            ],
            options={
                "verbose_name": "Genres",
                "verbose_name_plural": "Genres",
            },
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                ("tagline", models.CharField(default="", max_length=100)),
                ("description", models.TextField()),
                ("poster", models.ImageField(upload_to="movies/")),
                ("year", models.PositiveSmallIntegerField(default=2020)),
                ("country", models.CharField(max_length=100)),
                ("world_premiere", models.DateField(default=django.utils.timezone.now)),
                ("budget", models.PositiveIntegerField(default=0, help_text="USD")),
                ("fees_in_usa", models.PositiveIntegerField(default=0, help_text="USD")),
                ("fees_in_world", models.PositiveIntegerField(default=0, help_text="USD")),
                ("url", models.SlugField(max_length=150, unique=True)),
                ("draft", models.BooleanField(default=False)),
                (
                    "actors",
                    models.ManyToManyField(related_name="movie_actor", to="movies.Actor", verbose_name="actors"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="movies.Category",
                        verbose_name="Category",
                    ),
                ),
                (
                    "directors",
                    models.ManyToManyField(related_name="movie_director", to="movies.Actor", verbose_name="directors"),
                ),
                (
                    "genres",
                    models.ManyToManyField(related_name="movie_genre", to="movies.Genre", verbose_name="genres"),
                ),
            ],
            options={
                "verbose_name": "Movies",
                "verbose_name_plural": "Movies",
            },
        ),
        migrations.CreateModel(
            name="RatingStar",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("value", models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                "verbose_name": "RatingStar",
                "verbose_name_plural": "RatingStars",
            },
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("email", models.EmailField(max_length=254)),
                ("name", models.CharField(max_length=100)),
                ("text", models.TextField(max_length=5000)),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="movies.Movie", verbose_name="Movie"
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="movies.Review",
                        verbose_name="Parent",
                    ),
                ),
            ],
            options={
                "verbose_name": "Review",
                "verbose_name_plural": "Reviews",
            },
        ),
        migrations.CreateModel(
            name="Rating",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("ip", models.CharField(max_length=15)),
                (
                    "movie",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, to="movies.Movie", verbose_name="Movie"
                    ),
                ),
                (
                    "star",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="movies.RatingStar", verbose_name="Star"
                    ),
                ),
            ],
            options={
                "verbose_name": "Rating",
                "verbose_name_plural": "Ratings",
            },
        ),
        migrations.CreateModel(
            name="MovieShot",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="movie_shots/")),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="movies.Movie", verbose_name="Movie"
                    ),
                ),
            ],
            options={
                "verbose_name": "MovieShot",
                "verbose_name_plural": "MovieShots",
            },
        ),
    ]
