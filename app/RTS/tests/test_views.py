import os
from app import app, db
from flask_sqlalchemy import SQLAlchemy
import unittest
import tempfile

@unittest.skip("Not ready yet")
class TestViews(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        with app.app_context():
            db.create_all()

    def tearDown(self):
        pass

    def test_index(self):
        rv = self.app.get('/RTS')
        print(rv)
        assert b'Houses' in rv.data