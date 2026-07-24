from flask import Blueprint, jsonify, request
from utils.validaciones import validar_campos
from database.categoria import obtener_categoria_por_id
from database.estado import obtener_estado_por_id
from database.producto import (
    crear_producto,
    obtener_producto_por_id,
    obtener_productos,
    actualizar_producto,
    eliminar_producto
)

productos_bp = Blueprint("productos", __name__)

@productos_bp.get("/<int:id>")
def obtener_producto(id):
    producto = obtener_producto_por_id(id)
    if producto:
        return jsonify(producto), 200
    else:
        return jsonify({"mensaje": "producto no encontrado"}), 404
    
@productos_bp.get("/")
def listar_productos():
    productos = obtener_productos()
    if productos:
        return jsonify(productos), 200
    else:
        return jsonify({"mensaje": "No existen productos"}), 404

@productos_bp.post("/")
def agregar_producto():
    producto = request.get_json()
    errores = validar_campos(
        producto,
        ["nombre", "caracteristicas", "aroma", "tamannio", "precio", "costo", "stock", "id_estado", "id_categoria"]
    )
    
    if errores:
        return jsonify({"errores": errores}), 400
    
    if obtener_estado_por_id(producto["id_estado"]) is None:
        return jsonify({"error": "El estado no existe."}), 404
    
    if obtener_categoria_por_id(producto["id_categoria"]) is None:
        return jsonify({"error": "La categoría no existe."}), 404
    
    productoNuevo = crear_producto(producto)
    return jsonify(productoNuevo), 201

@productos_bp.put("/<int:id>")
def modificar_producto(id):
    producto_existente = obtener_producto_por_id(id)
        
    if producto_existente is None:
        return jsonify({"error": "No existe este producto"}), 404
        
    producto = request.get_json()
    
    if producto is None:
        return jsonify({"error": "Debe enviar al menos un campo para actualizar"}), 400
    
    if "id_estado" in producto:
        if obtener_estado_por_id(producto["id_estado"]) is None:
            return jsonify({"error": "El estado no existe."}), 404

    # Solo validar si se intenta cambiar la categoría
    if "id_categoria" in producto:
        if obtener_categoria_por_id(producto["id_categoria"]) is None:
            return jsonify({"error": "La categoría no existe."}), 404
    
    productoActualizado = actualizar_producto(id, producto)
    return jsonify(productoActualizado)

@productos_bp.delete("/<int:id>")
def borrar_producto(id):
    producto = obtener_producto_por_id(id)
    
    if producto is None:
        return jsonify({"error": "El producto no existe"})
    
    productoEliminado = eliminar_producto(id)
    return jsonify(productoEliminado), 200