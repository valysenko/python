__author__ = 'vladyslav'

from django.conf.urls import patterns, include, url
from .views import SignUpView

urlpatterns = patterns('user.views',
    url(r'^$', 'redirect_to_main', name='redirect_to_main'),
    url(r'^create_groups$', 'create_groups', name='create_groups'),
    url(r'^signup$', SignUpView.as_view(), name='user_signup'),
)

