from flask import Flask
from flask_cors import CORS
from .producto.producto_routes import producto_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(producto_bp)
    @app.route('/')
    def home():
        return "<h1>BIENVENIDOS A LA HELADERIA</h1>"
    return app