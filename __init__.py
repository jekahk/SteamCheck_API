from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import sqlite3


def create_app():

    con = sqlite3.connect("steamcheckerDB.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS history(name TEXT, level INTEGER, badge INTEGER, xp TEXT, timestamp DATETIME)")

    app = Flask(__name__)
    CORS(app)

    @app.route("/")
    def hello():
        return "<h1 style='color:blue>Hello There!</h1>"

    if __name__ == "__main__":
        app.run(ssl_context=('cert.pem', 'key.pem'))

    from .views import main
    app.register_blueprint(main)

    return app
