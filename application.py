from flask import Flask

from flaskr.blueprints import home, products, auth
from flaskr.models.Base import db

# create the app
application = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
application.config['SECRET_KEY'] = 'abc123..'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# initialize the app with the extension
db.init_app(application)

application.register_blueprint(home.bp)
application.add_url_rule('/', endpoint='home')
application.register_blueprint(products.bp)
application.register_blueprint(auth.bp)

with application.app_context():
    db.create_all()

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.

    application.debug = True
    application.run()