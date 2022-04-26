from pathlib import Path
import os

root = os.path.dirname(os.path.abspath(__file__))

def test_errorlog():
    errorLog = os.path.join(root, '../app/logs/errors.log')
    assert os.path.exists(errorLog) == True


def test_flasklog():
    flaskLog = os.path.join(root, '../app/logs/flask.log')
    assert os.path.exists(flaskLog) == True


def test_myapplog():
    myappLog = os.path.join(root, '../app/logs/myapp.log')
    assert os.path.exists(myappLog) == True


def test_requestlog():
    requestLog = os.path.join(root, '../app/logs/request.log')
    assert os.path.exists(requestLog) == True


def test_sqlalchemylog():
    sqlalchemyLog = os.path.join(root, '../app/logs/sqlalchemy.log')
    assert os.path.exists(sqlalchemyLog) == True


def test_werkzeuglog():
    werkzeugLog = os.path.join(root, '../app/logs/werkzeug.log')
    assert os.path.exists(werkzeugLog) == True

def test_debug():
    file_name = Path(__file__)
    test_dir = file_name.parent
    proj_dir = test_dir.parent
    app_dir = proj_dir / "app"
    log_dir = app_dir / "logs"
    debug_file = log_dir / "errors.log"
    assert debug_file.exists()

def test_request():
    file_name = Path(__file__)
    test_dir = file_name.parent
    proj_dir = test_dir.parent
    app_dir = proj_dir / "app"
    log_dir = app_dir / "logs"
    request_file = log_dir / "request.log"
    assert request_file.exists()