from flask import Blueprint, jsonify, request
from utils.validaciones import validar_campos
from database.detalle_pedido import (
    crear_detalle_pedido,
    obtener_detalle_pedido_por_id,
    obtener_detalles_pedido,
    obtener_detalles_pedido_por_pedido_id,
    actualizar_detalle_pedido,
    eliminar_detalle_pedido
)

detalle_pedidos_bp = Blueprint("detalle_pedidos", __name__)

@detalle_pedidos_bp.get("/<int:id>")
def obtener_detalle_pedido(id):
    detalle_pedido = obtener_detalle_pedido_por_id(id)
    if detalle_pedido:
        return jsonify(detalle_pedido), 200
    else:
        return jsonify({"mensaje": "detalle_pedido no encontrado"}), 404
    
@detalle_pedidos_bp.get("/<int:id_pedido>")
def obtener_detalle_pedido_por_pedido_id(id):
    detalle_pedido = obtener_detalles_pedido_por_pedido_id(id)
    if detalle_pedido:
        return jsonify(detalle_pedido), 200
    else:
        return jsonify({"mensaje": "detalle_pedido no encontrado"}), 404
    
@detalle_pedidos_bp.get("/")
def listar_detalle_pedidos():
    obtener_detalles_pedidos = obtener_detalles_pedido()
    if obtener_detalles_pedidos:
        return jsonify(obtener_detalles_pedidos), 200
    else:
        return jsonify({"mensaje": "No existen obtener_detalles_pedido"}), 404

@detalle_pedidos_bp.post("/")
def agregar_detalle_pedido():
    detalle_pedido = request.get_json()
    errores = validar_campos(
        detalle_pedido,
        ["cantidad", "precio_unitario", "id_pedido", "id_producto"]
        )
    
    if errores:
        return jsonify({"errores": errores}), 400
    
    detalle_pedidoNuevo = crear_detalle_pedido(detalle_pedido)
    return jsonify(detalle_pedidoNuevo), 201

@detalle_pedidos_bp.put("/<int:id>")
def modificar_detalle_pedido(id):
    detalle_pedido_existente = obtener_detalle_pedido_por_id(id)
    
    if detalle_pedido_existente is None:
        return jsonify({"error": "No existe el datalle"}), 404
        
    detalle_pedido = request.get_json()
    
    if detalle_pedido is None:
        return jsonify({"error": "Debe enviar al menos un campo para actualizar"}), 400
    
    detalle_pedidoActualizado = actualizar_detalle_pedido(id, detalle_pedido)
    return jsonify(detalle_pedidoActualizado), 200


@detalle_pedidos_bp.delete("/<int:id>")
def borrar_detalle_pedido(id):
    detalle_pedido = obtener_detalle_pedido_por_id(id)
        
    if detalle_pedido is None:
        return jsonify({"error": "No existe el detalle"}), 404
    
    detalle_pedidoEliminado = eliminar_detalle_pedido(id)
    return jsonify(detalle_pedidoEliminado), 200