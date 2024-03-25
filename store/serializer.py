from rest_framework.serializers import ModelSerializer
from .models import Category, Tag, Product, Review
from django.forms import widgets
from rest_framework import serializers

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']

class ProductSerializer(ModelSerializer):

    description = serializers.CharField(style={'widget': 'textarea', 'class': 'ckeditor'})
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Product
        fields = ['id', 'published_by', 'name', 'price', 'category', 'description', 'image', 'stock', 'tags', 'created_at', 'updated_at']
        read_only_fields = ['id', 'published_by', 'created_at', 'updated_at']

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'anonymous', 'user_name', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'created_at']