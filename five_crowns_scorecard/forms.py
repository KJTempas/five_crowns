from django import forms
from django.forms import FileInput
from .models import Score, Player, Game

class NewPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        exclude = ['points'] #points not needed on new form as is default 0


class NewGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['game_date', 'players']

class NewScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = [ 'points' ] #maybe need 'player' also?