from django.urls import path
from . import views

urlpatterns = [
    path('authors/', view=views.AuthorListView.as_view(), name='author_list'),
    path('authors/<slug:slug>/', view=views.AuthorDetailView.as_view(), name='author_detail'),
]