from django.urls import path
from . import views


urlpatterns = [
    path('category/<slug:slug>/', view=views.CategoryDetailView.as_view(), name='category_detail'),
]
