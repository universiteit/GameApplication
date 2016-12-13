import unittest
from app.RTS.models.town import Town
from app.RTS.models.attack import Attack
from app.RTS.models.player import Player

class TestTown(unittest.TestCase):
    def test_init(self):
        town = Town("username", "King's landing", farm = 2)
        self.assertEqual(town.username, "username")
        self.assertEqual(town.name, "King's landing")
        self.assertEqual(town.farm, 2)
        self.assertEqual(town.gold_mine, 1)

class TestPlayer(unittest.TestCase):
    def test_init(self):
        user = Player("Jaime", "Lannister")
        self.assertEqual(user.username, "Jaime")
        self.assertEqual(user.house, "Lannister")

class TestAttack(unittest.TestCase):
    def test_init(self):
        attack = Attack("Jaime", None, None, 4, 6 ,7)
        self.assertEqual(attack.pikemen_amount, 7)