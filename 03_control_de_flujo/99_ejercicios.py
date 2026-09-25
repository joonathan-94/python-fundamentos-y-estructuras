# ============================================================
# EJERCICIOS - CONTROL DE FLUJO
# ============================================================
#
# Ejercicios breves para practicar los conceptos esenciales
# del módulo.
#
# El objetivo es consolidar comprensión sin agregar
# complejidad innecesaria.


# ------------------------------------------------------------
# CF-01 - CLASIFICAR PRIORIDAD
# ------------------------------------------------------------
#
# Tienes:
#
# prioridad = "Alta"
#
# Utilizando if, elif y else:
#
# - Si prioridad es "Crítica", imprime:
#   "Atención inmediata"
#
# - Si prioridad es "Alta", imprime:
#   "Atención prioritaria"
#
# - En cualquier otro caso, imprime:
#   "Atención normal"
#
# Tu código aquí:

prioridad = "Alta"

if prioridad == "Crítica":
    print("Atención inmediata")
elif prioridad == "Alta":
    print("Atención prioritaria")
else:
    print("Atención normal")

# ------------------------------------------------------------
# CF-02 - RECORRER NÚMEROS
# ------------------------------------------------------------
#
# Utilizando for y range():
#
# Recorre los números desde 1 hasta 5
# e imprime cada número.
#
# Recuerda que el límite final de range()
# no se incluye.
#
# Tu código aquí:

for numero in range(1,6):
    print(numero)


# ------------------------------------------------------------
# CF-03 - DETENER UN CICLO
# ------------------------------------------------------------
#
# Crea:
#
# contador = 1
#
# Utiliza un ciclo while para imprimir el contador.
#
# Después de cada iteración aumenta contador en 1.
#
# Cuando contador llegue a 4:
#
# utiliza break para terminar el ciclo.
#
# El resultado esperado debe mostrar:
#
# 1
# 2
# 3
# 4
#
# Tu código aquí:

contador = 1

while True:
    print("Contador:", contador)

    if contador == 4:
        break

    contador += 1