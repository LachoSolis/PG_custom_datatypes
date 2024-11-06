from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os
from . import db

from .direccion import Direccion

bcrypt = Bcrypt()
load_dotenv()  

class User2(db.Model):    
    schema_name = os.getenv('SCHEMA_NAME')
    __tablename__ = 'user2'
    __table_args__ = {'schema': schema_name}
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    direccion = db.Column(Direccion) 

    def __init__(self, nombre, email, password, direccion=None):
        self.nombre = nombre
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.direccion = direccion

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
     
    def set_direccion(self, direccion):
        if isinstance(direccion, dict) and all(key in direccion for key in ["calle", "ciudad", "estado", "codigo_postal"]):
            self.direccion = direccion
        else:
            raise ValueError("La dirección debe incluir los campos calle, ciudad, estado y codigo_postal")

    def get_direccion(self):
        return self.direccion 
    
    def __repr__(self):
        return f'<User {self.nombre}>'
