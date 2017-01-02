import unittest
from app import app, db
from app import bcrypt
from app.RTS.models import *
from app.auth.models.user import User


class TestDb(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        with app.app_context():
            db.drop_all()
            db.create_all()

        # Create mock user
        password = bcrypt.generate_password_hash("password")
        self.user = User("test_user_1", password)
        self.user2 = User("test_user_2", password)
        db.session.add(self.user)
        db.session.add(self.user2)
        db.session.commit()

    def test_player(self):
        player = Player(self.user, "Lannister")
        db.session.add(player)
        db.session.commit()
        result = Player.query.first()
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
        db.session.commit()

    def test_player_town_relationship(self):
        player1 = Player(self.user, "Lannister")
        player2 = Player(self.user2, "Stark")
        db.session.add(player1)
        db.session.add(player2)
        db.session.commit()
        
        town = Town(player1, "Casterly Rock")
        db.session.add(town)
        db.session.commit()

        town.player = player2
        db.session.add(town)
        db.session.commit()

        result = Town.query.filter_by(name="Casterly Rock").first()
        self.assertEqual(result.player.user.username, player2.user.username)

        player1.towns.append(town)
        db.session.add(player1)
        db.session.commit()

        result = Town.query.filter_by(name="Casterly Rock").first()
        self.assertEqual(result.player.user.username, player1.user.username)
    
    def test_attack(self):
        player1 = Player(self.user, "Lannister")
        player2 = Player(self.user2, "Stark")
        db.session.add(player1)
        db.session.add(player2)
        db.session.commit()

        town = Town(player1, "Casterly Rock")
        town1 = Town(player2, "shithole")
        db.session.add(town1)        
        db.session.add(town)
        db.session.commit()

        attack = Attack(player1, town1, town, knights = 1)
        db.session.add(attack)
        db.session.commit()

    def tearDown(self):
        db.session.delete(self.user)