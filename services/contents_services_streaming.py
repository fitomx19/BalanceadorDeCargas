from flask import Flask, request, jsonify,session
from flask import render_template
#PROD
#from app.repository.repository_streaming import UsuarioRepository,ContentRepository
from repository.repository_streaming import UsuarioRepository,ContentRepository
import json


class ContentService:
    @staticmethod
    def obtener_catalogo():
        #catalogo = [
        #    {'id': '1', 'nombre': 'El Padrino', 'genero': 'Drama', 'anio': '1972' , 'poster': 'padrino.png', 'ubicacion' : 'padrino.mp4'},
        #    {'id': '2', 'nombre': 'Batman Begins', 'genero': 'Accion', 'anio': '2005' ,'poster': 'batman.png','ubicacion' : 'C:/Users/Usuario/Desktop/Proyecto-Streaming/archivos/El Padrino II.mp4'},
        #    {'id': '3', 'nombre': 'Memento', 'genero': 'Drama', 'anio': '2001' ,'poster': 'memento.png','ubicacion' : 'C:/Users/Usuario/Desktop/Proyecto-Streaming/archivos/El Padrino III.mp4'},
        #    {'id': '4', 'nombre': 'La naranja Mecanica', 'genero': 'Drama', 'anio': '1971' ,'poster': 'naranjamecanica.png','ubicacion' : 'C:/Users/Usuario/Desktop/Proyecto-Streaming/archivos/El Padrino IV.mp4'},
        #    {'id': '5', 'nombre': 'Oppenheimer', 'genero': 'Drama', 'anio': '2023' ,'poster': 'oppenheimer.png','ubicacion' : 'C:/Users/Usuario/Desktop/Proyecto-Streaming/archivos/El Padrino V.mp4'},
        #    {'id': '6', 'nombre': 'The house that jack built', 'genero': 'Drama', 'anio': '2018' ,'poster': 'thehousethatjackbuilt.png','ubicacion' : 'C:/Users/Usuario/Desktop/Proyecto-Streaming/archivos/El Padrino VI.mp4'},
        #    {'id': '7', 'nombre': 'The hunt', 'genero': 'Drama', 'anio': '2012' ,'poster': 'thehunt.png','ubicacion' : 'C:/Users/Usuario/Desktop/Proyecto-Streaming/archivos/El Padrino VII.mp4'},
        #    {'id': '8', 'nombre': 'Vangogh en la puerta de la eternidad', 'genero': 'Drama', 'anio': '2018' ,'poster': 'vangoghmovie.png','ubicacion' : 'C:/Users/Usuario/Desktop/Proyecto-Streaming/archivos/El Padrino VIII.mp4'},
        #    {'id': '9', 'nombre': 'Casino', 'genero': 'Crimen/Suspenso', 'anio': '1995' ,'poster': 'casino.png','ubicacion' : 'C:/Users/Usuario/Desktop/Proyecto-Streaming/archivos/El Padrino IX.mp4'},
        #     ]

        #buscar en la base de datos los archivos
        catalogo = ContentRepository.obtener_catalogo()

        dato_recuperado = session.get('id_usuario', 'No hay dato almacenado')
        if(dato_recuperado == 'No hay dato almacenado'):
            return render_template('login.html')
        else:
            return render_template('catalogo.html', catalogo=catalogo, id_usuario = dato_recuperado)
         
    
    
    @staticmethod
    def obtener_contenido(nombre_contenido):
        return render_template('reproductor.html', nombre_contenido=nombre_contenido)

    

    
    
 
 