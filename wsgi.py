from flask import Flask
import os

#production
from routes.routes_streaming import streaming_bp
from database import conectar_base_de_datos 

#dev
#from app.database import conectar_base_de_datos
#from app.routes.routes_streaming import streaming_bp 

app = Flask(__name__)
app.secret_key = 'memento_mori'
# Obtén la ruta del directorio actual (donde se encuentra tu aplicación)
base_dir = os.path.abspath(os.path.dirname(__file__))
print(base_dir)

# Configura la carpeta de carga como 'archivos' dentro de la raíz de la aplicación
app.config['UPLOAD_FOLDER'] = os.path.join(base_dir, 'archivos')
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # Establecer el límite en 100 MB

db = conectar_base_de_datos()

app.register_blueprint(streaming_bp)

if __name__ == '__main__':
    app.run(debug=True)
