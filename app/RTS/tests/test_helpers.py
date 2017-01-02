import unittest
from app.RTS.models import *
from app.RTS.helpers import *

class test_generators(unittest.TestCase):
    def test_generate_new_player(self):
        player = generate_new_player(self.user)
        self.assertIsNotNone(player)
        self.assertIsNotNone(player.house)

    def generate_random_town(self):
        town = generate_town()
        self.assertIsNotNone(town)
        self.assertIsNotNone(town.Name)

    def setUp(self):
        self.user = User("username", "password")