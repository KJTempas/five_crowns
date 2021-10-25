from django.urls import path
from . import views

urlpatterns=[
    #path of '' is to the home page
    path('', views.player_list, name='player_list'),
    path('add_player', views.add_player, name='add_player'),
    path('score/<int:game_pk>, <int:player_pk>/add_score', views.add_score, name='add_score'),
    #path('player', views.player_list, name= 'playerlist'),
    path('games/', views.game_list, name='game_list'),
]