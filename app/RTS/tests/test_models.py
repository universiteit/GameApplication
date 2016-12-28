import unittest
from app.auth.models.user import User
from app.RTS.models.town import Town
from app.RTS.models.attack import Attack
from app.RTS.models.player import Player

class TestTown(unittest.TestCase):
    def setUp(self):
        self.user = User("Jaime", "pass")
        self.player = Player(self.user, "")
        self.town = Town(self.player, "King's landing", farm = 2)

    def test_init(self):
        self.assertEqual(self.town.name, "King's landing")
        self.assertEqual(self.town.farm, 2)
        self.assertEqual(self.town.gold_mine, 1)

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.user = User("Jaime", "pass")

    def test_init(self):
        player = Player(self.user, "Lannister")
        self.assertEqual(player.user.username, "Jaime")
        self.assertEqual(player.house, "Lannister")

class TestAttack(unittest.TestCase):
    def setUp(self):
        self.user = User("Jaime", "pass")

    def test_init(self):
        player = Player(self.user, "Lannister")
        attack = Attack(player, None, None, knights = 4, cavalry = 6 , pikemen = 7)
        self.assertEqual(attack.pikemen, 7)