from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


def create_app():
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
