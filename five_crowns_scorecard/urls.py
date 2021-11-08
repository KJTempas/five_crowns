from django.urls import path
from . import views

urlpatterns=[
    #path of '' is to the home page
    path('', views.player_list, name='player_list'),
    path('add_player', views.add_player, name='add_player'),
    path('add_game', views.add_game, name='add_game'),
    path('game/<int:game_pk>/add_score', views.add_score, name='add_score'),
    path('game/', views.game_list, name='game_list'),
    #path('game/<int:game_pk>/add_score', views.add_score, name='add_score'),
    #path('game/add_score/<int:game_pk>', views.add_score, name='add_score'),
    path('game/<int:game_pk>', views.game_detail, name='game_detail'),
    path('game/', views.game_list, name='game_list') #needed?
    
    #path('player', views.player_list, name= 'playerlist'),
    
]