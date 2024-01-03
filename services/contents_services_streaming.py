from flask import Flask, request, jsonify,session
from flask import render_template
#dev
#from app.repository.repository_streaming import UsuarioRepository,ContentRepository

#prod
from repository.repository_streaming import UsuarioRepository,ContentRepository
import json


class ContentService:
    @staticmethod
    def obtener_catalogo():
        #catalogo = [
        #    {'id': '1', 'nombre': 'El Padrino', 'genero': 'Drama', 'anio': '1972' , 'poster': 'padrino.png', 'ubicacion' : 'padrino.mp4'},
        
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

    

    
    
 
 