from flask import Flask
from flask_jwt_extended import JWTManager
from config import config
from src.routes.userRoutes import usuario_blueprint as userRoutes
from src.routes.userRoutes2 import usuario_blueprint as userRoutes2
from src.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development'])
    db.init_app(app)
    jwt = JWTManager(app)
    app.register_blueprint(userRoutes)
    app.register_blueprint(userRoutes2)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
