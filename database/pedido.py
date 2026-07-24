from configs.supa_client import (supabase)

def obtener_pedido_por_id(id):
    """Devuelve un pedido por su ID."""
    respuesta = supabase.table("pedido").select("*").eq("id", id).execute()
    if respuesta.data:
        return respuesta.data[0]
    else:
        return None
    
def obtener_pedidos():
    """Devuelve todos los pedidos."""
    respuesta = supabase.table("pedido").select("*").order("id").execute()
    return respuesta.data

def crear_pedido(pedido):
    """Crea un nuevo pedido."""
    respuesta = supabase.table("pedido").insert(pedido).execute()
    return respuesta.data[0]

def actualizar_pedido(id, pedido_actualizado):
    """Actualiza un pedido existente por su ID."""
    respuesta = supabase.table("producto").update(pedido_actualizado).eq("id", id).execute()
    if respuesta.data:
        return respuesta.data[0]
    else:
        return None