from flask import Blueprint, jsonify, request
from utils.validaciones import validar_campos
from database.pedido import (
    crear_pedido,
    obtener_pedido_por_id,
    obtener_pedidos,
    actualizar_pedido
)

pedidos_bp = Blueprint("pedidos", __name__)

@pedidos_bp.get("/<int:id>")
def obtener_pedido(id):
    pedido = obtener_pedido_por_id(id)
    if pedido:
        return jsonify(pedido), 200
    else:
        return jsonify({"mensaje": "pedido no encontrado"}), 404
    
@pedidos_bp.get("/")
def listar_pedidos():
    pedidos = obtener_pedidos()
    if pedidos:
        return jsonify(pedidos), 200
    else:
        return jsonify({"mensaje": "No existen pedidos"}), 404

@pedidos_bp.post("/")
def agregar_pedido():
    pedido = request.get_json()
    errores = validar_campos(
        pedido,
        ["fecha", "total", "dui_cliente", "id_envio", "id_estado"]
    )
    
    if errores:
        return jsonify({"errores": errores}), 400
    
    pedidoNuevo = crear_pedido(pedido)
    return jsonify(pedidoNuevo), 201

@pedidos_bp.put("/<int:id>")
def modificar_pedido(id):
    pedido_existente = obtener_pedido_por_id(id)
        
    if pedido_existente is None:
        return jsonify({"error": "No existe el pedido"}), 404
        
    pedido = request.get_json()
    
    if pedido is None:
        return jsonify({"error": "Debe enviar al menos un campo para actualizar"}), 400
    
    pedidoActualizado = actualizar_pedido(id, pedido)
    return jsonify(pedidoActualizado), 200