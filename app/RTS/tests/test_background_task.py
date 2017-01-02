import unittest, datetime, time
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
    def test_update_towns(self, mock_Town, mock_db):
        mock_Town.query.all = mock.MagicMock(return_value = [self.town])
        self.town.update_resources = mock.MagicMock()
        self.town.update_upgrade = mock.MagicMock()
        background_tasks.update_towns()
        self.assertTrue(self.town.update_upgrade.called)
        self.assertTrue(self.town.update_resources.called)
        self.assertEqual(self.town, mock_db.session.add.call_args[0][0])
        self.assertTrue(mock_db.session.add.called)
        self.assertTrue(mock_db.session.commit.called)

    @mock.patch('app.RTS.background_tasks.datetime')    
    @mock.patch('app.RTS.background_tasks.Attack')
    def test_update_attacks(self, mock_attack, mock_datetime):
        mock_datetime.datetime.now = mock.MagicMock(return_value=datetime.datetime(1,1,1))
        mock_order_by = mock.MagicMock()
        mock_order_by.first = mock.MagicMock(side_effect=[self.attack, self.attack, None])
        mock_attack.query.order_by = mock.MagicMock(return_value = mock_order_by)
        self.attack.resolve = mock.MagicMock()

        background_tasks.update_attacks()
        self.assertTrue(self.attack.resolve.called)
        self.assertEqual(len(self.attack.resolve.call_args_list), 2)

    @mock.patch('app.RTS.background_tasks.update_towns')
    @mock.patch('app.RTS.background_tasks.update_attacks')
    def test_setup_scheduler(self, mock_update_attacks, mock_update_towns):
        background_tasks.setup_scheduler()
        time.sleep(6)
        self.assertTrue(mock_update_attacks.called)
        self.assertTrue(mock_update_towns.called)
        time.sleep(6)
        self.assertEqual(len(mock_update_attacks.call_args_list), 2)