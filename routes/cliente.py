from flask import Blueprint, jsonify, request
from utils.validaciones import validar_campos
from database.cliente import (
    obtener_cliente_por_dui,
    obtener_clientes,
    crear_cliente,
    actualizar_cliente,
    eliminar_cliente
)

clientes_bp = Blueprint("clientes", __name__)

@clientes_bp.get("/<string:dui>")
def obtener_cliente(dui):
    cliente = obtener_cliente_por_dui(dui)
    if cliente:
        return jsonify(cliente), 200
    else:
        return jsonify({"mensaje": "Cliente no encontrado"}), 404
    
@clientes_bp.get("/")
def listar_clientes():
    clientes = obtener_clientes()
    if clientes:
        return jsonify(clientes), 200
    else:
        return jsonify({"mensaje": "No existen clientes"}), 404

@clientes_bp.post("/")
def agregar_cliente():
    cliente = request.get_json()
    errores = validar_campos(
        cliente,
        ["dui", "nombre", "telefono", "direccion", "referencia"]
        )
    
    if errores:
        return jsonify({"errores": errores}), 400
    
    if obtener_cliente_por_dui(cliente["dui"]) is not None:
        return jsonify({"error": "Ya existe un cliente con ese DUI"}), 409
    
    clienteNuevo = crear_cliente(cliente)
    return jsonify(clienteNuevo), 201

@clientes_bp.put("/<string:dui>")
def modificar_cliente(dui):
    cliente_existente = obtener_cliente_por_dui(dui)
    
    if cliente_existente is None:
        return jsonify({"error": "No existe un cliente con ese DUI"}), 404
        
    cliente = request.get_json()
    
    if cliente is None:
        return jsonify({"error": "Debe enviar al menos un campo para actualizar"}), 400
    
    clienteActualizado = actualizar_cliente(dui, cliente)
    return jsonify(clienteActualizado), 200

@clientes_bp.delete("/<string:dui>")
def borrar_cliente(dui):
    cliente = obtener_cliente_por_dui(dui)
    
    if cliente is None:
        return jsonify({"error": "No existe un cliente con ese DUI"}), 404
    
    clienteEliminado = eliminar_cliente(dui)
    return jsonify(clienteEliminado), 200