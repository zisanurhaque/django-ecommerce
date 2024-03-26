from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Product(models.Model):
    published_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    description = RichTextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    stock = models.BooleanField(default=True),
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(default = timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)
    anonymous = models.BooleanField(default=False)
    user_name = models.CharField(max_length=100, blank=True)
    rating = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user_name}'s Review for {self.product.name}"