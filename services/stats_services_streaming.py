from flask import Flask, request, jsonify
 
import json
class StatsService:
    @staticmethod
    def obtener_estadisticas():
        estadisticas = [
            {'id': '1', 'pelicula': 'El Padrino', 'precio': '100'},
            {'id': '2', 'pelicula': 'El Padrino II', 'precio': '100'},
            {'id': '3', 'pelicula': 'El Padrino III', 'precio': '100'},
            {'id': '4', 'pelicula': 'El Padrino IV', 'precio': '100'},
            {'id': '5', 'pelicula': 'El Padrino V', 'precio': '100'},
            {'id': '6', 'pelicula': 'El Padrino VI', 'precio': '100'},
            {'id': '7', 'pelicula': 'El Padrino VII', 'precio': '100'},
            {'id': '8', 'pelicula': 'El Padrino VIII', 'precio': '100'},
            {'id': '9', 'pelicula': 'El Padrino IX', 'precio': '100'},
            {'id': '10', 'pelicula': 'El Padrino X', 'precio': '100'},
            {'id': '11', 'pelicula': 'El Padrino XI', 'precio': '100'},
            {'id': '12', 'pelicula': 'El Padrino XII', 'precio': '100'},
            {'id': '13', 'pelicula': 'El Padrino XIII', 'precio': '100'},
            {'id': '14', 'pelicula': 'El Padrino XIV', 'precio': '100'},
            {'id': '15', 'pelicula': 'El Padrino XV', 'precio': '100'},
        ]
        return jsonify({'estadisticas': estadisticas})
    