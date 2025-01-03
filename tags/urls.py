from django.urls import path
from . import views


urlpatterns = [
    path('tags/<slug:slug>/', view=views.TagDetailView.as_view(), name="tag_detail"),
]
