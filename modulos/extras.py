import subprocess
import time

def limpiar_terminal():
    subprocess.run('cls', shell=True)
    
def pedir_dato(mensaje: str, tipo=str):
    while True:
        try:
            dato = tipo(input(mensaje).strip())

            if isinstance(dato, (int, float)):
                if dato < 0:
                    print("No se permiten valores negativos")
                    continue

            if isinstance(dato, str) and dato == "":
                print("Entrada invalida, no debe estar vacio")
                continue

            return dato

        except ValueError:
            print(f"Debe ingresar un {tipo.__name__} válido.")
            
def asignar_id(lista: list):
    nuevo_id = 0
    
    if lista:
        nuevo_id = list[-1].id + 1
    else:
        nuevo_id = 1
        
    return nuevo_id

def listar_datos(lista: list):
    for dato in lista:
        print(dato)
        
def agregar_lista(lista: list, objeto):
    lista.append(objeto)