from django.test import TestCase
from django.urls import reverse

from .models import Player

# Create your tests here.

class TestViewPlayerList(TestCase):

    #load this into database before these tests
    fixtures = ['test_players']

    def test_view_playerlist(self):
        response = self.client.get(reverse('player_list'))
        #correct template used?
        self.assertTemplateUsed(response, 'five_crowns_scorecard/playerlist.html')
        #data sent to template
        data_rendered = list(response.context['players'])
        #data in dbase
        data_expected = list(Player.objects.all())
        #is it the same
        self.assertCountEqual(data_rendered, data_expected)

class TestAddNewPlayer(TestCase):
    fixtures = ['test_players']

    def test_add_new_player_to_playerlist(self):
        response = self.client.post(reverse('add_player'), {'name': 'Joan Arc'}, follow=True)
        #check correct template was used
        self.assertTemplateUsed(response, 'five_crowns_scorecard/playerlist.html')
        response_players = response.context['players']
        #should be 4 players ; 3 from fixtures + 1 just added
        self.assertEqual(len(response_players), 4)
        joan_arc = response_players[3]
        #retrieve data from dbase
        joan_arc_in_dbase = Player.objects.get(name='Joan Arc')
        #is data used to render template same as data in dbase?
        self.assertEqual(joan_arc_in_dbase, joan_arc)


class TestAddNewGame(TestCase):
    fixtures = ['test_games', 'test_players']

    def test_view_game_list(self):
        response = self.client.get(reverse('game_list'))
        #check correct template used to show results
        #this failing - maybe need fixtures to list pk of player, not name
        #self.assertTemplateUsed(response, 'five_crowns_scorecard/gamelist.html')

