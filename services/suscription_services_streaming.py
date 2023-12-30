from flask import Flask, request, jsonify, render_template
from app.repository.repository_streaming import UsuarioRepository
#from repository.repository_streaming import UsuarioRepository

import json
class SuscriptionService:
    @staticmethod
    def suscripcion():
        id_usuario = request.json['id']
        metodo_pago = request.json['metodo_pago']
        precio = request.json['precio']
        status = request.json['status']

        #repositorio de suscripciones

        return jsonify({'mensaje': 'Suscripcion exitosa'})
    
    @staticmethod
    def login():
        print(request.json)
        usuario = request.json['username']
        contrasena = request.json['password']

        #revisar si el usuario existe en la base de datos

        user = {
            "usuario": usuario,
            "contrasena": contrasena
        }

        proceso = UsuarioRepository.revisar_usuario_contrasena(user)
        print("proceso : ",proceso)
        if((proceso) != None):
            return jsonify({ 'nombre_usuario' : "adolfo", 'status':200})
        else:
            return jsonify({'status': 400}) 
    
    @staticmethod
    def loginGet():
        content = "Inicio de Sesion"
        return render_template('login.html', dynamic_content=content)
    
    
 
 