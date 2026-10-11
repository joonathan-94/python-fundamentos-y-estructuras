# ============================================================
# ED-01 - PILA
# ============================================================
#
# Crea una lista vacía llamada:
#
# historial
#
#
# Agrega utilizando append():
#
# "Abrir ticket"
# "Cambiar estado"
# "Asignar técnico"
#
#
# Después:
#
# 1. Retira la última acción utilizando pop().
# 2. Guarda el resultado en:
#
# ultima_accion
#
# 3. Imprime:
#
# ultima_accion
#
# 4. Imprime el historial restante.
#
#
# Resultado esperado conceptualmente:
#
# última acción:
# "Asignar técnico"
#
#
# historial restante:
#
# [
#     "Abrir ticket",
#     "Cambiar estado"
# ]

historial = []
historial.append("Abrir ticket")
historial.append("Cambiar estado")
historial.append("Asignar técnico")
print(f"Historial inicial: {historial}")

ultima_accion = historial.pop()
print(f"Ultima accion: {ultima_accion}")
print(f"Historial restante: {historial}")

# ============================================================
# ED-02 - COLA
# ============================================================
#
# Importa:
#
# deque
#
# desde:
#
# collections
#
#
# Crea una cola llamada:
#
# cola_tickets
#
#
# Agrega utilizando append():
#
# "TK-001"
# "TK-002"
# "TK-003"
#
#
# Después:
#
# 1. Retira el primer ticket utilizando popleft().
# 2. Guarda el resultado en:
#
# ticket_atendido
#
# 3. Imprime:
#
# ticket_atendido
#
# 4. Imprime la cola restante.
#
#
# Resultado esperado conceptualmente:
#
# ticket atendido:
#
# TK-001
#
#
# cola restante:
#
# TK-002
# TK-003

from collections import deque

cola_tickets = deque()

print(f"Cola tickets inicial: {cola_tickets}")

cola_tickets.append("TK-001")
cola_tickets.append("TK-002")
cola_tickets.append("TK-003")

print(f"Cola tickets con datos: {cola_tickets}")

ticket_atendido = cola_tickets.popleft()
print(f"Ticket atendido: {ticket_atendido}")
print(f"Cola tickets final: {cola_tickets}")

# ============================================================
# ED-03 - COLA DE PRIORIDAD
# ============================================================
#
# Importa:
#
# heapq
#
#
# Crea una lista vacía llamada:
#
# cola_prioridad
#
#
# Agrega mediante heapq.heappush():
#
# prioridad 3
# "TK-001"
#
# prioridad 1
# "TK-002"
#
# prioridad 2
# "TK-003"
#
#
# Recuerda:
#
# 1 → prioridad más alta
# 2 → prioridad intermedia
# 3 → prioridad más baja
#
#
# Después:
#
# 1. Retira el primer elemento utilizando:
#
# heapq.heappop()
#
#
# 2. Desempaqueta el resultado en:
#
# prioridad
# ticket_atendido
#
#
# 3. Imprime:
#
# prioridad
# ticket_atendido
#
#
# 4. Imprime la cola restante.
#
#
# Resultado esperado:
#
# prioridad:
# 1
#
# ticket:
# TK-002
#
#
# TK-002 debe salir primero aunque
# no haya sido el primero agregado.

import heapq


PRIORIDAD_ALTA = 1
PRIORIDAD_INTERMEDIA = 2
PRIORIDAD_BAJA = 3


cola_prioridad = []


print(
    f"Cola inicial: {cola_prioridad}"
)


heapq.heappush(
    cola_prioridad,
    (
        PRIORIDAD_BAJA,
        "TK-001"
    )
)


heapq.heappush(
    cola_prioridad,
    (
        PRIORIDAD_ALTA,
        "TK-002"
    )
)


heapq.heappush(
    cola_prioridad,
    (
        PRIORIDAD_INTERMEDIA,
        "TK-003"
    )
)


print(
    f"Cola con datos: {cola_prioridad}"
)


prioridad, ticket_atendido = (
    heapq.heappop(
        cola_prioridad
    )
)


print(
    f"Prioridad: {prioridad}"
)

print(
    f"Ticket atendido: {ticket_atendido}"
)

print(
    f"Cola final: {cola_prioridad}"
)


# ============================================================
# ED-04 - LISTA ENLAZADA
# ============================================================
#
# Crea una clase:
#
# Nodo
#
#
# Su __init__ debe recibir:
#
# valor
#
#
# y guardar:
#
# self.valor
#
#
# También debe crear:
#
# self.siguiente = None
#
#
# Después crea tres nodos:
#
# "Albert Einstein"
# "Nikola Tesla"
# "Alan Turing"
#
#
# Conéctalos para obtener:
#
# Albert Einstein
#       ↓
# Nikola Tesla
#       ↓
# Alan Turing
#       ↓
# None
#
#
# Utiliza:
#
# nodo_einstein.siguiente = ...
#
# nodo_tesla.siguiente = ...
#
#
# Después:
#
# 1. Crea una variable:
#
# actual
#
# que inicialmente apunte al primer nodo.
#
#
# 2. Utiliza un while para recorrer
# todos los nodos.
#
#
# 3. Imprime el valor de cada nodo.
#
#
# 4. En cada iteración avanza mediante:
#
# actual = actual.siguiente
#
#
# Resultado esperado:
#
# Albert Einstein
# Nikola Tesla
# Alan Turing
#
#
# No crees todavía una clase ListaEnlazada.
#
# El objetivo del ejercicio es practicar solamente:
#
# nodo
# referencia
# siguiente
# recorrido
# None

class Nodo:
    
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
    
einstein = Nodo("Albert Einstein")
print(f"Valor de bjeto cabecera: {einstein.valor}")
tesla = Nodo("Nikola Tesla")
turing = Nodo("Alan Turing")


einstein.siguiente = tesla
print(f"Siguiente valor: {einstein.siguiente.valor}")

tesla.siguiente = turing

actual = einstein

while actual is not None:
    print(f"Valor actual: {actual.valor}")
    actual = actual.siguiente
    
    

print("EJERCICIO ARBOLES")
# ============================================================
# ED-05 - ÁRBOL
# ============================================================
#
# Crea una clase:
#
# Nodo
#
#
# Su __init__ debe recibir:
#
# valor
#
#
# y crear:
#
# self.valor
# self.hijos
#
#
# donde:
#
# self.hijos
#
# debe comenzar como una lista vacía.
#
#

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

# ------------------------------------------------------------
#
# CREA LOS SIGUIENTES NODOS:
#
# Ciencia
#
# Física
# Computación
#
# Relatividad
# Mecánica cuántica
#
# Python
#
#

ciencia = Nodo("Ciencia")

fisica = Nodo("Física")
computacion = Nodo("Computación")

relatividad = Nodo("Relatividad")
mecanica_cuantica = Nodo("Mecánica cuántica")

python = Nodo("Python")
# ------------------------------------------------------------
#
# CONSTRÚYELOS CON ESTA JERARQUÍA:
#
#
#                 Ciencia
#                /       \
#           Física       Computación
#          /     \            |
# Relatividad   Mecánica      Python
#               cuántica
#
#
# ------------------------------------------------------------
#
# Para conectar nodos puedes utilizar:
#
# nodo.hijos.append(...)
#
#
ciencia.hijos.append(fisica)
ciencia.hijos.append(computacion)

fisica.hijos.append(relatividad)
fisica.hijos.append(mecanica_cuantica)

computacion.hijos.append(python)

# ------------------------------------------------------------
#
# DESPUÉS:
#
# 1. Imprime el valor de la raíz.
#
# 2. Recorre con un for los hijos directos
#    de Ciencia.
#
# 3. Imprime los hijos directos de Física.
#
# 4. Comprueba si Relatividad es una hoja.
#
#
# Puedes comprobarlo utilizando:
#
# if not relatividad.hijos:
#
#     ...
#
#

print(f"Nodo raíz: {ciencia.valor}")

for hijo in ciencia.hijos:
    print(hijo.valor)

for hijo in fisica.hijos:
    print(hijo.valor)
    
if not relatividad.hijos:
    print("Relatividad es hoja")

# ------------------------------------------------------------
#
# RESULTADO CONCEPTUAL:
#
# raíz:
#
# Ciencia
#
#
# hijos de Ciencia:
#
# Física
# Computación
#
#
# hijos de Física:
#
# Relatividad
# Mecánica cuántica
#
#
# Relatividad:
#
# es una hoja
#
#
# ------------------------------------------------------------
#
# NO necesitas todavía:
#
# - recorrer automáticamente todo el árbol;
# - utilizar recursividad;
# - crear algoritmos;
# - calcular profundidad;
# - calcular altura.
#
#
# El objetivo es practicar:
#
# nodo
# raíz
# padre
# hijos
# hoja
# jerarquía


print("EJERCICIO GRAFOS")


# ============================================================
# ED-06 - GRAFO
# ============================================================


# ------------------------------------------------------------
# ENUNCIADO
# ------------------------------------------------------------
#
# Representa mediante un diccionario y sets
# la siguiente red:
#
#
#             Servidor B
#                 |
#                 |
# Servidor C ─ Servidor A
#                 |
#                 |
#             Servidor D
#
#
# Es un grafo NO DIRIGIDO.
#
#
# Debes crear:
#
# red_servidores
#
#
# utilizando una estructura similar a:
#
# {
#     "Servidor A": {...},
#     ...
# }
#
#
# ------------------------------------------------------------
#
# LAS CONEXIONES SON:
#
# Servidor A - Servidor B
#
# Servidor A - Servidor C
#
# Servidor A - Servidor D
#
#
# ------------------------------------------------------------
#
# RECUERDA:
#
# Como es un grafo no dirigido:
#
# si Servidor A está conectado con Servidor B,
#
# Servidor B también debe estar conectado
# con Servidor A.
#
#
# ------------------------------------------------------------
#
# DESPUÉS:
#
# 1. Imprime todos los vecinos
#    de Servidor A.
#
# 2. Recorre los vecinos de
#    Servidor A mediante un for.
#
# 3. Comprueba utilizando "in"
#    si Servidor B está conectado
#    directamente con Servidor A.
#
# 4. Imprime:
#
# "Servidor B está conectado con Servidor A"
#
# si la conexión existe.
#
#
# ------------------------------------------------------------
#
# NO necesitas:
#
# - crear una clase Grafo;
# - utilizar BFS;
# - utilizar DFS;
# - buscar caminos;
# - utilizar recursividad;
# - utilizar pesos.
#
#
# El objetivo es practicar:
#
# - vértices;
# - aristas;
# - vecinos;
# - grafo no dirigido;
# - lista de adyacencia;
# - dict;
# - set.


# ============================================================
# SOLUCIÓN
# ============================================================


# Cada clave del diccionario representa un vértice.
#
# Cada set contiene los vecinos conectados directamente
# con ese vértice.

red_servidores = {
    "Servidor A": {
        "Servidor B",
        "Servidor C",
        "Servidor D"
    },

    "Servidor B": {
        "Servidor A"
    },

    "Servidor C": {
        "Servidor A"
    },

    "Servidor D": {
        "Servidor A"
    }
}


# ------------------------------------------------------------
# 1. IMPRIMIR LOS VECINOS DE SERVIDOR A
# ------------------------------------------------------------

print(
    f"Vecinos de Servidor A: "
    f"{red_servidores['Servidor A']}"
)


# ------------------------------------------------------------
# 2. RECORRER LOS VECINOS DE SERVIDOR A
# ------------------------------------------------------------

for vecino in red_servidores["Servidor A"]:

    print(
        f"Servidor A conectado con: {vecino}"
    )


# ------------------------------------------------------------
# 3. COMPROBAR UNA CONEXIÓN
# ------------------------------------------------------------

if "Servidor B" in red_servidores["Servidor A"]:

    print(
        "Servidor B está conectado con Servidor A"
    )