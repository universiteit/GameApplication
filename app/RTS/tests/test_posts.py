import os
import unittest.mock as mock
from app import app, db, bcrypt
from app.RTS.models import *
from app.auth.models.user import User
from flask_sqlalchemy import SQLAlchemy
import unittest
import tempfile
from flask import redirect

class TestPosts(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        with app.app_context():
            db.drop_all()
            db.create_all()

        password = bcrypt.generate_password_hash("password")
        self.user = User("test", password)
        self.player = Player(self.user, "Lannister")
        self.town = Town(self.player, "Lannisport")

        db.session.add(self.user)
        db.session.add(self.player)
        db.session.add(self.town)
        db.session.commit()
        self.user = User.query.first()
        self.player = Player.query.first()
        self.town = Town(self.player, "lannisport")

    def tearDown(self):
        self.clear_session()

    def create_session(self):
        with self.app.session_transaction() as sess:
            sess['user_id'] = '1'

    def clear_session(self):
        with self.app.session_transaction() as sess:
            sess.clear()

    def test_create_player(self):
        self.create_session()

        self.app.post('/rts/create-player')
        player = Player(self.user, "Lannister")
        self.assertTrue(player)
        self.assertTrue(self.user)

    def test_create_unit(self):
        self.create_session()
        self.app.post('/rts/purchase-unit', data=dict(
            amount_of_cavalry=1,
            amount_of_knights=1,
            amount_of_pikemen=1
        ), follow_redirects=True)

        player = None
        self.assertFalse(player)

    def test_upgrade_building(self):
        self.create_session()
        self.app.post('/rts/purchase-building', data=dict(
            building_name="barrack",
            townid=1
        ), follow_redirects=True)

        player = None
        self.assertFalse(player)

        player = Player(self.user, "Lannister")
        self.assertNotEqual(self.town.player.id, player.id)

    @mock.patch("app.RTS.posts.redirect")
    def test_send_attack(self, mock_redirect):
        self.create_session()
        mock_redirect.return_value = redirect("rts/town/1")
        self.app.post('/rts/send-attack', data=dict(
            townid=1,
            amount_of_cavalry=1,
            amount_of_knights=1,
            amount_of_pikemen=1
        ), follow_redirects=True)
        self.assertFalse()
        self.assertEqual(mock_redirect.call_args[0][0], "rts/town/1")

        player = None
        self.assertFalse(player)

        player = Player(self.user, "Lannister")
        self.assertNotEqual(self.town.player.id, player.id)
        self.assertTrue(self.town.remove_units(0,0,0))
        self.assertEqual(mock_redirect.call_args[0][0], "rts/town/1")