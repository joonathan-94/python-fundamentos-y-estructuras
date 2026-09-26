# ============================================================
# LISTAS EN PYTHON
# ============================================================
#
# Una lista (list) es una colección ordenada y mutable.
#
# "Ordenada" significa que los elementos mantienen una posición.
#
# "Mutable" significa que podemos modificar la lista después
# de haberla creado:
#
# - cambiar elementos;
# - agregar elementos;
# - eliminar elementos;
# - ordenar elementos.
#
# Las listas permiten valores duplicados.
#
# Son una de las estructuras de datos más utilizadas en Python.
#
# Algunos usos habituales:
#
# - lista de tickets;
# - usuarios;
# - productos;
# - resultados de una consulta;
# - nombres;
# - estados;
# - registros que deben procesarse;
# - elementos obtenidos desde una API.
#
# Sintaxis básica:
#
# lista = [elemento_1, elemento_2, elemento_3]


# ------------------------------------------------------------
# 1. CREACIÓN DE LISTAS
# ------------------------------------------------------------

pokemon = ["Pikachu", "Charizard", "Totodile"]

print(pokemon)
print(type(pokemon))


# También podemos crear una lista vacía.

tickets_pendientes = []

print(tickets_pendientes)


# Una lista puede contener elementos duplicados.

prioridades = ["Alta", "Media", "Alta", "Baja"]

print(prioridades)


# ------------------------------------------------------------
# 2. ACCESO MEDIANTE ÍNDICES
# ------------------------------------------------------------

# Al igual que los strings, las listas utilizan índices
# comenzando desde 0.

equipo = ["Pikachu", "Charizard", "Blastoise"]

#          0          1            2

print(equipo[0])  # Pikachu
print(equipo[1])  # Charizard
print(equipo[2])  # Blastoise


# También podemos utilizar índices negativos.

print(equipo[-1])  # Blastoise
print(equipo[-2])  # Charizard


# Si intentamos acceder a una posición inexistente:
#
# equipo[10]
#
# Python produciría:
#
# IndexError


# ------------------------------------------------------------
# 3. LONGITUD DE UNA LISTA
# ------------------------------------------------------------

# len() devuelve la cantidad de elementos.

tickets = ["WD-1001", "WD-1002", "WD-1003"]

cantidad_tickets = len(tickets)

print("Cantidad de tickets:", cantidad_tickets)


# ------------------------------------------------------------
# 4. SLICING
# ------------------------------------------------------------

# Podemos obtener una parte de una lista utilizando slicing.
#
# Sintaxis:
#
# lista[inicio:fin]
#
# El índice inicial se incluye.
# El índice final no se incluye.

pokemon = [
    "Bulbasaur",
    "Charmander",
    "Squirtle",
    "Chikorita",
    "Cyndaquil",
    "Totodile"
]

primera_generacion_iniciales = pokemon[0:3]

print(primera_generacion_iniciales)


# También podemos omitir límites.

print(pokemon[:3])
print(pokemon[3:])


# El slicing produce una nueva lista con los elementos
# seleccionados.


# ------------------------------------------------------------
# 5. MUTABILIDAD
# ------------------------------------------------------------

# A diferencia de los strings y las tuplas, una lista
# puede modificarse.

estados_ticket = [
    "Nuevo",
    "Asignado",
    "Cerrado"
]

print("Antes:", estados_ticket)


# Cambiamos el elemento ubicado en el índice 1.

estados_ticket[1] = "En progreso"

print("Después:", estados_ticket)


# La lista original fue modificada.


# ------------------------------------------------------------
# 6. OPERADORES in Y not in
# ------------------------------------------------------------

# in comprueba si un elemento está presente.

equipo = ["Pikachu", "Gengar", "Lapras"]

tiene_gengar = "Gengar" in equipo

print("¿Gengar está en el equipo?:", tiene_gengar)


# not in comprueba que un elemento no esté presente.

tiene_mewtwo = "Mewtwo" in equipo
no_tiene_mewtwo = "Mewtwo" not in equipo

print(tiene_mewtwo)
print(no_tiene_mewtwo)


# ------------------------------------------------------------
# 7. append()
# ------------------------------------------------------------

# append() agrega UN elemento al final de la lista.

tickets = ["WD-1001", "WD-1002"]

tickets.append("WD-1003")

print(tickets)


# Resultado:
#
# ["WD-1001", "WD-1002", "WD-1003"]


# ------------------------------------------------------------
# 8. insert()
# ------------------------------------------------------------

# insert(indice, elemento) agrega un elemento en una
# posición determinada.

tickets = ["WD-1001", "WD-1003"]

tickets.insert(1, "WD-1002")

print(tickets)


# El elemento que estaba en esa posición y los posteriores
# se desplazan hacia la derecha.


# ------------------------------------------------------------
# 9. extend()
# ------------------------------------------------------------

# extend() agrega a una lista todos los elementos provenientes
# de otro iterable.

equipo_kanto = ["Pikachu", "Charizard"]

nuevos_pokemon = ["Blastoise", "Venusaur"]

equipo_kanto.extend(nuevos_pokemon)

print(equipo_kanto)


# Resultado:
#
# ["Pikachu", "Charizard", "Blastoise", "Venusaur"]


# ------------------------------------------------------------
# 10. append() VS extend()
# ------------------------------------------------------------

# Esta diferencia es importante.


lista_1 = ["Pikachu", "Charizard"]

lista_1.append(["Totodile", "Cyndaquil"])

print(lista_1)


# append() agrega la lista completa como UN elemento:
#
# [
#     "Pikachu",
#     "Charizard",
#     ["Totodile", "Cyndaquil"]
# ]


lista_2 = ["Pikachu", "Charizard"]

lista_2.extend(["Totodile", "Cyndaquil"])

print(lista_2)


# extend() agrega individualmente los elementos:
#
# [
#     "Pikachu",
#     "Charizard",
#     "Totodile",
#     "Cyndaquil"
# ]


# ------------------------------------------------------------
# 11. remove()
# ------------------------------------------------------------

# remove(valor) elimina la PRIMERA aparición
# de un determinado valor.

estados = [
    "Nuevo",
    "Asignado",
    "Cancelado",
    "En progreso"
]

estados.remove("Cancelado")

print(estados)


# Si intentamos eliminar un elemento que no existe:
#
# estados.remove("Reabierto")
#
# Python produciría:
#
# ValueError


# ------------------------------------------------------------
# 12. pop()
# ------------------------------------------------------------

# pop() elimina un elemento Y devuelve el valor eliminado.
#
# Sin indicar índice, elimina el último elemento.

cola_tickets = [
    "WD-1001",
    "WD-1002",
    "WD-1003"
]

ticket_extraido = cola_tickets.pop()

print("Ticket extraído:", ticket_extraido)
print("Cola restante:", cola_tickets)


# También podemos especificar un índice.

ticket_extraido = cola_tickets.pop(0)

print("Ticket extraído:", ticket_extraido)
print("Cola restante:", cola_tickets)


# ------------------------------------------------------------
# 13. clear()
# ------------------------------------------------------------

# clear() elimina todos los elementos de una lista.

datos_temporales = [
    "registro_1",
    "registro_2",
    "registro_3"
]

datos_temporales.clear()

print(datos_temporales)


# Resultado:
#
# []


# ------------------------------------------------------------
# 14. count()
# ------------------------------------------------------------

# count(valor) devuelve cuántas veces aparece un elemento.

prioridades = [
    "Alta",
    "Media",
    "Alta",
    "Baja",
    "Alta"
]

cantidad_altas = prioridades.count("Alta")

print("Prioridades altas:", cantidad_altas)


# ------------------------------------------------------------
# 15. index()
# ------------------------------------------------------------

# index(valor) devuelve el índice de la PRIMERA aparición
# del elemento.

pokemon = [
    "Pikachu",
    "Gengar",
    "Lapras",
    "Gengar"
]

posicion_gengar = pokemon.index("Gengar")

print("Primer Gengar:", posicion_gengar)


# Si el valor no existe:
#
# pokemon.index("Mew")
#
# produce:
#
# ValueError


# ------------------------------------------------------------
# 16. sort()
# ------------------------------------------------------------

# sort() ordena la lista original.
#
# La modificación ocurre "in place":
# no crea otra lista con el resultado.

tiempos_resolucion = [45, 12, 80, 30, 20]

tiempos_resolucion.sort()

print(tiempos_resolucion)


# Resultado:
#
# [12, 20, 30, 45, 80]


# Para ordenar en sentido descendente:

tiempos_resolucion.sort(reverse=True)

print(tiempos_resolucion)


# IMPORTANTE:
#
# sort() modifica la lista original.
#
# No debemos hacer:
#
# resultado = tiempos_resolucion.sort()
#
# esperando obtener una nueva lista.
#
# sort() devuelve None.


# ------------------------------------------------------------
# 17. sorted()
# ------------------------------------------------------------

# sorted() es una función incorporada de Python.
#
# A diferencia de list.sort(), sorted() devuelve
# una NUEVA lista ordenada.

tiempos_originales = [45, 12, 80, 30]

tiempos_ordenados = sorted(tiempos_originales)

print("Original:", tiempos_originales)
print("Ordenados:", tiempos_ordenados)


# La lista original permanece sin cambios.


# ------------------------------------------------------------
# 18. reverse()
# ------------------------------------------------------------

# reverse() invierte el orden ACTUAL de la lista.
#
# No significa "ordenar de mayor a menor".

pokemon = [
    "Bulbasaur",
    "Charmander",
    "Squirtle"
]

pokemon.reverse()

print(pokemon)


# Resultado:
#
# ["Squirtle", "Charmander", "Bulbasaur"]


# ------------------------------------------------------------
# 19. RECORRER UNA LISTA CON for
# ------------------------------------------------------------

# Una de las operaciones más frecuentes sobre una lista
# consiste en recorrer sus elementos.

tickets = [
    "WD-1001",
    "WD-1002",
    "WD-1003"
]

for ticket in tickets:
    print("Procesando:", ticket)


# En cada iteración, la variable ticket referencia
# uno de los elementos de la lista.


# ------------------------------------------------------------
# 20. enumerate()
# ------------------------------------------------------------

# Cuando necesitamos tanto el elemento como su posición,
# podemos utilizar enumerate().

pokemon = [
    "Pikachu",
    "Charizard",
    "Blastoise"
]

for indice, nombre in enumerate(pokemon):
    print(indice, nombre)


# Resultado aproximado:
#
# 0 Pikachu
# 1 Charizard
# 2 Blastoise


# ------------------------------------------------------------
# 21. ASIGNACIÓN Y REFERENCIAS
# ------------------------------------------------------------

# Esta parte es importante.
#
# Si hacemos:

lista_original = ["Pikachu", "Gengar"]

otra_lista = lista_original


# NO estamos creando automáticamente una lista independiente.
#
# Ambos nombres hacen referencia a la misma lista.

otra_lista.append("Lapras")

print("Original:", lista_original)
print("Otra:", otra_lista)


# Ambas mostrarán Lapras.


# ------------------------------------------------------------
# 22. copy()
# ------------------------------------------------------------

# copy() crea una copia superficial de la lista.

lista_original = [
    "Pikachu",
    "Gengar",
    "Lapras"
]

lista_copia = lista_original.copy()

lista_copia.append("Charizard")

print("Original:", lista_original)
print("Copia:", lista_copia)


# Ahora agregar Charizard a lista_copia no modifica
# directamente lista_original.


# IMPORTANTE:
#
# copy() crea una copia SUPERFICIAL.
#
# Si la lista contiene objetos mutables dentro de ella,
# esos objetos internos pueden seguir estando compartidos.
#
# Profundizaremos en este concepto cuando sea necesario.


# ------------------------------------------------------------
# 23. EJEMPLO PRÁCTICO: COLA SIMPLE DE TICKETS
# ------------------------------------------------------------

tickets_pendientes = [
    "WD-1001",
    "WD-1002"
]


# Llega un nuevo ticket.

tickets_pendientes.append("WD-1003")


# Un ticket urgente debe quedar al comienzo.

tickets_pendientes.insert(0, "WD-URGENTE")


# Comprobamos si un ticket está en la cola.

existe_ticket = "WD-1002" in tickets_pendientes


# Obtenemos el primer ticket para procesarlo.

ticket_actual = tickets_pendientes.pop(0)


print("Ticket actual:", ticket_actual)
print("Tickets pendientes:", tickets_pendientes)
print("¿WD-1002 existe?:", existe_ticket)


# Este es un ejemplo sencillo.
#
# En una aplicación real podrían utilizarse otras estructuras
# dependiendo de los requisitos y del volumen de información.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# Una lista:
#
# - mantiene el orden de sus elementos;
# - es mutable;
# - permite elementos duplicados;
# - utiliza índices;
# - permite slicing;
# - puede recorrerse con for.
#
# Operaciones especialmente importantes:
#
# append()
# → agrega un elemento al final.
#
# extend()
# → agrega varios elementos provenientes de otro iterable.
#
# remove()
# → elimina por valor.
#
# pop()
# → elimina por posición y devuelve el elemento.
#
# sort()
# → ordena la lista original.
#
# sorted()
# → devuelve una nueva lista ordenada.
#
# copy()
# → crea una copia superficial.
#
# in
# → permite comprobar pertenencia.
#
# Estas operaciones serán utilizadas constantemente cuando
# trabajemos con datos y aplicaciones reales.