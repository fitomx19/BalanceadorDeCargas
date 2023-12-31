from flask import Flask, request, jsonify,render_template,session
#from app.repository.repository_streaming import UsuarioRepository
from repository.repository_streaming import UsuarioRepository


import json
class StreamingUserService:
    @staticmethod
    def crear_usuario():
        usuario = request.json['usuario']
        contrasena = request.json['contrasena']
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        correo = request.json['correo']
        tarjeta = request.json['tarjeta']
        fecha_expiracion = request.json['fecha_expiracion']
        cvv = request.json['cvv']
        tipo = request.json['tipo']


        user = {
            "usuario": usuario,
            "contrasena": contrasena,
            "nombre": nombre,
            "apellido": apellido,
            "correo": correo,
            "tarjeta": tarjeta,
            "fecha_expiracion": fecha_expiracion,
            "cvv" : cvv,
            "tipo": tipo,
            "suscripcion": False
        }

        proceso = UsuarioRepository.guardar_usuario(user)

        return jsonify({'mensaje': proceso})
    
    @staticmethod
    def obtener_usuarios():
        
        usuarios = UsuarioRepository.obtener_usuarios()
        usuario = session.get('id_usuario', 'No hay dato almacenado')
        usuario = UsuarioRepository.obtener_usuario(usuario)

        return render_template('usuarios.html' , usuarios = usuarios, usuario = usuario)
    
    @staticmethod
    def obtener_usuario(nombre_usuario):
        usuarios = [
            {'usuario': 'jose', 'contrasena': '1234', 'nombre': 'Jose', 'apellido': 'Perez', 'correo': 'adolfo@gmail.com', 'tarjeta': '123456789', 'fecha_expiracion': '12/12/2020', 'cvv': '123', 'tipo': 'visa'}
            ]
        for usuario in usuarios:
            if usuario['usuario'] == nombre_usuario:
                return jsonify(usuario)
        return jsonify({'mensaje': 'Usuario no encontrado'})
    @staticmethod
    def actualizar_usuario():
        id_usuario = request.json['id']
        usuario = request.json['usuario']
        correo = request.json['correo']
         
        usuario = {
            "usuario": usuario,
            "correo": correo
        }
        proceso = UsuarioRepository.actualizar_usuario(id_usuario, usuario)

        return jsonify({'mensaje': 'Usuario actualizado exitosamente'})
    
    @staticmethod
    def eliminar_usuario(nombre_usuario):
        return jsonify({'mensaje': 'Usuario eliminado exitosamente'})
    
    
    
    
 
 