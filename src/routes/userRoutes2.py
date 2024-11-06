from flask import Blueprint, request
from src.controllers.userController2 import crear_usuario, crear_usuario_base,login_usuario, obtener_usuario, eliminar_usuario

usuario_blueprint = Blueprint('usuarios2', __name__)

@usuario_blueprint.route('/users2', methods=['POST'])
def crear_usuario_ruta():
    data = request.get_json()
    return crear_usuario(data)

@usuario_blueprint.route('/users_base2', methods=['POST'])
def crear_usuario_base_ruta():
    data = request.get_json()
    return crear_usuario_base(data)

@usuario_blueprint.route('/login2', methods=['POST'])
def login_ruta():
    data = request.get_json()
    return login_usuario(data)

@usuario_blueprint.route('/profile2', methods=['GET'])
def obtener_usuario_ruta():
    return obtener_usuario()

@usuario_blueprint.route('/users2/<int:user_id>', methods=['DELETE'])
def eliminar_usuario_ruta(user_id):
    return eliminar_usuario(user_id)

