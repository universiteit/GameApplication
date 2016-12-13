import unittest
from app import db
from app.RTS.models.player import Player

@unittest.skip("Not ready yet")
class TestDb(unittest.TestCase):
    def setUp(self):
        self.player = Player("Jaime", "Lannister")
        
    def test_insert(self):
        db.session.add(self.player)
        db.session.commit()
        db.session.delete(self.player)
        result = Player.query.filter_by(username="Jaime").first()
        self.assertIsNone(result)