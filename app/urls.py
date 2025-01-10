from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from . import sitemaps


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce', include('tinymce.urls')),
    path('contact/', view=views.ContactView.as_view(), name='contact'),
    path('contact/success/', view=views.ContactSucessView.as_view(), name='contact_success'),
    path('', include('posts.urls')),
    path('', include('categories.urls')),
    path('', include('tags.urls')),
    path('', include('authors.urls')),
    path('sitemap.xml', sitemap, {
        'sitemaps': {
            'static': sitemaps.StaticViewSitemap,
            'author': sitemaps.AuthorSitemap,
            'category': sitemaps.CategorySitemap,
            'post': sitemaps.PostSitemap,
            'tag': sitemaps.TagSitemap
        }
    }),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
