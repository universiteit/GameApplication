import unittest, datetime
from unittest import mock
from app.auth.models.user import User
from app.RTS.models import *
from app.RTS.rts_config import *
from app import db

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
        print("oke")
        upgrade_cost = self.town.get_upgrade_cost(3) # Upgrade cost from level 3 to 4
        self.assertEqual(upgrade_cost, 81)

    def test_get_upgrade_time(self):
        upgrade_time = self.town.get_upgrade_time(5)
        self.assertEqual(upgrade_time, datetime.timedelta(minutes=25))
        upgrade_time = self.town.get_upgrade_time(20)
        self.assertGreater(upgrade_time, datetime.timedelta(hours = 6, minutes=30))

    def test_get_production(self):
        amount = self.town.get_production(4)
        self.assertEqual(amount, 578)

    def test_get_unit_cost(self):
        unit_cost = self.town.get_unit_cost("knight")
        self.assertEqual(unit_cost["gold"], 25)
        self.assertEqual(unit_cost["wood"], 60)

    def test_add_units(self):
        self.town.get_unit_cost = mock.MagicMock(return_value = { 'gold' : 0, 'wood' : 0, 'food' : 0, 'iron' : 0})
        self.town.add_units(pikemen = 5)
        self.assertEqual(self.town.knights, 0)
        self.assertEqual(self.town.pikemen, 5)
    
    @mock.patch("app.RTS.models.town.datetime")
    def test_add_upgrade(self, mock_datetime):
        mock_datetime.datetime.now = mock.MagicMock(return_value = datetime.datetime(1,1,1))
        mock_time = datetime.timedelta(hours = 0)
        self.town.get_upgrade_cost = mock.MagicMock(return_value = 0)
        self.town.get_upgrade_time = mock.MagicMock(name="get_upgrade_time", return_value=mock_time)
        self.town.add_upgrade("barrack")
        self.assertEqual(self.town.upgrade_time_done, datetime.datetime(1,1,1))
        self.assertEqual(self.town.upgrade, "barrack")
        self.assertEqual(self.town.food, 0)
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
        self.assertIsNone(self.town.upgrade)
        self.assertIsNone(self.town.upgrade_time_done)


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.user = User("Jaime", "pass")

    def test_init(self):
        player = Player(self.user, "Lannister")
        self.assertEqual(player.user.username, "Jaime")
        self.assertEqual(player.house, "Lannister")


class TestAttack(unittest.TestCase):
    def setUp(self):
        self.player1 = Player(None, "Lannister")
        self.player2 = Player(None, "Stark")
        self.destination = Town(self.player2, "Winterfell", knights = 1, cavalry = 1, pikemen = 1, wall=3)
        self.origin = Town(self.player1, "King's Landing")
        self.attack = Attack(self.player1, self.destination, self.origin, knights = 1, cavalry = 1 , pikemen = 1)

    def test_init(self):
        self.assertEqual(self.attack.player.house, self.player1.house)
        self.assertEqual(self.attack.knights, 1)

    def test_get_defender_stats(self):
        get_wall_defense = self.attack.get_wall_defense
        self.attack.get_wall_defense = mock.MagicMock(return_value = 2)
        defense, offense = self.attack.get_defender_stats()
        self.assertEqual(defense, 150)
        self.assertEqual(offense, 180)
        self.attack.get_wall_defense = get_wall_defense

    def test_get_attacker_stats(self):
        defense, offense = self.attack.get_attacker_stats()
        self.assertEqual(defense, 75)
        self.assertEqual(offense, 180)

    def test_take_damage(self):
        pikemen, cavalry, knights = self.attack.take_damage(1, 1, 1, 70)
        self.assertEqual(knights, 1)
        self.assertEqual(pikemen, 0)
        self.assertEqual(cavalry, 0)
    
    def test_simulate_battle(self):
        take_damage = self.attack.take_damage
        get_wall_defense = self.attack.get_wall_defense
        self.attack.take_damage = mock.MagicMock(return_value = (1,1,1))
        self.attack.get_wall_defense = mock.MagicMock(return_value = 0)
        # Both armies are 1, 1, 1. Total defense is 150, attack is 180
        # attacker wins. Attacker remains with 1, 1, 1 army
        result = self.attack.simulate_battle()
        self.assertTrue(result["success"])
        self.assertEqual(result["attacking army"][1], 1)
        self.attack.take_damage = take_damage
        self.attack.get_wall_defense = get_wall_defense

    def test_get_wall_defense(self):
        result = self.attack.get_wall_defense(3)
        self.assertEqual(result, 1.15)

    @mock.patch('app.RTS.models.attack.db')
    def test_resolve(self, mock_db):
        simulate_battle = self.attack.simulate_battle()
        mock_result = { "success" : True, "attacking army" : (2,2,2), "defending_army" : (0,0,0) }
        self.attack.simulate_battle = mock.MagicMock(return_value = mock_result)
        self.attack.resolve()
        # Check if calls made to db layer
        self.assertTrue(mock_db.session.add.called)
        self.assertTrue(mock_db.session.delete.called)
        self.assertTrue(mock_db.commit)
        # Check if given proper parameters to db calls
        self.assertEqual(mock_db.session.add.call_args[0][0], self.destination)
        self.assertEqual(mock_db.session.delete.call_args[0][0], self.attack)
        # Check if player switched after victory
        self.assertEqual(self.destination.player, self.player1)