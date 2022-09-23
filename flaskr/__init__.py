from flask import Flask, jsonify

from .blueprints import home, products
from .models.Base import db


def create_app():

    # create the app
    app = Flask(__name__)

    # configure the SQLite database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

    # initialize the app with the extension
    db.init_app(app)
    
    app.register_blueprint(home.bp)
    app.add_url_rule('/', endpoint='home')
    app.register_blueprint(products.bp)

    with app.app_context():
        db.create_all()

    return app
