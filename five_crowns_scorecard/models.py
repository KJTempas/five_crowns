from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    points = models.IntegerField(default=0)
    #average, min and max are calculated values
    # user Player.objects.filter(points.count() to get number of games played)

    # def get_average(self):
    #     return total_points/games_played

    def __str__(self):
        return self.name

class Game(models.Model):
    game_date= models.DateField()#(auto_now=False, auto_now_add=True)
    #players = models.ManyToManyField(Player, through='Score')
    players = models.ManyToManyField(Player, through='Score', related_name='games' )
    #what if two games/day with same player;  need datetime not date
    class Meta:
        ordering = ['-game_date'] #the '-' makes it desc order; remove for asc order
   # https://docs.djangoproject.com/en/3.2/topics/db/models/#many-to-many-relationships    


class Score(models.Model):
    game = models.ForeignKey(Game, related_name= 'scores', on_delete=models.SET_NULL, null=True)#on_delete=models.CASCADE) #need to review meaning of this
    player = models.ForeignKey(Player, related_name='scores', on_delete=models.SET_NULL, null=True, blank=True)#on_delete=models.CASCADE)
    points = models.IntegerField(default =0)#blank = False) #required field
    
    class Meta:
        unique_together = [['game', 'player', 'points']]
# helpful doc - https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/

    #https://stackoverflow.com/questions/26927705/django-migration-error-you-cannot-alter-to-or-from-m2m-fields-or-add-or-remove  21



    #pizza = game = group
    #topping = player = person
    #topping amt = score = membership
    #want to add a score for each player for each game
    #same as add a topping amt for each topping for each pizza