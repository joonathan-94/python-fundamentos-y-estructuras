# ============================================================
# RECORRIDOS BFS Y DFS
# ============================================================
#
# BFS y DFS son estrategias utilizadas
# para recorrer árboles y grafos.
#
#
# BFS:
#
# Breadth-First Search
#
# → recorrido en anchura;
# → avanza por niveles;
# → utiliza una cola.
#
#
# DFS:
#
# Depth-First Search
#
# → recorrido en profundidad;
# → profundiza por una rama;
# → utiliza una pila o recursión.


from collections import deque


# ============================================================
# 1. GRAFO DE EJEMPLO
# ============================================================

grafo = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}


# Representación:
#
#        A
#       / \
#      B   C
#     / \   \
#    D   E   F


# ============================================================
# 2. BFS
# ============================================================

# BFS recorre primero
# los nodos más cercanos.
#
#
# Resultado esperado:
#
# A
# B
# C
# D
# E
# F


def recorrer_bfs(
    grafo,
    inicio
):

    cola = deque(
        [inicio]
    )

    visitados = set()


    while cola:

        nodo = cola.popleft()


        if nodo in visitados:
            continue


        visitados.add(
            nodo
        )


        print(
            nodo
        )


        for vecino in grafo[nodo]:

            cola.append(
                vecino
            )


# ============================================================
# 3. EJECUTAR BFS
# ============================================================

print(
    "BFS:"
)


recorrer_bfs(
    grafo,
    "A"
)


# ============================================================
# 4. FUNCIONAMIENTO DE BFS
# ============================================================
#
# inicio:
#
# cola = [A]
#
#
# procesamos A:
#
# cola = [B, C]
#
#
# procesamos B:
#
# cola = [C, D, E]
#
#
# procesamos C:
#
# cola = [D, E, F]
#
#
# Resultado:
#
# A B C D E F


# ============================================================
# 5. POR QUÉ BFS UTILIZA UNA COLA
# ============================================================

# Una cola funciona:
#
# FIFO
#
# primero en entrar
# →
# primero en salir.
#
#
# Eso permite procesar primero
# los nodos descubiertos antes.


# ============================================================
# 6. VISITADOS
# ============================================================

# Un grafo puede contener ciclos.
#
#
# Por ejemplo:
#
# A → B
# B → C
# C → A
#
#
# Sin controlar nodos visitados
# podríamos recorrer:
#
# A
# B
# C
# A
# B
# C
# ...
#
#
# Por eso utilizamos:
#
# set()


grafo_circular = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}


# ============================================================
# 7. DFS
# ============================================================

# DFS profundiza por una rama
# antes de explorar otra.
#
#
# Resultado esperado:
#
# A
# B
# D
# E
# C
# F


def recorrer_dfs(
    grafo,
    inicio
):

    pila = [
        inicio
    ]

    visitados = set()


    while pila:

        nodo = pila.pop()


        if nodo in visitados:
            continue


        visitados.add(
            nodo
        )


        print(
            nodo
        )


        for vecino in reversed(
            grafo[nodo]
        ):

            pila.append(
                vecino
            )


# ============================================================
# 8. EJECUTAR DFS
# ============================================================

print(
    "DFS:"
)


recorrer_dfs(
    grafo,
    "A"
)


# ============================================================
# 9. POR QUÉ DFS UTILIZA UNA PILA
# ============================================================

# Una pila funciona:
#
# LIFO
#
# último en entrar
# →
# primero en salir.
#
#
# Esto hace que profundicemos
# por uno de los caminos
# antes de volver a los anteriores.


# ============================================================
# 10. reversed()
# ============================================================

# Si tenemos:
#
# A → B, C
#
#
# y agregamos a una pila:
#
# B
# C
#
#
# C saldría primero porque
# fue agregado al final.
#
#
# reversed() permite agregar:
#
# C
# B
#
#
# para que B quede arriba
# y sea procesado primero.
#
#
# reversed() no es un requisito
# general de DFS.
#
# Aquí se utiliza solamente
# para mantener un orden visual
# izquierda → derecha.


# ============================================================
# 11. DFS RECURSIVO
# ============================================================

# DFS también puede expresarse
# mediante recursión.


def recorrer_dfs_recursivo(
    grafo,
    nodo,
    visitados
):

    if nodo in visitados:
        return


    visitados.add(
        nodo
    )


    print(
        nodo
    )


    for vecino in grafo[nodo]:

        recorrer_dfs_recursivo(
            grafo,
            vecino,
            visitados
        )


# ============================================================
# 12. EJECUTAR DFS RECURSIVO
# ============================================================

print(
    "DFS recursivo:"
)


visitados_recursivo = set()


recorrer_dfs_recursivo(
    grafo,
    "A",
    visitados_recursivo
)


# ============================================================
# 13. RELACIÓN CON TEMAS ANTERIORES
# ============================================================
#
# BFS
#
# grafo
# +
# cola
# +
# deque
# +
# set
# +
# while
#
#
# DFS
#
# grafo
# +
# pila
# +
# list
# +
# set
# +
# while
#
#
# DFS recursivo
#
# grafo
# +
# set
# +
# recursión


# ============================================================
# 14. BFS VS DFS
# ============================================================
#
# BFS:
#
# recorrido por niveles.
#
# estructura:
#
# cola.
#
#
# ------------------------------------------------------------
#
# DFS:
#
# recorrido en profundidad.
#
# estructura:
#
# pila
#
# o:
#
# recursión.


# ============================================================
# 15. CUÁNDO PENSAR EN BFS
# ============================================================

# Cuando el problema se parece a:
#
# "primero quiero revisar
# lo que está más cerca".
#
#
# Ejemplos conceptuales:
#
# conexiones de una red;
# niveles de un árbol;
# rutas con pocas conexiones
# en grafos sin pesos.


# ============================================================
# 16. CUÁNDO PENSAR EN DFS
# ============================================================

# Cuando el problema se parece a:
#
# "quiero recorrer completamente
# una rama antes de pasar a otra".
#
#
# Ejemplos:
#
# árboles;
# carpetas;
# categorías anidadas;
# exploración de estructuras
# jerárquicas.


# ============================================================
# 17. COMPLEJIDAD
# ============================================================

# Para un grafo representado
# mediante listas de adyacencia:
#
# V:
#
# cantidad de vértices.
#
#
# E:
#
# cantidad de aristas.
#
#
# BFS:
#
# O(V + E)
#
#
# DFS:
#
# O(V + E)
#
#
# Idea:
#
# procesamos los nodos
# y sus conexiones.


# ============================================================
# 18. REGLA MENTAL
# ============================================================
#
# BFS
#
# B de Breadth
# ↓
# amplitud / niveles
#
# ↓
#
# COLA
#
#
# ------------------------------------------------------------
#
# DFS
#
# D de Depth
# ↓
# profundidad
#
# ↓
#
# PILA
#
# o:
#
# RECURSIÓN


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# BFS:
#
# cerca primero
#
# → cola
#
#
# DFS:
#
# profundidad primero
#
# → pila / recursión
#
#
# En grafos:
#
# usar visitados
#
# evita procesar repetidamente
# los mismos nodos.