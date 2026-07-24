from flask import Blueprint, jsonify, request
from utils.validaciones import validar_campos
from database.estado import (
    obtener_estados,
    crear_estado,
    obtener_estado_por_id
)

estados_bp = Blueprint("estados", __name__)

@estados_bp.get("/<int:id>")
def obtener_estado(id):
    estado = obtener_estado_por_id(id)
    if estado:
        return jsonify(estado), 200
    else:
        return jsonify({"mensaje": "Estado no encontrado"}), 404


@estados_bp.get("/")
def listar_estados():
    estados = obtener_estados()
    if estados:
        return jsonify(estados), 200
    else:
        return jsonify({"mensaje": "No existen estados"})
    
@estados_bp.post("/")
def agregar_estado():
    estado = request.get_json()
    errores = validar_campos(estado, ["nombre"])
    
    if errores:
        return jsonify({"errores": errores}), 400
    
    estadoNuevo = crear_estado(estado)
    return jsonify(estadoNuevo), 201