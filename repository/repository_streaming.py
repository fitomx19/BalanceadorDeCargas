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
        
    def actualizar_pelicula(id_pelicula, data):
        try:
            db = conectar_base_de_datos()
            db.catalogo.update_one({'id': id_pelicula}, {'$set': data})
            return "actualizacion exitosa"
        except Exception as e:
            print("Error al actualizar:", e)
            return "error al actualizar"
