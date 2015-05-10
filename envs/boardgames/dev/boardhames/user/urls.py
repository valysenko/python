from django.conf.urls import patterns, include, url


urlpatterns = patterns('user.views',
    url(r'^home$', 'home', name='user_home')
)