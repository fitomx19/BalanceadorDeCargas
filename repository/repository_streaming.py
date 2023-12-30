from app.database import conectar_base_de_datos
#from database import conectar_base_de_datos
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
