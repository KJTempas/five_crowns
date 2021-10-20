from django.shortcuts import render
from .models import Player

# Create your views here.
def player_list(request):
    players = Player.objects.all()
    return render(request, 'five_crowns_scorecard/playerlist.html', { 'players': players })
