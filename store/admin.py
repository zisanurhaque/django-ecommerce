from django.contrib import admin
from .models import Category, Product, Tag, Review

# Register your models here.
@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    def display_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])

    display_tags.short_description = 'Tags'

    def stock_display(self, obj):
        return obj.stock

    stock_display.short_description = 'Stock'

    list_display = ['id', 'published_by', 'name', 'price', 'category', 'description', 'image', 'stock_display', 'created_at', 'updated_at', 'display_tags']

@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    list_display = ['id', 'product', 'user', 'anonymous', 'user_name', 'rating', 'comment', 'created_at']