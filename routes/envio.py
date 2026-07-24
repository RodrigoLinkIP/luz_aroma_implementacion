from flask import Blueprint, jsonify, request
from utils.validaciones import validar_campos
from database.envio import (
    crear_envio,
    obtener_envio_por_id,
    obtener_envios,
    actualizar_envio
)

envios_bp = Blueprint("envios", __name__)

@envios_bp.get("/<int:id>")
def obtener_envio(id):
    envio = obtener_envio_por_id(id)
    if envio:
        return jsonify(envio), 200
    else:
        return jsonify({"mensaje": "envio no encontrado"}), 404
    
@envios_bp.get("/")
def listar_envios():
    envios = obtener_envios()
    if envios:
        return jsonify(envios), 200
    else:
        return jsonify({"mensaje": "No existen envios"}), 404

@envios_bp.post("/")
def agregar_envio():
    envio = request.get_json()
    errores = validar_campos(
        envio,
        ["direccion_entrega", "costo", "id_estado"]
    )
    
    if errores:
        return jsonify({"errores": errores}), 400
    
    envioNuevo = crear_envio(envio)
    return jsonify(envioNuevo), 201

@envios_bp.put("/<int:id>")
def modificar_envio(id):
    envio_existente = obtener_envio_por_id(id)
        
    if envio_existente is None:
        return jsonify({"error": "No existe el envio"}), 404
        
    envio = request.get_json()
    
    if envio is None:
        return jsonify({"error": "Debe enviar al menos un campo para actualizar"}), 400
    
    envioActualizado = actualizar_envio(id, envio)
    return jsonify(envioActualizado), 200