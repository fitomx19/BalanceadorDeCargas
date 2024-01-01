from flask import Flask

#production
from routes.routes_streaming import streaming_bp
from database import conectar_base_de_datos 

#dev
#from app.database import conectar_base_de_datos
#from app.routes.routes_streaming import streaming_bp 

app = Flask(__name__)
app.secret_key = 'memento_mori'

db = conectar_base_de_datos()

app.register_blueprint(streaming_bp)

if __name__ == '__main__':
    app.run(debug=True)
