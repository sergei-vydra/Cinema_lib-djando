from django.contrib import admin
from .models import Category, Genre, Movie, MovieShot, Actor, Rating, RatingStar, Review


# class ReviewInline(admin.StackedInline):
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name", "url")


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft")
    list_filter = ("title", "year")
    search_fields = ("title", "category__name")
    read_only_fields = ("title",)
    inlines = [ReviewInline]
    save_on_top = True


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id")
    read_only_fields = ("name",)


admin.site.register(Genre)
admin.site.register(MovieShot)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)

admin.site.site_title = "Django Cinema"
