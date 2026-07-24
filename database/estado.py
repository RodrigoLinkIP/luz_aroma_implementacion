from configs.supa_client import (supabase)

def obtener_estado_por_id(id):
    """Devuelve un estado por su ID."""
    respuesta = supabase.table("estado").select("*").eq("id", id).execute()
    if respuesta.data:
        return respuesta.data[0]
    else:
        return None

def obtener_estados():
    """Devuelve todos los estados."""
    respuesta = supabase.table("estado").select("*").order("id").execute()
    return respuesta.data

def crear_estado(estado):
    """Crea un nuevo estado."""
    respuesta = supabase.table("estado").insert(estado).execute()
    return respuesta.data[0]