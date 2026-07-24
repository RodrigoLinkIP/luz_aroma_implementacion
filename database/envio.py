from configs.supa_client import (supabase)

def obtener_envio_por_id(id):
    """Devuelve un envío por su ID."""
    respuesta = supabase.table("envio").select("*").eq("id", id).execute()
    if respuesta.data:
        return respuesta.data[0]
    else:
        return None

def obtener_envios():
    """Devuelve todos los envíos."""
    respuesta = supabase.table("envio").select("*").order("id").execute()
    return respuesta.data

def crear_envio(envio):
    """Crea un nuevo envío."""
    respuesta = supabase.table("envio").insert(envio).execute()
    return respuesta.data[0]

def actualizar_envio(id, envio_actualizado):
    """Actualiza un envío existente por su ID."""
    respuesta = supabase.table("envio").update(envio_actualizado).eq("id", id).execute()
    if respuesta.data:
        return respuesta.data[0]
    else:
        return None