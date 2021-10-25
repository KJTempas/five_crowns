from django import forms
from django.forms import FileInput
from .models import Score, Player, Game

class NewPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        exclude = ['points'] #points not needed on new form as is default 0


class NewScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ('player', 'game', 'points')