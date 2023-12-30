# database.py
from pymongo import MongoClient

# Variable global para la base de datos
db = None

def conectar_base_de_datos():
    global db
    if db is None:
        client = MongoClient('mongodb+srv://danielaas17:mongodb24@streamingpeliculas.tg4qlb3.mongodb.net/?retryWrites=true&w=majority')
        db = client['streamingpeliculas']  # Reemplaza con el nombre de tu base de datos
    return db
