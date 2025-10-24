from flask import Flask
from flask_cors import CORS
from .modules.producto.producto_routes import producto_bp
from .modules.proveedor.proveedor_routes import proveedor_bp
from .modules.venta.venta_routes import venta_bp
from .modules.sabor.sabor_routes import sabor_bp
from .modules.item_venta.itemventa_routes import itemventa_bp
from .modules.cliente.cliente_routes import cliente_bp
from .modules.empleado.empleado_routes import empleado_bp
from .modules.categoria.categoria_routes import categoria_bp
from .modules.itemventa_sabor.itemventasabor_routes import itemventasabor_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(producto_bp)
    app.register_blueprint(proveedor_bp)
    app.register_blueprint(venta_bp)
    app.register_blueprint(sabor_bp)
    app.register_blueprint(itemventa_bp)
    app.register_blueprint(cliente_bp)
    app.register_blueprint(empleado_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(itemventasabor_bp)
    @app.route('/')
    def home():
        return "<h1>BIENVENIDOS A LA HELADERIA</h1>"
    return app