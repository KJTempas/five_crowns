from django.shortcuts import render
from .models import Player
from .forms import NewScoreForm
#from django.db.models import Avg

# Create your views here.
def player_list(request):
    players = Player.objects.all()
    # for player in players:#p = Player.objects.get(score)
    #     average_score = total_points/games_played
        #maybe use aggregation
    return render(request, 'five_crowns_scorecard/playerlist.html', { 'players': players })


#def add_score(request):#need player pk and game pk?
def add_score(request, game_pk, player_pk):
    #games = Game.objects.all()
    new_score_form = NewScoreForm()
    return render(request, 'five_crowns_scorecard/game.html', {'new_score_form': new_score_form})
    #return render(request, 'five_crowns_scorecard/game.html', {'games': games, 'new_score_form': new_score_form })
    