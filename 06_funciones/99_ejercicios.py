# ============================================================
# EJERCICIOS - FUNCIONES
# ============================================================
#
# El objetivo es practicar solamente los conceptos esenciales:
#
# - definir funciones;
# - utilizar parámetros;
# - llamar funciones;
# - utilizar return.
#
# No es necesario complicarlos.


# ------------------------------------------------------------
# FUNC-01 - CALCULAR TOTAL
# ------------------------------------------------------------
#
# Crea una función llamada:
#
# calcular_total
#
# La función debe recibir:
#
# - cantidad
# - precio_unitario
#
# Debe calcular:
#
# cantidad * precio_unitario
#
# y devolver el resultado utilizando return.
#
#
# Luego:
#
# 1. Llama a la función utilizando:
#
#    cantidad = 3
#    precio_unitario = 15000
#
# 2. Guarda el resultado en una variable.
#
# 3. Imprime el resultado.
#
#
# Resultado esperado:
#
# 45000
#
# Tu código aquí:

def calcular_total(cantidad, precio_unitario):
    return cantidad * precio_unitario

total = calcular_total(3, 15000)
print(total)


# ------------------------------------------------------------
# FUNC-02 - CREAR RESUMEN DE TICKET
# ------------------------------------------------------------
#
# Crea una función llamada:
#
# crear_resumen_ticket
#
# La función debe recibir:
#
# - id_ticket
# - titulo_ticket
#
# Debe devolver un diccionario con esta estructura:
#
# {
#     "id": ...,
#     "titulo": ...,
#     "estado": "Nuevo"
# }
#
#
# Luego llama a la función utilizando:
#
# id_ticket = "WD-1001"
# titulo_ticket = "Usuario sin acceso"
#
# Guarda el resultado en una variable e imprime
# el diccionario.
#
#
# Tu código aquí:

def crear_resumen_ticket (id_ticket, titulo_ticket):
    return {
        "id": id_ticket,
        "titulo": titulo_ticket,
        "estado": "Nuevo"
    }

resumen = crear_resumen_ticket("WD-1001", "Usuario sin acceso")
print(resumen)