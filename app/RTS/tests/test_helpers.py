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

class test_battle(unittest.TestCase):
    def setUp(self):
        self.origin = Town(None, "origin")
        self.destination = Town(None, "destination", 0, 0, 0)
        self.player = Player(None, "Lannister")
        self.attack = Attack(self.player, self.destination, self.origin, knights = 10)

    def test_run_attack(self):
        self.assertTrue(run_attack(self.attack))

class test_backend_updates(unittest.TestCase):
    pass