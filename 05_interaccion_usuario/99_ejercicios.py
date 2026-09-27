# ============================================================
# EJERCICIOS - INTERACCIÓN CON EL USUARIO
# ============================================================
#
# El objetivo es practicar la recepción y transformación
# de datos ingresados mediante input().


# ------------------------------------------------------------
# INPUT-01 - REGISTRAR UN AUTO CLÁSICO
# ------------------------------------------------------------
#
# Solicita al usuario:
#
# - modelo del auto;
# - año de fabricación.
#
# Realiza lo siguiente:
#
# 1. Limpia el modelo utilizando strip().
#
# 2. Convierte el año a int.
#
# 3. Guarda ambos valores en un diccionario:
#
# auto_registrado
#
# 4. Imprime el diccionario.
#
# Tu código aquí:

modelo = input("Ingrese modelo del auto: ")
anio = input("Ingrese año del auto: ")

modelo_normalizado = modelo.strip()
anio_normalizado = int(anio)

auto_registrado = {
    "modelo_auto" : modelo_normalizado,
    "anio_auto" : anio_normalizado
}

print(auto_registrado)


# ------------------------------------------------------------
# INPUT-02 - CALCULAR COSTO TOTAL
# ------------------------------------------------------------
#
# Solicita al usuario:
#
# - cantidad de unidades;
# - precio por unidad.
#
# Realiza lo siguiente:
#
# 1. Convierte la cantidad a int.
#
# 2. Convierte el precio a float.
#
# 3. Calcula:
#
# total = cantidad * precio
#
# 4. Imprime el total utilizando una f-string.
#
# Tu código aquí:

cantidad = int(input("Ingrese la cantidad de unidades: "))
precio = float(input("Ingrese el precio por unidad: "))

total = cantidad * precio

print(f"El costo total es: {total}")