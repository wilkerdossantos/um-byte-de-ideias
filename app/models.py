from django.db import models


class PageVisitors(models.Model):
    title = models.CharField(max_length=255)
    number_visitors = models.BigIntegerField()
    path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} {self.number_visitors} visitors'

