from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Player, Game, Score
from .forms import NewScoreForm, NewPlayerForm, NewGameForm
from django.contrib import messages
from django.db.models import Avg, Max, Min 
from django.forms import model_to_dict

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

            for player in request.POST.getlist('players'):
                form = NewGameForm({'player': player}, instance=Game())
                form.save
            new_game_form.save()
           
            return redirect('game_list')
        else: #create an empty form
            return render(request, 'five_crowns_scorecard/add_game.html', {'new_game_form': new_game_form})
    new_game_form = NewGameForm
    return render(request, 'five_crowns_scorecard/add_game.html', {'new_game_form': new_game_form})


def player_list(request):
    players_query = Player.objects.all() #yields a queryset
    # for player in players_query:
    #     player_dict =model_to_dict(player)
    #     print(player_dict)
    context = {
        "players": players_query
    }


       #TODO get these to display in template correctly
     
    return render(request, 'five_crowns_scorecard/playerlist.html',  context)
 

def game_list(request):
    games = Game.objects.all()#.order_by('game_date')#filter().values()
    #print(games.count())
    return render(request, 'five_crowns_scorecard/gamelist.html', { 'games': games })
    # new_game_form = NewGameForm()
    # return render(request, 'five_crowns_scorecard/gamelist.html', { 'games' : games , 'new_game_form': new_game_form})

def game_detail(request, game_pk):
    game = get_object_or_404(Game, pk=game_pk)
    players = game.players
    
    if request.method == 'POST':
       # https://stackoverflow.com/questions/13563475/how-to-loop-through-form-fields-and-store-them-all-in-the-database
        #in Score table, game_id and player_id are added when game is saved
       
        game_players = Score.objects.all().filter(game= game)
        formScores = request.POST.getlist('points')
        i=0
        while i<len(game_players):
            #make the first game players points equal to the first score on the points list
            game_players[i].points = formScores[i]
            game_players[i].save()
            i = i+1
        return redirect(('player_list'))

    else: #GET game details
        #TODO fix so shows game score on GET
        new_score_form = NewScoreForm(instance=game)
        return render(request, 'five_crowns_scorecard/game_detail.html', {'game': game , 'new_score_form': new_score_form})

#TODO WHY IS THIS NEEDED - WHERE IS IT CALLED?
def add_score(request, game_pk):

    game = get_object_or_404(pk = game.pk)
    players = game.players
    if request.method == 'POST':
            #create a form instance with the submitted data
        form = NewScoreForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('player_list')

        else: #create an empty form
            return render(request, 'five_crowns_scorecard/add_score.html', {'form': form, 'game': game} )
    #if not a post,  a GET, so make blank form
    form = NewScoreForm
    print('you are here- GET request for add_score')
    return render(request, 'five_crowns_scorecard/add_score.html', {'form': form, 'game': game, 'players': players})




        
       