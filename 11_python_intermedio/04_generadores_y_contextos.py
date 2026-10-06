# ============================================================
# GENERADORES Y CONTEXT MANAGERS
# ============================================================
#
# En este archivo estudiaremos:
#
# - yield
# - funciones generadoras
# - next()
# - consumo progresivo de datos
# - generator expressions
# - context managers
# - with
#
#
# IDEA PRINCIPAL:
#
# GENERADOR
# → produce valores cuando se necesitan.
#
#
# CONTEXT MANAGER
# → administra correctamente el ciclo de vida
#   de un recurso.


# ------------------------------------------------------------
# 1. FUNCIÓN NORMAL CON return
# ------------------------------------------------------------

def obtener_numeros():
    return [
        1,
        2,
        3
    ]


numeros = obtener_numeros()


print(numeros)


# Aquí la función:
#
# crea toda la lista
# ↓
# la retorna completa
# ↓
# termina


# ------------------------------------------------------------
# 2. PRIMER GENERADOR CON yield
# ------------------------------------------------------------

def generar_numeros():

    yield 1
    yield 2
    yield 3


numeros_generados = generar_numeros()


print(numeros_generados)


# El resultado NO es:
#
# [1, 2, 3]
#
#
# Es un objeto generador.
#
# Los valores se producen cuando los necesitamos.


# ------------------------------------------------------------
# 3. RECORRER UN GENERADOR
# ------------------------------------------------------------

for numero in generar_numeros():
    print(numero)


# Resultado:
#
# 1
# 2
# 3


# ------------------------------------------------------------
# 4. yield VS return
# ------------------------------------------------------------

# return:
#
# entrega un resultado
# ↓
# termina la función
#
#
# yield:
#
# entrega un resultado
# ↓
# pausa la función
# ↓
# puede continuar posteriormente


# ------------------------------------------------------------
# 5. GENERADOR CON for
# ------------------------------------------------------------

def generar_ids(
    cantidad
):

    for numero in range(
        1,
        cantidad + 1
    ):
        yield numero


for id_actual in generar_ids(5):
    print(
        f"ID: {id_actual}"
    )


# Podemos generar:
#
# 1
# 2
# 3
# 4
# 5
#
# uno por uno.


# ------------------------------------------------------------
# 6. EJEMPLO CON TICKETS
# ------------------------------------------------------------

def generar_codigos_ticket(
    cantidad
):

    for numero in range(
        1,
        cantidad + 1
    ):

        yield (
            f"TK-{numero:04d}"
        )


for codigo in generar_codigos_ticket(4):
    print(codigo)


# Resultado:
#
# TK-0001
# TK-0002
# TK-0003
# TK-0004


# ------------------------------------------------------------
# 7. next()
# ------------------------------------------------------------

# Podemos solicitar manualmente el siguiente valor.


generador = generar_numeros()


primer_valor = next(
    generador
)


print(primer_valor)


segundo_valor = next(
    generador
)


print(segundo_valor)


# Cada next():
#
# reanuda
# ↓
# hasta encontrar el siguiente yield


# ------------------------------------------------------------
# 8. GENERADOR AGOTADO
# ------------------------------------------------------------

tercer_valor = next(
    generador
)


print(tercer_valor)


# Después de consumir todos los valores,
# el generador queda agotado.
#
#
# Si utilizáramos otro:
#
# next(generador)
#
# aparecería:
#
# StopIteration
#
#
# Normalmente utilizaremos:
#
# for
#
# porque gestiona esto automáticamente.


# ------------------------------------------------------------
# 9. UN GENERADOR SE CONSUME
# ------------------------------------------------------------

generador_ids = generar_ids(3)


for numero in generador_ids:
    print(numero)


print(
    "Segundo recorrido:"
)


for numero in generador_ids:
    print(numero)


# El segundo for no muestra valores.
#
# El generador ya fue consumido.
#
#
# Para recorrer nuevamente:
#
# debemos crear otro generador.


# ------------------------------------------------------------
# 10. CREAR UNO NUEVO
# ------------------------------------------------------------

nuevo_generador = generar_ids(3)


for numero in nuevo_generador:
    print(numero)


# ------------------------------------------------------------
# 11. ¿POR QUÉ USAR GENERADORES?
# ------------------------------------------------------------

# Imaginemos millones de registros.
#
#
# LISTA:
#
# crear todos
# ↓
# almacenar todos
# ↓
# comenzar a procesar
#
#
# GENERADOR:
#
# producir uno
# ↓
# procesarlo
# ↓
# producir siguiente
#
#
# Esto puede reducir el uso de memoria.


# ------------------------------------------------------------
# 12. EJEMPLO DE PROCESAMIENTO
# ------------------------------------------------------------

def generar_mediciones():

    mediciones = [
        21.5,
        22.1,
        23.0,
        22.8
    ]

    for medicion in mediciones:
        yield medicion


for temperatura in generar_mediciones():

    print(
        f"Procesando: {temperatura}"
    )


# En un caso real los datos podrían venir de:
#
# - archivos;
# - consultas;
# - APIs;
# - grandes conjuntos de datos.


# ------------------------------------------------------------
# 13. GENERADOR CON FILTRO
# ------------------------------------------------------------

def generar_pares(
    limite
):

    for numero in range(
        1,
        limite + 1
    ):

        if numero % 2 == 0:
            yield numero


for numero in generar_pares(10):
    print(numero)


# El generador puede contener:
#
# for
# if
# funciones
# cálculos
#
# igual que otras funciones.


# ------------------------------------------------------------
# 14. GENERATOR EXPRESSION
# ------------------------------------------------------------

# Ya estudiamos list comprehensions:
#
# [
#     numero * 2
#     for numero in numeros
# ]
#
#
# También existe una expresión generadora.


numeros_base = [
    1,
    2,
    3,
    4,
    5
]


dobles_generador = (
    numero * 2
    for numero in numeros_base
)


print(
    dobles_generador
)


for numero in dobles_generador:
    print(numero)


# Observa:
#
# LIST COMPREHENSION:
#
# [...]
#
#
# GENERATOR EXPRESSION:
#
# (...)


# ------------------------------------------------------------
# 15. LISTA VS GENERADOR
# ------------------------------------------------------------

lista_dobles = [
    numero * 2
    for numero in numeros_base
]


generador_dobles = (
    numero * 2
    for numero in numeros_base
)


print(lista_dobles)
print(generador_dobles)


# lista_dobles:
#
# contiene todos los valores.
#
#
# generador_dobles:
#
# produce los valores progresivamente.


# ------------------------------------------------------------
# 16. CUÁNDO PREFERIR UNA LISTA
# ------------------------------------------------------------

# Una lista es conveniente cuando:
#
# - necesitamos todos los resultados;
# - vamos a recorrerlos varias veces;
# - necesitamos posiciones;
# - modificaremos la colección;
# - el volumen de datos es pequeño o razonable.


# ------------------------------------------------------------
# 17. CUÁNDO PUEDE SERVIR UN GENERADOR
# ------------------------------------------------------------

# Puede resultar útil cuando:
#
# - tenemos muchos datos;
# - procesamos elementos secuencialmente;
# - no necesitamos almacenarlos todos;
# - queremos producir resultados progresivamente.


# ============================================================
# CONTEXT MANAGERS
# ============================================================


# ------------------------------------------------------------
# 18. RECORDATORIO DE open()
# ------------------------------------------------------------

# Ya hemos trabajado con:
#
#
# with open(...) as archivo:
#     ...
#
#
# Antes lo aprendimos como la forma recomendada
# de trabajar con archivos.
#
#
# Ahora entenderemos mejor qué representa "with".


# ------------------------------------------------------------
# 19. PROBLEMA SIN with
# ------------------------------------------------------------

archivo_manual = open(
    "11_python_intermedio/ejemplo_contexto.txt",
    "w",
    encoding="utf-8"
)


archivo_manual.write(
    "Archivo creado sin with.\n"
)


archivo_manual.close()


# Aquí tuvimos que cerrar manualmente:
#
# archivo_manual.close()


# ------------------------------------------------------------
# 20. MISMO CASO CON with
# ------------------------------------------------------------

with open(
    "11_python_intermedio/ejemplo_contexto.txt",
    "w",
    encoding="utf-8"
) as archivo:

    archivo.write(
        "Archivo administrado con with.\n"
    )


# Al salir del bloque:
#
# with
#
# el archivo se cierra correctamente.
#
#
# No necesitamos escribir:
#
# archivo.close()


# ------------------------------------------------------------
# 21. QUÉ HACE CONCEPTUALMENTE with
# ------------------------------------------------------------

# Podemos imaginar:
#
# adquirir recurso
# ↓
# entrar al bloque
# ↓
# utilizar recurso
# ↓
# salir del bloque
# ↓
# liberar recurso
#
#
# En el caso de archivos:
#
# abrir
# ↓
# leer / escribir
# ↓
# cerrar


# ------------------------------------------------------------
# 22. CONTEXT MANAGER
# ------------------------------------------------------------

# Un objeto preparado para trabajar con:
#
# with
#
# se denomina:
#
# context manager
#
#
# open()
#
# nos entrega un objeto que puede utilizarse
# como context manager.


# ------------------------------------------------------------
# 23. LEER EL ARCHIVO
# ------------------------------------------------------------

with open(
    "11_python_intermedio/ejemplo_contexto.txt",
    "r",
    encoding="utf-8"
) as archivo:

    contenido = archivo.read()


print(contenido)


# Después del bloque:
#
# archivo
#
# ya fue cerrado.


# ------------------------------------------------------------
# 24. COMPROBAR SI FUE CERRADO
# ------------------------------------------------------------

print(
    archivo.closed
)


# Resultado:
#
# True


# ------------------------------------------------------------
# 25. ¿POR QUÉ ES IMPORTANTE?
# ------------------------------------------------------------

# Algunos recursos necesitan liberarse
# correctamente.
#
#
# Ejemplos:
#
# archivos
# conexiones
# bloqueos
# recursos externos
#
#
# "with" ayuda a controlar ese ciclo de vida.


# ------------------------------------------------------------
# 26. MANEJO DE ERRORES
# ------------------------------------------------------------

# Una ventaja importante es que el context manager
# puede encargarse de liberar el recurso aunque
# dentro del bloque ocurra un problema.


archivo_error = None


try:

    with open(
        "11_python_intermedio/ejemplo_contexto.txt",
        "r",
        encoding="utf-8"
    ) as archivo_error:

        contenido = archivo_error.read()

        raise ValueError(
            "Error de ejemplo."
        )


except ValueError as error:
    print(error)


if archivo_error is not None:

    print(
        archivo_error.closed
    )


# Aunque ocurrió una excepción:
#
# el archivo fue cerrado.


# ------------------------------------------------------------
# 27. RELACIÓN CON LO QUE YA SABÍAMOS
# ------------------------------------------------------------

# Antes:
#
# with open(...)
#
# era simplemente una práctica recomendada.
#
#
# Ahora sabemos:
#
# open()
# ↓
# context manager
#
# with
# ↓
# administra entrada y salida del contexto
#
# archivo
# ↓
# recurso utilizado dentro del bloque


# ------------------------------------------------------------
# 28. DETALLE INTERNO: __enter__ Y __exit__
# ------------------------------------------------------------

# Los context managers utilizan internamente
# métodos especiales como:
#
# __enter__()
# __exit__()
#
#
# Por ahora NO necesitamos implementarlos.
#
#
# Basta con comprender:
#
# __enter__
# → prepara/entrega el recurso
#
# __exit__
# → realiza la limpieza al terminar
#
#
# Lo estudiaremos solamente si algún proyecto
# realmente lo necesita.


# ------------------------------------------------------------
# 29. EJEMPLO REAL: PROCESAR LÍNEAS
# ------------------------------------------------------------

with open(
    "11_python_intermedio/ejemplo_contexto.txt",
    "r",
    encoding="utf-8"
) as archivo:

    for linea in archivo:

        print(
            linea.strip()
        )


# Aquí combinamos:
#
# context manager
# +
# iteración
#
#
# No necesitamos hacer:
#
# archivo.readlines()
#
# obligatoriamente.


# ------------------------------------------------------------
# 30. ARCHIVOS TAMBIÉN PUEDEN RECORRERSE
# PROGRESIVAMENTE
# ------------------------------------------------------------

# Esto resulta especialmente útil para archivos grandes.
#
#
# En vez de:
#
# contenido_completo = archivo.read()
#
#
# podemos:
#
# for linea in archivo:
#
#     procesar(linea)
#
#
# Las líneas se procesan progresivamente.


# ------------------------------------------------------------
# 31. GENERADOR PARA PROCESAR DATOS
# ------------------------------------------------------------

def generar_estados():

    estados = [
        "Nuevo",
        "En progreso",
        "Resuelto",
        "Cerrado"
    ]

    for estado in estados:
        yield estado


for estado in generar_estados():

    print(
        f"Procesando estado: {estado}"
    )


# En un proyecto real este patrón podría representar:
#
# obtener registros
# ↓
# procesarlos uno por uno
# ↓
# generar resultados
#
# sin crear colecciones intermedias innecesarias.


# ------------------------------------------------------------
# 32. NO TODO NECESITA UN GENERADOR
# ------------------------------------------------------------

# Si tenemos:
#
# tres elementos
#
# y necesitamos usarlos varias veces:
#
# una lista probablemente sea más sencilla.
#
#
# No debemos sustituir automáticamente
# todas las listas por generadores.


# ------------------------------------------------------------
# 33. NO TODO NECESITA UN CONTEXT MANAGER PROPIO
# ------------------------------------------------------------

# En este nivel debemos principalmente:
#
# reconocerlos
# entender with
# utilizarlos correctamente
#
#
# No necesitamos crear nuestros propios
# context managers todavía.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# GENERADOR:
#
# función que produce valores progresivamente.
#
#
# ------------------------------------------------------------
#
# yield:
#
# entrega un valor
# ↓
# pausa
# ↓
# puede continuar posteriormente
#
#
# ------------------------------------------------------------
#
# return:
#
# entrega un resultado
# ↓
# termina la función
#
#
# ------------------------------------------------------------
#
# next():
#
# solicita el siguiente elemento
# de un generador.
#
#
# Normalmente utilizaremos:
#
# for
#
#
# ------------------------------------------------------------
#
# GENERATOR EXPRESSION:
#
# (
#     expresion
#     for elemento in coleccion
# )
#
#
# ------------------------------------------------------------
#
# GENERADOR:
#
# útil cuando queremos procesar datos
# progresivamente sin almacenarlos todos
# necesariamente en memoria.
#
#
# ------------------------------------------------------------
#
# CONTEXT MANAGER:
#
# administra el ciclo de vida de un recurso.
#
#
# ------------------------------------------------------------
#
# with:
#
# entrar
# ↓
# usar recurso
# ↓
# salir
# ↓
# liberar recurso
#
#
# ------------------------------------------------------------
#
# EJEMPLO PRINCIPAL:
#
# with open(...) as archivo:
#     ...
#
#
# el archivo se cierra al terminar
# el bloque.
#
#
# ------------------------------------------------------------
#
# REGLA PRÁCTICA:
#
# generadores
# → procesamiento progresivo
#
# with
# → recursos que deben administrarse
#   correctamente