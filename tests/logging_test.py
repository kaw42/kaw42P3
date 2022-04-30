from pathlib import Path
import os

root = os.path.dirname(os.path.abspath(__file__))

def test_errorlog():
    errorLog = os.path.join(root, '../logs/errors.log')
    assert os.path.exists(errorLog) == True


def test_myapplog():
    myappLog = os.path.join(root, '../logs/myapp.log')
    assert os.path.exists(myappLog) == True


def test_requestlog():
    requestLog = os.path.join(root, '../logs/request.log')
    assert os.path.exists(requestLog) == True


def test_sqlalchemylog():
    sqlalchemyLog = os.path.join(root, '../logs/sqlalchemy.log')
    assert os.path.exists(sqlalchemyLog) == True


def test_werkzeuglog():
    werkzeugLog = os.path.join(root, '../logs/werkzeug.log')
    assert os.path.exists(werkzeugLog) == True
