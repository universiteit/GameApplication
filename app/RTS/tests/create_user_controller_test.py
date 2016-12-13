import unittest
from app.RTS.controllers import create_user_controller as unit
from app.RTS.models.player import Player

class Test_Create_User_Controller(unittest.TestCase):
    def test_generate_new_user(self):
        username = "bob"
        player = unit.generate_new_player(username)
        self.assertIsNotNone(player)
        self.assertIsNotNone(player.house)
        self.assertIsNotNone(player.towns)
        self.assertEqual(player.username, username)

    def test_generate_town(self):
        mock_player = Player("bob", "Bobcastle")
        town = unit.generate_random_town(mock_player)
        self.assertIsNotNone(town)
        self.assertEqual(town.username, mock_player.username)
        self.assertIsNotNone(town.name)