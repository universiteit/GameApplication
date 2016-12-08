import unittest
from app.RTS.models.* import *

class TestUnit(unittest.TestCase):
    def test_init(self):
        unit = Unit("Soldier", 10, 20)
        self.assertEqual(unit.type, "Soldier")
        self.assertEqual(unit.offense, 10)
        self.assertEqual(unit.defense, 20)

class TestTown(unittest.TestCase):
    def test_init(self):
        town = Town("username", "King's landing", farm = 2)
        self.assertEqual(town.username, "username")
        self.assertEqual(town.name, "King's landing")
        self.assertEqual(town.farm, 2)
        self.assertEqual(town.gold_mine, 1)

class TestUser(unittest.TestCase):
    def test_init(self):
        user = User("Jaime", "Lannister")
        self.assertEqual(user.username, "Jaime")
        self.assertEqual(user.house, "Lannister")

class TestAttack(unittest.TestCase):
    def test_init(self):
        attack = Attack("Jaime", None, None, 4, 6 ,7)
        self.assertEqual(attack.pikemen_amount, 7)