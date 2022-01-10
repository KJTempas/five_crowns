from django.urls import path
from . import views

urlpatterns=[
    #path of '' is to the home page
    path('', views.player_list, name='player_list'),
    path('add_player', views.add_player, name='add_player'),
    path('add_game', views.add_game, name='add_game'),
    path('game/', views.game_list, name='game_list'),
    path('game/<int:game_pk>', views.game_detail, name='game_detail'),
    
]