from flask import Flask

from .blueprints import home, products, auth
from .models.Base import db


def create_app():

    # create the app
    app = Flask(__name__)

    # configure the SQLite database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    app.config['SECRET_KEY'] = 'abc123..'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # initialize the app with the extension
    db.init_app(app)
    
    app.register_blueprint(home.bp)
    app.add_url_rule('/', endpoint='home')
    app.register_blueprint(products.bp)
    app.register_blueprint(auth.bp)

    with app.app_context():
        db.create_all()

    return app
