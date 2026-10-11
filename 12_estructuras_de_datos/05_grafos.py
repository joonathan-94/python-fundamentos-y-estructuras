# ============================================================
# GRAFOS
# ============================================================
#
# Un grafo es una estructura de datos utilizada
# para representar:
#
# elementos
# +
# relaciones entre esos elementos
#
#
# Los elementos suelen llamarse:
#
# vértices
# o
# nodos
#
#
# Las conexiones suelen llamarse:
#
# aristas
#
#
# Ejemplo:
#
# A ───── B
# │       │
# │       │
# C ───── D
#
#
# A, B, C y D:
#
# son vértices.
#
#
# Las líneas:
#
# son aristas.
#
#
# Los grafos pueden representar:
#
# - redes;
# - carreteras;
# - conexiones entre computadores;
# - redes sociales;
# - dependencias;
# - rutas;
# - relaciones entre entidades.
#
#
# En este archivo estudiaremos solamente
# los fundamentos.
#
# Los algoritmos de recorrido:
#
# BFS
# DFS
#
# serán estudiados posteriormente en:
#
# 13_algoritmos_y_complejidad


# ============================================================
# 1. ÁRBOL VS GRAFO
# ============================================================

# Un árbol representa normalmente
# una estructura jerárquica.
#
#
# Ejemplo:
#
#            Empresa
#           /       \
# Desarrollo       Soporte
#      |
#   Backend
#
#
# Tenemos conceptos como:
#
# raíz
# padre
# hijo
# hoja
#
#
# ------------------------------------------------------------
#
# En un grafo:
#
# A ─── B
# │   / │
# │  /  │
# C ─── D
#
#
# las conexiones pueden existir
# libremente entre diferentes nodos.
#
#
# No necesitamos:
#
# raíz
# padre
# hijo
#
#
# Lo importante es:
#
# quién está conectado con quién.


# ============================================================
# 2. VÉRTICES Y ARISTAS
# ============================================================

# Supongamos esta red:
#
#
# Servidor A ───── Servidor B
#      │
#      │
# Servidor C
#
#
# VÉRTICES:
#
# Servidor A
# Servidor B
# Servidor C
#
#
# ARISTAS:
#
# A - B
# A - C


# ============================================================
# 3. UNA REPRESENTACIÓN MUY COMÚN EN PYTHON
# ============================================================

# Una forma sencilla de representar un grafo
# es utilizar un diccionario.
#
#
# Cada clave representa un nodo.
#
# Su valor contiene los nodos vecinos.


grafo = {
    "A": ["B", "C"],
    "B": ["A"],
    "C": ["A"]
}


print(
    grafo
)


# Conceptualmente:
#
#       B
#       |
#       |
#       A
#       |
#       |
#       C
#
#
# A está conectado con:
#
# B
# C
#
#
# B está conectado con:
#
# A
#
#
# C está conectado con:
#
# A


# ============================================================
# 4. LISTA DE ADYACENCIA
# ============================================================

# La representación anterior se conoce como:
#
# lista de adyacencia.
#
#
# No significa necesariamente que usemos
# únicamente objetos list.
#
#
# La idea es almacenar:
#
# nodo
# ↓
# vecinos
#
#
# Ejemplo:
#
# A → B, C
# B → A
# C → A


# ============================================================
# 5. CONSULTAR LOS VECINOS
# ============================================================

vecinos_a = grafo["A"]


print(
    "Vecinos de A:",
    vecinos_a
)


# Resultado:
#
# ["B", "C"]


# ============================================================
# 6. RECORRER LOS VECINOS
# ============================================================

for vecino in grafo["A"]:

    print(
        "A está conectado con:",
        vecino
    )


# Estamos recorriendo solamente:
#
# los vecinos directos de A.
#
#
# No estamos recorriendo todavía
# todo el grafo.


# ============================================================
# 7. GRAFO NO DIRIGIDO
# ============================================================

# En un grafo no dirigido:
#
# A ─── B
#
# significa:
#
# A está conectado con B
#
# y
#
# B está conectado con A.
#
#
# Por eso escribimos:
#
# "A": ["B"]
# "B": ["A"]


grafo_no_dirigido = {
    "Einstein": [
        "Tesla"
    ],

    "Tesla": [
        "Einstein",
        "Turing"
    ],

    "Turing": [
        "Tesla"
    ]
}


# Representación:
#
# Einstein ─── Tesla ─── Turing


# ============================================================
# 8. CONEXIÓN EN AMBOS SENTIDOS
# ============================================================

print(
    grafo_no_dirigido[
        "Einstein"
    ]
)


print(
    grafo_no_dirigido[
        "Tesla"
    ]
)


# Einstein conoce a Tesla.
#
# Tesla también contiene a Einstein
# entre sus vecinos.
#
#
# La conexión existe conceptualmente
# en ambos sentidos.


# ============================================================
# 9. GRAFO DIRIGIDO
# ============================================================

# En un grafo dirigido:
#
# las conexiones tienen dirección.
#
#
# Se representan mediante flechas:
#
# A ───→ B
#
#
# Esto NO implica necesariamente:
#
# B ───→ A
#
#
# Son relaciones diferentes.


grafo_dirigido = {
    "Servicio A": [
        "Servicio B"
    ],

    "Servicio B": [
        "Base de datos"
    ],

    "Base de datos": []
}


# Conceptualmente:
#
# Servicio A
#     |
#     v
# Servicio B
#     |
#     v
# Base de datos


# ============================================================
# 10. EJEMPLO REAL: DEPENDENCIAS
# ============================================================

# Supongamos que:
#
# Servicio A necesita Servicio B.
#
# Servicio B necesita Base de datos.
#
#
# Eso se puede representar:
#
#
# Servicio A
#     ↓
# Servicio B
#     ↓
# Base de datos
#
#
# La relación tiene dirección.
#
#
# Base de datos no necesariamente
# depende de Servicio B.


# ============================================================
# 11. DIFERENCIA FUNDAMENTAL
# ============================================================

# NO DIRIGIDO:
#
# A ─── B
#
# conexión mutua.
#
#
# DIRIGIDO:
#
# A ───→ B
#
# conexión desde A hacia B.


# ============================================================
# 12. UTILIZAR set PARA LOS VECINOS
# ============================================================

# También podemos utilizar sets.
#
#
# Esto resulta útil porque:
#
# un set evita elementos duplicados.
#
#
# Además permite comprobar pertenencia
# eficientemente.


red = {
    "Servidor A": set(),
    "Servidor B": set(),
    "Servidor C": set()
}


red["Servidor A"].add(
    "Servidor B"
)


red["Servidor B"].add(
    "Servidor A"
)


print(
    red
)


# Tenemos:
#
# Servidor A ─── Servidor B


# ============================================================
# 13. AGREGAR UNA CONEXIÓN NO DIRIGIDA
# ============================================================

red["Servidor A"].add(
    "Servidor C"
)


red["Servidor C"].add(
    "Servidor A"
)


# Ahora:
#
#              Servidor B
#                  |
#                  |
#              Servidor A
#                  |
#                  |
#              Servidor C


# ============================================================
# 14. POR QUÉ AGREGAMOS AMBOS SENTIDOS
# ============================================================

# Si hacemos solamente:
#
# A.add(B)
#
# nuestra representación contiene:
#
# A → B
#
#
# Pero para representar:
#
# A ─ B
#
# debemos almacenar también:
#
# B → A


# ============================================================
# 15. FUNCIÓN PARA CONECTAR NODOS
# ============================================================

# Podemos evitar repetir código
# mediante una función.


red_computadores = {
    "PC-01": set(),
    "PC-02": set(),
    "PC-03": set()
}


def conectar(
    grafo,
    nodo_a,
    nodo_b
):

    grafo[nodo_a].add(
        nodo_b
    )

    grafo[nodo_b].add(
        nodo_a
    )


conectar(
    red_computadores,
    "PC-01",
    "PC-02"
)


conectar(
    red_computadores,
    "PC-01",
    "PC-03"
)


print(
    red_computadores
)


# Resultado conceptual:
#
#        PC-02
#          |
#          |
#        PC-01
#          |
#          |
#        PC-03


# ============================================================
# 16. COMPROBAR UNA CONEXIÓN
# ============================================================

if (
    "PC-02"
    in red_computadores["PC-01"]
):

    print(
        "PC-01 está conectado con PC-02."
    )


# Aquí reutilizamos:
#
# in
# +
# set
# +
# dict


# ============================================================
# 17. RECORRER TODOS LOS NODOS
# ============================================================

for nodo in red_computadores:

    print(
        "Nodo:",
        nodo
    )


# Cuando recorremos un diccionario:
#
# obtenemos sus claves.
#
#
# En este caso:
#
# cada clave es un nodo.


# ============================================================
# 18. RECORRER NODOS Y SUS VECINOS
# ============================================================

for nodo, vecinos in (
    red_computadores.items()
):

    print(
        nodo,
        "→",
        vecinos
    )


# Esto permite observar:
#
# nodo
# +
# conexiones directas


# ============================================================
# 19. EJEMPLO REAL: RED DE CIUDADES
# ============================================================

rutas = {
    "Santiago": {
        "Valparaíso",
        "Rancagua"
    },

    "Valparaíso": {
        "Santiago",
        "Viña del Mar"
    },

    "Viña del Mar": {
        "Valparaíso"
    },

    "Rancagua": {
        "Santiago"
    }
}


# Conceptualmente:
#
# Viña del Mar
#      |
# Valparaíso
#      |
# Santiago
#      |
# Rancagua


print(
    "Desde Santiago:",
    rutas["Santiago"]
)


# Estamos preguntando:
#
# ¿qué ciudades están conectadas
# directamente con Santiago?


# ============================================================
# 20. VECINO
# ============================================================

# Dos vértices conectados directamente
# mediante una arista suelen considerarse:
#
# vecinos.
#
#
# Ejemplo:
#
# A ─── B
#
#
# B es vecino de A.
#
# A es vecino de B
# si el grafo es no dirigido.


# ============================================================
# 21. CAMINO
# ============================================================

# Podemos recorrer varias conexiones:
#
#
# A ─── B ─── C
#
#
# Existe un camino desde:
#
# A
#
# hasta:
#
# C
#
#
# pasando por:
#
# B.
#
#
# Encontrar automáticamente caminos
# será un problema de algoritmos.


# ============================================================
# 22. CICLOS
# ============================================================

# Un grafo puede contener ciclos.
#
#
# Ejemplo:
#
# A ─── B
# |     |
# |     |
# C ─── D
#
#
# Podemos recorrer:
#
# A
# ↓
# B
# ↓
# D
# ↓
# C
# ↓
# A
#
#
# y volver al punto inicial.
#
#
# Eso es un ciclo.


grafo_ciclo = {
    "A": {
        "B",
        "C"
    },

    "B": {
        "A",
        "D"
    },

    "C": {
        "A",
        "D"
    },

    "D": {
        "B",
        "C"
    }
}


# ============================================================
# 23. DIFERENCIA IMPORTANTE CON UN ÁRBOL
# ============================================================

# Un árbol tiene una estructura
# mucho más restringida.
#
#
# Un grafo puede:
#
# - tener ciclos;
# - tener múltiples conexiones;
# - no tener raíz;
# - no tener relación padre/hijo;
# - tener conexiones dirigidas.
#
#
# Por eso:
#
# todo árbol puede entenderse
# dentro de la familia general de grafos,
#
# pero:
#
# no todo grafo es un árbol.


# ============================================================
# 24. NODO AISLADO
# ============================================================

# Un vértice puede existir
# sin tener ninguna conexión.


grafo_aislado = {
    "A": {
        "B"
    },

    "B": {
        "A"
    },

    "C": set()
}


# C existe dentro del grafo,
#
# pero no está conectado
# con ningún otro nodo.
#
#
# Conceptualmente:
#
# A ─── B
#
#
# C


# ============================================================
# 25. GRAFOS CON PESOS
# ============================================================

# A veces una conexión necesita
# almacenar información adicional.
#
#
# Por ejemplo:
#
# distancia.
#
#
# Santiago ─── 120 km ─── Valparaíso
#
#
# Podemos representar algo similar
# mediante un diccionario anidado.


rutas_con_distancia = {
    "Santiago": {
        "Valparaíso": 120,
        "Rancagua": 87
    },

    "Valparaíso": {
        "Santiago": 120
    },

    "Rancagua": {
        "Santiago": 87
    }
}


print(
    rutas_con_distancia[
        "Santiago"
    ]
)


# Aquí:
#
# 120
# 87
#
# representan pesos.
#
#
# Un peso puede representar:
#
# distancia
# tiempo
# costo
# prioridad
# capacidad
#
#
# Los algoritmos que utilizan esos pesos
# se estudiarán más adelante.


# ============================================================
# 26. ARISTA CON PESO
# ============================================================

# En:
#
# Santiago ─── 120 ─── Valparaíso
#
#
# Santiago y Valparaíso:
#
# son vértices.
#
#
# La conexión:
#
# es una arista.
#
#
# 120:
#
# es el peso de la arista.


# ============================================================
# 27. CLASE GRAFO SENCILLA
# ============================================================

# También podríamos encapsular
# la estructura dentro de una clase.
#
#
# No es obligatorio para utilizar grafos,
# pero sirve para combinar este tema con POO.


class Grafo:

    def __init__(self):
        self.adyacencias = {}

    def agregar_vertice(
        self,
        vertice
    ):

        if (
            vertice
            not in self.adyacencias
        ):

            self.adyacencias[
                vertice
            ] = set()

    def agregar_arista(
        self,
        vertice_a,
        vertice_b
    ):

        self.agregar_vertice(
            vertice_a
        )

        self.agregar_vertice(
            vertice_b
        )

        self.adyacencias[
            vertice_a
        ].add(
            vertice_b
        )

        self.adyacencias[
            vertice_b
        ].add(
            vertice_a
        )


# Esta clase representa
# un grafo no dirigido.


# ============================================================
# 28. UTILIZAR LA CLASE
# ============================================================

grafo_servidores = Grafo()


grafo_servidores.agregar_arista(
    "Servidor A",
    "Servidor B"
)


grafo_servidores.agregar_arista(
    "Servidor A",
    "Servidor C"
)


print(
    grafo_servidores.adyacencias
)


# Conceptualmente:
#
# Servidor B
#      |
# Servidor A
#      |
# Servidor C


# ============================================================
# 29. NO NECESITAMOS UNA CLASE SIEMPRE
# ============================================================

# Para muchos problemas sencillos:
#
# dict
# +
# list
#
# o:
#
# dict
# +
# set
#
# puede ser suficiente.
#
#
# Ejemplo:
#
# grafo = {
#     "A": {"B", "C"},
#     "B": {"A"},
#     "C": {"A"}
# }
#
#
# Crear una clase tiene sentido
# cuando necesitamos encapsular:
#
# comportamiento
# validaciones
# operaciones adicionales


# ============================================================
# 30. MATRIZ DE ADYACENCIA
# ============================================================

# Existe otra forma de representar grafos:
#
# matriz de adyacencia.
#
#
# Por ejemplo:
#
#     A B C
#
# A   0 1 1
# B   1 0 0
# C   1 0 0
#
#
# Un 1 puede indicar:
#
# existe conexión.
#
#
# Un 0:
#
# no existe conexión.
#
#
# No la implementaremos ahora.
#
# Para nuestro nivel actual,
# una lista de adyacencia resulta
# más sencilla y práctica.


# ============================================================
# 31. GRAFO Y RECORRIDOS
# ============================================================

# Supongamos:
#
# A ─── B ─── D
# |
# C
#
#
# Si queremos responder:
#
# ¿puedo llegar desde A hasta D?
#
# necesitamos recorrer el grafo.
#
#
# Ahí aparecerán algoritmos como:
#
# BFS
#
# Breadth-First Search
#
#
# y:
#
# DFS
#
# Depth-First Search
#
#
# NO los estudiaremos todavía.
#
# Serán parte de:
#
# 13_algoritmos_y_complejidad


# ============================================================
# 32. RELACIÓN CON PILAS Y COLAS
# ============================================================

# Cuando estudiemos recorridos:
#
# BFS
#
# suele relacionarse con:
#
# COLA
#
#
# DFS
#
# suele relacionarse con:
#
# PILA
#
# o recursividad.
#
#
# Esto demuestra nuevamente
# que las estructuras estudiadas
# están relacionadas entre sí.


# ============================================================
# 33. EJEMPLO REAL: SERVICIOS
# ============================================================

servicios = {
    "API": {
        "Usuarios",
        "Tickets"
    },

    "Usuarios": {
        "Base de datos"
    },

    "Tickets": {
        "Base de datos"
    },

    "Base de datos": set()
}


# Podríamos interpretar:
#
#
#             API
#            /   \
#      Usuarios  Tickets
#           \     /
#          Base de datos
#
#
# Aquí una misma entidad:
#
# Base de datos
#
# puede estar relacionada
# con varios elementos.
#
#
# Esto ya no encaja tan naturalmente
# con una jerarquía de árbol simple.


# ============================================================
# 34. ¿CUÁNDO TIENE SENTIDO UN GRAFO?
# ============================================================

# Pregúntate:
#
# ¿mi problema consiste principalmente
# en conexiones o relaciones?
#
#
# Ejemplos:
#
# ciudades conectadas por carreteras
# computadores conectados por red
# usuarios relacionados
# servicios dependientes
# estaciones conectadas
# rutas
#
#
# Entonces:
#
# un grafo puede representar
# naturalmente el problema.


# ============================================================
# 35. ¿CUÁNDO NO NECESITAMOS UN GRAFO?
# ============================================================

# Si tenemos:
#
# una simple secuencia
#
# → list
#
#
# último en entrar / primero en salir
#
# → pila
#
#
# primero en entrar / primero en salir
#
# → cola
#
#
# prioridad
#
# → heap
#
#
# jerarquía clara
#
# → árbol
#
#
# relaciones generales
#
# → grafo


# ============================================================
# 36. CONCEPTOS QUE DEBES MANEJAR
# ============================================================

# VÉRTICE / NODO:
#
# elemento del grafo.
#
#
# ARISTA:
#
# conexión entre nodos.
#
#
# VECINO:
#
# nodo conectado directamente
# con otro nodo.
#
#
# GRAFO NO DIRIGIDO:
#
# conexión en ambos sentidos.
#
#
# GRAFO DIRIGIDO:
#
# conexión con dirección.
#
#
# PESO:
#
# valor asociado a una conexión.
#
#
# CAMINO:
#
# secuencia de conexiones
# entre diferentes nodos.
#
#
# CICLO:
#
# camino que puede regresar
# al punto inicial.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# GRAFO:
#
# estructura utilizada para representar
# relaciones entre elementos.
#
#
# ------------------------------------------------------------
#
# ELEMENTOS:
#
# vértices / nodos
#
#
# ------------------------------------------------------------
#
# CONEXIONES:
#
# aristas
#
#
# ------------------------------------------------------------
#
# REPRESENTACIÓN SENCILLA EN PYTHON:
#
# grafo = {
#     "A": {"B", "C"},
#     "B": {"A"},
#     "C": {"A"}
# }
#
#
# ------------------------------------------------------------
#
# SIGNIFICA:
#
# A está conectado con B y C.
#
#
# ------------------------------------------------------------
#
# ÁRBOL:
#
# jerarquía.
#
#
# GRAFO:
#
# relaciones generales.
#
#
# ------------------------------------------------------------
#
# GRAFO NO DIRIGIDO:
#
# A ─── B
#
#
# ------------------------------------------------------------
#
# GRAFO DIRIGIDO:
#
# A ───→ B
#
#
# ------------------------------------------------------------
#
# GRAFO CON PESOS:
#
# A ─── 10 ─── B
#
#
# ------------------------------------------------------------
#
# CONCEPTO MÁS IMPORTANTE:
#
# nodo
# +
# conexiones con otros nodos.
#
#
# ------------------------------------------------------------
#
# PRÓXIMO BLOQUE:
#
# 13_algoritmos_y_complejidad
#
# donde podremos estudiar cómo recorrer
# y buscar información dentro de
# estructuras como estas.