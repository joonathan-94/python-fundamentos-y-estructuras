# ============================================================
# PILAS Y COLAS
# ============================================================
#
# Una estructura de datos define una forma de organizar
# información según cómo necesitamos utilizarla.
#
#
# En este archivo estudiaremos:
#
# PILA
# → LIFO

#
# COLA
# → FIFO
#
#
# No son necesariamente tipos especiales de Python.
#
# Podemos implementar estas estructuras utilizando
# colecciones que Python ya proporciona.
#
#
# Para este estudio utilizaremos:
#
# pila
# → list
#
# cola
# → collections.deque


# ============================================================
# 1. PILAS
# ============================================================


# ------------------------------------------------------------
# 1.1 ¿QUÉ ES UNA PILA?
# ------------------------------------------------------------

# Una pila sigue la regla:
#
# LIFO
#
# Last In, First Out
#
#
# Traducido:
#
# último en entrar
# ↓
# primero en salir
#
#
# Podemos imaginar una pila de platos:
#
#     plato 3  ← sale primero
#     plato 2
#     plato 1
#
#
# El último plato agregado queda arriba
# y será el primero que retiremos.


# ------------------------------------------------------------
# 1.2 PILA CON UNA LISTA
# ------------------------------------------------------------

pila = []


# Python no necesita una clase especial llamada Stack
# para casos sencillos.
#
# Una list ya permite las dos operaciones principales:
#
# append()
# → agregar al final
#
# pop()
# → retirar el último elemento


# ------------------------------------------------------------
# 1.3 AGREGAR ELEMENTOS A LA PILA
# ------------------------------------------------------------

pila.append(
    "Primera acción"
)

pila.append(
    "Segunda acción"
)

pila.append(
    "Tercera acción"
)


print(pila)


# Estado:
#
# [
#     "Primera acción",
#     "Segunda acción",
#     "Tercera acción"
# ]
#
#
# La última acción agregada fue:
#
# "Tercera acción"
#
# Por lo tanto será la primera en salir.


# ------------------------------------------------------------
# 1.4 RETIRAR UN ELEMENTO
# ------------------------------------------------------------

ultima_accion = pila.pop()


print(
    "Acción retirada:",
    ultima_accion
)


print(
    "Pila restante:",
    pila
)


# Resultado conceptual:
#
# sale:
#
# Tercera acción
#
#
# quedan:
#
# Primera acción
# Segunda acción


# ------------------------------------------------------------
# 1.5 VISUALIZAR LIFO
# ------------------------------------------------------------

# Entrada:
#
# Acción A
# Acción B
# Acción C
#
#
# Pila:
#
# Acción C  ← sale primero
# Acción B
# Acción A
#
#
# Salida:
#
# C
# B
# A


# ------------------------------------------------------------
# 1.6 EJEMPLO REAL: DESHACER ACCIONES
# ------------------------------------------------------------

historial_acciones = []


historial_acciones.append(
    "Crear ticket"
)

historial_acciones.append(
    "Cambiar prioridad"
)

historial_acciones.append(
    "Asignar técnico"
)


print(
    historial_acciones
)


# Supongamos que queremos deshacer
# la última acción realizada.


accion_a_deshacer = (
    historial_acciones.pop()
)


print(
    "Deshacer:",
    accion_a_deshacer
)


# Resultado:
#
# Deshacer: Asignar técnico
#
#
# Tiene sentido porque esa fue
# la acción realizada más recientemente.


# ------------------------------------------------------------
# 1.7 OTRO CASO REAL: NAVEGACIÓN
# ------------------------------------------------------------

historial_paginas = []


historial_paginas.append(
    "Inicio"
)

historial_paginas.append(
    "Tickets"
)

historial_paginas.append(
    "Detalle TK-1001"
)


pagina_actual = (
    historial_paginas.pop()
)


print(
    "Página retirada:",
    pagina_actual
)


print(
    "Página anterior:",
    historial_paginas[-1]
)


# Este concepto puede aparecer en:
#
# historial
# deshacer
# navegación
# procesamiento interno
# algoritmos


# ------------------------------------------------------------
# 1.8 CONSULTAR EL ÚLTIMO SIN RETIRARLO
# ------------------------------------------------------------

pila_cientificos = [
    "Albert Einstein",
    "Nikola Tesla",
    "Alan Turing"
]


ultimo_cientifico = (
    pila_cientificos[-1]
)


print(
    ultimo_cientifico
)


# [-1]
#
# permite consultar el último elemento
# sin eliminarlo.
#
#
# pop()
#
# consulta Y elimina.


# ------------------------------------------------------------
# 1.9 CUIDADO CON UNA PILA VACÍA
# ------------------------------------------------------------

pila_vacia = []


# Esto produciría IndexError:
#
# pila_vacia.pop()
#
#
# Por eso podemos comprobar primero:


if pila_vacia:

    elemento = pila_vacia.pop()

    print(elemento)

else:

    print(
        "La pila está vacía."
    )


# Una lista vacía se evalúa como False.


# ------------------------------------------------------------
# 1.10 OPERACIONES FUNDAMENTALES DE UNA PILA
# ------------------------------------------------------------

# APILAR:
#
# pila.append(elemento)
#
#
# DESAPILAR:
#
# pila.pop()
#
#
# CONSULTAR EL ÚLTIMO:
#
# pila[-1]
#
#
# COMPROBAR SI ESTÁ VACÍA:
#
# if pila:
#     ...


# ============================================================
# 2. COLAS
# ============================================================


# ------------------------------------------------------------
# 2.1 ¿QUÉ ES UNA COLA?
# ------------------------------------------------------------

# Una cola sigue la regla:
#
# FIFO
#
# First In, First Out
#
#
# Traducido:
#
# primero en entrar
# ↓
# primero en salir
#
#
# Pensemos en una fila:
#
# Persona A
# Persona B
# Persona C
#
#
# La persona A llegó primero.
#
# Por lo tanto:
#
# Persona A
#
# debe ser atendida primero.


# ------------------------------------------------------------
# 2.2 EJEMPLO CON TICKETS
# ------------------------------------------------------------

# Si los tickets se atienden solamente
# según orden de llegada:
#
#
# TK-001
# llega primero
#
# TK-002
# llega segundo
#
# TK-003
# llega tercero
#
#
# Orden de atención:
#
# TK-001
# TK-002
# TK-003


# ------------------------------------------------------------
# 2.3 ¿POR QUÉ NO UTILIZAR list.pop(0)?
# ------------------------------------------------------------

# Técnicamente podríamos hacer:
#
# cola = []
#
# cola.append("TK-001")
# cola.append("TK-002")
#
# cola.pop(0)
#
#
# Funcionaría.
#
# Sin embargo, retirar repetidamente el primer elemento
# de una list obliga a reorganizar los elementos restantes.
#
#
# Python proporciona una estructura más adecuada:
#
# deque


# ------------------------------------------------------------
# 2.4 IMPORTAR deque
# ------------------------------------------------------------

from collections import deque


# deque significa:
#
# double-ended queue
#
# o:
#
# cola de doble extremo.
#
#
# Puede agregar y retirar elementos eficientemente
# desde ambos extremos.
#
#
# Para una cola FIFO utilizaremos principalmente:
#
# append()
# popleft()


# ------------------------------------------------------------
# 2.5 CREAR UNA COLA
# ------------------------------------------------------------

cola_tickets = deque()


print(
    cola_tickets
)


# ------------------------------------------------------------
# 2.6 AGREGAR ELEMENTOS
# ------------------------------------------------------------

cola_tickets.append(
    "TK-001"
)

cola_tickets.append(
    "TK-002"
)

cola_tickets.append(
    "TK-003"
)


print(
    cola_tickets
)


# Conceptualmente:
#
# entrada →
#
# TK-001
# TK-002
# TK-003
#
# ↑
# este fue el primero


# ------------------------------------------------------------
# 2.7 ATENDER EL PRIMERO
# ------------------------------------------------------------

ticket_atendido = (
    cola_tickets.popleft()
)


print(
    "Ticket atendido:",
    ticket_atendido
)


print(
    "Cola restante:",
    cola_tickets
)


# Sale:
#
# TK-001
#
#
# Quedan:
#
# TK-002
# TK-003


# ------------------------------------------------------------
# 2.8 VISUALIZAR FIFO
# ------------------------------------------------------------

# Entrada:
#
# A
# B
# C
#
#
# Cola:
#
# A ← sale primero
# B
# C
#
#
# Salida:
#
# A
# B
# C


# ------------------------------------------------------------
# 2.9 EJEMPLO REALISTA
# ------------------------------------------------------------

cola_solicitudes = deque()


cola_solicitudes.append(
    {
        "id": "TK-1001",
        "titulo": "Crear usuario"
    }
)

cola_solicitudes.append(
    {
        "id": "TK-1002",
        "titulo": "Problema de impresión"
    }
)

cola_solicitudes.append(
    {
        "id": "TK-1003",
        "titulo": "Actualizar software"
    }
)


primera_solicitud = (
    cola_solicitudes.popleft()
)


print(
    "Atendiendo:",
    primera_solicitud["id"],
    primera_solicitud["titulo"]
)


# El primero que llegó:
#
# TK-1001
#
# es el primero que atendemos.


# ------------------------------------------------------------
# 2.10 CONSULTAR EL PRIMERO SIN RETIRARLO
# ------------------------------------------------------------

if cola_solicitudes:

    siguiente_ticket = (
        cola_solicitudes[0]
    )

    print(
        "Siguiente:",
        siguiente_ticket["id"]
    )


# [0]
#
# consulta el primer elemento.
#
#
# popleft()
#
# consulta Y elimina.


# ------------------------------------------------------------
# 2.11 COMPROBAR SI ESTÁ VACÍA
# ------------------------------------------------------------

cola_vacia = deque()


if cola_vacia:

    siguiente = (
        cola_vacia.popleft()
    )

    print(siguiente)

else:

    print(
        "No existen elementos en la cola."
    )


# Igual que las listas:
#
# deque vacío
# → False
#
# deque con elementos
# → True


# ------------------------------------------------------------
# 2.12 PROCESAR TODA UNA COLA
# ------------------------------------------------------------

cola_procesamiento = deque(
    [
        "Solicitud A",
        "Solicitud B",
        "Solicitud C"
    ]
)


while cola_procesamiento:

    solicitud = (
        cola_procesamiento.popleft()
    )

    print(
        "Procesando:",
        solicitud
    )


# Flujo:
#
# mientras existan elementos
# ↓
# retirar el primero
# ↓
# procesarlo
# ↓
# continuar


# ------------------------------------------------------------
# 2.13 ESTADO FINAL
# ------------------------------------------------------------

print(
    cola_procesamiento
)


# Después del while:
#
# deque([])
#
#
# Todos los elementos fueron procesados.


# ------------------------------------------------------------
# 2.14 OPERACIONES FUNDAMENTALES DE UNA COLA
# ------------------------------------------------------------

# AGREGAR:
#
# cola.append(elemento)
#
#
# RETIRAR EL PRIMERO:
#
# cola.popleft()
#
#
# CONSULTAR EL PRIMERO:
#
# cola[0]
#
#
# COMPROBAR SI ESTÁ VACÍA:
#
# if cola:
#     ...


# ============================================================
# 3. PILA VS COLA
# ============================================================


# ------------------------------------------------------------
# 3.1 MISMO ORDEN DE ENTRADA
# ------------------------------------------------------------

# Supongamos:
#
# A
# B
# C
#
# entran exactamente en ese orden.


# ------------------------------------------------------------
# 3.2 PILA
# ------------------------------------------------------------

# Pila:
#
# A entra
# B entra
# C entra
#
#
# Sale:
#
# C
# B
# A
#
#
# LIFO


# ------------------------------------------------------------
# 3.3 COLA
# ------------------------------------------------------------

# Cola:
#
# A entra
# B entra
# C entra
#
#
# Sale:
#
# A
# B
# C
#
#
# FIFO


# ------------------------------------------------------------
# 3.4 EJEMPLO EJECUTABLE
# ------------------------------------------------------------

datos = [
    "A",
    "B",
    "C"
]


pila_ejemplo = []


for dato in datos:
    pila_ejemplo.append(
        dato
    )


print(
    "Salida de pila:"
)


while pila_ejemplo:

    print(
        pila_ejemplo.pop()
    )


cola_ejemplo = deque()


for dato in datos:
    cola_ejemplo.append(
        dato
    )


print(
    "Salida de cola:"
)


while cola_ejemplo:

    print(
        cola_ejemplo.popleft()
    )


# Resultado:
#
# PILA:
#
# C
# B
# A
#
#
# COLA:
#
# A
# B
# C


# ============================================================
# 4. CÓMO ELEGIR
# ============================================================


# ------------------------------------------------------------
# PILA
# ------------------------------------------------------------

# Pregunta:
#
# ¿Necesito trabajar primero con
# lo último que agregué?
#
#
# Sí:
#
# probablemente necesitamos una pila.
#
#
# Ejemplos:
#
# deshacer acciones
# historial
# navegación
# algoritmos


# ------------------------------------------------------------
# COLA
# ------------------------------------------------------------

# Pregunta:
#
# ¿Necesito respetar el orden
# en que llegaron los elementos?
#
#
# Sí:
#
# probablemente necesitamos una cola.
#
#
# Ejemplos:
#
# solicitudes
# tareas pendientes
# trabajos de procesamiento
# mensajes
# personas esperando atención


# ============================================================
# 5. CASO IMPORTANTE: PRIORIDADES
# ============================================================

# Supongamos:
#
# TK-001 → prioridad baja
# TK-002 → prioridad crítica
#
#
# Si utilizamos una cola FIFO pura:
#
# TK-001
#
# sería atendido primero porque llegó primero.
#
#
# Pero quizá nuestra regla indique:
#
# TK-002
#
# debe atenderse primero porque es crítico.
#
#
# En ese caso:
#
# una cola FIFO normal
#
# NO representa completamente nuestro problema.
#
#
# Necesitamos otra estructura:
#
# COLA DE PRIORIDAD
#
#
# Esa será precisamente la siguiente sección:
#
# 02_colas_de_prioridad.py


# ============================================================
# 6. PILA Y COLA SON REGLAS DE ACCESO
# ============================================================

# Este concepto es importante.
#
#
# PILA y COLA no describen simplemente:
#
# "qué datos tengo"
#
#
# describen principalmente:
#
# "en qué orden voy a acceder a ellos"
#
#
# Los mismos datos:
#
# A
# B
# C
#
# pueden producir resultados diferentes
# dependiendo de la estructura utilizada.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# PILA:
#
# LIFO
#
# Last In, First Out
#
# último en entrar
# ↓
# primero en salir
#
#
# Implementación sencilla en Python:
#
# pila = []
#
# pila.append(elemento)
# pila.pop()
#
#
# Consulta:
#
# pila[-1]
#
#
# ------------------------------------------------------------
#
# COLA:
#
# FIFO
#
# First In, First Out
#
# primero en entrar
# ↓
# primero en salir
#
#
# Implementación recomendada:
#
# from collections import deque
#
# cola = deque()
#
# cola.append(elemento)
# cola.popleft()
#
#
# Consulta:
#
# cola[0]
#
#
# ------------------------------------------------------------
#
# DIFERENCIA FUNDAMENTAL:
#
# mismos datos:
#
# A
# B
# C
#
#
# PILA:
#
# C
# B
# A
#
#
# COLA:
#
# A
# B
# C
#
#
# ------------------------------------------------------------
#
# PREGUNTA PRÁCTICA:
#
# ¿quiero procesar primero
# lo último agregado?
#
# → PILA
#
#
# ¿quiero procesar primero
# lo que llegó antes?
#
# → COLA
#
#
# ------------------------------------------------------------
#
# SIGUIENTE TEMA:
#
# COLA DE PRIORIDAD
#
# donde el orden de procesamiento dependerá
# de la importancia de cada elemento.