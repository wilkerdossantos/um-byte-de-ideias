from django.db import models
from django.contrib.auth.models import User 

class AccessLog(models.Model):
    path = models.CharField(max_length=255)
    view = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    method = models.CharField(max_length=10)
    ip = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Access Log'
        verbose_name_plural = 'Access Logs'

    def __str__(self):
        return self.path
