from django.shortcuts import render, redirect, get_object_or_404
from .models import Player, Game, Score
from .forms import NewScoreForm, NewPlayerForm
#from django.db.models import Avg

# Create your views here.
def add_player(request):
    if request.method == 'POST':
        new_player_form = NewPlayerForm(request.POST)
        if new_player_form.is_valid():
            new_player_form.save()
            return redirect('player_list')
        else:
            return render(request, 'five_crowns_scorecard/add_player.html', {'new_player_form': new_player_form})
    new_player_form = NewPlayerForm
    return render(request, 'five_crowns_scorecard/add_player.html', {'new_player_form': new_player_form})


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
    

def game_list(request):
    games = Game.objects.all().order_by('game_date')#filter().values()
    #game_objects = Game.objects.get().all()
  
    return render(request, 'five_crowns_scorecard/gamelist.html', { 'games' : games })