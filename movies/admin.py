from django.contrib import admin
from .models import Movie, Review
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'user', 'reported', 'date']
    list_filter = ['reported', 'date']
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)