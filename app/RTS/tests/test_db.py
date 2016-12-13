import unittest
from app import db
from app import bcrypt
from app.RTS.models.player import Player
from app.auth.models.user import User

#@unittest.skip("Not ready yet")
class TestDb(unittest.TestCase):
    def setUp(self):
        password = bcrypt.generate_password_hash("password")
        self.user = User("test_user", password)
        db.session.add(self.user)
        db.session.commit()
        
    def test_insert(self):
        player = Player(user, "Lannister")
        db.session.add(player)
        db.session.commit()
        result = Player.query.filter_by(username="Jaime").first()
        self.assertIsNotNone(result)
        self.assertequal(result.user.username, "test_user")
        db.session.delete(self.player)
        db.session.commit()
        result = Player.query.filter_by(username="Jaime").first()
        self.assertIsNone(result)

    def tearDown(self):
        db.session.delete(self.user)
        db.session.commit()