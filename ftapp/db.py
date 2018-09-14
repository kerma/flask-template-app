import os

import psycopg2

from flask import current_app
from flask import g


def init_db(app):
    try:
        app.config['db_dsn'] = ('host={DB_HOST} '
                                'dbname={DB_NAME} '
                                'user={DB_USER} '
                                'password={DB_PASSWORD}').format(**os.environ)
    except KeyError as e:
        app.logger.error('Missing database configuration: %s', e)

    @app.teardown_appcontext
    def close_db(error):
        """Close the database at the end of the request"""
        if hasattr(g, 'db'):
            g.db.close()


def connect_db():
    dsn = current_app.config['db_dsn']
    return psycopg2.connect(dsn)


def get_db():
    """Open a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'db'):
        g.db = connect_db()
    return g.db
