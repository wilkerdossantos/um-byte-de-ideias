from django.db import models
from posts.models import Post


class Comment(models.Model):
    name = models.CharField(max_length=255) # Refatorar para UserName
    email = models.EmailField(max_length=255)
    comment = models.TextField(null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='comments', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.name
