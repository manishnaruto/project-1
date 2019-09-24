from django.contrib import admin
from .models import Category,Album,AlbumImage

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['category','name','slug','show','created']
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['show']
    search_fields = ['name']

@admin.register(AlbumImage)
class AlbumImageAdmin(admin.ModelAdmin):
    list_display = ['album']