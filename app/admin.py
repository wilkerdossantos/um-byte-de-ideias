from django.contrib import admin
from .models import PageVisitors

@admin.register(PageVisitors)
class PageVisitorsAdmin(admin.ModelAdmin):
    list_display = ('title', 'number_visitors','created_at')
