__author__ = 'vladyslav'

from django.conf.urls import patterns, include, url


urlpatterns = patterns('user.views',
    url(r'^$', 'redirect_to_main', name='redirect_to_main'),
    url(r'^create_groups$', 'create_groups', name='create_groups'),
)

