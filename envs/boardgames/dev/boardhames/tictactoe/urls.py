from django.conf.urls import patterns, include, url


urlpatterns = patterns('tictactoe.views',
    url(r'^invite$', 'new_invitation', name='tictactoe_invite'),
    url(r'^invitation/(?P<pk>\d+)/$', 'accept_invitation', name='tictactoe_accept_invitation'),
    url(r'^game/(?P<pk>\d+)/$', 'game_detail', name='tictactoe_game_detail'),
    url(r'^game/(?P<pk>\d+)/do_move$', 'game_do_move', name='tictactoe_game_do_move'),

)
