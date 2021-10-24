from django import forms
from django.forms import FileInput
from .models import Score, Player, Game

class NewScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ('player', 'game', 'points')