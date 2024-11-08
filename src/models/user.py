from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os
from . import db

from sqlalchemy.dialects.postgresql import JSONB
import json

bcrypt = Bcrypt()
load_dotenv()  
class User(db.Model):    
    schema_name = os.getenv('SCHEMA_NAME')
    __tablename__ = 'user'
    __table_args__ = {'schema': schema_name}
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    direccion = db.Column(JSONB, nullable=True)

    def __init__(self, nombre, email, password, direccion):
        self.nombre = nombre
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.direccion = json.dumps(direccion) if direccion else None

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    def get_direccion(self):
        return json.loads(self.direccion) if self.direccion else {}

    def __repr__(self):
        return f'<User {self.nombre}>'
