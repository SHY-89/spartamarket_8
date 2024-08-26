from django.db import models
from django.conf import settings


class HashTag(models.Model):
    name = models.CharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="images/", blank=True, default="images/product1.jpg") 
    cnt = models.IntegerField(default=0)
    uuid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products")

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_products"
    )

    hashtags = models.ManyToManyField(
        HashTag, related_name="hash_products"
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

