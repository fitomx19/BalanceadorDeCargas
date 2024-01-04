from bson import ObjectId
#from app.database import conectar_base_de_datos
from database import conectar_base_de_datos
class UsuarioRepository():
    def guardar_usuario(data):
        try:
            db = conectar_base_de_datos()
            db.usuarios.insert_one(data)
            return "insercion exitosa"
        except Exception as e:
            print("Error al insertar:", e)
            return "error al insertar"
        
    def revisar_usuario_contrasena(data):
        try:
            db = conectar_base_de_datos()
            usuario = db.usuarios.find_one(data)
            print(usuario)
            return usuario
        except Exception as e:
            print("Error al buscar usuario:", e)
            return "error al insertar"
        
    def actualizar_usuario(id_usuario, data):
        try:
            db = conectar_base_de_datos()
            db.usuarios.update_one({'_id': ObjectId(id_usuario)}, {'$set': data})
            return "actualizacion exitosa"
        except Exception as e:
            print("Error al actualizar:", e)
            return "error al actualizar"
        
        
    
    def obtener_usuarios():
        try:
            db = conectar_base_de_datos()
            usuarios = db.usuarios.find()
            return usuarios
        except Exception as e:
            print("Error al obtener usuarios:", e)
            return "error al obtener usuarios"
    def obtener_usuario(id_usuario):
        try:
            db = conectar_base_de_datos()
            usuario = db.usuarios.find_one({'_id': ObjectId(id_usuario)})
            return usuario
        except Exception as e:
            print("Error al obtener usuario:", e)
            return "error al obtener usuario"
        
class SuscripcionRepository():
    def actualizar_suscripcion(id_usuario):
        try:
            db = conectar_base_de_datos()
            db.usuarios.update_one({'_id': ObjectId(id_usuario)}, {'$set': {'suscripcion': True}})
            return "actualizacion exitosa"
        except Exception as e:
            print("Error al actualizar:", e)
            return "error al actualizar"
        

class ContentRepository():
    def obtener_catalogo():
        try:
            db = conectar_base_de_datos()
            catalogo = db.catalogo.find()
            return catalogo
        except Exception as e:
            print("Error al obtener catalogo:", e)
            return "error al obtener catalogo"
        
    def obtener_contenido(nombre_contenido):
        try:
            db = conectar_base_de_datos()
            contenido = db.catalogo.find_one({'id': nombre_contenido})
            return contenido
        except Exception as e:
            print("Error al obtener contenido:", e)
            return "error al obtener contenido"
    def obtener_contenido_nombre(ubicacion):
        try:
            db = conectar_base_de_datos()
            contenido = db.catalogo.find_one({'ubicacion': ubicacion})
            return contenido
        except Exception as e:
            print("Error al obtener contenido:", e)
            return "error al obtener contenido"
        
    def actualizar_pelicula(id_pelicula, data):
        try:
            db = conectar_base_de_datos()
            db.catalogo.update_one({'id': id_pelicula}, {'$set': data})
            return "actualizacion exitosa"
        except Exception as e:
            print("Error al actualizar:", e)
            return "error al actualizar"
        
class  StatsRepository():

    def aumentar_descargas(id):
        try:
            db = conectar_base_de_datos()
            db.catalogo.update_one({'id': id}, {'$inc': {'descargas': 1}})
            return "actualizacion exitosa"
        except Exception as e:
            print("Error al actualizar:", e)
            return "error al actualizar"
        
    def aumentar_visitas(id):
        try:
            db = conectar_base_de_datos()
            db.catalogo.update_one({'id': id}, {'$inc': {'visitas': 1}})
            return "actualizacion exitosa"
        except Exception as e:
            print("Error al actualizar:", e)
            return "error al actualizar"
        
    def obtener_estadisticas():
        try:
            db = conectar_base_de_datos()
            estadisticas = db.catalogo.find()
            return estadisticas
        except Exception as e:
            print("Error al obtener estadisticas:", e)
            return "error al obtener estadisticas"
