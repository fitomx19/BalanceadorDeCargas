# models/Usuario.py
from flask_mongoengine import MongoEngine

db = MongoEngine()

class Usuario(db.Document):
    usuario = db.StringField(required=True, unique=True)
    contrasena = db.StringField(required=True)
    nombre = db.StringField(required=True)
    apellido = db.StringField(required=True)
    correo = db.EmailField(required=True, unique=True)
    tarjeta = db.StringField(required=True)
    fecha_expiracion = db.StringField(required=True)
    cvv = db.StringField(required=True)
    tipo = db.StringField(required=True)
    suscripcion = db.BooleanField(default=False)
