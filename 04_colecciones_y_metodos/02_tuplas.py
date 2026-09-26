# ============================================================
# TUPLAS EN PYTHON
# ============================================================
#
# Una tupla (tuple) es una secuencia ordenada e inmutable.
#
# "Ordenada" significa que sus elementos mantienen una posición.
#
# "Inmutable" significa que, después de crear una tupla,
# no podemos:
#
# - cambiar directamente sus elementos;
# - agregar elementos;
# - eliminar elementos.
#
# Las tuplas permiten:
#
# - elementos duplicados;
# - índices;
# - índices negativos;
# - slicing;
# - recorridos con for;
# - desempaquetado.
#
# Son útiles cuando queremos representar un conjunto de valores
# cuya estructura no debería modificarse accidentalmente.


# ------------------------------------------------------------
# 1. CREACIÓN DE TUPLAS
# ------------------------------------------------------------

pokemon_iniciales = (
    "Bulbasaur",
    "Charmander",
    "Squirtle"
)

print(pokemon_iniciales)
print(type(pokemon_iniciales))


# También podemos crear una tupla vacía.

tupla_vacia = ()

print(tupla_vacia)


# ------------------------------------------------------------
# 2. LA COMA ES IMPORTANTE
# ------------------------------------------------------------

# Esta expresión NO crea una tupla:

valor = ("Pikachu")

print(valor)
print(type(valor))


# Resultado:
#
# str


# Para crear una tupla con UN solo elemento
# debemos incluir una coma:

pokemon_unico = ("Pikachu",)

print(pokemon_unico)
print(type(pokemon_unico))


# Resultado:
#
# tuple


# Técnicamente, es la coma la que forma la tupla.
#
# Por ejemplo, esto también es una tupla:

coordenadas = 10, 20

print(coordenadas)
print(type(coordenadas))


# Sin embargo, normalmente utilizaremos paréntesis porque
# mejoran la legibilidad.


# ------------------------------------------------------------
# 3. ACCESO MEDIANTE ÍNDICES
# ------------------------------------------------------------

estados_ticket = (
    "Nuevo",
    "Asignado",
    "En progreso",
    "Cerrado"
)

print(estados_ticket[0])   # Nuevo
print(estados_ticket[2])   # En progreso


# También podemos utilizar índices negativos.

print(estados_ticket[-1])  # Cerrado
print(estados_ticket[-2])  # En progreso


# ------------------------------------------------------------
# 4. LONGITUD
# ------------------------------------------------------------

prioridades = (
    "Baja",
    "Media",
    "Alta",
    "Crítica"
)

cantidad_prioridades = len(prioridades)

print("Cantidad:", cantidad_prioridades)


# ------------------------------------------------------------
# 5. SLICING
# ------------------------------------------------------------

generaciones = (
    "Kanto",
    "Johto",
    "Hoenn",
    "Sinnoh"
)

primeras_tres = generaciones[:3]

print(primeras_tres)


# Resultado:
#
# ("Kanto", "Johto", "Hoenn")


# El slicing de una tupla produce otra tupla.


# ------------------------------------------------------------
# 6. INMUTABILIDAD
# ------------------------------------------------------------

estados = (
    "Nuevo",
    "Asignado",
    "Cerrado"
)


# Esto NO es válido:
#
# estados[1] = "En progreso"
#
# Python produciría:
#
# TypeError


# Tampoco existen métodos como:
#
# estados.append(...)
# estados.remove(...)
#
# porque esos métodos modificarían la estructura.


# La inmutabilidad es una diferencia fundamental
# respecto de las listas.


# ------------------------------------------------------------
# 7. in Y not in
# ------------------------------------------------------------

tipos_pokemon = (
    "Agua",
    "Fuego",
    "Planta"
)

tiene_fuego = "Fuego" in tipos_pokemon
no_tiene_electrico = "Eléctrico" not in tipos_pokemon

print(tiene_fuego)
print(no_tiene_electrico)


# ------------------------------------------------------------
# 8. count()
# ------------------------------------------------------------

codigos_http = (
    200,
    404,
    200,
    500,
    200,
    404
)

cantidad_200 = codigos_http.count(200)

print("Código 200:", cantidad_200)


# count() devuelve cuántas veces aparece un valor.


# ------------------------------------------------------------
# 9. index()
# ------------------------------------------------------------

prioridades = (
    "Baja",
    "Media",
    "Alta",
    "Crítica"
)

posicion_alta = prioridades.index("Alta")

print("Índice de Alta:", posicion_alta)


# index() devuelve la posición de la PRIMERA aparición.
#
# Si el valor no existe:
#
# prioridades.index("Urgente")
#
# Python produciría:
#
# ValueError


# ------------------------------------------------------------
# 10. RECORRER UNA TUPLA
# ------------------------------------------------------------

regiones = (
    "Kanto",
    "Johto",
    "Hoenn"
)

for region in regiones:
    print(region)


# Al igual que otras secuencias, una tupla puede recorrerse
# utilizando for.


# ------------------------------------------------------------
# 11. EMPAQUETADO
# ------------------------------------------------------------

# Python puede agrupar varios valores dentro de una tupla.

datos_ticket = (
    "WD-1001",
    "Alta",
    "En progreso"
)

print(datos_ticket)


# También podríamos escribir:

datos_ticket = "WD-1001", "Alta", "En progreso"

print(datos_ticket)


# Esto se conoce como tuple packing o empaquetado.


# ------------------------------------------------------------
# 12. DESEMPAQUETADO
# ------------------------------------------------------------

# Podemos extraer los elementos de una tupla
# asignándolos a varias variables.

datos_ticket = (
    "WD-1001",
    "Alta",
    "En progreso"
)

id_ticket, prioridad, estado = datos_ticket

print(id_ticket)
print(prioridad)
print(estado)


# Debe existir la cantidad adecuada de variables
# para los elementos de la tupla.


# También podemos utilizar ejemplos de otros dominios:

pokemon = (
    "Totodile",
    "Agua",
    2
)

nombre, tipo, generacion = pokemon

print(nombre)
print(tipo)
print(generacion)


# ------------------------------------------------------------
# 13. INTERCAMBIO DE VALORES
# ------------------------------------------------------------

# El intercambio que ya estudiamos en variables:

principal = "Walter White"
secundario = "Jesse Pinkman"

principal, secundario = secundario, principal

print(principal)
print(secundario)


# Internamente esta sintaxis está relacionada con
# empaquetado y desempaquetado.


# ------------------------------------------------------------
# 14. CONVERSIÓN ENTRE LISTA Y TUPLA
# ------------------------------------------------------------

# list() puede crear una lista desde una tupla.

estados_tupla = (
    "Nuevo",
    "Asignado",
    "Cerrado"
)

estados_lista = list(estados_tupla)

print(estados_lista)


# tuple() puede crear una tupla desde otro iterable.

estados_nuevamente_tupla = tuple(estados_lista)

print(estados_nuevamente_tupla)


# IMPORTANTE:
#
# Convertir una tupla en lista y modificar esa lista
# NO modifica la tupla original.
#
# Estamos creando objetos nuevos.


# ------------------------------------------------------------
# 15. UNA TUPLA PUEDE CONTENER OBJETOS MUTABLES
# ------------------------------------------------------------

# La tupla misma es inmutable, pero sus elementos pueden
# ser objetos mutables.

datos = (
    "WD-1001",
    ["Neo", "Morpheus"]
)


# No podemos reemplazar directamente:

# datos[1] = ["Trinity"]


# Pero la lista interna sí es mutable:

datos[1].append("Trinity")

print(datos)


# Esto demuestra una precisión importante:
#
# inmutable significa que no podemos cambiar qué objetos
# ocupan directamente las posiciones de la tupla.
#
# No significa necesariamente que todo objeto contenido
# dentro de ella sea inmutable.


# ------------------------------------------------------------
# 16. LISTA VS TUPLA
# ------------------------------------------------------------

# En términos generales:
#
# LISTA
# ------------------------------------------------------------
# Utilízala cuando la colección debe cambiar.
#
# Ejemplos:
#
# - tickets pendientes;
# - usuarios encontrados;
# - resultados que se agregan o eliminan;
# - equipo Pokémon que puede modificarse.


# TUPLA
# ------------------------------------------------------------
# Utilízala cuando una secuencia de valores debe permanecer
# estructuralmente estable.
#
# Ejemplos:
#
# - coordenadas;
# - datos agrupados que no deberían alterarse;
# - conjuntos pequeños de configuración estable;
# - resultados que conceptualmente forman una unidad fija.


# No debemos elegir una tupla únicamente pensando:
#
# "es más profesional"
#
# o:
#
# "es más rápida".
#
# La elección principal debe depender del significado
# y del comportamiento esperado de los datos.


# ------------------------------------------------------------
# 17. EJEMPLO PRÁCTICO: RESUMEN INMUTABLE DE UN TICKET
# ------------------------------------------------------------

resumen_ticket = (
    "WD-1050",
    "Problema de conexión",
    "Alta",
    "En progreso"
)


id_ticket, titulo, prioridad, estado = resumen_ticket


print("ID:", id_ticket)
print("Título:", titulo)
print("Prioridad:", prioridad)
print("Estado:", estado)


# En este ejemplo utilizamos una tupla porque queremos
# representar un grupo fijo de cuatro valores.
#
# En una aplicación real, para representar tickets completos
# normalmente utilizaremos estructuras más expresivas,
# como diccionarios, objetos o modelos de base de datos.
#
# La tupla aquí se utiliza únicamente para comprender
# correctamente el concepto.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# Una tupla:
#
# - es una secuencia;
# - mantiene el orden;
# - es inmutable;
# - permite duplicados;
# - permite índices;
# - permite slicing;
# - puede recorrerse con for.
#
# Métodos principales:
#
# count()
# index()
#
# Conceptos especialmente importantes:
#
# empaquetado
# desempaquetado
# tupla de un elemento -> ("valor",)
#
# LISTA:
# colección que normalmente queremos modificar.
#
# TUPLA:
# secuencia cuya estructura queremos mantener estable.