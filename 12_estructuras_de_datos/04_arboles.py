# ============================================================
# ÁRBOLES
# ============================================================
#
# Un árbol es una estructura de datos utilizada para
# representar información jerárquica.
#
#
# Algunos ejemplos:
#
# - carpetas y subcarpetas;
# - estructura de una empresa;
# - categorías y subcategorías;
# - menús;
# - árboles genealógicos;
# - estructuras internas de programas;
# - algunos algoritmos.
#
#
# Ejemplo:
#
#                 Ciencia
#                /       \
#           Física       Computación
#          /    \             |
# Relatividad   Mecánica     Python
#
#
# A diferencia de una lista enlazada:
#
# Nodo A
#   ↓
# Nodo B
#   ↓
# Nodo C
#
#
# en un árbol un nodo puede tener
# más de un nodo conectado debajo de él.


# ============================================================
# 1. CONCEPTOS FUNDAMENTALES
# ============================================================

# RAÍZ
#
# Es el primer nodo del árbol.
#
#
# Ejemplo:
#
# Ciencia
#
# sería la raíz.
#
#
# ------------------------------------------------------------
#
# PADRE
#
# Un nodo que tiene otros nodos debajo.
#
#
# Ciencia
# ├── Física
# └── Computación
#
#
# Ciencia es padre de:
#
# Física
# Computación
#
#
# ------------------------------------------------------------
#
# HIJO
#
# Nodo conectado debajo de otro nodo.
#
#
# Física
#
# es hijo de Ciencia.
#
#
# ------------------------------------------------------------
#
# HOJA
#
# Nodo que no tiene hijos.
#
#
# Ejemplo:
#
# Relatividad
#
# si no tiene elementos debajo,
# es una hoja.
#
#
# ------------------------------------------------------------
#
# HERMANOS
#
# Nodos que tienen el mismo padre.
#
#
# Física y Computación
#
# son hermanos porque ambos
# dependen de Ciencia.


# ============================================================
# 2. DIFERENCIA CON UNA LISTA ENLAZADA
# ============================================================

# En una lista enlazada utilizábamos:
#
# self.siguiente
#
#
# porque cada nodo apuntaba normalmente
# a un único siguiente nodo.
#
#
# Ejemplo:
#
# Einstein
# ↓
# Tesla
# ↓
# Turing
#
#
# En un árbol necesitaremos algo diferente:
#
# self.hijos
#
#
# porque un nodo puede tener:
#
# 0 hijos
# 1 hijo
# varios hijos


# ============================================================
# 3. CREAR UN NODO DE ÁRBOL
# ============================================================


class NodoArbol:

    def __init__(self, valor):
        self.valor = valor
        self.hijos = []


# Cada nodo contiene:
#
# valor
#
# y
#
# hijos
#
#
# hijos es una lista porque un nodo
# puede tener varios nodos debajo.


# ============================================================
# 4. CREAR LA RAÍZ
# ============================================================

raiz_ciencia = NodoArbol(
    "Ciencia"
)


print(
    raiz_ciencia.valor
)


print(
    raiz_ciencia.hijos
)


# Resultado inicial:
#
# Ciencia
# []
#
#
# El nodo existe,
# pero todavía no tiene hijos.


# ============================================================
# 5. CREAR NODOS HIJOS
# ============================================================

fisica = NodoArbol(
    "Física"
)


computacion = NodoArbol(
    "Computación"
)


# De momento siguen siendo
# objetos independientes.
#
# Todavía debemos conectarlos
# con la raíz.


# ============================================================
# 6. CONECTAR LOS NODOS
# ============================================================

raiz_ciencia.hijos.append(
    fisica
)


raiz_ciencia.hijos.append(
    computacion
)


# Ahora tenemos:
#
#           Ciencia
#          /       \
#     Física       Computación


# ============================================================
# 7. LOS HIJOS SON OBJETOS
# ============================================================

print(
    raiz_ciencia.hijos[0].valor
)


print(
    raiz_ciencia.hijos[1].valor
)


# raiz_ciencia.hijos[0]
#
# contiene el objeto:
#
# fisica
#
#
# Por eso:
#
# raiz_ciencia.hijos[0].valor
#
# devuelve:
#
# Física


# ============================================================
# 8. AGREGAR OTRO NIVEL
# ============================================================

relatividad = NodoArbol(
    "Relatividad"
)


mecanica_cuantica = NodoArbol(
    "Mecánica cuántica"
)


python = NodoArbol(
    "Python"
)


fisica.hijos.append(
    relatividad
)


fisica.hijos.append(
    mecanica_cuantica
)


computacion.hijos.append(
    python
)


# Ahora:
#
#                 Ciencia
#                /       \
#           Física       Computación
#          /     \            |
# Relatividad   Mecánica      Python
#               cuántica


# ============================================================
# 9. IDENTIFICAR PADRES E HIJOS
# ============================================================

# Ciencia:
#
# padre de:
#
# Física
# Computación
#
#
# Física:
#
# hijo de Ciencia
#
# y al mismo tiempo padre de:
#
# Relatividad
# Mecánica cuántica
#
#
# Un nodo puede ser:
#
# hijo de otro nodo
#
# y también:
#
# padre de otros nodos.


# ============================================================
# 10. NODOS HOJA
# ============================================================

# Una hoja no tiene hijos.
#
#
# Por ejemplo:
#
# relatividad.hijos
#
# contiene:
#
# []


print(
    relatividad.hijos
)


# Podemos comprobarlo:


if not relatividad.hijos:

    print(
        "Relatividad es una hoja."
    )


# Una lista vacía se evalúa como False.
#
# Por eso:
#
# not relatividad.hijos
#
# será True.


# ============================================================
# 11. MÉTODO PARA AGREGAR HIJOS
# ============================================================

# Podemos mejorar nuestra clase y encapsular
# esta operación dentro de un método.


class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(
        self,
        nodo
    ):
        self.hijos.append(
            nodo
        )


# Ahora podemos hacer:


raiz = Nodo(
    "Ciencia"
)


fisica_nodo = Nodo(
    "Física"
)


computacion_nodo = Nodo(
    "Computación"
)


raiz.agregar_hijo(
    fisica_nodo
)


raiz.agregar_hijo(
    computacion_nodo
)


# Esto:
#
# raiz.agregar_hijo(fisica_nodo)
#
# internamente hace:
#
# self.hijos.append(nodo)


# ============================================================
# 12. MÉTODO es_hoja()
# ============================================================

class NodoCompleto:

    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(
        self,
        nodo
    ):
        self.hijos.append(
            nodo
        )

    def es_hoja(self):
        return not self.hijos


nodo_galileo = NodoCompleto(
    "Galileo Galilei"
)


print(
    nodo_galileo.es_hoja()
)


# Resultado:
#
# True
#
#
# porque todavía:
#
# nodo_galileo.hijos
#
# está vacío.


# ============================================================
# 13. RECORRER HIJOS DIRECTOS
# ============================================================

raiz_personajes = Nodo(
    "Científicos"
)


einstein = Nodo(
    "Albert Einstein"
)

tesla = Nodo(
    "Nikola Tesla"
)

turing = Nodo(
    "Alan Turing"
)


raiz_personajes.agregar_hijo(
    einstein
)

raiz_personajes.agregar_hijo(
    tesla
)

raiz_personajes.agregar_hijo(
    turing
)


for hijo in raiz_personajes.hijos:

    print(
        hijo.valor
    )


# Resultado:
#
# Albert Einstein
# Nikola Tesla
# Alan Turing


# ============================================================
# 14. ACCEDER A UN HIJO DE UN HIJO
# ============================================================

fisica_nodo.agregar_hijo(
    Nodo(
        "Relatividad"
    )
)


print(
    fisica_nodo.hijos[0].valor
)


# Tenemos:
#
# Ciencia
# ↓
# Física
# ↓
# Relatividad


# ============================================================
# 15. EL ÁRBOL NO ES NECESARIAMENTE BINARIO
# ============================================================

# A veces escucharás:
#
# árbol binario
#
#
# Un árbol binario es un tipo particular
# de árbol donde cada nodo puede tener
# como máximo:
#
# 2 hijos.
#
#
# Habitualmente se habla de:
#
# hijo izquierdo
# hijo derecho
#
#
# Ejemplo:
#
#          A
#         / \
#        B   C
#
#
# Pero NO todos los árboles son binarios.
#
#
# Nuestro ejemplo:
#
# self.hijos = []
#
# permite que un nodo tenga tantos hijos
# como necesitemos.


# ============================================================
# 16. ÁRBOL GENERAL
# ============================================================

# La estructura que estamos construyendo es
# un árbol general.
#
#
# Por ejemplo:
#
#                 Sistema
#              /     |      \
#          Usuarios Tickets Reportes
#
#
# "Sistema"
#
# tiene tres hijos.
#
#
# Esto no sería posible en un árbol binario
# sin utilizar otra representación.


# ============================================================
# 17. EJEMPLO: ESTRUCTURA DE UNA EMPRESA
# ============================================================

empresa = Nodo(
    "Empresa"
)


administracion = Nodo(
    "Administración"
)

desarrollo = Nodo(
    "Desarrollo"
)

soporte = Nodo(
    "Soporte"
)


empresa.agregar_hijo(
    administracion
)

empresa.agregar_hijo(
    desarrollo
)

empresa.agregar_hijo(
    soporte
)


backend = Nodo(
    "Backend"
)

frontend = Nodo(
    "Frontend"
)


desarrollo.agregar_hijo(
    backend
)

desarrollo.agregar_hijo(
    frontend
)


# Estructura:
#
# Empresa
# ├── Administración
# ├── Desarrollo
# │   ├── Backend
# │   └── Frontend
# └── Soporte


# ============================================================
# 18. RECORRER TODO EL ÁRBOL
# ============================================================

# Recorrer solamente:
#
# empresa.hijos
#
# muestra:
#
# Administración
# Desarrollo
# Soporte
#
#
# Pero no mostraría automáticamente:
#
# Backend
# Frontend
#
#
# porque esos nodos están dentro de:
#
# desarrollo.hijos
#
#
# Necesitamos recorrer distintos niveles.


# ============================================================
# 19. RECORRIDO UTILIZANDO UNA PILA
# ============================================================

# Podemos reutilizar algo que ya estudiamos:
#
# PILAS.
#
#
# La idea será:
#
# 1. poner la raíz en la pila;
# 2. sacar un nodo;
# 3. procesarlo;
# 4. agregar sus hijos;
# 5. repetir.


pila = [
    empresa
]


while pila:

    nodo_actual = pila.pop()

    print(
        nodo_actual.valor
    )

    for hijo in reversed(
        nodo_actual.hijos
    ):

        pila.append(
            hijo
        )


# Con reversed() agregamos los hijos
# en orden inverso a la pila.
#
# Esto permite que al utilizar pop()
# se procesen siguiendo el orden
# visual en que fueron agregados.


# ============================================================
# 20. VISUALIZAR EL RECORRIDO
# ============================================================

# Inicialmente:
#
# pila:
#
# Empresa
#
#
# sacamos:
#
# Empresa
#
#
# agregamos:
#
# Soporte
# Desarrollo
# Administración
#
#
# como pop() retira el último:
#
# Administración
#
# será procesado primero.
#
#
# Después:
#
# Desarrollo
#
# agrega:
#
# Backend
# Frontend
#
#
# y el recorrido continúa.


# ============================================================
# 21. NO MEMORIZAR TODAVÍA ALGORITMOS
# ============================================================

# Este tipo de recorrido está relacionado con:
#
# búsqueda en profundidad
#
# o:
#
# DFS
#
# Depth-First Search
#
#
# Pero NO necesitamos estudiar todavía
# el algoritmo formalmente.
#
#
# Eso corresponde mejor al bloque:
#
# 13_algoritmos_y_complejidad
#
#
# Aquí solamente queremos entender:
#
# podemos recorrer un árbol siguiendo
# sus conexiones entre nodos.


# ============================================================
# 22. EJEMPLO DE CARPETAS
# ============================================================

proyecto = Nodo(
    "proyecto"
)


src = Nodo(
    "src"
)

tests = Nodo(
    "tests"
)

docs = Nodo(
    "docs"
)


proyecto.agregar_hijo(
    src
)

proyecto.agregar_hijo(
    tests
)

proyecto.agregar_hijo(
    docs
)


backend_archivo = Nodo(
    "backend.py"
)

frontend_archivo = Nodo(
    "frontend.py"
)


src.agregar_hijo(
    backend_archivo
)

src.agregar_hijo(
    frontend_archivo
)


# Estructura:
#
# proyecto
# ├── src
# │   ├── backend.py
# │   └── frontend.py
# ├── tests
# └── docs
#
#
# Un sistema de archivos es un excelente ejemplo
# para visualizar una estructura jerárquica.


# ============================================================
# 23. NIVELES DEL ÁRBOL
# ============================================================

# Podemos pensar el árbol por niveles.
#
#
# NIVEL 0:
#
# proyecto
#
#
# NIVEL 1:
#
# src
# tests
# docs
#
#
# NIVEL 2:
#
# backend.py
# frontend.py
#
#
# La raíz suele considerarse nivel 0.


# ============================================================
# 24. PROFUNDIDAD
# ============================================================

# La profundidad indica qué tan lejos
# se encuentra un nodo respecto de la raíz.
#
#
# proyecto
#
# profundidad 0
#
#
# src
#
# profundidad 1
#
#
# backend.py
#
# profundidad 2
#
#
# No necesitamos calcularla todavía.
#
# Por ahora basta comprender el concepto.


# ============================================================
# 25. ALTURA
# ============================================================

# También encontrarás el concepto:
#
# altura de un árbol.
#
#
# Está relacionado con la distancia
# desde un nodo hasta los nodos
# más profundos debajo de él.
#
#
# La definición exacta puede expresarse
# de distintas maneras según se cuenten
# nodos o aristas.
#
# No necesitamos calcularla todavía.


# ============================================================
# 26. ÁRBOL VACÍO
# ============================================================

# Si no tenemos una raíz:
#
# raiz = None
#
#
# podemos considerar que todavía
# no existe ningún nodo en el árbol.
#
#
# Esto es parecido a lo que vimos
# con una lista enlazada vacía:
#
# cabeza = None


# ============================================================
# 27. RELACIÓN CON LISTAS ENLAZADAS
# ============================================================

# LISTA ENLAZADA:
#
# Nodo
# |
# siguiente
# ↓
# Nodo
#
#
# ÁRBOL:
#
# Nodo
# |
# hijos
# ├── Nodo
# ├── Nodo
# └── Nodo
#
#
# En ambos casos trabajamos con:
#
# objetos
# referencias
# conexiones
# recorridos


# ============================================================
# 28. RELACIÓN CON POO
# ============================================================

# Nuevamente utilizamos:
#
# clase
# objetos
# atributos
# métodos
#
#
# Nodo:
#
# representa una entidad.
#
#
# hijos:
#
# almacena relaciones con otros objetos Nodo.
#
#
# agregar_hijo():
#
# modifica la estructura.


# ============================================================
# 29. ¿CUÁNDO TIENE SENTIDO UN ÁRBOL?
# ============================================================

# Un árbol resulta especialmente útil
# cuando los datos forman una jerarquía.
#
#
# Ejemplos:
#
# empresa
# ↓
# departamentos
# ↓
# equipos
#
#
# carpetas
# ↓
# subcarpetas
# ↓
# archivos
#
#
# categoría
# ↓
# subcategorías
#
#
# menú
# ↓
# opciones
# ↓
# subopciones


# ============================================================
# 30. CUÁNDO NO NECESITAMOS UN ÁRBOL
# ============================================================

# Si solamente necesitamos almacenar:
#
# una secuencia sencilla
#
# probablemente una:
#
# list
#
# sea suficiente.
#
#
# Si necesitamos:
#
# clave → valor
#
# probablemente:
#
# dict
#
#
# Si necesitamos:
#
# orden de llegada
#
# probablemente:
#
# deque
#
#
# La estructura debe responder
# a la naturaleza del problema.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# ÁRBOL:
#
# estructura jerárquica formada por nodos.
#
#
# ------------------------------------------------------------
#
# RAÍZ:
#
# primer nodo del árbol.
#
#
# ------------------------------------------------------------
#
# PADRE:
#
# nodo que contiene hijos.
#
#
# ------------------------------------------------------------
#
# HIJO:
#
# nodo ubicado debajo de otro.
#
#
# ------------------------------------------------------------
#
# HOJA:
#
# nodo sin hijos.
#
#
# ------------------------------------------------------------
#
# EJEMPLO:
#
#                 Ciencia
#                /       \
#           Física       Computación
#          /     \            |
# Relatividad   Mecánica      Python
#
#
# ------------------------------------------------------------
#
# IMPLEMENTACIÓN BÁSICA:
#
# class Nodo:
#
#     def __init__(self, valor):
#         self.valor = valor
#         self.hijos = []
#
#
# ------------------------------------------------------------
#
# AGREGAR HIJO:
#
# padre.hijos.append(hijo)
#
#
# o mediante:
#
# padre.agregar_hijo(hijo)
#
#
# ------------------------------------------------------------
#
# HOJA:
#
# nodo.hijos == []
#
#
# ------------------------------------------------------------
#
# DIFERENCIA CON LISTA ENLAZADA:
#
# lista enlazada:
#
# un siguiente
#
#
# árbol:
#
# varios hijos posibles
#
#
# ------------------------------------------------------------
#
# CONCEPTO MÁS IMPORTANTE:
#
# un árbol representa relaciones jerárquicas.
#
#
# ------------------------------------------------------------
#
# SIGUIENTE TEMA:
#
# GRAFOS
#
# donde las conexiones ya no necesitan
# seguir una estructura jerárquica.