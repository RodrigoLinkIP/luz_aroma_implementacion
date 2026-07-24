from configs.supa_client import (supabase)

def obtener_producto_por_id(id):
    """Devuelve un producto por su ID."""
    respuesta = supabase.table("producto").select("*").eq("id", id).execute()
    if respuesta.data:
        return respuesta.data[0]
    else:
        return None
    
def obtener_productos():
    """Devuelve todos los productos."""
    respuesta = supabase.table("producto").select("*").order("id").execute()
    return respuesta.data

def crear_producto(producto):
    """Crea un nuevo producto."""
    respuesta = supabase.table("producto").insert(producto).execute()
    return respuesta.data[0]

def actualizar_producto(id, producto_actualizado):
    """Actualiza un producto existente por su ID."""
    respuesta = supabase.table("producto").update(producto_actualizado).eq("id", id).execute()
    if respuesta.data:
        return respuesta.data[0]
    else:
        return None
    
def eliminar_producto(id):
    """Elimina un producto por su ID."""
    respuesta = supabase.table("producto").delete().eq("id", id).execute()
    if respuesta.data:
        return True
    else:
        return False