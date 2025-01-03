from django.db.models import Q
from django.views.generic import DetailView
from . import models
from posts.models import Post
from categories.models import Category


class TagDetailView(DetailView):
    model = models.Tag
    template_name = 'tag_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = self.object
        search = self.request.GET.get('search')
        queryset = Post.objects.filter(tag=tag, published=True)
        if search:
            queryset = Post.objects.filter(
                Q(title__icontains=search) | Q(content__icontains=search),
                tag=tag,
                published=True
            )
        context['posts'] = queryset
        context['categories'] = Category.objects.all()
        return context
