def validar_campos(datos, campos):
    errores = []

    for campo in campos:
        if campo not in datos or datos[campo] is None:
            errores.append(f"El campo '{campo}' es obligatorio.")
        elif isinstance(datos[campo], str) and datos[campo].strip() == "":
            errores.append(f"El campo '{campo}' no puede estar vacío.")
        elif isinstance(datos[campo], (int, float)) and datos[campo] < 0:
            errores.append(f"El campo '{campo}' no puede ser negativo.")

    return errores