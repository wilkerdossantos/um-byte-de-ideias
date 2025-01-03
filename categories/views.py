from django.db.models import Q
from django.views.generic import DetailView
from . import models
from posts.models import Post


class CategoryDetailView(DetailView):
    model = models.Category
    template_name = 'category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object
        search = self.request.GET.get('search')
        queryset = Post.objects.filter(category=category, published=True)
        if search:
            queryset = Post.objects.filter(
                Q(title__icontains=search) | Q(content__icontains=search),
                category=category,
                published=True
            )
        context['posts'] = queryset
        context['categories'] = models.Category.objects.all()
        return context
