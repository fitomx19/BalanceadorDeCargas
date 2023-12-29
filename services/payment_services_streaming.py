from flask import Flask, request, jsonify
 
import json
class PaymentService:
    @staticmethod
    def realizar_pago():
        id_cliente = request.json['id']
        id_pelicula = request.json['id_pelicula']
        metodo_pago = request.json['metodo_pago']
        status = request.json['status']
        return jsonify({'mensaje': 'Pago exitoso'})
    
    @staticmethod
    def obtener_pago():
        #listar pagos
        pagos = [
            {'id': '1', 'id_cliente': '1', 'id_pelicula': '1', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
            {'id': '2', 'id_cliente': '2', 'id_pelicula': '2', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
            {'id': '3', 'id_cliente': '3', 'id_pelicula': '3', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
            {'id': '4', 'id_cliente': '4', 'id_pelicula': '4', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
            {'id': '5', 'id_cliente': '5', 'id_pelicula': '5', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
            {'id': '6', 'id_cliente': '6', 'id_pelicula': '6', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
            {'id': '7', 'id_cliente': '7', 'id_pelicula': '7', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
            {'id': '8', 'id_cliente': '8', 'id_pelicula': '8', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
            {'id': '9', 'id_cliente': '9', 'id_pelicula': '9', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
            {'id': '10', 'id_cliente': '10', 'id_pelicula': '10', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
        ]
        return jsonify({'pagos': pagos})
    
    @staticmethod
    def obtener_pago(nombre_pago):
        #listar pagos
        pagos = [
            {'id': '1', 'id_cliente': '1', 'id_pelicula': '1', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
            {'id': '2', 'id_cliente': '2', 'id_pelicula': '2', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
            {'id': '3', 'id_cliente': '3', 'id_pelicula': '3', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
            {'id': '4', 'id_cliente': '4', 'id_pelicula': '4', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
            {'id': '5', 'id_cliente': '5', 'id_pelicula': '5', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
            {'id': '6', 'id_cliente': '6', 'id_pelicula': '6', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
            {'id': '7', 'id_cliente': '7', 'id_pelicula': '7', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
            {'id': '8', 'id_cliente': '8', 'id_pelicula': '8', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
            {'id': '9', 'id_cliente': '9', 'id_pelicula': '9', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
            {'id': '10', 'id_cliente': '10', 'id_pelicula': '10', 'metodo_pago': 'Tarjeta', 'status': 'Exitoso'},
        ]
        pago = [pago for pago in pagos if (pago['id'] == nombre_pago)]
        return jsonify({'pago': pago})
    
    @staticmethod
    def actualizar_pago(nombre_pago):
        id_cliente = request.json['id']
        id_pelicula = request.json['id_pelicula']
        metodo_pago = request.json['metodo_pago']
        status = request.json['status']
        return jsonify({'mensaje': 'Pago actualizado exitosamente'})
    
    
    