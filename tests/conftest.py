"""This makes the test configuration setup"""
# pylint: disable=redefined-outer-name

import pytest
from app import create_app
from app.db import db

@pytest.fixture()
def application():
    """This makes the app"""
    application = create_app()
    application.config.update(

        ENV='development',

    )
    with application.app_context():
        db.create_all()
        yield application
        db.session.remove()

        db.drop_all()

@pytest.fixture()
def add_user(application):
    with application.app_context():
        #new record
        user = User('keith@webizly.com', 'testtest')
        db.session.add(user)
        db.session.commit()


@pytest.fixture()
def client(application):
    """This makes the http client"""
    return application.test_client()


@pytest.fixture()
def runner(application):
    """This makes the task runner"""
    return application.test_cli_runner()
