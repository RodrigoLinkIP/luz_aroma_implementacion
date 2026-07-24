from configs.supa_client import (supabase)

def obtener_categoria_por_id(id):
    """Devuelve una categoría por su ID."""
    respuesta = supabase.table("categoria").select("*").eq("id", id).execute()
    if respuesta.data:
        return respuesta.data[0]
    else:
        return None
    
def obtener_categorias():
    """Devuelve todas las categorías."""
    respuesta = supabase.table("categoria").select("*").order("id").execute()
    return respuesta.data

def crear_categoria(categoria):
    """Crea una nueva categoría."""
    respuesta = supabase.table("categoria").insert(categoria).execute()
    return respuesta.data[0]