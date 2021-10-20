from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    average_score = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    lowest_score = models.IntegerField(default=0)
    highest_score = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Game(models.Model):
    game_date= models.DateField()#(auto_now=False, auto_now_add=True)
    players = models.ManyToManyField(Player, through='Score')

        

class Score(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE) #need to review meaning of this
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    points = models.IntegerField(blank = False) #required field