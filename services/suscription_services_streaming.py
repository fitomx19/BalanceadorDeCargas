from flask import Flask, request, jsonify, render_template,session
#from app.repository.repository_streaming import UsuarioRepository,SuscripcionRepository
from repository.repository_streaming import UsuarioRepository,SuscripcionRepository

import json
class SuscriptionService:
    @staticmethod
    def suscripcion():
        id_usuario = request.form.get('id_usuario')

        #actualizar suscripcion
        SuscripcionRepository.actualizar_suscripcion(id_usuario)
        return jsonify({'suscripcion': 'Suscripcion exitosa'})
    
    def get_suscripcion():
        dato_recuperado = session.get('id_usuario', 'No hay dato almacenado')
        print(dato_recuperado)
        return render_template('suscripcion.html', id_usuario=dato_recuperado)
    
    @staticmethod
    def login():
        usuario = request.json['username']
        contrasena = request.json['password']
        #revisar si el usuario existe en la base de datos
        user = {
            "usuario": usuario,
            "contrasena": contrasena
        }
        proceso = UsuarioRepository.revisar_usuario_contrasena(user)
        if((proceso) != None):
            #almacenamos la sesion
            session['id_usuario'] = str(proceso['_id'])
            #revisaremos si tiene suscripcion activa
            suscripcion = proceso['suscripcion']
            if isinstance(suscripcion, bool) and suscripcion:
                #tiene suscripcion activa
                return jsonify({'id_usuario': str(proceso['_id']) ,'nombre_usuario' : proceso['usuario'],  'status':200})
            else:
                #no tiene suscripcion activa  
                return jsonify({'id_usuario': str(proceso['_id']) ,'nombre_usuario' : proceso['usuario'],  'status':202})
        else:
            return jsonify({'status': 400}) 
        
    @staticmethod
    def logout():
        session.clear()
        return render_template('login.html' )
    
    @staticmethod
    def loginGet():
        content = "Inicio de Sesion"
        return render_template('login.html', dynamic_content=content)
    
    
 
 