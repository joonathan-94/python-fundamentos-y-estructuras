# ============================================================
# DESEMPAQUETADO, *args Y **kwargs
# ============================================================
#
# En Python podemos:
#
# - desempaquetar colecciones;
# - enviar varios valores a una función;
# - recibir una cantidad variable de argumentos.
#
#
# Las herramientas principales serán:
#
# *
# **
# *args
# **kwargs
#
#
# IDEA GENERAL:
#
# *
# → valores posicionales
#
# **
# → pares clave-valor / argumentos nombrados


# ------------------------------------------------------------
# 1. DESEMPAQUETADO BÁSICO
# ------------------------------------------------------------

# Ya conocemos algo parecido:


cientifico = (
    "Albert Einstein",
    "Física",
    1879
)


nombre, area, anio = cientifico


print(nombre)
print(area)
print(anio)


# La tupla:
#
# ("Albert Einstein", "Física", 1879)
#
# se distribuye entre:
#
# nombre
# area
# anio
#
#
# Esto se llama:
#
# desempaquetado


# ------------------------------------------------------------
# 2. DESEMPAQUETADO DE LISTAS
# ------------------------------------------------------------

datos_turing = [
    "Alan Turing",
    "Computación",
    1912
]


nombre_turing, area_turing, anio_turing = datos_turing


print(nombre_turing)
print(area_turing)
print(anio_turing)


# No está limitado a tuplas.
#
# También podemos desempaquetar listas.


# ------------------------------------------------------------
# 3. UTILIZAR * DURANTE EL DESEMPAQUETADO
# ------------------------------------------------------------

# Imaginemos que tenemos más elementos de los que queremos
# guardar individualmente.


cientificos = [
    "Einstein",
    "Tesla",
    "Curie",
    "Sagan",
    "Hawking"
]


primero, *restantes = cientificos


print(primero)
print(restantes)


# Resultado:
#
# Einstein
# ["Tesla", "Curie", "Sagan", "Hawking"]
#
#
# *
#
# permite capturar varios elementos.


# ------------------------------------------------------------
# 4. CAPTURAR EL PRIMERO Y EL ÚLTIMO
# ------------------------------------------------------------

primero, *intermedios, ultimo = cientificos


print(primero)
print(intermedios)
print(ultimo)


# Resultado:
#
# Einstein
# ["Tesla", "Curie", "Sagan"]
# Hawking


# ------------------------------------------------------------
# 5. DESEMPAQUETAR AL LLAMAR UNA FUNCIÓN
# ------------------------------------------------------------

def mostrar_cientifico(
    nombre,
    area,
    anio_nacimiento
):
    print(nombre)
    print(area)
    print(anio_nacimiento)


datos_einstein = [
    "Albert Einstein",
    "Física",
    1879
]


mostrar_cientifico(
    *datos_einstein
)


# Aquí:
#
# *datos_einstein
#
# convierte:
#
# [
#     "Albert Einstein",
#     "Física",
#     1879
# ]
#
# conceptualmente en:
#
# mostrar_cientifico(
#     "Albert Einstein",
#     "Física",
#     1879
# )


# ------------------------------------------------------------
# 6. * NO SIGNIFICA SIEMPRE MULTIPLICACIÓN
# ------------------------------------------------------------

# Ya conocemos:
#
# 5 * 3
#
# donde "*" representa multiplicación.
#
#
# Pero en este contexto:
#
# *datos
#
# significa:
#
# desempaquetar valores.
#
#
# El significado depende del contexto.


# ------------------------------------------------------------
# 7. DESEMPAQUETAR UN DICCIONARIO
# ------------------------------------------------------------

def registrar_usuario(
    nombre,
    correo,
    activo
):
    print(nombre)
    print(correo)
    print(activo)


usuario = {
    "nombre": "Grace Hopper",
    "correo": "hopper@example.com",
    "activo": True
}


registrar_usuario(
    **usuario
)


# Aquí:
#
# **usuario
#
# conceptualmente se transforma en:
#
# registrar_usuario(
#     nombre="Grace Hopper",
#     correo="hopper@example.com",
#     activo=True
# )


# ------------------------------------------------------------
# 8. IMPORTANCIA DE LAS CLAVES
# ------------------------------------------------------------

# Para utilizar:
#
# **diccionario
#
# las claves deben corresponder con los nombres
# de los parámetros esperados por la función.
#
#
# Tenemos:
#
# def registrar_usuario(
#     nombre,
#     correo,
#     activo
# )
#
#
# Por eso el diccionario utiliza:
#
# "nombre"
# "correo"
# "activo"


# ------------------------------------------------------------
# 9. *args
# ------------------------------------------------------------

# Hasta ahora nuestras funciones normalmente esperaban
# una cantidad determinada de argumentos.


def sumar_dos(
    numero_a,
    numero_b
):
    return numero_a + numero_b


print(
    sumar_dos(
        10,
        20
    )
)


# Pero a veces no sabemos cuántos argumentos
# recibirá una función.
#
# Podemos utilizar:
#
# *args


def sumar(*args):
    total = 0

    for numero in args:
        total += numero

    return total


print(
    sumar(
        10,
        20,
        30
    )
)


print(
    sumar(
        5,
        10,
        15,
        20,
        25
    )
)


# La función acepta cantidades diferentes de argumentos.


# ------------------------------------------------------------
# 10. ¿QUÉ ES args?
# ------------------------------------------------------------

def mostrar_argumentos(*args):
    print(args)
    print(type(args))


mostrar_argumentos(
    "Einstein",
    "Tesla",
    "Curie"
)


# Veremos algo similar a:
#
# (
#     "Einstein",
#     "Tesla",
#     "Curie"
# )
#
# <class 'tuple'>
#
#
# Es decir:
#
# *args
# ↓
# recibe argumentos posicionales
# ↓
# Python los agrupa en una tuple


# ------------------------------------------------------------
# 11. args ES UNA CONVENCIÓN DE NOMBRE
# ------------------------------------------------------------

# Técnicamente podríamos escribir:
#
#
# def funcion(*valores):
#     ...
#
#
# Pero la convención habitual es:
#
# *args
#
#
# args viene de:
#
# arguments


def mostrar_nombres(*args):

    for nombre in args:
        print(nombre)


mostrar_nombres(
    "Nikola Tesla",
    "Carl Sagan",
    "Stephen Hawking"
)


# ------------------------------------------------------------
# 12. PARÁMETROS NORMALES + *args
# ------------------------------------------------------------

def registrar_aportes(
    cientifico,
    *aportes
):

    print(
        f"Científico: {cientifico}"
    )

    for aporte in aportes:
        print(
            f"- {aporte}"
        )


registrar_aportes(
    "Alan Turing",
    "Máquina de Turing",
    "Criptoanálisis",
    "Fundamentos de computación"
)


# Aquí:
#
# cientifico
# → primer argumento normal
#
#
# *aportes
# → todos los argumentos posicionales restantes


# ------------------------------------------------------------
# 13. **kwargs
# ------------------------------------------------------------

# **kwargs permite recibir una cantidad variable
# de argumentos CON NOMBRE.


def mostrar_datos(**kwargs):
    print(kwargs)
    print(type(kwargs))


mostrar_datos(
    nombre="Marie Curie",
    area="Física y química",
    anio=1867
)


# Resultado conceptual:
#
# {
#     "nombre": "Marie Curie",
#     "area": "Física y química",
#     "anio": 1867
# }
#
#
# **kwargs
# ↓
# recibe argumentos nombrados
# ↓
# Python los agrupa en un dict


# ------------------------------------------------------------
# 14. RECORRER kwargs
# ------------------------------------------------------------

def mostrar_ficha(**kwargs):

    for clave, valor in kwargs.items():
        print(
            clave,
            "=",
            valor
        )


mostrar_ficha(
    nombre="Carl Sagan",
    area="Astronomía",
    pais="Estados Unidos"
)


# Aquí reutilizamos:
#
# diccionarios
# .items()
# for
# kwargs


# ------------------------------------------------------------
# 15. kwargs TAMBIÉN ES UNA CONVENCIÓN
# ------------------------------------------------------------

# Técnicamente podríamos escribir:
#
#
# def funcion(**datos):
#     ...
#
#
# pero la convención habitual es:
#
# **kwargs
#
#
# kwargs viene de:
#
# keyword arguments


# ------------------------------------------------------------
# 16. ARGUMENTOS NORMALES + **kwargs
# ------------------------------------------------------------

def registrar_ticket(
    titulo,
    **kwargs
):

    print(
        f"Ticket: {titulo}"
    )

    print(
        kwargs
    )


registrar_ticket(
    "Servidor sin conexión",
    prioridad="Alta",
    estado="Nuevo",
    categoria="Infraestructura"
)


# Aquí:
#
# titulo
#
# es un parámetro normal.
#
#
# Los demás:
#
# prioridad
# estado
# categoria
#
# terminan dentro de kwargs.


# ------------------------------------------------------------
# 17. *args + **kwargs
# ------------------------------------------------------------

# También pueden utilizarse juntos.


def procesar_datos(
    identificador,
    *args,
    **kwargs
):

    print(
        f"ID: {identificador}"
    )

    print(
        "Argumentos posicionales:"
    )

    print(args)

    print(
        "Argumentos nombrados:"
    )

    print(kwargs)


procesar_datos(
    "REG-001",
    "valor uno",
    "valor dos",
    activo=True,
    prioridad="Alta"
)


# Conceptualmente:
#
# identificador
# → parámetro obligatorio normal
#
#
# *args
# → argumentos posicionales adicionales
#
#
# **kwargs
# → argumentos nombrados adicionales


# ------------------------------------------------------------
# 18. EJEMPLO PRÁCTICO CON UNA FUNCIÓN
# ------------------------------------------------------------

def crear_usuario(
    nombre,
    correo,
    rol="Usuario"
):

    return {
        "nombre": nombre,
        "correo": correo,
        "rol": rol
    }


datos_usuario = {
    "nombre": "Ada Lovelace",
    "correo": "ada@example.com",
    "rol": "Analista"
}


usuario_creado = crear_usuario(
    **datos_usuario
)


print(
    usuario_creado
)


# Este patrón es importante.
#
# Tenemos datos estructurados en un diccionario:
#
# datos_usuario
#
# y podemos utilizarlos directamente como argumentos:
#
# **datos_usuario


# ------------------------------------------------------------
# 19. EJEMPLO CON POO
# ------------------------------------------------------------

class Cientifico:

    def __init__(
        self,
        nombre,
        area,
        anio_nacimiento
    ):
        self.nombre = nombre
        self.area = area
        self.anio_nacimiento = anio_nacimiento


datos_tesla = {
    "nombre": "Nikola Tesla",
    "area": "Ingeniería eléctrica",
    "anio_nacimiento": 1856
}


tesla = Cientifico(
    **datos_tesla
)


print(tesla.nombre)
print(tesla.area)
print(tesla.anio_nacimiento)


# Esto equivale conceptualmente a:
#
# Cientifico(
#     nombre="Nikola Tesla",
#     area="Ingeniería eléctrica",
#     anio_nacimiento=1856
# )


# ------------------------------------------------------------
# 20. COMBINAR DOS LISTAS CON *
# ------------------------------------------------------------

cientificos_clasicos = [
    "Galileo Galilei",
    "Isaac Newton"
]


cientificos_modernos = [
    "Albert Einstein",
    "Stephen Hawking"
]


todos_cientificos = [
    *cientificos_clasicos,
    *cientificos_modernos
]


print(
    todos_cientificos
)


# Aquí:
#
# *
#
# expande los elementos de ambas listas
# dentro de una nueva lista.


# ------------------------------------------------------------
# 21. COMBINAR DICCIONARIOS CON **
# ------------------------------------------------------------

datos_basicos = {
    "nombre": "Albert Einstein",
    "area": "Física"
}


datos_adicionales = {
    "anio": 1879,
    "pais": "Alemania"
}


ficha_completa = {
    **datos_basicos,
    **datos_adicionales
}


print(
    ficha_completa
)


# **
#
# permite expandir pares clave-valor
# dentro de otro diccionario.


# ------------------------------------------------------------
# 22. DIFERENCIA FUNDAMENTAL
# ------------------------------------------------------------

# Cuando DEFINIMOS:
#
#
# def funcion(*args):
#
# Python:
#
# RECIBE varios argumentos
# y los AGRUPA.
#
#
# Cuando LLAMAMOS:
#
#
# funcion(*lista)
#
# Python:
#
# toma una colección
# y la EXPANDE.
#
#
# Esta diferencia es importante.


# ------------------------------------------------------------
# 23. LO MISMO CON **
# ------------------------------------------------------------

# DEFINICIÓN:
#
#
# def funcion(**kwargs):
#
# recibe argumentos nombrados
# y los agrupa en un diccionario.
#
#
# LLAMADA:
#
#
# funcion(**diccionario)
#
# expande un diccionario como argumentos nombrados.


# ------------------------------------------------------------
# 24. RESUMEN VISUAL DE *
# ------------------------------------------------------------

# DEFINICIÓN:
#
# def funcion(*args):
#
# muchos valores
# ↓
# tuple


# LLAMADA:
#
# funcion(*lista)
#
# lista
# ↓
# varios argumentos


# ------------------------------------------------------------
# 25. RESUMEN VISUAL DE **
# ------------------------------------------------------------

# DEFINICIÓN:
#
# def funcion(**kwargs):
#
# muchos argumentos nombrados
# ↓
# dict


# LLAMADA:
#
# funcion(**diccionario)
#
# dict
# ↓
# argumentos clave=valor


# ------------------------------------------------------------
# 26. CUÁNDO UTILIZAR *args
# ------------------------------------------------------------

# Tiene sentido cuando una función realmente puede recibir
# una cantidad variable de argumentos posicionales.
#
#
# Ejemplo:
#
# sumar(1, 2)
#
# sumar(1, 2, 3, 4)
#
#
# No debemos utilizar *args solamente porque existe.


# ------------------------------------------------------------
# 27. CUÁNDO UTILIZAR **kwargs
# ------------------------------------------------------------

# Puede ser útil cuando:
#
# - existen opciones adicionales;
# - trabajamos con datos estructurados;
# - una función acepta parámetros configurables;
# - trabajamos con librerías o frameworks.
#
#
# Pero tampoco reemplaza parámetros normales bien definidos.


# ------------------------------------------------------------
# 28. NO ABUSAR DE args Y kwargs
# ------------------------------------------------------------

# Esto:
#
# def crear_usuario(**kwargs):
#
# puede ser flexible.
#
#
# Pero si sabemos exactamente qué necesitamos:
#
#
# def crear_usuario(
#     nombre,
#     correo
# ):
#
# puede ser más claro.
#
#
# Flexibilidad no siempre significa mejor diseño.


# ------------------------------------------------------------
# 29. EJEMPLO FINAL
# ------------------------------------------------------------

def crear_registro(
    codigo,
    *etiquetas,
    **datos
):

    return {
        "codigo": codigo,
        "etiquetas": etiquetas,
        "datos": datos
    }


registro = crear_registro(
    "REG-1001",
    "ciencia",
    "fisica",
    autor="Albert Einstein",
    activo=True
)


print(
    registro
)


# Resultado conceptual:
#
# {
#     "codigo": "REG-1001",
#     "etiquetas": (
#         "ciencia",
#         "fisica"
#     ),
#     "datos": {
#         "autor": "Albert Einstein",
#         "activo": True
#     }
# }


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# DESEMPAQUETADO:
#
# nombre, area = datos
#
# distribuye elementos entre variables.
#
#
# ------------------------------------------------------------
#
# *lista
#
# expande valores posicionales.
#
#
# ------------------------------------------------------------
#
# **diccionario
#
# expande pares clave-valor como argumentos nombrados.
#
#
# ------------------------------------------------------------
#
# *args
#
# recibe una cantidad variable de argumentos posicionales.
#
# Dentro de la función:
#
# args
# → tuple
#
#
# ------------------------------------------------------------
#
# **kwargs
#
# recibe una cantidad variable de argumentos nombrados.
#
# Dentro de la función:
#
# kwargs
# → dict
#
#
# ------------------------------------------------------------
#
# DIFERENCIA IMPORTANTE:
#
# EN LA DEFINICIÓN:
#
# *args / **kwargs
# → agrupan
#
#
# EN LA LLAMADA:
#
# *lista / **diccionario
# → desempaquetan
#
#
# ------------------------------------------------------------
#
# REGLA PRINCIPAL:
#
# utilizar estas herramientas cuando realmente
# mejoran flexibilidad y claridad.
#
# No utilizarlas solamente porque permiten
# recibir cualquier cantidad de datos.