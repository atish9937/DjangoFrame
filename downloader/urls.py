from django.urls import path, include
from . import views
from django.contrib.sitemaps.views import sitemap, index
from .sitemaps import downloadersitemap, staticsitemap

sitemaps={"post":downloadersitemap,'static':staticsitemap}

urlpatterns = [  
    path('', views.home, name='home'),
    path('<slug:slug>/', views.downloader, name='downloader'),    
    path('dmca/', views.dmca, name='dmca'),
    path('contact-us/', views.contactus, name='contactus'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('terms-and-condition/', views.terms, name='terms'),
    path('privacy/', views.terms, name='privacy'),
    path('robots.txt', views.robots, name='robots'),
    path('ads.txt', views.ads, name='ads'),
    path('sitemap.xml',index,{'sitemaps':sitemaps},name='django.contrib.sitemaps.views.index'),
    path('sitemap-<section>.xml',sitemap,{'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap')
    
]