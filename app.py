from flask import Flask, jsonify, request
from routes import (
    categorias_bp, clientes_bp,
    detalle_pedidos_bp, envios_bp,
    estados_bp, pagos_bp,
    pedidos_bp, productos_bp
)

app = Flask(__name__)

@app.get("/")
def inicio():
    return jsonify({"mensaje": "API de luz y aroma en funcionamiento"}), 200

app.register_blueprint(categorias_bp, url_prefix="/categorias")
app.register_blueprint(clientes_bp, url_prefix="/clientes")
app.register_blueprint(detalle_pedidos_bp, url_prefix="/detalles_pedido")
app.register_blueprint(envios_bp, url_prefix="/envios")
app.register_blueprint(estados_bp, url_prefix="/estados")
app.register_blueprint(pagos_bp, url_prefix="/pagos")
app.register_blueprint(pedidos_bp, url_prefix="/pedidos")
app.register_blueprint(productos_bp, url_prefix="/productos")

@app.errorhandler(Exception)
def manejar_error(error):
    return jsonify({"error": str(error)}), 500

if __name__ == "__main__":
    app.run(debug=True)