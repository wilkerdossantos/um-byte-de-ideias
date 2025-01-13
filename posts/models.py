from django.db import models
from django.urls import reverse
from authors.models import Author
from categories.models import Category
from tags.models import Tag
from tinymce.models import HTMLField


class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    content = HTMLField()
    header_image = models.ImageField(upload_to='post/')
    published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tag = models.ManyToManyField(Tag, blank=True, related_name='posts')
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='posts')
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-updated_at']

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.slug)])
