from django.contrib import admin
from .models import *

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['title']

@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    search_fields = ['article']
    list_filter = ['article']
    autocomplete_fields = ['article']
