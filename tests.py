import unittest

from flask_testing import TestCase

from app import create_app, db
from app.models import User

class TestBase(TestCase):

    def create_app(self):

        # pass in test configurations
        config_name = 'testing'
        app = create_app(config_name)
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql://admin_kospedia:Admkpd1!@localhost/kospedia_test'
        )
        return app

    def setUp(self):
        """
        Will be called before every test
        """

        db.create_all()

        # create test admin user
        admin = User(email="admin@99.com", username="admin99", password="admin99", is_admin=True)

        # create test non-admin user
        user = User(email="user@99.com", username="user99", password="user99")

        # save users to database
        db.session.add(admin)
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()
