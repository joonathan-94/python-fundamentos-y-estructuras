# ============================================================
# COLAS DE PRIORIDAD
# ============================================================
#
# En el archivo anterior estudiamos una cola FIFO:
#
# primero en entrar
# ↓
# primero en salir
#
#
# Pero existen problemas donde el orden de llegada
# no es suficiente.
#
#
# Ejemplo:
#
# TK-001 → prioridad Baja
# TK-002 → prioridad Crítica
# TK-003 → prioridad Media
#
#
# Aunque TK-001 llegó primero, puede ser necesario
# atender TK-002 antes.
#
#
# Para esos casos podemos utilizar una:
#
# COLA DE PRIORIDAD


# ============================================================
# 1. COLA NORMAL VS COLA DE PRIORIDAD
# ============================================================

# COLA NORMAL:
#
# A
# B
# C
#
# salida:
#
# A
# B
# C
#
#
# COLA DE PRIORIDAD:
#
# cada elemento tiene además un nivel de prioridad.
#
#
# Ejemplo:
#
# A → prioridad 3
# B → prioridad 1
# C → prioridad 2
#
#
# salida:
#
# B
# C
# A


# ============================================================
# 2. REPRESENTAR LAS PRIORIDADES
# ============================================================

# Utilizaremos números.
#
# En nuestros ejemplos:
#
# 1 → Crítica
# 2 → Alta
# 3 → Media
# 4 → Baja
#
#
# IMPORTANTE:
#
# cuanto MENOR sea el número,
# MAYOR será la prioridad.
#
#
# Esto será útil porque heapq trabaja por defecto
# colocando primero el valor más pequeño.


PRIORIDAD_CRITICA = 1
PRIORIDAD_ALTA = 2
PRIORIDAD_MEDIA = 3
PRIORIDAD_BAJA = 4


# ============================================================
# 3. heapq
# ============================================================

import heapq


# heapq permite trabajar con una estructura llamada:
#
# heap
#
# o montículo.
#
#
# Para nuestro nivel basta con comprender:
#
# heapq
# ↓
# permite agregar elementos
# y retirar eficientemente
# el elemento con menor valor.
#
#
# En nuestro caso:
#
# menor número
# ↓
# mayor prioridad


# ============================================================
# 4. CREAR UNA COLA DE PRIORIDAD
# ============================================================

cola_prioridad = []


# heapq trabaja sobre una list.
#
# No existe una clase especial:
#
# PriorityQueue
#
# cuando utilizamos directamente heapq.
#
#
# Utilizamos una lista normal y las funciones
# de heapq se encargan de mantener la propiedad del heap.


# ============================================================
# 5. AGREGAR ELEMENTOS CON heappush()
# ============================================================

heapq.heappush(
    cola_prioridad,
    (
        PRIORIDAD_MEDIA,
        "TK-001"
    )
)


heapq.heappush(
    cola_prioridad,
    (
        PRIORIDAD_CRITICA,
        "TK-002"
    )
)


heapq.heappush(
    cola_prioridad,
    (
        PRIORIDAD_ALTA,
        "TK-003"
    )
)


print(
    cola_prioridad
)


# Estamos guardando tuplas:
#
# (
#     prioridad,
#     ticket
# )
#
#
# Por ejemplo:
#
# (
#     1,
#     "TK-002"
# )
#
#
# Python compara primero:
#
# prioridad


# ============================================================
# 6. RETIRAR EL ELEMENTO PRIORITARIO
# ============================================================

ticket_prioritario = heapq.heappop(
    cola_prioridad
)


print(
    "Primer elemento:",
    ticket_prioritario
)


# El resultado será:
#
# (1, "TK-002")
#
#
# aunque TK-002 fue agregado después de TK-001.
#
#
# La prioridad modificó el orden de atención.


# ============================================================
# 7. DESEMPAQUETAR EL RESULTADO
# ============================================================

prioridad, codigo = heapq.heappop(
    cola_prioridad
)


print(
    "Prioridad:",
    prioridad
)


print(
    "Ticket:",
    codigo
)


# Aquí reutilizamos algo que ya estudiamos:
#
# desempaquetado de tuplas.
#
#
# (
#     2,
#     "TK-003"
# )
#
# ↓
#
# prioridad = 2
# codigo = "TK-003"


# ============================================================
# 8. ORDEN REAL DE ATENCIÓN
# ============================================================

cola_ejemplo = []


heapq.heappush(
    cola_ejemplo,
    (4, "TK-1001")
)

heapq.heappush(
    cola_ejemplo,
    (1, "TK-1002")
)

heapq.heappush(
    cola_ejemplo,
    (3, "TK-1003")
)

heapq.heappush(
    cola_ejemplo,
    (2, "TK-1004")
)


while cola_ejemplo:

    prioridad, ticket = heapq.heappop(
        cola_ejemplo
    )

    print(
        prioridad,
        ticket
    )


# Salida:
#
# 1 TK-1002
# 2 TK-1004
# 3 TK-1003
# 4 TK-1001


# ============================================================
# 9. heappush()
# ============================================================

# heappush():
#
# agrega un elemento manteniendo
# la estructura del heap.
#
#
# Ejemplo:
#
# heapq.heappush(
#     cola,
#     (prioridad, elemento)
# )


# ============================================================
# 10. heappop()
# ============================================================

# heappop():
#
# retira el elemento que debe salir primero.
#
#
# En un min-heap:
#
# será el elemento con menor valor.


# ============================================================
# 11. CONSULTAR SIN RETIRAR
# ============================================================

cola_consulta = []


heapq.heappush(
    cola_consulta,
    (3, "TK-2001")
)

heapq.heappush(
    cola_consulta,
    (1, "TK-2002")
)

heapq.heappush(
    cola_consulta,
    (2, "TK-2003")
)


siguiente = cola_consulta[0]


print(
    "Siguiente:",
    siguiente
)


# Igual que vimos anteriormente:
#
# [0]
#
# permite consultar el elemento que está primero
# sin retirarlo.
#
#
# heappop()
#
# lo consulta Y lo retira.


# ============================================================
# 12. IMPORTANTE: EL HEAP NO ES UNA LISTA ORDENADA
# ============================================================

# Este concepto es importante.
#
# Si imprimimos directamente:
#
# cola_consulta
#
# no debemos asumir que toda la lista
# aparecerá visualmente ordenada.
#
#
# heapq garantiza principalmente que:
#
# cola_consulta[0]
#
# contiene el elemento mínimo.
#
#
# Y que:
#
# heappop()
#
# irá entregando los elementos
# respetando el orden del heap.


print(
    cola_consulta
)


# No debemos utilizar la representación interna
# del heap como si fuera una lista completamente ordenada.


# ============================================================
# 13. EJEMPLO MÁS REALISTA
# ============================================================

cola_tickets = []


heapq.heappush(
    cola_tickets,
    (
        PRIORIDAD_BAJA,
        "TK-3001",
        "Cambio de fondo de pantalla"
    )
)


heapq.heappush(
    cola_tickets,
    (
        PRIORIDAD_CRITICA,
        "TK-3002",
        "Servidor principal sin conexión"
    )
)


heapq.heappush(
    cola_tickets,
    (
        PRIORIDAD_ALTA,
        "TK-3003",
        "Usuario sin acceso"
    )
)


while cola_tickets:

    prioridad, codigo, titulo = (
        heapq.heappop(
            cola_tickets
        )
    )

    print(
        codigo,
        "-",
        titulo,
        "- prioridad:",
        prioridad
    )


# Orden esperado:
#
# TK-3002
# ↓
# prioridad Crítica
#
# TK-3003
# ↓
# prioridad Alta
#
# TK-3001
# ↓
# prioridad Baja


# ============================================================
# 14. TRADUCIR NÚMERO A TEXTO
# ============================================================

nombres_prioridad = {
    1: "Crítica",
    2: "Alta",
    3: "Media",
    4: "Baja"
}


cola_traducida = []


heapq.heappush(
    cola_traducida,
    (
        2,
        "TK-4001"
    )
)


prioridad, ticket = (
    heapq.heappop(
        cola_traducida
    )
)


print(
    ticket,
    nombres_prioridad[prioridad]
)


# Aquí combinamos:
#
# heap
# +
# tupla
# +
# diccionario


# ============================================================
# 15. ¿QUÉ OCURRE SI DOS ELEMENTOS TIENEN
# LA MISMA PRIORIDAD?
# ============================================================

# Las tuplas se comparan de izquierda a derecha.
#
#
# Ejemplo:
#
# (1, "TK-001")
# (1, "TK-002")
#
#
# Como ambas tienen prioridad 1,
# Python compara el siguiente elemento:
#
# "TK-001"
# "TK-002"
#
#
# En ejemplos sencillos esto puede ser suficiente.
#
# En sistemas reales normalmente puede existir además
# un criterio secundario, como:
#
# - orden de llegada;
# - fecha de creación;
# - identificador incremental.
#
#
# Veremos estas decisiones cuando trabajemos
# con problemas reales.
#
# Por ahora no necesitamos complicar la estructura.


# ============================================================
# 16. EJEMPLO CON ORDEN DE LLEGADA
# ============================================================

# Conceptualmente podríamos guardar:
#
# (
#     prioridad,
#     orden_llegada,
#     ticket
# )
#
#
# Ejemplo:
#
# (
#     1,
#     1,
#     "TK-001"
# )
#
# (
#     1,
#     2,
#     "TK-002"
# )
#
#
# Primero se compara:
#
# prioridad
#
# y si empatan:
#
# orden_llegada


cola_con_orden = []


heapq.heappush(
    cola_con_orden,
    (
        1,
        2,
        "TK-5002"
    )
)


heapq.heappush(
    cola_con_orden,
    (
        1,
        1,
        "TK-5001"
    )
)


while cola_con_orden:

    prioridad, orden, ticket = (
        heapq.heappop(
            cola_con_orden
        )
    )

    print(
        prioridad,
        orden,
        ticket
    )


# Aunque ambos son críticos:
#
# TK-5001
#
# sale primero porque su orden de llegada es menor.


# ============================================================
# 17. heapify()
# ============================================================

# A veces ya tenemos datos dentro de una lista
# y queremos convertirla en heap.


tickets_existentes = [
    (3, "TK-6001"),
    (1, "TK-6002"),
    (4, "TK-6003"),
    (2, "TK-6004")
]


heapq.heapify(
    tickets_existentes
)


# Ahora la lista puede utilizarse como heap.


while tickets_existentes:

    print(
        heapq.heappop(
            tickets_existentes
        )
    )


# heapify()
#
# resulta útil cuando:
#
# ya tenemos los datos
# ↓
# queremos comenzar a tratarlos como heap


# ============================================================
# 18. heappush() VS append()
# ============================================================

# Si estamos utilizando una lista como heap:
#
# debemos utilizar:
#
# heapq.heappush()
#
#
# y no simplemente:
#
# lista.append()
#
#
# porque heappush() mantiene correctamente
# la estructura del heap.


# ============================================================
# 19. heappop() VS pop()
# ============================================================

# Igualmente:
#
# heapq.heappop()
#
# retira el elemento correspondiente al heap.
#
#
# No debemos sustituirlo por:
#
# lista.pop()
#
# porque pop() retiraría simplemente
# el último elemento de la lista.


# ============================================================
# 20. CASO REAL: TAREAS DE PROCESAMIENTO
# ============================================================

cola_trabajos = []


heapq.heappush(
    cola_trabajos,
    (
        3,
        "Generar reporte mensual"
    )
)


heapq.heappush(
    cola_trabajos,
    (
        1,
        "Restaurar servicio crítico"
    )
)


heapq.heappush(
    cola_trabajos,
    (
        2,
        "Procesar actualización"
    )
)


while cola_trabajos:

    prioridad, trabajo = (
        heapq.heappop(
            cola_trabajos
        )
    )

    print(
        "Procesando:",
        trabajo
    )


# Una cola de prioridad no sirve solamente
# para tickets.
#
# Puede utilizarse para:
#
# tareas
# trabajos
# eventos
# procesos
# solicitudes
# algoritmos


# ============================================================
# 21. CUÁNDO USAR UNA COLA NORMAL
# ============================================================

# Si la regla es:
#
# "atender estrictamente
# según orden de llegada"
#
# podemos utilizar:
#
# deque
#
#
# FIFO:
#
# primero en entrar
# primero en salir


# ============================================================
# 22. CUÁNDO USAR UNA COLA DE PRIORIDAD
# ============================================================

# Si la regla es:
#
# "algunos elementos deben procesarse
# antes que otros"
#
# puede tener sentido:
#
# heapq
#
#
# El orden depende de una prioridad
# y no solamente del momento de llegada.


# ============================================================
# 23. COMPARACIÓN
# ============================================================

# COLA NORMAL:
#
# TK-001 Baja
# TK-002 Crítica
#
#
# atención:
#
# TK-001
# TK-002
#
#
# porque TK-001 llegó primero.
#
#
# ------------------------------------------------------------
#
# COLA DE PRIORIDAD:
#
# TK-001 Baja
# TK-002 Crítica
#
#
# atención:
#
# TK-002
# TK-001
#
#
# porque TK-002 tiene mayor prioridad.


# ============================================================
# 24. UNA ACLARACIÓN SOBRE "MAYOR PRIORIDAD"
# ============================================================

# Nosotros decidimos representar:
#
# Crítica → 1
# Alta    → 2
# Media   → 3
# Baja    → 4
#
#
# Por eso:
#
# número menor
# ↓
# prioridad mayor
#
#
# Esto es una decisión de nuestro modelo.
#
# Los números no tienen ese significado
# automáticamente en Python.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# COLA NORMAL:
#
# FIFO
#
# orden de llegada.
#
#
# ------------------------------------------------------------
#
# COLA DE PRIORIDAD:
#
# orden según importancia.
#
#
# ------------------------------------------------------------
#
# PYTHON:
#
# import heapq
#
#
# ------------------------------------------------------------
#
# AGREGAR:
#
# heapq.heappush(
#     cola,
#     (prioridad, elemento)
# )
#
#
# ------------------------------------------------------------
#
# RETIRAR PRIORITARIO:
#
# heapq.heappop(cola)
#
#
# ------------------------------------------------------------
#
# CONSULTAR SIGUIENTE:
#
# cola[0]
#
#
# ------------------------------------------------------------
#
# CONVERTIR LISTA EXISTENTE:
#
# heapq.heapify(lista)
#
#
# ------------------------------------------------------------
#
# heapq utiliza un min-heap:
#
# el menor valor
# sale primero.
#
#
# Por eso podemos definir:
#
# 1 → Crítica
# 2 → Alta
# 3 → Media
# 4 → Baja
#
#
# ------------------------------------------------------------
#
# PREGUNTA PRÁCTICA:
#
# ¿debo respetar estrictamente
# el orden de llegada?
#
# → cola FIFO
#
#
# ¿debo procesar primero
# los elementos más importantes?
#
# → cola de prioridad