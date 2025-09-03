from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from core.models import Blog

class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        # List of static URL names
        return ["core:index", "core:dr-gary", "core:contact-us",]

    def location(self, item):
        return reverse(item)