from flask import Flask, request, jsonify,session
from flask import render_template
#dev
#from app.repository.repository_streaming import UsuarioRepository,ContentRepository

#prod
from repository.repository_streaming import UsuarioRepository,ContentRepository,StatsRepository
import json


class ContentService:
    @staticmethod
    def obtener_catalogo():
         
        catalogo = ContentRepository.obtener_catalogo()

        dato_recuperado = session.get('id_usuario', 'No hay dato almacenado')
        if(dato_recuperado == 'No hay dato almacenado'):
            return render_template('login.html')
        else:
            return render_template('catalogo.html', catalogo=catalogo, id_usuario = dato_recuperado)
         
    
    
    @staticmethod
    def obtener_contenido(nombre_contenido):
        #obtener informacion del contenido
        print(nombre_contenido)
        contenido = ContentRepository.obtener_contenido(nombre_contenido)

        #Aumentar en 1 el contador de visitas
        StatsRepository.aumentar_visitas(nombre_contenido)

        print(contenido)
        return render_template('reproductor.html', contenido=contenido)

    

    
    
 
 