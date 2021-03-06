from django.db import models
from django.db.models import Avg, Min, Max

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    
    #https://stackoverflow.com/questions/2689664/get-average-from-set-of-objects-in-django
   
    @property
    def avg_score(self):
        return Score.objects.filter(player = self).aggregate(Avg('points')) 
    
    @property
    def max_score(self):
        return Score.objects.filter(player = self).aggregate(Max('points'))

    @property
    def min_score(self):
        return Score.objects.filter(player = self).aggregate(Min('points'))
    #note - when accessing these @ property values in a template, do as follows 
    # {{ player.min_score.points__min}}
    #  when you call an aggregate fx, it returns a mapping of the result from the column name
    # to value; need to pull the value out of the hash this way(thanks to Joshua Shanks)
    
    @property
    def num_of_games(self):
        return Score.objects.filter(player = self).count()

    def __str__(self):
        return self.name

class Game(models.Model):
    game_date= models.DateField()#(auto_now=False, auto_now_add=True)
    players = models.ManyToManyField(Player, through='Score', related_name='games' )
    #what if two games/day with same player;  need datetime not date
    class Meta:
        ordering = ['-game_date'] #the '-' makes it desc order; remove for asc order
   # https://docs.djangoproject.com/en/3.2/topics/db/models/#many-to-many-relationships    


class Score(models.Model):
    game = models.ForeignKey(Game, related_name= 'scores', on_delete=models.SET_NULL, null=True)#on_delete=models.CASCADE) #need to review meaning of this
    player = models.ForeignKey(Player, related_name='scores', on_delete=models.SET_NULL, null=True, blank=True)#on_delete=models.CASCADE)
    points = models.IntegerField(default=0 ) #required field
    

    class Meta:
        unique_together = [['game', 'player', 'points']]
# helpful doc - https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/

    #https://stackoverflow.com/questions/26927705/django-migration-error-you-cannot-alter-to-or-from-m2m-fields-or-add-or-remove  21



    #pizza = game = group
    #topping = player = person
    #topping amt = score = membership
    #want to add a score for each player for each game
    #same as add a topping amt for each topping for each pizza

    # idea for Score table
    # game_id   player_id   score
    #   1       1           100
    #   1       2           150
    #   1       3           200
