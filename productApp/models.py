from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ("electronics", "Electronics"),
        ("clothings", "Clothings"),
        ("jewelries", "Jewelries"),
        ("groceries", "Groceries"),
        ("unknown", "Unknown")
    ]
    
    product_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES, default="unknown")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


class ProductFeatures(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="features")
    label = models.CharField(max_length=20, null=True, blank=True)
    value = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.product.title} feat-0{self.pk}"
    
    
class ProductReview(models.Model):
    RATING_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]
    
    message = models.CharField(max_length=225)
    ratings = models.PositiveIntegerField(choices=RATING_CHOICES, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.product.title} image-0{self.pk}"
    
