import os
import unittest.mock as mock
from app import app, db, bcrypt
from app.RTS.models import *
from app.auth.models.user import User
from flask_sqlalchemy import SQLAlchemy
import unittest
import tempfile

class TestViews(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        with app.app_context():
            db.drop_all()
            db.create_all()
        
        password = bcrypt.generate_password_hash("password")
        self.user = User("test", password)
        
        db.session.add(self.user)
        db.session.commit()
        self.user = User.query.first()

    def tearDown(self):
        self.clear_session()

    def create_session(self):
        with self.app.session_transaction() as sess:
            sess['user_id'] = '1'
    
    def clear_session(self):
        with self.app.session_transaction() as sess:
            sess.clear()

    def test_index(self):
        rv = self.app.get('/rts/')
        self.assertEqual(rv.headers['location'], 'http://localhost/auth/login')
        
        self.create_session()
        rv = self.app.get('/rts/')
        assert b'You have not yet created' in rv.data
        player = Player(self.user, "Lannister")
        db.session.add(player)
        db.session.commit()

        rv = self.app.get('/rts/')
        assert b'View your house!' in rv.data

    @mock.patch('app.RTS.views.Town')
    @mock.patch('app.RTS.views.current_user')
    def test_all_towns(self, mock_current_user, mock_town):
        self.create_session()
        mock_current_user.return_value = self.user
        player = Player(self.user, "Lannister")
        mock_town.query.all = mock.MagicMock(return_value = [Town(player, "Lannisport")])

        rv = self.app.get('/rts/towns', follow_redirects = True)
        assert b'Lannisport' in rv.data

    