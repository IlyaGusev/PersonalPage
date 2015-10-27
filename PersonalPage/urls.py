"""DIHT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from PersonalPage.views import index, game

urlpatterns = i18n_patterns(
    url(r'^$', index, name='home'),
    url(r'^game/$', game, name='game'),
    url(r'^projects/', include('projects.urls', namespace='projects')),
    url(r'^entries/', include('entries.urls', namespace='entries')),
    url(r'^games/', include('games.urls', namespace='games')),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from sitetree.sitetreeapp import register_i18n_trees
register_i18n_trees(['main'])
