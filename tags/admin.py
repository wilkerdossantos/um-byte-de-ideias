from django.contrib import admin
from .models import Tag

@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
