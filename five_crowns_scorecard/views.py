from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Player, Game, Score
from .forms import NewScoreForm, NewPlayerForm, NewGameForm
from django.contrib import messages

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

def add_game(request):
    if request.method == 'POST':
        #create a form instance with the submitted data
        new_game_form = NewGameForm(request.POST)
        if new_game_form.is_valid():
            new_game_form.save()
            game = Game.objects.last() #retrieve last saved game  
            return redirect('game_list')
        else: #create an empty form
            return render(request, 'five_crowns_scorecard/add_game.html', {'new_game_form': new_game_form})
    new_game_form = NewGameForm
    return render(request, 'five_crowns_scorecard/add_game.html', {'new_game_form': new_game_form})


def player_list(request):
    players = Player.objects.all()
    return render(request, 'five_crowns_scorecard/playerlist.html', { 'players': players })


def add_score(request, game_pk):
    game = get_object_or_404(pk = game.pk)
    players = game.players
    if request.method == 'POST':
            #create a form instance with the submitted data
        new_score_form = NewScoreForm(request.POST)
        if new_score_form.is_valid():
            new_score_form.save()
            return redirect('player_list')

        else: #create an empty form
            return render(request, 'five_crowns_scorecard/add_score.html', {'new_score_form': new_score_form, 'game': game} )
    new_score_form = NewScoreForm
    return render(request, 'five_crowns_scorecard/add_score.html', {'new_score_form': new_score_form, 'game': game, 'players': players})


def game_list(request):
    games = Game.objects.all()#.order_by('game_date')#filter().values()
    print(games.count())
    return render(request, 'five_crowns_scorecard/gamelist.html', { 'games': games })
    # new_game_form = NewGameForm()
    # return render(request, 'five_crowns_scorecard/gamelist.html', { 'games' : games , 'new_game_form': new_game_form})

def game_detail(request, game_pk):
    game = get_object_or_404(Game, pk=game_pk)
    print(game.pk)
    
    if request.method == 'POST':
        form = NewScoreForm(request.POST)#, instance=game)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, form.errors) #temp error message

        return redirect('game_details', game_pk=game_pk) #redirects are GET; this is calling this method again

    else: #GET game details
        form = NewScoreForm(instance=game)
        return render(request, 'five_crowns_scorecard/game_detail.html', {'game': game, 'form': form} )


        
       