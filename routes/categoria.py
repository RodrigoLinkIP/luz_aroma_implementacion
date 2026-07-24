from flask import Blueprint, jsonify, request
from utils.validaciones import validar_campos
from database.categoria import (
    obtener_categoria_por_id,
    obtener_categorias,
    crear_categoria
)

categorias_bp = Blueprint("categorias", __name__)

@categorias_bp.get("/<int:id>")
def obtener_categoria(id):
    categoria = obtener_categoria_por_id(id)
    if categoria:
        return jsonify(categoria), 200
    else:
        return jsonify({"mensaje": "Categoría no encontrada"}), 404
    
@categorias_bp.get("/")
def listar_categorias():
    categorias = obtener_categorias()
    if categorias:
        return jsonify(obtener_categorias()), 200
    else:
        return jsonify({"mensaje": "No existen categorias"})

@categorias_bp.post("/")
def agregar_categoria():
    categoria = request.get_json()
    errores = validar_campos(categoria, ["nombre"])
    
    if errores:
        return jsonify({"errores": errores}), 400
    
    categoriaNueva = crear_categoria(categoria)
    return jsonify(categoriaNueva), 201