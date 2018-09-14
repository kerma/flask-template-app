from flask import Flask

from . import rest  # noqa
from . import views  # noqa
from . import db  # noqa


def create_app():
    """Implement Flask application factory
    http://flask.pocoo.org/docs/1.0/patterns/appfactories/
    """

    app = Flask(__name__)

    db.init_db(app)

    app.register_blueprint(views.blueprint)
    app.register_blueprint(rest.blueprint, url_prefix='/rest')

    return app
