import sqlite3
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def seed_db(db):
    with current_app.open_resource('seed-data.sql') as f:
        db.executescript(f.read().decode('utf8'))

def init_db(app):
    with app.app_context():
        db = get_db()
        with current_app.open_resource('entities.sql') as f:
            db.executescript(f.read().decode('utf8'))
        seed_db(db)


def init_app(app):
    app.teardown_appcontext(close_db)
    init_db(app)
