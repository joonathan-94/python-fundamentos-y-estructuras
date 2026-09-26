# ============================================================
# EJERCICIOS - COLECCIONES Y MÉTODOS
# ============================================================
#
# Este archivo contiene ejercicios correspondientes a los temas
# estudiados dentro del módulo de colecciones.
#
# Los ejercicios se agregarán progresivamente a medida que se
# estudien listas, tuplas, diccionarios y sets.

# ============================================================
# LISTAS
# ============================================================


# ------------------------------------------------------------
# LIST-01 - GESTIONAR UNA COLA DE TICKETS
# ------------------------------------------------------------
#
# Tienes:
#
# tickets = ["WD-1001", "WD-1002"]
#
# Realiza lo siguiente:
#
# 1. Agrega "WD-1003" al final utilizando append().
#
# 2. Inserta "WD-URGENTE" al comienzo de la lista
#    utilizando insert().
#
# 3. Extrae el primer ticket utilizando pop(0)
#    y guárdalo en:
#
#    ticket_actual
#
# 4. Imprime ticket_actual.
#
# 5. Imprime la lista final de tickets.
#
# Tu código aquí:

tickets = ["WD-1001", "WD-1002"]

tickets.append("WD-1003")
tickets.insert(0, "WD-URGENTE")

ticket_actual = tickets.pop(0)

print(ticket_actual)
print(tickets)

# ------------------------------------------------------------
# LIST-02 - TRABAJAR CON UN EQUIPO POKÉMON
# ------------------------------------------------------------
#
# Tienes:
#
# equipo = [
#     "Pikachu",
#     "Charizard",
#     "Totodile",
#     "Gengar"
# ]
#
# Realiza lo siguiente:
#
# 1. Obtén el primer Pokémon mediante su índice.
#
# 2. Obtén el último Pokémon utilizando un índice negativo.
#
# 3. Cambia "Charizard" por "Blastoise"
#    modificando directamente la lista.
#
# 4. Comprueba utilizando in si "Gengar"
#    pertenece al equipo.
#
# 5. Imprime:
#
#    - primer Pokémon;
#    - último Pokémon;
#    - lista modificada;
#    - resultado de la comprobación.
#
# Tu código aquí:

equipo = [
    "Pikachu",
    "Charizard",
    "Totodile",
    "Gengar"
]

primer_pokemon = equipo[0]
ultimo_pokemon = equipo[-1]

equipo[1] = "Blastoise"

pertenece_gengar = "Gengar" in equipo

print(primer_pokemon)
print(ultimo_pokemon)
print(equipo)
print(pertenece_gengar)


# ============================================================
# TUPLAS
# ============================================================


# ------------------------------------------------------------
# TUP-01 - DESEMPAQUETAR DATOS DE UN TICKET
# ------------------------------------------------------------
#
# Tienes:
#
# ticket = (
#     "WD-2001",
#     "Alta",
#     "En progreso"
# )
#
# Desempaqueta sus valores en:
#
# id_ticket
# prioridad
# estado
#
# Después imprime las tres variables.
#
# Tu código aquí:

ticket = (
    "WD-2001",
    "Alta",
    "En progreso"
)

id_ticket, prioridad, estado = ticket

print("Id ticket: ",id_ticket)
print("Prioridad", prioridad)
print("Estado", estado)


# ------------------------------------------------------------
# TUP-02 - CONSULTAR UNA TUPLA DE POKÉMON
# ------------------------------------------------------------
#
# Tienes:
#
# equipo = (
#     "Pikachu",
#     "Gengar",
#     "Totodile",
#     "Blaziken"
# )
#
# Realiza lo siguiente:
#
# 1. Obtén el primer Pokémon mediante su índice.
#
# 2. Obtén el último Pokémon utilizando un índice negativo.
#
# 3. Comprueba con in si "Totodile" pertenece a la tupla.
#
# 4. Obtén con index() la posición de "Gengar".
#
# 5. Imprime los cuatro resultados.
#
# Tu código aquí:

equipo = (
    "Pikachu",
    "Gengar",
    "Totodile",
    "Blaziken"
)

primer_pokemon = equipo[0]
print("Primer pokemon: ", primer_pokemon)
ultimo_pokemon = equipo[-1]
print("Ultimo pokemon: ",ultimo_pokemon)
existe_totodile = "Totodile" in equipo
print("¿Existe totodile?", existe_totodile)
indice_gengar = equipo.index("Gengar")
print(indice_gengar)

# ============================================================
# DICCIONARIOS
# ============================================================


# ------------------------------------------------------------
# DICT-01 - ACTUALIZAR DATOS DE UN TICKET
# ------------------------------------------------------------
#
# Tienes:
#
# registro_ticket = {
#     "id": "WD-7001",
#     "titulo": "Error de conexión",
#     "estado": "Nuevo",
#     "tecnico": None
# }
#
# Realiza lo siguiente:
#
# 1. Obtén el título utilizando su clave.
#
# 2. Cambia el estado a "Asignado".
#
# 3. Asigna como técnico a "Misty".
#
# 4. Comprueba con in si existe la clave "prioridad".
#
# 5. Imprime:
#
#    - título;
#    - diccionario actualizado;
#    - resultado de la comprobación.
#
# Tu código aquí:

registro_ticket = {
    "id": "WD-7001",
    "titulo": "Error de conexión",
    "estado": "Nuevo",
    "tecnico": None
}

titulo_ticket = registro_ticket["titulo"]
registro_ticket["estado"] = "Asignado"
registro_ticket["tecnico"] = "Misty"
existe_prioridad = "prioridad" in registro_ticket

print("Titulo ticket: ", titulo_ticket)
print(f"Nuevo estado: {registro_ticket['estado']}")
print(f"Tecnico asignado: {registro_ticket['tecnico']}")
print("¿Existe prioridad?", existe_prioridad)

# ------------------------------------------------------------
# DICT-02 - CONSULTAR DATOS DE UN AUTO CLÁSICO
# ------------------------------------------------------------
#
# Tienes:
#
# ficha_corvette = {
#     "modelo": "Corvette Stingray",
#     "anio": 1963,
#     "motor": "V8"
# }
#
# Realiza lo siguiente:
#
# 1. Utiliza get() para obtener "modelo".
#
# 2. Utiliza get() para intentar obtener la clave "color".
#    Si no existe, debe devolver:
#
#    "Color no registrado"
#
# 3. Recorre el diccionario utilizando items()
#    e imprime cada clave junto con su valor.
#
# 4. Imprime también el modelo y el resultado de buscar color.
#
# Tu código aquí:

ficha_corvette = {
    "modelo": "Corvette Stingray",
    "anio": 1963,
    "motor": "V8"
}

modelo = ficha_corvette.get("modelo")
color = ficha_corvette.get("color", "Color no registrado")

for clave, valor in ficha_corvette.items():
    print(clave, valor)

print(modelo)
print(color)

# ============================================================
# SETS
# ============================================================


# ------------------------------------------------------------
# SET-01 - LIMPIAR CATEGORÍAS IMPORTADAS
# ------------------------------------------------------------
#
# Tienes:
#
# categorias_importadas = [
#     "hardware",
#     "software",
#     "redes",
#     "hardware",
#     "software"
# ]
#
# Realiza lo siguiente:
#
# 1. Convierte la lista en un set para eliminar duplicados.
#
# 2. Agrega "seguridad" utilizando add().
#
# 3. Intenta eliminar "telefonia" utilizando discard().
#
# 4. Comprueba con in si "redes" pertenece al set.
#
# 5. Imprime:
#
#    - el set final;
#    - el resultado de la comprobación.
#
# Tu código aquí:

categorias_importadas = [
    "hardware",
    "software",
    "redes",
    "hardware",
    "software"
]

categorias_unicas = set(categorias_importadas)

print(f"Lista inicial: {categorias_importadas}")
print(f"set inicial convertido: {categorias_unicas}")

categorias_unicas.add("seguridad")
categorias_unicas.discard("telefonia")
existe_redes = "redes" in categorias_unicas

print(f"¿Existe 'redes'?: {existe_redes}")
print(f"set final: {categorias_unicas}")

# ------------------------------------------------------------
# SET-02 - COMPARAR ÓRDENES ENTRE DOS SISTEMAS
# ------------------------------------------------------------
#
# Una integración tiene estos IDs:
#
# ordenes_erp = {
#     "ORD-2001",
#     "ORD-2002",
#     "ORD-2003",
#     "ORD-2004"
# }
#
# ordenes_wms = {
#     "ORD-2001",
#     "ORD-2003",
#     "ORD-2004",
#     "ORD-2005"
# }
#
# Utilizando operaciones de conjuntos:
#
# 1. Obtén las órdenes presentes en ambos sistemas.
#
# 2. Obtén las órdenes presentes en ERP pero
#    que faltan en WMS.
#
# 3. Obtén las órdenes presentes en WMS pero
#    que faltan en ERP.
#
# Guarda los resultados en:
#
# ordenes_coincidentes
# pendientes_en_wms
# pendientes_en_erp
#
# Puedes utilizar:
#
# intersection()
#
# y
#
# difference()
#
# o sus operadores equivalentes.
#
# Imprime los tres resultados.
#
# Tu código aquí:

ordenes_erp = {
    "ORD-2001",
    "ORD-2002",
    "ORD-2003",
    "ORD-2004"
}

ordenes_wms = {
    "ORD-2001",
    "ORD-2003",
    "ORD-2004",
    "ORD-2005"
}

ordenes_coincidentes = ordenes_erp.intersection(ordenes_wms)
pendientes_en_wms = ordenes_erp.difference(ordenes_wms)
pendientes_en_erp = ordenes_wms.difference(ordenes_erp)

print(ordenes_coincidentes)
print(pendientes_en_wms)
print(pendientes_en_erp)