from configs.supa_client import (supabase)


def obtener_pago_por_id(id):
    """Devuelve un pago por su ID."""
    respuesta = supabase.table("pago").select("*").eq("id", id).execute()
    if respuesta.data:
        return respuesta.data[0]
    else:
        return None
    
def obtener_pagos():
    """Devuelve todos los pagos."""
    respuesta = supabase.table("pago").select("*").order("id").execute()
    return respuesta.data

def crear_pago(pago):
    """Crea un nuevo pago."""
    respuesta = supabase.table("pago").insert(pago).execute()
    return respuesta.data[0]

def actualizar_pago(id, pago_actualizado):
    """Actualiza un pago existente por su ID."""
    respuesta = supabase.table("producto").update(pago_actualizado).eq("id", id).execute()
    if respuesta.data:
        return respuesta.data[0]
    else:
        return None