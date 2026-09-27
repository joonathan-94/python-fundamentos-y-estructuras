# ============================================================
# EJERCICIOS - MÓDULOS Y PAQUETES
# ============================================================
#
# Objetivo:
#
# - importar código desde un módulo propio;
# - importar código desde un paquete;
# - utilizar funciones ya definidas en otros archivos.
#
# No necesitas crear funciones nuevas para estos ejercicios.


# ------------------------------------------------------------
# MOD-01 - IMPORTAR DESDE UN MÓDULO
# ------------------------------------------------------------
#
# En el archivo:
#
# operaciones.py
#
# ya existe la función:
#
# calcular_total()
#
#
# Realiza lo siguiente:
#
# 1. Importa solamente calcular_total desde operaciones.
#
# 2. Utiliza la función con:
#
#    cantidad = 2
#    precio_unitario = 12000
#
# 3. Guarda el resultado en una variable llamada:
#
#    total_calculado
#
# 4. Imprime el resultado.
#
#
# Resultado esperado:
#
# 24000
#
#
# Tu código aquí:

from operaciones import calcular_total

total_calculado = calcular_total(2, 12000)

print(f"Total: {total_calculado}")


# ------------------------------------------------------------
# MOD-02 - IMPORTAR DESDE UN PAQUETE
# ------------------------------------------------------------
#
# Dentro del paquete:
#
# utilidades
#
# existe el módulo:
#
# texto.py
#
# y dentro de ese módulo está la función:
#
# normalizar_nombre()
#
#
# Realiza lo siguiente:
#
# 1. Importa normalizar_nombre desde:
#
#    utilidades.texto
#
# 2. Utiliza la función con este valor:
#
#    "   jose maza   "
#
# 3. Guarda el resultado en:
#
#    nombre_cientifico
#
# 4. Imprime el resultado.
#
#
# Resultado esperado:
#
# Jose Maza
#
#
# Tu código aquí:

from utilidades.texto import normalizar_nombre

nombre_cientifico = normalizar_nombre("   jose maza   ")
print(f"Nombre del cientifico: {nombre_cientifico}")