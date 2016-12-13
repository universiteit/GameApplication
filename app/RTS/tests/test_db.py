import unittest
from app.db import db
from app.RTS.models.player import Player


class TestDb(unittest.TestCase):
    def setUp(self):
        self.player = Player("Jaime", "Lannister")
        
    def test_insert(self):
        db.session.add(self.player)
        db.session.commit()

    def test_select(self):
        result = Player.query.filter_by(username="Jaime").first()
        self.assertIsNotNone(result)
        self.assertEqual(result.username, self.player.username)

    def test_delete(self):
        db.session.delete(self.player)
        db.session.commit()
        result = Player.query.filter_by(username="Jaime").first()
        self.assertIsNone(result)