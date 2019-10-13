from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ifkgqahuxzyvjb:fb3d75cc5ee7ba82a81f8282404ef5a08ade7b2870fb7b92c0eee8c37a2fff90@ec2-54-83-55-125.compute-1.amazonaws.com:5432/dcac5vga7nf0fc'

    db.init_app(app)

    from .views import api
    app.register_blueprint(api)


    return app
