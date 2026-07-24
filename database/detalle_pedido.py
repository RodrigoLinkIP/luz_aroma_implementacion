from configs.supa_client import (supabase)

def obtener_detalle_pedido_por_id(id):
    """Devuelve un detalle de pedido por su ID."""
    respuesta = supabase.table("detalle_pedido").select("*").eq("id", id).execute()
    if respuesta.data:
        return respuesta.data[0]
    else:
        return None
    
def obtener_detalles_pedido():
    """Devuelve todos los detalles de pedido."""
    respuesta = supabase.table("detalle_pedido").select("*").order("id").execute()
    return respuesta.data

def obtener_detalles_pedido_por_pedido_id(pedido_id):
    """Devuelve todos los detalles de pedido para un pedido específico."""
    respuesta = supabase.table("detalle_pedido").select("*").eq("pedido_id", pedido_id).execute()
    return respuesta.data

def crear_detalle_pedido(detalle_pedido):
    """Crea un nuevo detalle de pedido."""
    respuesta = supabase.table("detalle_pedido").insert(detalle_pedido).execute()
    return respuesta.data[0]

def actualizar_detalle_pedido(id, detalle_pedido_actualizado):
    """Actualiza un detalle de pedido existente por su ID."""
    respuesta = supabase.table("detalle_pedido").update(detalle_pedido_actualizado).eq("id", id).execute()
    if respuesta.data:
        return respuesta.data[0]
    else:
        return None
    
def eliminar_detalle_pedido(id):
    """Elimina un detalle de pedido por su ID."""
    respuesta = supabase.table("detalle_pedido").delete().eq("id", id).execute()
    if respuesta.data:
        return True
    else:
        return False