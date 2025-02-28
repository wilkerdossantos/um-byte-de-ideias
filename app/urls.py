from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView
from . import views 
from . import sitemaps
from .feeds import LatestPostsFeed


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce', include('tinymce.urls')),
    path('dashboard/', view=views.DashboardView.as_view(), name='dashboard'),
    path('contact/', view=views.ContactView.as_view(), name='contact'),
    path('contact/success/', view=views.ContactSucessView.as_view(), name='contact_success'),
    path('', include('posts.urls')),
    path('', include('categories.urls')),
    path('', include('tags.urls')),
    path('', include('authors.urls')),
    path('feed/rss', LatestPostsFeed(), name='feed'),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name='robots'),
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
