import unittest
from app import app, db
from app import bcrypt
from app.RTS.models.player import Player
from app.auth.models.user import User

@unittest.skip("Not ready yet")
class TestDb(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        with app.app_context():
            db.create_all()

        # Create mock user
        password = bcrypt.generate_password_hash("password")
        self.user = User("test_user", password)
        db.session.insert(user)
        db.session.commit()

    def test_player(self):
        player = Player(self.user, "Lannister")
        db.session.add(player)
        db.session.commit()
        result = Player.query.filter_by(username="Jaime").first()
        self.assertIsNotNone(result)
        db.session.delete(player)
        db.session.commit()

    def test_town(self):
        player = Player(self.user, "Lannister")
        db.session.add(player)
        town = Town(player, "Casterly Rock")
        db.session.add(town)
        db.session.commit()

        result = Town.query.filter_by(name="Casterly Rock").first()
        self.assertIsNotNone(result)

        db.session.delete(town)
        db.session.delete(player)
        db.commit()
        
    def tearDown(self):
        db.session.delete(self.user)
        db.session.commit()