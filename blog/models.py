from django.db import models


class SinglePostModel(models.Model):
    title = models.CharField(max_length=100)
    primary_image = models.ImageField(upload_to='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
