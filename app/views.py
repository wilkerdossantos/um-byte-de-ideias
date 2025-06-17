from django.views.generic import FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Count
from .forms import ContactForm
from .models import AccessLog
from posts.models import Post
from categories.models import Category
from tags.models import Tag
from comments.models import Comment
from authors.models import Author


class ContactSucessView(TemplateView):
    template_name = 'contact_success.html'


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm 
    success_url = reverse_lazy('contact_success')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        send_mail(
            f"Mensagem de {name}",
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return super().form_valid(form)

class DashboardView(TemplateView, LoginRequiredMixin):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_access'] = AccessLog.objects.count()
        context['access_per_date'] = list(
            AccessLog.objects.extra(
            select={'date': 'date(created_at)'}
            ).values('date').annotate(count=Count('id'))
        )
        context['total_posts'] = Post.objects.count()
        access_per_path = list(
            AccessLog.objects.filter(view='post_detail').values('path').annotate(count=Count('id'))
        )
        if access_per_path:
            context['access_per_post'] = {}
            for access in access_per_path:
                try:
                    post = Post.objects.get(slug=access['path'].split('/')[-2])
                    context['access_per_post'][str(post)] = access['count']
                except Post.DoesNotExist:
                    continue
        return context
