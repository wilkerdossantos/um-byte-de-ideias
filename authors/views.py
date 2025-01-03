from django.db.models import Q
from django.views.generic import DetailView, ListView
from . import models
from categories.models import Category
from posts.models import Post


class AuthorListView(ListView):
    model = models.Author
    template_name = 'author_list.html'
    context_object_name = 'authors'


class AuthorDetailView(DetailView):
    model = models.Author
    template_name = 'author_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.object
        search = self.request.GET.get('search')
        queryset = Post.objects.filter(author=author, published=True)
        if search:
            queryset = Post.objects.filter(
                Q(title__icontains=search) | Q(content__icontains=search),
                author=author,
                published=True
            )
        context['posts'] = queryset
        context['categories'] = Category.objects.all()
        return context
