from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", args=[str(self.slug)])
