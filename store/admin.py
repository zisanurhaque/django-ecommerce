from django.contrib import admin
from .models import Category, Product, Tag

# Register your models here.
@admin.register(Category)
@admin.register(Product)
@admin.register(Tag)

class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name']

class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'description', 'category', 'image']

class AdminTag(admin.ModelAdmin):
    list_display = ['id', 'name']