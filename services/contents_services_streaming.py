from flask import Flask, request, jsonify
 
import json
class ContentService:
    @staticmethod
    def obtener_catalogo():
        catalogo = [
            {'id': '1', 'nombre': 'El Padrino', 'genero': 'Drama', 'anio': '1972' ,'ubicacion' : 'C:/Users/Usuario/Desktop/Proyecto-Streaming/archivos/El Padrino.mp4'},
            {'id': '2', 'nombre': 'El Padrino II', 'genero': 'Drama', 'anio': '1974' ,'ubicacion' : 'C:/Users/Usuario/Desktop/Proyecto-Streaming/archivos/El Padrino II.mp4'},
            {'id': '3', 'nombre': 'El Padrino III', 'genero': 'Drama', 'anio': '1990' ,'ubicacion' : 'C:/Users/Usuario/Desktop/Proyecto-Streaming/archivos/El Padrino III.mp4'},
            {'id': '4', 'nombre': 'El Padrino IV', 'genero': 'Drama', 'anio': '1994' ,'ubicacion' : 'C:/Users/Usuario/Desktop/Proyecto-Streaming/archivos/El Padrino IV.mp4'},
            {'id': '5', 'nombre': 'El Padrino V', 'genero': 'Drama', 'anio': '1998' ,'ubicacion' : 'C:/Users/Usuario/Desktop/Proyecto-Streaming/archivos/El Padrino V.mp4'},
            {'id': '6', 'nombre': 'El Padrino VI', 'genero': 'Drama', 'anio': '2002' ,'ubicacion' : 'C:/Users/Usuario/Desktop/Proyecto-Streaming/archivos/El Padrino VI.mp4'},
            {'id': '7', 'nombre': 'El Padrino VII', 'genero': 'Drama', 'anio': '2006' ,'ubicacion' : 'C:/Users/Usuario/Desktop/Proyecto-Streaming/archivos/El Padrino VII.mp4'},
            {'id': '8', 'nombre': 'El Padrino VIII', 'genero': 'Drama', 'anio': '2010' ,'ubicacion' : 'C:/Users/Usuario/Desktop/Proyecto-Streaming/archivos/El Padrino VIII.mp4'},
            {'id': '9', 'nombre': 'El Padrino IX', 'genero': 'Drama', 'anio': '2014' ,'ubicacion' : 'C:/Users/Usuario/Desktop/Proyecto-Streaming/archivos/El Padrino IX.mp4'},
            {'id': '10', 'nombre': 'El Padrino X', 'genero': 'Drama', 'anio': '2018' ,'ubicacion' : 'C:/Users/Usuario/Desktop/Proyecto-Streaming/archivos/El Padrino X.mp4'},
        ]
        
        
        return jsonify({'catalogo': catalogo})
    
    
    
    

    
    
 
 