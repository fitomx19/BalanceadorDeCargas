from flask import Flask
from routes.routes_streaming import streaming_bp
 

app = Flask(__name__)
 

app.register_blueprint(streaming_bp)

if __name__ == '__main__':
    app.run(debug=True)
