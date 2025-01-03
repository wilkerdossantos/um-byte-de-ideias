from django.db import models
from tinymce.models import HTMLField


class Author(models.Model):
    name = models.CharField(max_length=255)
    profile = models.ImageField(upload_to='authors/')
    bio = HTMLField()
    github = models.URLField(max_length=255, null=True, blank=True)
    linkedin = models.URLField(max_length=255, null=True, blank=True)
    x = models.URLField(max_length=255, null=True, blank=True)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
