# ============================================================
# ORDENAMIENTO Y EFICIENCIA
# ============================================================
#
# Ordenar significa reorganizar una colección
# siguiendo algún criterio.
#
#
# Ejemplos:
#
# números:
#
# 30, 10, 20
#
# ↓
#
# 10, 20, 30
#
#
# nombres:
#
# Tesla
# Einstein
# Turing
#
# ↓
#
# Einstein
# Tesla
# Turing
#
#
# También podemos ordenar objetos
# según una característica:
#
# tickets por prioridad;
# productos por precio;
# películas por año;
# usuarios por nombre.
#
#
# En este archivo estudiaremos:
#
# - sorted();
# - list.sort();
# - orden ascendente;
# - orden descendente;
# - reverse=True;
# - key=;
# - eficiencia básica del ordenamiento;
# - un algoritmo manual sencillo.
#
#
# No estudiaremos muchos algoritmos
# de ordenamiento diferentes.
#
# En Python normalmente utilizaremos
# las herramientas incorporadas.


# ============================================================
# 1. ORDENAR NÚMEROS
# ============================================================

numeros = [
    50,
    10,
    40,
    20,
    30
]


numeros_ordenados = sorted(
    numeros
)


print(
    "Original:",
    numeros
)


print(
    "Ordenados:",
    numeros_ordenados
)


# Resultado conceptual:
#
# Original:
#
# [50, 10, 40, 20, 30]
#
#
# Ordenados:
#
# [10, 20, 30, 40, 50]


# ============================================================
# 2. sorted() NO MODIFICA LA LISTA ORIGINAL
# ============================================================

# Esto es muy importante.
#
#
# Cuando hacemos:
#
# sorted(numeros)
#
#
# Python crea:
#
# una NUEVA lista ordenada.
#
#
# La lista original:
#
# numeros
#
# continúa igual.


print(
    numeros
)


# Sigue siendo:
#
# [50, 10, 40, 20, 30]


# ============================================================
# 3. GUARDAR EL RESULTADO
# ============================================================

# Como sorted() devuelve una nueva lista,
# normalmente hacemos:


resultado_ordenado = sorted(
    numeros
)


print(
    resultado_ordenado
)


# Podemos pensar:
#
# original
# ↓
# sorted()
# ↓
# nueva colección ordenada


# ============================================================
# 4. ORDEN DESCENDENTE
# ============================================================

# Por defecto:
#
# sorted()
#
# ordena de menor a mayor.
#
#
# Podemos utilizar:
#
# reverse=True
#
# para invertir el orden.


numeros_descendentes = sorted(
    numeros,
    reverse=True
)


print(
    numeros_descendentes
)


# Resultado:
#
# [50, 40, 30, 20, 10]


# ============================================================
# 5. ORDENAR STRINGS
# ============================================================

cientificos = [
    "Nikola Tesla",
    "Albert Einstein",
    "Grace Hopper",
    "Alan Turing"
]


cientificos_ordenados = sorted(
    cientificos
)


print(
    cientificos_ordenados
)


# Python puede ordenar strings
# utilizando su orden lexicográfico.
#
#
# Para nuestro nivel podemos pensarlo
# de manera similar al orden alfabético.


# ============================================================
# 6. sorted() VS .sort()
# ============================================================

# Tenemos dos herramientas frecuentes:
#
# sorted()
#
# y:
#
# list.sort()
#
#
# La diferencia principal es:
#
#
# sorted()
#
# → devuelve una nueva lista;
#
# → no modifica la original.
#
#
# .sort()
#
# → modifica directamente
#   la lista existente.


autos = [
    "Corvette",
    "Camaro",
    "Mustang"
]


autos.sort()


print(
    autos
)


# Ahora la propia lista:
#
# autos
#
# quedó modificada.


# ============================================================
# 7. COMPARACIÓN VISUAL
# ============================================================
#
# sorted()
#
# lista original
#      |
#      v
#   sorted()
#      |
#      v
# nueva lista
#
#
# ------------------------------------------------------------
#
# .sort()
#
# lista original
#      |
#      v
#   .sort()
#      |
#      v
# la misma lista queda modificada


# ============================================================
# 8. EJEMPLO PRÁCTICO DE sorted()
# ============================================================

precios = [
    25000,
    8000,
    15000,
    12000
]


precios_ordenados = sorted(
    precios
)


print(
    "Precios originales:",
    precios
)


print(
    "Precios ordenados:",
    precios_ordenados
)


# Esto puede ser útil cuando queremos:
#
# conservar los datos originales
#
# pero obtener otra versión
# para mostrar o procesar.


# ============================================================
# 9. EJEMPLO PRÁCTICO DE .sort()
# ============================================================

puntajes = [
    70,
    95,
    60,
    85
]


puntajes.sort(
    reverse=True
)


print(
    puntajes
)


# Ahora:
#
# puntajes
#
# quedó directamente ordenado
# de mayor a menor.


# ============================================================
# 10. ORDENAR DATOS MÁS COMPLEJOS
# ============================================================

# Hasta ahora ordenamos:
#
# números
# strings
#
#
# Pero en aplicaciones reales
# normalmente tenemos estructuras
# más complejas.
#
#
# Por ejemplo:


autos_clasicos = [
    {
        "modelo": "Chevrolet Camaro",
        "anio": 1967
    },
    {
        "modelo": "Chevrolet Bel Air",
        "anio": 1957
    },
    {
        "modelo": "Chevrolet Corvette",
        "anio": 1963
    }
]


# Queremos ordenar:
#
# por año.
#
#
# Python necesita saber:
#
# "¿qué valor de cada diccionario
# debo utilizar para comparar?"


# ============================================================
# 11. key=
# ============================================================

# Para indicar el criterio
# podemos utilizar:
#
# key=
#
#
# Primero creamos una función.


def obtener_anio(auto):

    return auto["anio"]


# Esta función recibe:
#
# un auto
#
# y devuelve:
#
# su año.
#
#
# Python utilizará ese valor
# para ordenar.


autos_por_anio = sorted(
    autos_clasicos,
    key=obtener_anio
)


print(
    autos_por_anio
)


# Resultado conceptual:
#
# Bel Air      → 1957
# Corvette     → 1963
# Camaro       → 1967


# ============================================================
# 12. ¿QUÉ HACE key=?
# ============================================================

# Este código:
#
# sorted(
#     autos_clasicos,
#     key=obtener_anio
# )
#
#
# puede entenderse así:
#
#
# Chevrolet Camaro
# ↓
# obtener_anio()
# ↓
# 1967
#
#
# Chevrolet Bel Air
# ↓
# obtener_anio()
# ↓
# 1957
#
#
# Chevrolet Corvette
# ↓
# obtener_anio()
# ↓
# 1963
#
#
# Python utiliza:
#
# 1967
# 1957
# 1963
#
# como criterio para ordenar.


# ============================================================
# 13. key= NO CAMBIA LOS DATOS
# ============================================================

# IMPORTANTE:
#
# obtener_anio()
#
# NO reemplaza los diccionarios.
#
#
# Solamente indica:
#
# qué valor debe utilizar Python
# para compararlos.
#
#
# El resultado sigue conteniendo:
#
# diccionarios completos.


for auto in autos_por_anio:

    print(
        auto["modelo"],
        auto["anio"]
    )


# ============================================================
# 14. OTRO EJEMPLO: TICKETS
# ============================================================

tickets = [
    {
        "id": "TK-001",
        "prioridad": 3
    },
    {
        "id": "TK-002",
        "prioridad": 1
    },
    {
        "id": "TK-003",
        "prioridad": 2
    }
]


def obtener_prioridad(ticket):

    return ticket["prioridad"]


tickets_ordenados = sorted(
    tickets,
    key=obtener_prioridad
)


for ticket in tickets_ordenados:

    print(
        ticket["id"],
        ticket["prioridad"]
    )


# Resultado:
#
# TK-002 1
# TK-003 2
# TK-001 3


# ============================================================
# 15. EL CRITERIO DEPENDE DEL PROBLEMA
# ============================================================

# Los mismos datos pueden ordenarse
# de maneras diferentes.
#
#
# Por ejemplo:
#
# tickets por:
#
# prioridad
# fecha
# ID
# nombre del usuario
#
#
# La pregunta correcta es:
#
# "¿según qué característica
# necesito ordenar?"


# ============================================================
# 16. ORDENAMIENTO Y EFICIENCIA
# ============================================================

# Ordenar una colección requiere trabajo.
#
#
# Python utiliza algoritmos de ordenamiento
# altamente optimizados.
#
#
# Para nuestro nivel podemos pensar
# de manera general en:
#
# O(n log n)
#
# para ordenar grandes colecciones.
#
#
# No necesitamos calcularlo
# manualmente ahora.


# ============================================================
# 17. ¿POR QUÉ NO O(n)?
# ============================================================

# Recorrer:
#
# 10 elementos
#
# una vez
#
# puede ser:
#
# O(n).
#
#
# Ordenar es diferente.
#
#
# Para ordenar:
#
# no solamente debemos mirar
# cada elemento.
#
#
# También necesitamos decidir:
#
# dónde debe quedar
# respecto de los demás.
#
#
# Por eso ordenar suele requerir
# más trabajo que simplemente
# recorrer una colección.


# ============================================================
# 18. RECORDATORIO DE COMPLEJIDADES
# ============================================================
#
# O(1)
#
# acceso directo
#
#
# O(log n)
#
# reducir el problema
# repetidamente
#
#
# O(n)
#
# recorrer los elementos
#
#
# O(n log n)
#
# común en buenos algoritmos
# generales de ordenamiento
#
#
# O(n²)
#
# algunos algoritmos sencillos
# de ordenamiento pueden llegar aquí


# ============================================================
# 19. NO NECESITAMOS PROGRAMAR TODO A MANO
# ============================================================

# Como programadores Python:
#
# normalmente utilizaremos:
#
# sorted()
#
# o:
#
# .sort()
#
#
# No tiene sentido escribir
# nuestro propio algoritmo
# cada vez que necesitamos ordenar.


# ============================================================
# 20. PERO VEAMOS UN ALGORITMO MANUAL
# ============================================================

# Solamente para entender
# qué significa ordenar manualmente,
# veremos una idea sencilla.
#
#
# Supongamos:
#
# [30, 10, 20]
#
#
# Comparamos:
#
# 30 y 10
#
#
# están al revés:
#
# intercambiamos.
#
#
# [10, 30, 20]
#
#
# Después:
#
# 30 y 20
#
#
# intercambiamos.
#
#
# [10, 20, 30]


# ============================================================
# 21. INTERCAMBIAR DOS POSICIONES
# ============================================================

valores = [
    30,
    10
]


valores[0], valores[1] = (
    valores[1],
    valores[0]
)


print(
    valores
)


# Resultado:
#
# [10, 30]


# ============================================================
# 22. ORDENAMIENTO BURBUJA
# ============================================================

# Existe un algoritmo sencillo
# llamado:
#
# Bubble Sort
#
# u:
#
# ordenamiento burbuja.
#
#
# Su idea es comparar
# elementos vecinos.
#
#
# Si están en el orden incorrecto:
#
# los intercambia.


numeros_burbuja = [
    30,
    10,
    40,
    20
]


for recorrido in range(
    len(numeros_burbuja)
):

    for indice in range(
        len(numeros_burbuja) - 1
    ):

        if (
            numeros_burbuja[indice]
            >
            numeros_burbuja[indice + 1]
        ):

            numeros_burbuja[indice], numeros_burbuja[indice + 1] = (
                numeros_burbuja[indice + 1],
                numeros_burbuja[indice]
            )


print(
    numeros_burbuja
)


# ============================================================
# 23. NO NECESITAS MEMORIZAR BUBBLE SORT
# ============================================================

# Este ejemplo está aquí
# solamente para mostrar:
#
# cuánto trabajo puede implicar
# ordenar manualmente.
#
#
# Observa:
#
# tenemos un for
#
# dentro de otro for.
#
#
# Eso ya debería recordarte:
#
# O(n²)
#
#
# Bubble Sort puede tener
# comportamiento cuadrático.
#
#
# Para aplicaciones normales
# NO lo utilizaremos
# en lugar de sorted().


# ============================================================
# 24. LA LECCIÓN IMPORTANTE DE BUBBLE SORT
# ============================================================

# No quiero que memorices:
#
# range(...)
# índices
# intercambio
#
#
# Quiero que observes:
#
# ordenar manualmente
# puede requerir muchas comparaciones.
#
#
# Python ya posee herramientas
# mejores para hacerlo.


# ============================================================
# 25. sorted() ES NORMALMENTE LA OPCIÓN MÁS CLARA
# ============================================================

datos = [
    50,
    30,
    10,
    40,
    20
]


resultado = sorted(
    datos
)


print(
    resultado
)


# Simple.
#
# Legible.
#
# Correcto.
#
# Optimizado.


# ============================================================
# 26. ¿CUÁNDO USAR sorted()?
# ============================================================

# Utiliza sorted()
# cuando quieras:
#
# obtener una versión ordenada
# sin modificar el original.


original = [
    3,
    1,
    2
]


ordenada = sorted(
    original
)


print(
    original
)


print(
    ordenada
)


# ============================================================
# 27. ¿CUÁNDO USAR .sort()?
# ============================================================

# Utiliza .sort()
# cuando quieras modificar
# directamente la lista.


lista_modificable = [
    3,
    1,
    2
]


lista_modificable.sort()


print(
    lista_modificable
)


# ============================================================
# 28. ERROR FRECUENTE CON .sort()
# ============================================================

# CUIDADO:
#
# .sort()
#
# modifica la lista
# y NO devuelve la lista ordenada.
#
#
# Es decir:
#
# resultado = lista.sort()
#
# deja:
#
# resultado
#
# con:
#
# None


ejemplo_sort = [
    3,
    2,
    1
]


resultado_sort = ejemplo_sort.sort()


print(
    "Lista:",
    ejemplo_sort
)


print(
    "Retorno de sort:",
    resultado_sort
)


# Resultado:
#
# Lista:
# [1, 2, 3]
#
#
# Retorno:
# None


# ============================================================
# 29. REGLA PRÁCTICA
# ============================================================
#
# Quiero conservar la lista original:
#
# → sorted()
#
#
# Quiero modificar directamente
# la lista:
#
# → .sort()
#
#
# Quiero orden descendente:
#
# → reverse=True
#
#
# Quiero ordenar diccionarios
# u objetos según una propiedad:
#
# → key=


# ============================================================
# 30. EJEMPLO COMPLETO
# ============================================================

cientificos_datos = [
    {
        "nombre": "Albert Einstein",
        "nacimiento": 1879
    },
    {
        "nombre": "Alan Turing",
        "nacimiento": 1912
    },
    {
        "nombre": "Nikola Tesla",
        "nacimiento": 1856
    }
]


def obtener_nacimiento(cientifico):

    return cientifico["nacimiento"]


cientificos_por_nacimiento = sorted(
    cientificos_datos,
    key=obtener_nacimiento
)


for cientifico in cientificos_por_nacimiento:

    print(
        cientifico["nombre"],
        cientifico["nacimiento"]
    )


# Resultado:
#
# Nikola Tesla      1856
# Albert Einstein   1879
# Alan Turing       1912


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# ORDENAR:
#
# reorganizar datos
# siguiendo un criterio.
#
#
# ------------------------------------------------------------
#
# sorted()
#
# devuelve:
#
# una NUEVA lista.
#
#
# ------------------------------------------------------------
#
# .sort()
#
# modifica:
#
# la lista original.
#
#
# ------------------------------------------------------------
#
# reverse=True
#
# permite:
#
# invertir el orden.
#
#
# ------------------------------------------------------------
#
# key=
#
# permite:
#
# seleccionar el valor utilizado
# como criterio de ordenamiento.
#
#
# ------------------------------------------------------------
#
# EFICIENCIA:
#
# los buenos algoritmos generales
# de ordenamiento suelen trabajar
# alrededor de:
#
# O(n log n)
#
#
# ------------------------------------------------------------
#
# BUBBLE SORT:
#
# sirve para comprender
# el proceso manual.
#
# Puede comportarse como:
#
# O(n²)
#
#
# No necesitamos utilizarlo
# en programas reales
# cuando Python ya proporciona
# herramientas mejores.
#
#
# ------------------------------------------------------------
#
# COMO PROGRAMADOR PYTHON:
#
# comprender el concepto
# ↓
# utilizar las herramientas
# del lenguaje correctamente.