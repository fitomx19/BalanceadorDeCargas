from flask import Blueprint

#production
#from app.controller.controller_streaming import StreamingController

#dev
from controller.controller_streaming import StreamingController

streaming_bp = Blueprint('streaming', __name__)

@streaming_bp.route('/streaming', methods=['GET'])
def saludar():
    return StreamingController().saludar()

@streaming_bp.route('/streaming/subir-archivo', methods=['POST'])
def subir_archivo_al_servidor():
    return StreamingController().subir_archivo_al_servidor()


@streaming_bp.route('/streaming/subir-archivo', methods=['GET'])
def subir_archivo_al_servidor_get():
    return StreamingController().subir_archivo_al_servidor_get()

@streaming_bp.route('/streaming/files', methods=['GET'])
def obtener_archivos():
    return StreamingController().obtener_archivos()

@streaming_bp.route('/streaming/files/<string:nombre_archivo>', methods=['GET'])
def obtener_archivo(nombre_archivo):
    return StreamingController().obtener_archivo(nombre_archivo)

@streaming_bp.route('/download/<filename>', methods=['GET'])
def download(filename):
    return StreamingController().download(filename)
 

#Administracion de Usuarios

@streaming_bp.route('/streaming/usuarios', methods=['POST'])
def crear_usuario():
    return StreamingController().crear_usuario()

@streaming_bp.route('/streaming/usuarios', methods=['GET'])
def obtener_usuarios():
    return StreamingController().obtener_usuarios()

@streaming_bp.route('/streaming/usuarios/<string:nombre_usuario>', methods=['GET'])
def obtener_usuario(nombre_usuario):
    return StreamingController().obtener_usuario(nombre_usuario)

@streaming_bp.route('/streaming/actualizar-usuario', methods=['POST'])
def actualizar_usuario():
    return StreamingController().actualizar_usuario()

@streaming_bp.route('/streaming/usuarios/<string:nombre_usuario>', methods=['DELETE'])
def eliminar_usuario(nombre_usuario):
    return StreamingController().eliminar_usuario(nombre_usuario)

#Suscripción e Inicio de Sesión:
@streaming_bp.route('/streaming/suscripcion', methods=['POST'])
def suscripcion():
    return StreamingController().suscripcion()

@streaming_bp.route('/streaming/suscripcion', methods=['GET'])
def get_suscripcion():
    return StreamingController().get_suscripcion()

@streaming_bp.route('/streaming/login', methods=['POST'])
def login():
    return StreamingController().login()

@streaming_bp.route('/streaming/login', methods=['GET'])
def loginGet():
    return StreamingController().logingGET()

@streaming_bp.route('/streaming/logout', methods=['GET'])
def logout():
    return StreamingController().logout()

#Gestion de Contenidos
@streaming_bp.route('/streaming/catalogo', methods=['GET'])
def obtener_catalogo():
    return StreamingController().obtener_catalogo()

@streaming_bp.route('/streaming/catalogo/<string:nombre_contenido>', methods=['GET'])
def obtener_contenido(nombre_contenido):
    return StreamingController().obtener_contenido(nombre_contenido)

#Gestión de Pagos:
@streaming_bp.route('/streaming/pagos', methods=['POST'])
def realizar_pago():
    return StreamingController().realizar_pago()

@streaming_bp.route('/streaming/pagos', methods=['GET'])
def obtener_pagos():
    return StreamingController().obtener_pagos()

@streaming_bp.route('/streaming/pagos/<string:nombre_usuario>', methods=['GET'])
def obtener_pago(nombre_usuario):
    return StreamingController().obtener_pago(nombre_usuario)

@streaming_bp.route('/streaming/pagos/<string:nombre_usuario>', methods=['PUT'])
def actualizar_pago(nombre_usuario):
    return StreamingController().actualizar_pago(nombre_usuario)

#Estadisticas
@streaming_bp.route('/streaming/estadisticas', methods=['GET'])
def obtener_estadisticas():
    return StreamingController().obtener_estadisticas()
