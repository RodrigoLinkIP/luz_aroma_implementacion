from configs.supa_client import (supabase)

def obtener_cliente_por_dui(dui):
    """Devuelve un cliente por su DUI."""
    respuesta = supabase.table("cliente").select("*").eq("dui", dui).execute()
    if respuesta.data:
        return respuesta.data[0]
    else:
        return None
    
def obtener_clientes():
    """Devuelve todos los clientes."""
    respuesta = supabase.table("cliente").select("*").order("dui").execute()
    return respuesta.data

def crear_cliente(cliente):
    """Crea un nuevo cliente."""
    respuesta = supabase.table("cliente").insert(cliente).execute()
    return respuesta.data[0]

def actualizar_cliente(dui, cliente_actualizado):
    """Actualiza un cliente existente por su DUI."""
    respuesta = supabase.table("cliente").update(cliente_actualizado).eq("dui", dui).execute()
    if respuesta.data:
        return respuesta.data[0]
    else:
        return None
    
def eliminar_cliente(dui):
    """Elimina un cliente por su DUI."""
    respuesta = supabase.table("cliente").delete().eq("dui", dui).execute()
    if respuesta.data:
        return True
    else:
        return False