from django.contrib.sitemaps import Sitemap
from django.utils import timezone
from .models import Post

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.objects.filter(published__lte=timezone.now()).order_by('-published')

    def lastmod(self, obj):
        return obj.published