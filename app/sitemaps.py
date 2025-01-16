from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from authors.models import Author
from categories.models import Category
from posts.models import Post
from tags.models import Tag


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['author_list', 'post_list', 'contact']
    
    def location(self, obj):
        return reverse(obj)


class AuthorSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return Author.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at


class CategorySitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return Category.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at


class PostSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return Post.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at


class TagSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return Tag.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
