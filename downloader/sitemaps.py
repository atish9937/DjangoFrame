from django.contrib.sitemaps import Sitemap
from .models import Downloader, Pages
from django.utils.text import slugify
from django.urls import reverse
def converttoslug(string):
	string=string.split("(")[0].strip()
	string=slugify(string,allow_unicode=True)
	return string

class downloadersitemap(Sitemap):
    changefreq="daily"
    protocol="http"
    priority= 0.9
    limit=50
    def items(self):
        return Downloader.objects.all()
    def lastupdated(self,obj):
        return obj.Updatedon
    def location(self,obj):
        slug=converttoslug(obj.Name)
        return f'/{slug}/'
class staticsitemap(Sitemap):
    changefreq='monthly'
    protocol='http'
    priority=0.4
    def items(self):
        return ['privacy','terms','dmca','disclaimer','contactus']
    def location(self,item):
        return reverse(item)
