import unittest
from app.auth.models.user import User
from app.RTS.models.town import Town
from app.RTS.models.attack import Attack
from app.RTS.models.player import Player

class TestTown(unittest.TestCase):
    def test_init(self):
        town = Town(None, "King's landing", farm = 2)
        self.assertEqual(town.name, "King's landing")
        self.assertEqual(town.farm, 2)
        self.assertEqual(town.gold_mine, 1)

class TestPlayer(unittest.TestCase):
    def test_init(self):
        mock_user = User("Jaime", "pass")
        player = Player(mock_user, "Lannister")
        self.assertEqual(player.user.username, "Jaime")
        self.assertEqual(player.house, "Lannister")

class TestAttack(unittest.TestCase):
    def test_init(self):
        player = Player(None, "Lannister")
        attack = Attack(player, None, None, 4, 6 ,7)
        self.assertEqual(attack.pikemen_amount, 7)