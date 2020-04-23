""" create init file """

from flask import Flask

# TODO: need import from routes models that we will create
from my_app.models import db, migrate
from my_app.routes.hello_routes import hello_routes
from my_app.routes.BGG_routes import BGG_routes


# application factory patter
def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///BGG_Game.db"
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(hello_routes)
    app.register_blueprint(BGG_routes)
    
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)