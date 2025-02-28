from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import PageVisitors


class ContactSucessView(TemplateView):
    template_name = 'contact_success.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        print("Oi Mundo")
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        PageVisitors.objects.create(
            title="Contact",
            path='/contact/',
            number_visitors=PageVisitors.objects.all().count() + 1,
        )
        return context


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
