from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import HelloWorldView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hello$', HelloWorldView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('user.urls')),
    url(r'^tictactoe/', include('tictactoe.urls')),
    url(r'^$', 'main.views.home', name='boardgames_home')
)


urlpatterns += patterns(
    'django.contrib.auth.views',

    url(r'^login/$', 'login',
        {'template_name': 'login.html'},
        name='boardgames_login'),

    url(r'^logout/$', 'logout',
        {'next_page': 'boardgames_home'},
        name='boardgames_logout'),
)