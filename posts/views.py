from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from . import models
from categories.models import Category
from comments.models import Comment
from comments.forms import CommentModelForm


class PostListView(ListView):
    model = models.Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        """
        Filtra os posts publicados e, se houver um termo de busca, 
        aplica o filtro por título.
        """
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '').strip()
        queryset = queryset.filter(published=True)
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PostDetailView(FormMixin, DetailView):
    model = models.Post
    template_name = 'post_detail.html'
    form_class = CommentModelForm

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(published=True)
        return queryset

    def get_context_data(self, **kwargs):
        post = self.object
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['comments'] = Comment.objects.filter(post=post)
        return context

    def get_success_url(self):
        base_url = reverse('post_detail', kwargs={'slug': self.object.slug})
        return f"{base_url}#comments"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.post = self.object
        form.save()
        return super().form_valid(form)
