import unittest, datetime
from unittest import mock
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

    def test_get_upgrade_cost(self):
        upgrade_cost = self.town.get_upgrade_cost(3) # Upgrade cost from level 3 to 4
        self.assertEqual(upgrade_cost, 81)

    def test_get_upgrade_time(self):
        upgrade_time = self.town.get_upgrade_time(5)
        self.assertEqual(upgrade_time, datetime.time(minute=25))
        upgrade_time = self.town.get_upgrade_time(20)
        self.assertGreater(upgrade_time, datetime.time(hour = 6, minute=30))

    def test_get_production(self):
        amount = self.town.get_production(4)
        self.assertEqual(amount, 578)

    def test_get_unit_cost(self):
        unit_cost = self.town.get_unit_cost("knight")
        self.assertEqual(unit_cost["gold"], 25)
        self.assertEqual(unit_cost["wood"], 60)

    def test_add_units(self):
        self.town.add_units(pikemen = 5)
        self.assertEqual(self.town.knights, 0)
        self.assertEqual(self.town.pikemen, 5)
    
    def test_add_upgrade(self):
        mock_time = datetime.datetime(1, 1, 1)
        self.town.get_upgrade_time = mock.MagicMock(name="get_upgrade_time", return_value=mock_time)
        self.town.add_upgrade("barrack")
        self.assertEqual(self.town.upgrade_time_done, mock_time)
        self.assertEqual(self.town.upgrade, "barrack")
        self.town.upgrade = None
        self.town.upgrade_time_done = None

    def test_update_resources(self):
        self.town.get_production = mock.MagicMock(return_value = 120)
        self.town.update_resources()
        self.assertEqual(self.town.gold, 10)
        self.assertLess(self.town.wood, 20)
        self.assertGreater(self.town.iron, 5)

    def test_update_upgrade(self):
        self.town.upgrade = "barrack"
        self.town.upgrade_time_done = datetime.datetime.now()
        self.town.update_upgrade()
        self.assertEqual(self.town.barracks, 2)
        self.assertEqual(self.town.lumber_mill, 1)

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