from flask import Flask, request, jsonify
 
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
        usuario = request.json['usuario']
        contrasena = request.json['contrasena']

        #revisar si el usuario existe en la base de datos

        

        return jsonify({'mensaje': 'Login exitoso'})
    
    
    
 
 