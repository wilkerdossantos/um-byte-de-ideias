from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce', include('tinymce.urls')),
    path('contact/', view=views.ContactView.as_view(), name='contact'),
    path('contact/success/', view=views.ContactSucessView.as_view(), name='contact_success'),
    path('', include('posts.urls')),
    path('', include('categories.urls')),
    path('', include('tags.urls')),
    path('', include('authors.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
