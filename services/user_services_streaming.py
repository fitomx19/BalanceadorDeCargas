from flask import Flask, request, jsonify
 
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
        return jsonify({'mensaje': 'Usuario creado exitosamente'})
    
    @staticmethod
    def obtener_usuarios():
        usuarios = [
            {'usuario': 'jose', 'contrasena': '1234', 'nombre': 'Jose', 'apellido': 'Perez', 'correo': 'adolfo@gmail.com', 'tarjeta': '123456789', 'fecha_expiracion': '12/12/2020', 'cvv': '123', 'tipo': 'visa'}
        ]
        return jsonify({'usuarios': usuarios})
    
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
    def actualizar_usuario(nombre_usuario):
        usuario = request.json['usuario']
        contrasena = request.json['contrasena']
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        correo = request.json['correo']
        tarjeta = request.json['tarjeta']
        fecha_expiracion = request.json['fecha_expiracion']
        cvv = request.json['cvv']
        tipo = request.json['tipo']
        return jsonify({'mensaje': 'Usuario actualizado exitosamente'})
    
    @staticmethod
    def eliminar_usuario(nombre_usuario):
        return jsonify({'mensaje': 'Usuario eliminado exitosamente'})
    
    
    
    
 
 