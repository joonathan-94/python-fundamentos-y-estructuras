# ============================================================
# SETS EN PYTHON
# ============================================================
#
# Un set (conjunto) es una colección que almacena elementos
# ÚNICOS.
#
# Sus características principales son:
#
# - no permite elementos duplicados;
# - no mantiene posiciones;
# - no soporta índices;
# - no soporta slicing;
# - es mutable;
# - sus elementos deben ser hashables.
#
# Un set es especialmente útil cuando nos importa:
#
# - saber si un elemento existe;
# - eliminar duplicados;
# - comparar grupos de elementos;
# - encontrar elementos comunes;
# - encontrar elementos faltantes;
# - trabajar con permisos, etiquetas, IDs o categorías.
#
# Los sets aparecen con frecuencia en:
#
# - backend;
# - integraciones entre sistemas;
# - validaciones;
# - procesamiento de datos;
# - análisis de datos;
# - automatizaciones.
#
# No debemos pensar en un set como una "lista diferente".
#
# Una lista representa normalmente una SECUENCIA.
# Un set representa normalmente un CONJUNTO de elementos únicos.


# ------------------------------------------------------------
# 1. CREACIÓN DE UN SET
# ------------------------------------------------------------

tipos_pokemon = {
    "Agua",
    "Fuego",
    "Planta"
}

print(tipos_pokemon)
print(type(tipos_pokemon))


# El orden en que se muestran los elementos no debe utilizarse
# como parte de nuestra lógica.
#
# Un set no mantiene posiciones.


# ------------------------------------------------------------
# 2. SET VACÍO
# ------------------------------------------------------------

# Para crear un set vacío debemos utilizar set().

permisos_usuario = set()

print(permisos_usuario)
print(type(permisos_usuario))


# IMPORTANTE:
#
# {}
#
# NO crea un set vacío.
#
# Crea un diccionario vacío.

estructura_vacia = {}

print(type(estructura_vacia))


# ------------------------------------------------------------
# 3. ELEMENTOS ÚNICOS
# ------------------------------------------------------------

# Los sets eliminan automáticamente los valores duplicados.

categorias_importadas = {
    "hardware",
    "software",
    "hardware",
    "redes",
    "software"
}

print(categorias_importadas)


# El resultado contiene únicamente:
#
# hardware
# software
# redes
#
# sin importar cuántas veces aparecían originalmente.


# ------------------------------------------------------------
# 4. ELIMINAR DUPLICADOS DE OTRA COLECCIÓN
# ------------------------------------------------------------

# Uno de los usos más frecuentes de set() consiste en
# eliminar valores repetidos.

etiquetas_importadas = [
    "python",
    "backend",
    "api",
    "python",
    "backend",
    "postgresql"
]

etiquetas_unicas = set(etiquetas_importadas)

print(etiquetas_unicas)


# Esto puede ser útil, por ejemplo, después de:
#
# - importar datos desde un CSV;
# - procesar resultados de una API;
# - recibir identificadores repetidos;
# - limpiar categorías duplicadas.
#
# IMPORTANTE:
#
# Al convertir una lista en set dejamos de trabajar con
# posiciones y orden.
#
# Por eso no debemos utilizar este procedimiento si necesitamos
# conservar el orden original de los elementos.


# ------------------------------------------------------------
# 5. NO EXISTEN ÍNDICES
# ------------------------------------------------------------

modelos_clasicos = {
    "Corvette Stingray",
    "Camaro 1967",
    "Chevrolet Bel Air"
}


# Esto NO es válido:
#
# modelos_clasicos[0]
#
# Los sets no permiten acceder a elementos mediante posiciones.


# Tampoco podemos hacer:
#
# modelos_clasicos[0:2]
#
# porque los sets no soportan slicing.


# ------------------------------------------------------------
# 6. len()
# ------------------------------------------------------------

# len() devuelve la cantidad de elementos únicos.

periodos_dinosaurios = {
    "Triásico",
    "Jurásico",
    "Cretácico"
}

cantidad_periodos = len(periodos_dinosaurios)

print("Cantidad:", cantidad_periodos)


# ------------------------------------------------------------
# 7. in Y not in
# ------------------------------------------------------------

# Una de las grandes utilidades de los sets es comprobar
# pertenencia.

roles_permitidos = {
    "Técnico",
    "Supervisor",
    "Administrador"
}

es_rol_valido = "Supervisor" in roles_permitidos
es_rol_inexistente = "Invitado" in roles_permitidos

print(es_rol_valido)
print(es_rol_inexistente)


# También podemos comprobar ausencia.

sin_rol_auditor = "Auditor" not in roles_permitidos

print(sin_rol_auditor)


# Cuando necesitamos realizar comprobaciones de pertenencia
# repetidamente, un set suele ser una estructura especialmente
# apropiada.


# ------------------------------------------------------------
# 8. add()
# ------------------------------------------------------------

# add() agrega UN elemento al set.

estados_habilitados = {
    "Nuevo",
    "Asignado"
}

estados_habilitados.add("En progreso")

print(estados_habilitados)


# Si intentamos agregar un elemento que ya existe:

estados_habilitados.add("Nuevo")


# no se crea un duplicado.

print(estados_habilitados)


# ------------------------------------------------------------
# 9. update()
# ------------------------------------------------------------

# update() incorpora múltiples elementos provenientes
# de otro iterable.

tecnologias_backend = {
    "Python",
    "Flask"
}

tecnologias_adicionales = [
    "PostgreSQL",
    "Git",
    "Docker"
]

tecnologias_backend.update(tecnologias_adicionales)

print(tecnologias_backend)


# A diferencia de add():
#
# add()
# → agrega un elemento.
#
# update()
# → agrega varios elementos provenientes de un iterable.


# ------------------------------------------------------------
# 10. remove()
# ------------------------------------------------------------

# remove(valor) elimina un elemento.

permisos_tecnico = {
    "ver_ticket",
    "editar_ticket",
    "cerrar_ticket"
}

permisos_tecnico.remove("cerrar_ticket")

print(permisos_tecnico)


# Si intentamos eliminar un valor inexistente:
#
# permisos_tecnico.remove("eliminar_ticket")
#
# Python produce:
#
# KeyError


# ------------------------------------------------------------
# 11. discard()
# ------------------------------------------------------------

# discard() también elimina un elemento.
#
# La diferencia importante es que NO produce KeyError
# si el elemento no existe.

permisos_supervisor = {
    "ver_ticket",
    "editar_ticket",
    "asignar_ticket"
}

permisos_supervisor.discard("eliminar_ticket")

print(permisos_supervisor)


# No ocurrió ningún error aunque "eliminar_ticket"
# no existía.


# ------------------------------------------------------------
# 12. remove() VS discard()
# ------------------------------------------------------------

# remove()
#
# Utilízalo cuando consideras que el elemento DEBERÍA existir.
#
# Si no existe, recibir un KeyError puede revelar un problema
# en nuestros datos o en nuestra lógica.


# discard()
#
# Utilízalo cuando es aceptable que el elemento pueda no existir
# y simplemente queremos asegurarnos de que ya no esté presente.


# No debemos pensar:
#
# "discard() es mejor porque no da error".
#
# La elección depende de qué comportamiento esperamos.


# ------------------------------------------------------------
# 13. pop()
# ------------------------------------------------------------

# pop() elimina y devuelve UN elemento arbitrario.

cola_temporal = {
    "JOB-001",
    "JOB-002",
    "JOB-003"
}

trabajo_extraido = cola_temporal.pop()

print("Extraído:", trabajo_extraido)
print("Restantes:", cola_temporal)


# IMPORTANTE:
#
# No debemos decir que pop() selecciona un elemento "aleatorio".
#
# La documentación habla de un elemento arbitrario.
#
# Tampoco debemos depender de cuál elemento será eliminado.


# ------------------------------------------------------------
# 14. clear()
# ------------------------------------------------------------

# clear() elimina todos los elementos.

cache_ids = {
    "USR-001",
    "USR-002",
    "USR-003"
}

cache_ids.clear()

print(cache_ids)


# Resultado:
#
# set()


# ------------------------------------------------------------
# 15. RECORRER UN SET CON for
# ------------------------------------------------------------

especies_jurassic_park = {
    "Tyrannosaurus rex",
    "Velociraptor",
    "Triceratops"
}

for especie in especies_jurassic_park:
    print(especie)


# Podemos recorrer los elementos normalmente.
#
# Lo que NO debemos hacer es depender del orden de recorrido.


# ============================================================
# OPERACIONES ENTRE CONJUNTOS
# ============================================================
#
# Esta es una de las características más importantes de set.
#
# Podemos comparar colecciones y responder preguntas como:
#
# ¿Qué elementos aparecen en ambos sistemas?
#
# ¿Qué elementos faltan?
#
# ¿Qué elementos existen solo en un sistema?
#
# ¿Qué elementos existen en cualquiera de los dos?
#
# Estas operaciones son especialmente útiles en:
#
# - integraciones;
# - sincronización de sistemas;
# - análisis de permisos;
# - comparación de datos;
# - inventarios;
# - procesamiento de IDs.


# ------------------------------------------------------------
# 16. UNION
# ------------------------------------------------------------

# La unión contiene todos los elementos presentes
# en cualquiera de los dos sets, sin duplicados.

habilidades_backend = {
    "Python",
    "SQL",
    "Git"
}

habilidades_automatizacion = {
    "Python",
    "Git",
    "PowerShell"
}

todas_habilidades = habilidades_backend.union(
    habilidades_automatizacion
)

print(todas_habilidades)


# También existe el operador:

todas_habilidades_operador = (
    habilidades_backend
    | habilidades_automatizacion
)

print(todas_habilidades_operador)


# Los sets originales no son modificados por union().


# ------------------------------------------------------------
# 17. INTERSECTION
# ------------------------------------------------------------

# La intersección devuelve únicamente los elementos
# presentes en AMBOS sets.

herramientas_comunes = habilidades_backend.intersection(
    habilidades_automatizacion
)

print(herramientas_comunes)


# Resultado conceptual:
#
# Python
# Git


# También podemos utilizar:

herramientas_comunes_operador = (
    habilidades_backend
    & habilidades_automatizacion
)

print(herramientas_comunes_operador)


# ------------------------------------------------------------
# 18. DIFFERENCE
# ------------------------------------------------------------

# difference() devuelve los elementos presentes en el primer
# set pero NO presentes en el segundo.

solo_backend = habilidades_backend.difference(
    habilidades_automatizacion
)

print(solo_backend)


# También podemos utilizar:

solo_backend_operador = (
    habilidades_backend
    - habilidades_automatizacion
)

print(solo_backend_operador)


# IMPORTANTE:
#
# La dirección importa.
#
# A - B
#
# no necesariamente produce lo mismo que:
#
# B - A


# ------------------------------------------------------------
# 19. SYMMETRIC DIFFERENCE
# ------------------------------------------------------------

# La diferencia simétrica devuelve los elementos que aparecen
# en uno u otro set, pero NO en ambos.

habilidades_exclusivas = (
    habilidades_backend.symmetric_difference(
        habilidades_automatizacion
    )
)

print(habilidades_exclusivas)


# También podemos utilizar:

habilidades_exclusivas_operador = (
    habilidades_backend
    ^ habilidades_automatizacion
)

print(habilidades_exclusivas_operador)


# ------------------------------------------------------------
# 20. EJEMPLO REAL: COMPARAR DOS SISTEMAS
# ------------------------------------------------------------

# Imaginemos una integración entre un ERP y un WMS.
#
# Ambos sistemas deberían compartir determinados IDs de órdenes.

ordenes_erp = {
    "ORD-1001",
    "ORD-1002",
    "ORD-1003",
    "ORD-1004"
}

ordenes_wms = {
    "ORD-1001",
    "ORD-1003",
    "ORD-1004",
    "ORD-1005"
}


# Órdenes presentes en ambos sistemas.

ordenes_sincronizadas = ordenes_erp & ordenes_wms


# Órdenes presentes en ERP pero ausentes en WMS.

faltantes_en_wms = ordenes_erp - ordenes_wms


# Órdenes presentes en WMS pero ausentes en ERP.

faltantes_en_erp = ordenes_wms - ordenes_erp


print("Sincronizadas:", ordenes_sincronizadas)
print("Faltan en WMS:", faltantes_en_wms)
print("Faltan en ERP:", faltantes_en_erp)


# Este es un caso realista donde un set resulta especialmente
# útil.
#
# No necesitamos posiciones.
#
# Necesitamos comparar IDs y determinar:
#
# - coincidencias;
# - faltantes;
# - diferencias.


# ------------------------------------------------------------
# 21. issubset()
# ------------------------------------------------------------

# issubset() permite comprobar si TODOS los elementos
# de un set están contenidos dentro de otro.

permisos_requeridos = {
    "ver_ticket",
    "editar_ticket"
}

permisos_actuales = {
    "ver_ticket",
    "editar_ticket",
    "asignar_ticket",
    "cerrar_ticket"
}

cumple_permisos = permisos_requeridos.issubset(
    permisos_actuales
)

print(cumple_permisos)


# Podemos interpretarlo como:
#
# ¿Todos los permisos requeridos están dentro de
# los permisos actuales?


# ------------------------------------------------------------
# 22. issuperset()
# ------------------------------------------------------------

# issuperset() realiza la comprobación desde la perspectiva
# contraria.

contiene_requisitos = permisos_actuales.issuperset(
    permisos_requeridos
)

print(contiene_requisitos)


# Aquí preguntamos:
#
# ¿permisos_actuales contiene TODOS los permisos requeridos?


# ------------------------------------------------------------
# 23. isdisjoint()
# ------------------------------------------------------------

# isdisjoint() devuelve True cuando los sets NO comparten
# ningún elemento.

roles_finanzas = {
    "contador",
    "analista_financiero"
}

roles_infraestructura = {
    "administrador_red",
    "administrador_servidores"
}

sin_roles_comunes = roles_finanzas.isdisjoint(
    roles_infraestructura
)

print(sin_roles_comunes)


# True significa que no existe ningún elemento compartido.


# ------------------------------------------------------------
# 24. LOS ELEMENTOS DEBEN SER HASHABLES
# ------------------------------------------------------------

# Los elementos almacenados directamente dentro de un set
# deben ser hashables.
#
# Valores habituales que podemos almacenar:
#
# strings
# números
# tuplas cuyos elementos también sean hashables


identificadores = {
    "USR-001",
    "USR-002",
    "USR-003"
}

coordenadas_egipto = {
    (29.9792, 31.1342),
    (25.7402, 32.6014)
}

print(identificadores)
print(coordenadas_egipto)


# Una lista NO puede ser elemento de un set:
#
# ejemplo_invalido = {
#     ["Pikachu", "Charizard"]
# }
#
# produciría:
#
# TypeError


# Un diccionario tampoco puede almacenarse directamente
# dentro de un set.


# ------------------------------------------------------------
# 25. SET VS LISTA
# ------------------------------------------------------------

# LISTA
#
# Tiene sentido cuando:
#
# - importa el orden;
# - necesitamos posiciones;
# - queremos índices;
# - queremos slicing;
# - permitimos duplicados;
# - queremos representar una secuencia.


cola_tickets = [
    "WD-1001",
    "WD-1002",
    "WD-1003"
]


# En esta situación el orden puede importar:
#
# primero WD-1001,
# después WD-1002,
# después WD-1003.


# SET
#
# Tiene sentido cuando:
#
# - no necesitamos posiciones;
# - queremos elementos únicos;
# - comprobamos pertenencia;
# - queremos comparar grupos;
# - necesitamos encontrar diferencias.


ids_usuarios_activos = {
    "USR-001",
    "USR-002",
    "USR-003"
}


# Aquí lo importante es saber qué usuarios pertenecen
# al conjunto, no cuál ocupa la posición 0.


# ------------------------------------------------------------
# 26. SET VS TUPLA
# ------------------------------------------------------------

# TUPLA
#
# Es una secuencia ordenada e inmutable.
#
# Tiene posiciones y permite índices.

coordenada_piramide = (
    29.9792,
    31.1342
)


# SET
#
# No representa posiciones.
# Representa pertenencia a un conjunto.

sitios_egipcios = {
    "Giza",
    "Luxor",
    "Karnak"
}


# ------------------------------------------------------------
# 27. SET VS DICCIONARIO
# ------------------------------------------------------------

# DICCIONARIO
#
# Relaciona claves con valores.

corvette_1963 = {
    "modelo": "Corvette Stingray",
    "anio": 1963,
    "motor": "V8"
}


# SET
#
# Solamente representa elementos únicos.

autos_coleccion = {
    "Corvette Stingray",
    "Camaro 1967",
    "Chevrolet Bel Air"
}


# Si necesitamos algo como:
#
# "modelo" -> "Corvette Stingray"
# "anio"   -> 1963
#
# necesitamos un diccionario.
#
# Si únicamente necesitamos saber qué modelos pertenecen
# a una colección, un set puede ser más apropiado.


# ------------------------------------------------------------
# 28. TABLA MENTAL PARA ELEGIR COLECCIÓN
# ------------------------------------------------------------
#
# LISTA
# ------------------------------------------------------------
# "Necesito una secuencia que pueda modificar."
#
# Orden:          sí
# Índices:        sí
# Duplicados:     sí
# Mutable:        sí
#
#
# TUPLA
# ------------------------------------------------------------
# "Necesito una secuencia estable."
#
# Orden:          sí
# Índices:        sí
# Duplicados:     sí
# Mutable:        no
#
#
# DICCIONARIO
# ------------------------------------------------------------
# "Necesito relacionar claves con valores."
#
# Clave -> valor
# Mutable:        sí
# Claves únicas:  sí
#
#
# SET
# ------------------------------------------------------------
# "Necesito elementos únicos y trabajar con pertenencia
# o comparación de conjuntos."
#
# Posiciones:     no
# Índices:        no
# Duplicados:     no
# Mutable:        sí


# ------------------------------------------------------------
# 29. FROZENSET - REFERENCIA
# ------------------------------------------------------------

# Python también dispone de frozenset.
#
# Conceptualmente es un conjunto inmutable.

tipos_permitidos = frozenset({
    "hardware",
    "software",
    "redes"
})

print(tipos_permitidos)


# No podemos hacer:
#
# tipos_permitidos.add("seguridad")
#
# porque un frozenset no puede modificarse.
#
# Por ahora basta con saber que existe.
#
# Trabajaremos con él en profundidad solamente si aparece
# una necesidad real durante proyectos futuros.


# ============================================================
# CUÁNDO UTILIZAR UN SET
# ============================================================
#
# Una buena pregunta es:
#
# "¿Me importa la posición de cada elemento?"
#
# Si la respuesta es sí:
# probablemente necesitas una lista o tupla.
#
#
# "¿Necesito asociar un nombre o clave con un valor?"
#
# Si la respuesta es sí:
# probablemente necesitas un diccionario.
#
#
# "¿Lo importante es saber qué elementos existen,
# evitar duplicados o comparar grupos?"
#
# Si la respuesta es sí:
# probablemente un set sea una buena opción.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# Un set:
#
# - contiene elementos únicos;
# - no tiene posiciones;
# - no soporta índices;
# - es mutable;
# - requiere elementos hashables.
#
#
# OPERACIONES FUNDAMENTALES
#
# set(iterable)
# → crear un set / eliminar duplicados.
#
# add()
# → agregar un elemento.
#
# update()
# → agregar múltiples elementos.
#
# remove()
# → eliminar y generar error si no existe.
#
# discard()
# → eliminar sin generar error si no existe.
#
# in
# → comprobar pertenencia.
#
#
# OPERACIONES ENTRE CONJUNTOS
#
# union()
# A | B
# → todos los elementos.
#
# intersection()
# A & B
# → elementos presentes en ambos.
#
# difference()
# A - B
# → elementos de A que no están en B.
#
# symmetric_difference()
# A ^ B
# → elementos exclusivos de A o B.
#
#
# COMPROBACIONES
#
# issubset()
# → comprobar si todos los elementos están contenidos
#   dentro de otro conjunto.
#
# issuperset()
# → comprobar si contiene completamente otro conjunto.
#
# isdisjoint()
# → comprobar si dos conjuntos no tienen elementos en común.
#
#
# CASOS REALES ESPECIALMENTE BUENOS PARA SET
#
# - eliminar duplicados;
# - comparar identificadores entre sistemas;
# - permisos;
# - roles;
# - categorías;
# - etiquetas;
# - detectar registros faltantes;
# - obtener coincidencias;
# - validaciones de pertenencia.