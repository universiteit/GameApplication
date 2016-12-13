import unittest
from app.RTS.controllers import create_player_controller as controller
from app.RTS.models.player import Player
from app.auth.models.user import User

class Test_Create_Player_Controller(unittest.TestCase):
    def setUp(self):
        self.mock_user = User("Jaime", "password")

    def test_generate_new_user(self):
        player = controller.generate_new_player(self.mock_user)
        self.assertIsNotNone(player)
        self.assertIsNotNone(player.house)
        self.assertIsNotNone(player.towns)
        self.assertEqual(player.user.username, "Jaime")

    def test_generate_town(self):
        mock_player = Player(self.mock_user, "Lannister")
        town = controller.generate_random_town(mock_player)
        self.assertIsNotNone(town)
        self.assertIsNotNone(town.name)
        self.assertEqual(mock_player, town.player)