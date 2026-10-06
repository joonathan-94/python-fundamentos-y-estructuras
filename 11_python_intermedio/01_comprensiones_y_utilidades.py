# ============================================================
# COMPRENSIONES Y UTILIDADES FRECUENTES DE PYTHON
# ============================================================
#
# En esta sección estudiaremos herramientas que permiten
# trabajar con colecciones de una forma más expresiva.
#
#
# Contenidos:
#
# - list comprehensions
# - filtros en comprehensions
# - dict comprehensions
# - set comprehensions
# - enumerate()
# - zip()
# - any()
# - all()
# - sorted() con key
#
#
# El objetivo NO es escribir código lo más corto posible.
#
# El objetivo es reconocer formas comunes de escribir Python
# manteniendo claridad y legibilidad.


# ------------------------------------------------------------
# 1. RECORDATORIO: CREAR UNA LISTA CON FOR
# ------------------------------------------------------------

nombres = [
    "Albert Einstein",
    "Stephen Hawking",
    "Nikola Tesla"
]


nombres_mayusculas = []


for nombre in nombres:
    nombres_mayusculas.append(
        nombre.upper()
    )


print(nombres_mayusculas)


# Este código es completamente válido.
#
# Tenemos:
#
# lista vacía
# ↓
# recorrer datos
# ↓
# transformar cada elemento
# ↓
# append()
#
#
# Python permite expresar este patrón de una manera
# más compacta mediante una:
#
# LIST COMPREHENSION


# ------------------------------------------------------------
# 2. LIST COMPREHENSION
# ------------------------------------------------------------

nombres_mayusculas_comp = [
    nombre.upper()
    for nombre in nombres
]


print(nombres_mayusculas_comp)


# Podemos leer:
#
# [
#     nombre.upper()
#     for nombre in nombres
# ]
#
# como:
#
# "crea una nueva lista utilizando nombre.upper()
# para cada nombre existente en nombres"


# ------------------------------------------------------------
# 3. ESTRUCTURA BÁSICA
# ------------------------------------------------------------

# Forma general:
#
# nueva_lista = [
#     expresion
#     for elemento in coleccion
# ]
#
#
# Ejemplo:
#
# numeros = [1, 2, 3]
#
# dobles = [
#     numero * 2
#     for numero in numeros
# ]


numeros = [
    1,
    2,
    3,
    4,
    5
]


dobles = [
    numero * 2
    for numero in numeros
]


print(dobles)


# Resultado:
#
# [2, 4, 6, 8, 10]


# ------------------------------------------------------------
# 4. COMPREHENSION CON FILTRO
# ------------------------------------------------------------

# También podemos agregar una condición.


numeros_pares = [
    numero
    for numero in numeros
    if numero % 2 == 0
]


print(numeros_pares)


# Podemos leerlo:
#
# "crea una lista con numero
# para cada numero en numeros
# solamente si es par"


# ------------------------------------------------------------
# 5. COMPARACIÓN CON FOR TRADICIONAL
# ------------------------------------------------------------

numeros_pares_tradicional = []


for numero in numeros:

    if numero % 2 == 0:
        numeros_pares_tradicional.append(
            numero
        )


print(numeros_pares_tradicional)


# Ambos enfoques producen el mismo resultado.
#
#
# FOR TRADICIONAL:
#
# útil cuando existe más lógica.
#
#
# COMPREHENSION:
#
# útil cuando la transformación o filtro es sencillo.


# ------------------------------------------------------------
# 6. EJEMPLO CON DATOS MÁS REALES
# ------------------------------------------------------------

cientificos = [
    {
        "nombre": "Albert Einstein",
        "area": "Física"
    },
    {
        "nombre": "Carl Sagan",
        "area": "Astronomía"
    },
    {
        "nombre": "Marie Curie",
        "area": "Química"
    }
]


nombres_cientificos = [
    cientifico["nombre"]
    for cientifico in cientificos
]


print(nombres_cientificos)


# Aquí tenemos:
#
# lista de diccionarios
# ↓
# extraemos solamente "nombre"
# ↓
# obtenemos una nueva lista


# ------------------------------------------------------------
# 7. FILTRAR DICCIONARIOS
# ------------------------------------------------------------

fisicos = [
    cientifico["nombre"]
    for cientifico in cientificos
    if cientifico["area"] == "Física"
]


print(fisicos)


# Resultado:
#
# ["Albert Einstein"]


# ------------------------------------------------------------
# 8. DICT COMPREHENSION
# ------------------------------------------------------------

# También podemos crear diccionarios mediante
# comprehensions.


cientificos_por_area = {
    cientifico["nombre"]: cientifico["area"]
    for cientifico in cientificos
}


print(cientificos_por_area)


# Resultado conceptual:
#
# {
#     "Albert Einstein": "Física",
#     "Carl Sagan": "Astronomía",
#     "Marie Curie": "Química"
# }
#
#
# Estructura:
#
# {
#     clave: valor
#     for elemento in coleccion
# }


# ------------------------------------------------------------
# 9. OTRO EJEMPLO DE DICT COMPREHENSION
# ------------------------------------------------------------

numeros_cuadrados = {
    numero: numero ** 2
    for numero in numeros
}


print(numeros_cuadrados)


# Resultado:
#
# {
#     1: 1,
#     2: 4,
#     3: 9,
#     4: 16,
#     5: 25
# }


# ------------------------------------------------------------
# 10. SET COMPREHENSION
# ------------------------------------------------------------

# También podemos crear sets.


areas = [
    "Física",
    "Astronomía",
    "Física",
    "Química",
    "Astronomía"
]


areas_unicas = {
    area
    for area in areas
}


print(areas_unicas)


# Como se trata de un set:
#
# los valores repetidos desaparecen.


# ------------------------------------------------------------
# 11. CUÁNDO UTILIZAR COMPREHENSIONS
# ------------------------------------------------------------

# Buena opción:
#
# nombres = [
#     usuario["nombre"]
#     for usuario in usuarios
# ]
#
#
# Buena opción:
#
# activos = [
#     usuario
#     for usuario in usuarios
#     if usuario["activo"]
# ]
#
#
# Menos recomendable:
#
# una comprehension con muchas condiciones,
# funciones y operaciones diferentes.
#
#
# Si comienza a ser difícil de leer:
#
# utiliza un for tradicional.


# ------------------------------------------------------------
# 12. enumerate()
# ------------------------------------------------------------

# Muchas veces necesitamos:
#
# elemento
# +
# posición
#
#
# Sin enumerate podríamos hacer algo como:


cientificos_nombres = [
    "Alan Turing",
    "Ada Lovelace",
    "Grace Hopper"
]


indice = 0


for nombre in cientificos_nombres:

    print(
        indice,
        nombre
    )

    indice += 1


# Python proporciona:
#
# enumerate()


for indice, nombre in enumerate(
    cientificos_nombres
):
    print(
        indice,
        nombre
    )


# Resultado:
#
# 0 Alan Turing
# 1 Ada Lovelace
# 2 Grace Hopper


# ------------------------------------------------------------
# 13. enumerate() EMPEZANDO EN 1
# ------------------------------------------------------------

# Muchas veces queremos mostrar posiciones humanas:
#
# 1
# 2
# 3
#
# en lugar de:
#
# 0
# 1
# 2


for posicion, nombre in enumerate(
    cientificos_nombres,
    start=1
):

    print(
        posicion,
        nombre
    )


# Muy útil para:
#
# menús
# listados
# reportes
# resultados numerados


# ------------------------------------------------------------
# 14. zip()
# ------------------------------------------------------------

# zip() permite recorrer varias colecciones
# en paralelo.


nombres_investigadores = [
    "Albert Einstein",
    "Nikola Tesla",
    "Carl Sagan"
]


areas_investigadores = [
    "Física",
    "Electricidad",
    "Astronomía"
]


for nombre, area in zip(
    nombres_investigadores,
    areas_investigadores
):

    print(
        nombre,
        "-",
        area
    )


# Conceptualmente:
#
# nombres:
#
# Einstein
# Tesla
# Sagan
#
#
# areas:
#
# Física
# Electricidad
# Astronomía
#
#
# zip():
#
# Einstein → Física
# Tesla    → Electricidad
# Sagan    → Astronomía


# ------------------------------------------------------------
# 15. CREAR UN DICCIONARIO CON zip()
# ------------------------------------------------------------

investigadores = dict(
    zip(
        nombres_investigadores,
        areas_investigadores
    )
)


print(investigadores)


# Resultado conceptual:
#
# {
#     "Albert Einstein": "Física",
#     "Nikola Tesla": "Electricidad",
#     "Carl Sagan": "Astronomía"
# }


# ------------------------------------------------------------
# 16. IMPORTANTE SOBRE zip()
# ------------------------------------------------------------

# Si las colecciones tienen tamaños diferentes,
# zip() se detiene cuando termina la más corta.


nombres_prueba = [
    "Einstein",
    "Tesla",
    "Sagan"
]


areas_prueba = [
    "Física",
    "Electricidad"
]


for nombre, area in zip(
    nombres_prueba,
    areas_prueba
):

    print(
        nombre,
        area
    )


# "Sagan" no tendrá pareja.
#
# Esto es importante conocer para evitar asumir
# que zip() siempre recorrerá todos los datos.


# ------------------------------------------------------------
# 17. any()
# ------------------------------------------------------------

# any() pregunta:
#
# ¿Existe AL MENOS un elemento verdadero?


estados_tickets = [
    "Cerrado",
    "Cerrado",
    "En progreso"
]


hay_ticket_activo = any(
    estado == "En progreso"
    for estado in estados_tickets
)


print(hay_ticket_activo)


# Resultado:
#
# True
#
#
# porque al menos uno cumple la condición.


# ------------------------------------------------------------
# 18. CONCEPTO DE any()
# ------------------------------------------------------------

# Podemos pensarlo:
#
# False
# False
# True
#
# ↓
#
# any(...)
#
# ↓
#
# True
#
#
# Basta con encontrar un True.


# ------------------------------------------------------------
# 19. all()
# ------------------------------------------------------------

# all() pregunta:
#
# ¿TODOS los elementos son verdaderos?


estados_finalizados = [
    "Cerrado",
    "Cerrado",
    "Cerrado"
]


todos_cerrados = all(
    estado == "Cerrado"
    for estado in estados_finalizados
)


print(todos_cerrados)


# Resultado:
#
# True


# ------------------------------------------------------------
# 20. EJEMPLO DE all() CON VALIDACIÓN
# ------------------------------------------------------------

edades = [
    31,
    25,
    42,
    19
]


todos_mayores = all(
    edad >= 18
    for edad in edades
)


print(todos_mayores)


# Podemos leer:
#
# "¿todas las edades son mayores o iguales a 18?"


# ------------------------------------------------------------
# 21. any() VS all()
# ------------------------------------------------------------

# any()
#
# → al menos uno debe cumplir.
#
#
# all()
#
# → todos deben cumplir.
#
#
# Ejemplo mental:
#
# [False, False, True]
#
# any()
# → True
#
# all()
# → False


# ------------------------------------------------------------
# 22. sorted()
# ------------------------------------------------------------

# sorted() ya lo hemos utilizado anteriormente.
#
# Recordatorio:
#
# sorted()
#
# devuelve una NUEVA lista ordenada.
#
#
# No modifica necesariamente la colección original.


cientificos_orden = [
    "Nikola Tesla",
    "Albert Einstein",
    "Carl Sagan"
]


cientificos_ordenados = sorted(
    cientificos_orden
)


print(cientificos_ordenados)
print(cientificos_orden)


# ------------------------------------------------------------
# 23. sorted() CON reverse
# ------------------------------------------------------------

orden_descendente = sorted(
    numeros,
    reverse=True
)


print(orden_descendente)


# Resultado:
#
# [5, 4, 3, 2, 1]


# ------------------------------------------------------------
# 24. sorted() CON key
# ------------------------------------------------------------

# key permite indicar:
#
# "según qué valor quiero ordenar"


cientificos_datos = [
    {
        "nombre": "Albert Einstein",
        "anio": 1879
    },
    {
        "nombre": "Stephen Hawking",
        "anio": 1942
    },
    {
        "nombre": "Nikola Tesla",
        "anio": 1856
    }
]


def obtener_anio(cientifico):
    return cientifico["anio"]


cientificos_por_anio = sorted(
    cientificos_datos,
    key=obtener_anio
)


print(cientificos_por_anio)


# Aquí:
#
# sorted()
#
# no intenta ordenar directamente los diccionarios.
#
#
# Le indicamos:
#
# key=obtener_anio
#
# es decir:
#
# "utiliza el año como criterio de ordenamiento"


# ------------------------------------------------------------
# 25. ORDENAR STRINGS IGNORANDO MAYÚSCULAS
# ------------------------------------------------------------

nombres_mixtos = [
    "tesla",
    "Einstein",
    "sagan",
    "Curie"
]


nombres_ordenados = sorted(
    nombres_mixtos,
    key=str.lower
)


print(nombres_ordenados)


# str.lower
#
# se utiliza como criterio para comparar los elementos.
#
#
# IMPORTANTE:
#
# escribimos:
#
# key=str.lower
#
# y no:
#
# key=str.lower()
#
#
# Estamos entregando la función para que sorted()
# pueda utilizarla con cada elemento.


# ------------------------------------------------------------
# 26. COMBINAR enumerate() CON OBJETOS O DICCIONARIOS
# ------------------------------------------------------------

tickets = [
    {
        "id": "TK-001",
        "titulo": "Usuario sin acceso"
    },
    {
        "id": "TK-002",
        "titulo": "Equipo sin conexión"
    },
    {
        "id": "TK-003",
        "titulo": "Error de impresión"
    }
]


for posicion, ticket in enumerate(
    tickets,
    start=1
):

    print(
        posicion,
        ticket["id"],
        ticket["titulo"]
    )


# Esto puede ser útil para crear:
#
# 1 TK-001 Usuario sin acceso
# 2 TK-002 Equipo sin conexión
# 3 TK-003 Error de impresión


# ------------------------------------------------------------
# 27. COMBINAR COMPREHENSION Y any()
# ------------------------------------------------------------

prioridades = [
    "Baja",
    "Media",
    "Crítica",
    "Alta"
]


hay_prioridad_critica = any(
    prioridad == "Crítica"
    for prioridad in prioridades
)


print(
    hay_prioridad_critica
)


# Este tipo de código aparece con frecuencia:
#
# comprobar si una colección contiene
# al menos un elemento que cumple una condición.


# ------------------------------------------------------------
# 28. COMBINAR COMPREHENSION Y all()
# ------------------------------------------------------------

codigos = [
    "TK-001",
    "TK-002",
    "TK-003"
]


codigos_validos = all(
    codigo.startswith("TK-")
    for codigo in codigos
)


print(
    codigos_validos
)


# ------------------------------------------------------------
# 29. EJEMPLO PRÁCTICO INTEGRADO
# ------------------------------------------------------------

usuarios = [
    {
        "nombre": "Alan Turing",
        "activo": True
    },
    {
        "nombre": "Grace Hopper",
        "activo": False
    },
    {
        "nombre": "Ada Lovelace",
        "activo": True
    }
]


usuarios_activos = [
    usuario["nombre"]
    for usuario in usuarios
    if usuario["activo"]
]


print(
    usuarios_activos
)


for posicion, nombre in enumerate(
    usuarios_activos,
    start=1
):

    print(
        posicion,
        nombre
    )


hay_usuarios_activos = any(
    usuario["activo"]
    for usuario in usuarios
)


print(
    hay_usuarios_activos
)


todos_usuarios_activos = all(
    usuario["activo"]
    for usuario in usuarios
)


print(
    todos_usuarios_activos
)


# En este ejemplo combinamos:
#
# list comprehension
# filtros
# diccionarios
# enumerate()
# any()
# all()


# ------------------------------------------------------------
# 30. CUÁNDO NO UTILIZAR UNA COMPREHENSION
# ------------------------------------------------------------

# Si necesitamos:
#
# - muchas condiciones;
# - varios pasos;
# - manejo de excepciones;
# - múltiples modificaciones;
# - lógica difícil de explicar;
#
# normalmente será más claro utilizar:
#
# for
#
#
# Ejemplo:
#
# una comprehension no debería transformarse
# en una línea difícil de comprender solamente
# para ahorrar líneas de código.


# ------------------------------------------------------------
# 31. LEGIBILIDAD PRIMERO
# ------------------------------------------------------------

# Esto:
#
# numeros_pares = [
#     numero
#     for numero in numeros
#     if numero % 2 == 0
# ]
#
# es sencillo de leer.
#
#
# Pero si necesitamos muchas reglas:
#
# for elemento in elementos:
#
#     ...
#
# puede ser una mejor solución.
#
#
# Python permite escribir código compacto.
#
# Eso no significa que siempre debamos hacerlo.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# LIST COMPREHENSION:
#
# nueva_lista = [
#     expresion
#     for elemento in coleccion
# ]
#
#
# CON FILTRO:
#
# nueva_lista = [
#     elemento
#     for elemento in coleccion
#     if condicion
# ]
#
#
# DICT COMPREHENSION:
#
# nuevo_diccionario = {
#     clave: valor
#     for elemento in coleccion
# }
#
#
# SET COMPREHENSION:
#
# nuevo_set = {
#     elemento
#     for elemento in coleccion
# }
#
#
# enumerate():
#
# permite obtener:
#
# posición + elemento
#
#
# zip():
#
# permite recorrer colecciones en paralelo.
#
#
# any():
#
# True si AL MENOS UNO cumple.
#
#
# all():
#
# True si TODOS cumplen.
#
#
# sorted():
#
# devuelve datos ordenados.
#
#
# sorted(..., key=...)
#
# permite elegir el criterio de ordenamiento.
#
#
# REGLA PRINCIPAL:
#
# utilizar estas herramientas cuando mejoran
# claridad y expresividad.
#
# No utilizarlas solamente para reducir líneas.