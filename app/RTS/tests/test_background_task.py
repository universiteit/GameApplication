import unittest
import app.RTS.background_tasks as background_tasks
from app import db, app
from unittest import mock
from app import bcrypt
from app.RTS.models import *
from app.auth.models.user import User

class test_background_tasks(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        with app.app_context():
            db.drop_all()
            db.create_all()

        # Create mock user
        password = bcrypt.generate_password_hash("password")
        self.user = User("test_user_1", password)
        self.user2 = User("test_user_2", password)
        self.player = Player(self.user, "Lannister")
        self.player2 = Player(self.user2, "Stark")
        self.town = Town(self.player2, "Winterfell", knights = 1)
        self.attack = Attack(self.player, self.town, None, cavalry = 100)
        db.session.add(self.user)
        db.session.add(self.user2)
        db.session.commit()

    @mock.patch('app.RTS.background_tasks.db')
    @mock.patch('app.RTS.background_tasks.Town')
    def test_update_towns(self, mock_db, mock_Town):
        background_tasks.update_towns()
        mock_Town.query.all = mock.MagicMock(return_value = [self.town], name="disco")
        self.town.update_resources = mock.MagicMock()
        self.town.update_upgrade = mock.MagicMock()
        

    def test_update_attacks(self):
        pass

    def test_setup_scheduler(self):
        pass