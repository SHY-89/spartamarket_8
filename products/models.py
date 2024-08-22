from django.db import models
from django.contrib.auth import get_user_model


class Index(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    poto = models.ImageField(upload_to="images/", blank=True)
    uuid = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="indexs" 
    )

