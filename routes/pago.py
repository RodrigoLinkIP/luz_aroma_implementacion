from flask import Blueprint, jsonify, request
from utils.validaciones import validar_campos
from database.pago import (
    crear_pago,
    obtener_pago_por_id,
    obtener_pagos,
    actualizar_pago
)

pagos_bp = Blueprint("pagos", __name__)

@pagos_bp.get("/<int:id>")
def obtener_pago(id):
    pago = obtener_pago_por_id(id)
    if pago:
        return jsonify(pago), 200
    else:
        return jsonify({"mensaje": "pago no encontrado"}), 404
    
@pagos_bp.get("/")
def listar_pagos():
    pagos = obtener_pagos()
    if pagos:
        return jsonify(pagos), 200
    else:
        return jsonify({"mensaje": "No existen pagos"}), 404

@pagos_bp.post("/")
def agregar_pago():
    pago = request.get_json()
    errores = validar_campos(
        pago,
        ["metodo_pago", "monto", "id_estado", "id_pedido"]
    )
    
    if errores:
        return jsonify({"errores": errores}), 400
    
    pagoNuevo = crear_pago(pago)
    return jsonify(pagoNuevo), 201

@pagos_bp.put("/<int:id>")
def modificar_pago(id):
    pago_existente = obtener_pago_por_id(id)
        
    if pago_existente is None:
        return jsonify({"error": "No existe el pago"}), 404
        
    pago = request.get_json()
    
    if pago is None:
        return jsonify({"error": "Debe enviar al menos un campo para actualizar"}), 400
    
    pagoActualizado = actualizar_pago(id, pago)
    return jsonify(pagoActualizado), 200