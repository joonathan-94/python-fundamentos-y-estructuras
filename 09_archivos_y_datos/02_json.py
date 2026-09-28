# ============================================================
# ARCHIVOS JSON EN PYTHON
# ============================================================
#
# JSON significa:
#
# JavaScript Object Notation
#
# Es un formato de texto utilizado para representar
# información estructurada.
#
# Es muy común en:
#
# - APIs;
# - integraciones entre sistemas;
# - archivos de configuración;
# - intercambio de información;
# - aplicaciones web;
# - automatizaciones.
#
#
# Python incluye el módulo:
#
# json
#
# dentro de su biblioteca estándar.


import json


# ------------------------------------------------------------
# 1. DATOS ESTRUCTURADOS EN PYTHON
# ------------------------------------------------------------

# Ya sabemos trabajar con diccionarios.

cientifico = {
    "nombre": "Stephen Hawking",
    "area": "Física",
    "anio_nacimiento": 1942
}


print(cientifico)


# Python puede transformar estructuras como esta
# a formato JSON.


# ------------------------------------------------------------
# 2. CÓMO SE VE JSON
# ------------------------------------------------------------

# Un JSON equivalente podría verse así:
#
# {
#     "nombre": "Stephen Hawking",
#     "area": "Física",
#     "anio_nacimiento": 1942
# }
#
#
# Visualmente se parece mucho a un diccionario.
#
# Pero debemos recordar:
#
# JSON
# → formato de texto
#
# dict
# → objeto de Python


# ------------------------------------------------------------
# 3. TIPOS PYTHON Y JSON
# ------------------------------------------------------------

# Algunos tipos tienen equivalencias directas.
#
#
# PYTHON          JSON
#
# dict            object
# list            array
# str             string
# int / float     number
# True            true
# False           false
# None            null
#
#
# Ejemplo Python:

datos_ejemplo = {
    "nombre": "Albert Einstein",
    "activo": True,
    "premios": 1,
    "observacion": None
}


print(datos_ejemplo)


# Si estos datos se convierten a JSON aparecerían:
#
# True
# ↓
# true
#
# None
# ↓
# null


# ------------------------------------------------------------
# 4. RUTA DEL ARCHIVO JSON
# ------------------------------------------------------------

ruta_ticket = (
    "09_archivos_y_datos/datos/ticket.json"
)


# Igual que con los archivos .txt,
# estamos utilizando una ruta relativa.
#
# Ejecutaremos el programa desde la raíz
# del repositorio.


# ------------------------------------------------------------
# 5. GUARDAR UN DICCIONARIO EN JSON
# ------------------------------------------------------------

ticket = {
    "id": "WD-1001",
    "titulo": "Usuario sin acceso",
    "prioridad": "Alta",
    "estado": "Nuevo"
}


# Para guardar una estructura Python utilizamos:
#
# json.dump()


with open(
    ruta_ticket,
    "w",
    encoding="utf-8"
) as archivo:

    json.dump(
        ticket,
        archivo
    )


# Después de ejecutar esto:
#
# ticket.json
#
# contendrá los datos del diccionario.


# ------------------------------------------------------------
# 6. json.dump()
# ------------------------------------------------------------

# Podemos pensar:
#
# Python
# ↓
# dict
# ↓
# json.dump()
# ↓
# archivo JSON


# Estructura básica:
#
# json.dump(
#     objeto_python,
#     archivo
# )


# ------------------------------------------------------------
# 7. HACER EL JSON MÁS LEGIBLE
# ------------------------------------------------------------

# Podemos utilizar:
#
# indent=4
#
# para escribir el archivo con sangría.


ticket_detallado = {
    "id": "WD-2001",
    "titulo": "Servidor sin conexión",
    "prioridad": "Crítica",
    "estado": "En progreso"
}


with open(
    ruta_ticket,
    "w",
    encoding="utf-8"
) as archivo:

    json.dump(
        ticket_detallado,
        archivo,
        indent=4
    )


# El archivo se verá aproximadamente así:
#
# {
#     "id": "WD-2001",
#     "titulo": "Servidor sin conexión",
#     "prioridad": "Crítica",
#     "estado": "En progreso"
# }


# ------------------------------------------------------------
# 8. CARACTERES UTF-8
# ------------------------------------------------------------

# Por defecto JSON puede representar ciertos caracteres
# utilizando secuencias especiales.
#
# Podemos agregar:
#
# ensure_ascii=False
#
# para conservar caracteres como:
#
# í
# é
# ñ
#
# directamente en el archivo.


datos_astronomo = {
    "nombre": "José Maza",
    "profesion": "Astrónomo",
    "pais": "Chile"
}


with open(
    ruta_ticket,
    "w",
    encoding="utf-8"
) as archivo:

    json.dump(
        datos_astronomo,
        archivo,
        indent=4,
        ensure_ascii=False
    )


# Para nuestros ejemplos utilizaremos frecuentemente:
#
# indent=4
# ensure_ascii=False


# ------------------------------------------------------------
# 9. LEER JSON DESDE UN ARCHIVO
# ------------------------------------------------------------

# Para leer utilizamos:
#
# json.load()


with open(
    ruta_ticket,
    "r",
    encoding="utf-8"
) as archivo:

    datos_leidos = json.load(archivo)


print(datos_leidos)


# ------------------------------------------------------------
# 10. ¿QUÉ DEVUELVE json.load()?
# ------------------------------------------------------------

print(type(datos_leidos))


# Como nuestro JSON contiene un objeto:
#
# Python lo convierte a:
#
# dict


print(datos_leidos["nombre"])
print(datos_leidos["profesion"])


# Una vez cargados los datos podemos trabajar con ellos
# utilizando exactamente los conocimientos que ya tenemos
# sobre diccionarios.


# ------------------------------------------------------------
# 11. FLUJO COMPLETO
# ------------------------------------------------------------

# Podemos visualizar:
#
# DICCIONARIO PYTHON
#
# {
#     "nombre": "José Maza"
# }
#
# ↓
#
# json.dump()
#
# ↓
#
# archivo .json
#
# ↓
#
# json.load()
#
# ↓
#
# DICCIONARIO PYTHON


# ------------------------------------------------------------
# 12. JSON CON LISTAS
# ------------------------------------------------------------

# JSON también puede representar listas.


cientificos = [
    "Werner Heisenberg",
    "Albert Einstein",
    "Stephen Hawking",
    "Nikola Tesla",
    "Galileo Galilei",
    "Carl Sagan"
]


# No necesitamos guardarla todavía.
#
# Lo importante es saber que una lista Python puede
# convertirse a un array JSON.


# ------------------------------------------------------------
# 13. ESTRUCTURAS MÁS COMPLETAS
# ------------------------------------------------------------

cientificos_destacados = [
    {
        "nombre": "Albert Einstein",
        "area": "Física"
    },
    {
        "nombre": "Stephen Hawking",
        "area": "Cosmología"
    },
    {
        "nombre": "Alan Turing",
        "area": "Computación"
    },
    {
        "nombre": "Ada Lovelace",
        "area": "Matemáticas y computación"
    }
]


print(cientificos_destacados)


# Aquí tenemos:
#
# lista
# ↓
# varios diccionarios
#
#
# Este tipo de estructura aparece constantemente
# cuando trabajamos con datos reales.


# ------------------------------------------------------------
# 14. ACCEDER A DATOS CARGADOS
# ------------------------------------------------------------

primer_cientifico = cientificos_destacados[0]

print(primer_cientifico)


nombre_primer_cientifico = primer_cientifico["nombre"]

print(nombre_primer_cientifico)


# No necesitamos aprender una sintaxis especial para JSON
# después de cargarlo.
#
# Volvemos a trabajar con:
#
# listas
# diccionarios
# strings
# números
#
# que ya conocemos.


# ------------------------------------------------------------
# 15. json.dumps()
# ------------------------------------------------------------

# Hasta ahora utilizamos:
#
# json.dump()
#
# para escribir directamente en un archivo.
#
#
# También existe:
#
# json.dumps()
#
# que devuelve un STRING JSON.


datos_tesla = {
    "nombre": "Nikola Tesla",
    "area": "Electricidad"
}


texto_json = json.dumps(
    datos_tesla,
    indent=4,
    ensure_ascii=False
)


print(texto_json)
print(type(texto_json))


# Resultado:
#
# str


# Regla sencilla:
#
# dump
# → archivo
#
# dumps
# → string


# ------------------------------------------------------------
# 16. json.loads()
# ------------------------------------------------------------

# También podemos realizar el proceso contrario.
#
# Tenemos un string que contiene JSON:


texto_recibido = """
{
    "nombre": "Galileo Galilei",
    "area": "Astronomía"
}
"""


datos_galileo = json.loads(
    texto_recibido
)


print(datos_galileo)
print(type(datos_galileo))


# json.loads()
#
# convierte:
#
# string JSON
# ↓
# objeto Python


# En este caso:
#
# str
# ↓
# dict


# ------------------------------------------------------------
# 17. dump VS dumps
# ------------------------------------------------------------

# MUY IMPORTANTE:
#
#
# json.dump()
#
# objeto Python
# ↓
# ARCHIVO
#
#
# json.dumps()
#
# objeto Python
# ↓
# STRING JSON


# ------------------------------------------------------------
# 18. load VS loads
# ------------------------------------------------------------

# json.load()
#
# ARCHIVO JSON
# ↓
# objeto Python
#
#
# json.loads()
#
# STRING JSON
# ↓
# objeto Python


# ------------------------------------------------------------
# 19. REGLA RÁPIDA
# ------------------------------------------------------------

# Sin "s":
#
# dump()
# load()
#
# normalmente trabajamos con archivos.
#
#
# Con "s":
#
# dumps()
# loads()
#
# trabajamos con strings.


# ------------------------------------------------------------
# 20. EJEMPLO CON WORKDESK
# ------------------------------------------------------------

ticket_workdesk = {
    "id": "WD-3001",
    "titulo": "Error en sistema ERP",
    "prioridad": "Alta",
    "estado": "Nuevo",
    "tecnicos": [
        "Alan Turing",
        "Grace Hopper"
    ]
}


texto_ticket = json.dumps(
    ticket_workdesk,
    indent=4,
    ensure_ascii=False
)


print(texto_ticket)


# Este ejemplo es solamente pedagógico.
#
# WorkDesk utilizará posteriormente una base de datos
# para almacenar su información principal.
#
# JSON podría utilizarse en otros contextos:
#
# - APIs;
# - importaciones;
# - exportaciones;
# - configuraciones;
# - integraciones.


# ------------------------------------------------------------
# 21. EJEMPLO DE UNA RESPUESTA DE API
# ------------------------------------------------------------

# Más adelante, cuando trabajemos con APIs, será común
# encontrar información parecida a:
#
# {
#     "id": 1001,
#     "nombre": "Alan Turing",
#     "activo": true
# }
#
#
# Cuando Python procesa ese JSON podríamos terminar
# trabajando con:
#
# {
#     "id": 1001,
#     "nombre": "Alan Turing",
#     "activo": True
# }
#
#
# Es decir:
#
# JSON externo
# ↓
# Python
# ↓
# estructuras conocidas


# ------------------------------------------------------------
# 22. MANEJO DE ARCHIVO INEXISTENTE
# ------------------------------------------------------------

# Como ya conocemos excepciones, podemos manejar
# FileNotFoundError.


ruta_inexistente = (
    "09_archivos_y_datos/datos/"
    "archivo_inexistente.json"
)


try:

    with open(
        ruta_inexistente,
        "r",
        encoding="utf-8"
    ) as archivo:

        datos = json.load(archivo)

except FileNotFoundError:
    print("El archivo JSON no existe.")


# ------------------------------------------------------------
# 23. JSON INVÁLIDO
# ------------------------------------------------------------

# También puede ocurrir que el archivo exista,
# pero su contenido no sea JSON válido.
#
# Ejemplo incorrecto:
#
# {
#     nombre: Stephen Hawking
# }
#
# Faltan comillas alrededor de claves y valores.
#
#
# json.load() o json.loads() pueden producir:
#
# json.JSONDecodeError


texto_json_invalido = """
{
    nombre: "Stephen Hawking"
}
"""


try:
    datos_invalidos = json.loads(
        texto_json_invalido
    )

except json.JSONDecodeError:
    print("El contenido no tiene un formato JSON válido.")


# Aquí estamos combinando:
#
# módulos
# JSON
# excepciones


# ------------------------------------------------------------
# 24. JSON NO ES UNA BASE DE DATOS
# ------------------------------------------------------------

# Un archivo JSON puede guardar información.
#
# Pero no debemos confundirlo con una base de datos.
#
#
# JSON funciona muy bien para:
#
# - configuraciones;
# - intercambio de información;
# - pequeñas estructuras;
# - exportaciones;
# - APIs.
#
#
# Para grandes aplicaciones utilizaremos otras herramientas
# cuando corresponda.


# ------------------------------------------------------------
# 25. EJEMPLO CON RICK SANCHEZ
# ------------------------------------------------------------

# Rick Sanchez es un personaje ficticio de Rick and Morty.
#
# Podemos utilizarlo simplemente como dato de ejemplo.


personaje = {
    "nombre": "Rick Sanchez",
    "tipo": "Personaje ficticio",
    "profesion": "Científico"
}


personaje_json = json.dumps(
    personaje,
    indent=4,
    ensure_ascii=False
)


print(personaje_json)


# ------------------------------------------------------------
# 26. JSON COMO FORMATO DE INTERCAMBIO
# ------------------------------------------------------------

# Podemos visualizar:
#
# SISTEMA A
# ↓
# genera JSON
# ↓
# SISTEMA B
# ↓
# interpreta JSON
#
#
# Esto hace que JSON sea muy utilizado para integrar
# aplicaciones diferentes.


# ------------------------------------------------------------
# 27. RELACIÓN CON LO QUE YA ESTUDIAMOS
# ------------------------------------------------------------

# JSON conecta conceptos anteriores:
#
# módulos
# ↓
# import json
#
# archivos
# ↓
# open()
#
# diccionarios
# ↓
# objetos JSON
#
# listas
# ↓
# arrays JSON
#
# excepciones
# ↓
# FileNotFoundError
# JSONDecodeError


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# JSON
#
# es un formato de texto para representar
# información estructurada.
#
#
# GUARDAR EN ARCHIVO:
#
# json.dump(
#     datos,
#     archivo
# )
#
#
# LEER ARCHIVO:
#
# datos = json.load(
#     archivo
# )
#
#
# CONVERTIR A STRING JSON:
#
# texto = json.dumps(
#     datos
# )
#
#
# CONVERTIR STRING JSON A PYTHON:
#
# datos = json.loads(
#     texto
# )
#
#
# REGLA RÁPIDA:
#
# dump
# → escribir archivo
#
# load
# → leer archivo
#
# dumps
# → crear string JSON
#
# loads
# → leer string JSON
#
#
# Para escribir archivos legibles:
#
# indent=4
#
#
# Para conservar caracteres:
#
# ensure_ascii=False
#
#
# FLUJO PRINCIPAL:
#
# dict / list Python
# ↓
# JSON
# ↓
# archivo o intercambio de datos
# ↓
# JSON
# ↓
# dict / list Python
#
#
# Una vez convertido nuevamente a Python,
# seguimos trabajando con las estructuras que
# ya conocemos.