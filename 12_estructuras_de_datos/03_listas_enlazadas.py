# ============================================================
# LISTAS ENLAZADAS
# ============================================================
#
# Una lista enlazada es una estructura formada por:
#
# NODOS
#
# Cada nodo contiene normalmente:
#
# - un valor;
# - una referencia al siguiente nodo.
#
#
# ESTRUCTURA:
#
# Nodo A
#    ↓
# Nodo B
#    ↓
# Nodo C
#    ↓
# None
#
#
# En este archivo estudiaremos:
#
# - qué es un nodo;
# - qué significa "siguiente";
# - cómo conectar nodos;
# - qué es la cabeza de una lista;
# - cómo recorrer una lista enlazada;
# - cómo agregar elementos;
# - cómo buscar elementos.
#
#
# El objetivo principal NO es reemplazar las listas
# normales de Python.
#
# El objetivo es comprender:
#
# referencias
# nodos
# enlaces
# recorridos
#
# porque estas ideas aparecerán nuevamente
# en árboles y grafos.


# ============================================================
# 1. LISTA DE PYTHON VS LISTA ENLAZADA
# ============================================================

# Una lista normal de Python puede verse así:


cientificos = [
    "Albert Einstein",
    "Nikola Tesla",
    "Alan Turing"
]


print(cientificos)


# Accedemos directamente:
#
# cientificos[0]
# cientificos[1]
# cientificos[2]


print(
    cientificos[1]
)


# Una lista enlazada funciona conceptualmente distinto.
#
#
# No pensamos:
#
# posición 0
# posición 1
# posición 2
#
#
# Pensamos:
#
# nodo actual
# ↓
# siguiente nodo
# ↓
# siguiente nodo
# ↓
# ...


# ============================================================
# 2. QUÉ ES UN NODO
# ============================================================

# Crearemos una clase muy sencilla.


class Nodo:

    def __init__(
        self,
        valor
    ):
        self.valor = valor
        self.siguiente = None


# Cada Nodo contiene:
#
# valor
# → dato almacenado
#
#
# siguiente
# → referencia al próximo nodo
#
#
# Inicialmente:
#
# siguiente = None
#
# porque todavía no está conectado con nada.


# ============================================================
# 3. CREAR UN NODO
# ============================================================

nodo_einstein = Nodo(
    "Albert Einstein"
)


print(
    nodo_einstein.valor
)


print(
    nodo_einstein.siguiente
)


# Resultado:
#
# Albert Einstein
# None
#
#
# Tenemos:
#
# nodo_einstein
#
# valor:
# "Albert Einstein"
#
# siguiente:
# None


# ============================================================
# 4. CREAR VARIOS NODOS
# ============================================================

nodo_tesla = Nodo(
    "Nikola Tesla"
)


nodo_turing = Nodo(
    "Alan Turing"
)


# Ahora tenemos tres objetos independientes:
#
# nodo_einstein
# nodo_tesla
# nodo_turing
#
#
# Todavía NO están conectados.


# ============================================================
# 5. CONECTAR NODOS
# ============================================================

nodo_einstein.siguiente = (
    nodo_tesla
)


nodo_tesla.siguiente = (
    nodo_turing
)


# Ahora tenemos:
#
# Einstein
#    ↓
# Tesla
#    ↓
# Turing
#    ↓
# None


# ============================================================
# 6. LA REFERENCIA "SIGUIENTE"
# ============================================================

print(
    nodo_einstein.siguiente.valor
)


# nodo_einstein.siguiente
#
# representa:
#
# nodo_tesla
#
#
# Por eso:
#
# nodo_einstein.siguiente.valor
#
# devuelve:
#
# Nikola Tesla


# ============================================================
# 7. AVANZAR DOS NODOS
# ============================================================

print(
    nodo_einstein
    .siguiente
    .siguiente
    .valor
)


# Conceptualmente:
#
# Einstein
# ↓
# Tesla
# ↓
# Turing
#
#
# Resultado:
#
# Alan Turing


# ============================================================
# 8. QUÉ SIGNIFICA None
# ============================================================

print(
    nodo_turing.siguiente
)


# Resultado:
#
# None
#
#
# Esto representa:
#
# fin de la lista
#
#
# Turing
# ↓
# None


# ============================================================
# 9. CABEZA DE LA LISTA
# ============================================================

# Normalmente necesitamos saber dónde comienza
# la lista enlazada.
#
# Ese primer nodo suele llamarse:
#
# cabeza
#
# o:
#
# head


cabeza = nodo_einstein


# Tenemos:
#
# cabeza
# ↓
# Einstein
# ↓
# Tesla
# ↓
# Turing
# ↓
# None


# ============================================================
# 10. RECORRER UNA LISTA ENLAZADA
# ============================================================

# No utilizamos índices.
#
# Empezamos desde:
#
# cabeza
#
# y avanzamos usando:
#
# siguiente


actual = cabeza


while actual is not None:

    print(
        actual.valor
    )

    actual = actual.siguiente


# Este es uno de los patrones más importantes
# del tema.
#
#
# PASO 1:
#
# actual = Einstein
#
#
# PASO 2:
#
# actual = Tesla
#
#
# PASO 3:
#
# actual = Turing
#
#
# PASO 4:
#
# actual = None
#
#
# termina el while.


# ============================================================
# 11. VISUALIZAR EL RECORRIDO
# ============================================================

# cabeza
#   ↓
#
# [ Einstein | siguiente ]
#                 ↓
#          [ Tesla | siguiente ]
#                       ↓
#                [ Turing | None ]


# ============================================================
# 12. EL OBJETO actual NO ES EL DATO
# ============================================================

# Esto es importante.
#
#
# actual
#
# contiene un Nodo.
#
#
# actual.valor
#
# contiene el dato almacenado.
#
#
# actual.siguiente
#
# contiene la referencia al siguiente Nodo.


# ============================================================
# 13. LISTA ENLAZADA COMO CLASE
# ============================================================

# Hasta ahora conectamos nodos manualmente.
#
# Podemos crear una clase para administrar
# la estructura completa.


class ListaEnlazada:

    def __init__(self):
        self.cabeza = None


# Una lista recién creada:
#
# cabeza
# ↓
# None
#
#
# porque todavía no contiene nodos.


lista = ListaEnlazada()


print(
    lista.cabeza
)


# ============================================================
# 14. AGREGAR AL INICIO
# ============================================================

class ListaEnlazadaInicio:

    def __init__(self):
        self.cabeza = None

    def agregar_inicio(
        self,
        valor
    ):

        nuevo_nodo = Nodo(
            valor
        )

        nuevo_nodo.siguiente = (
            self.cabeza
        )

        self.cabeza = (
            nuevo_nodo
        )


# Este método puede parecer extraño inicialmente.
#
# Veámoslo paso a paso.


lista_inicio = (
    ListaEnlazadaInicio()
)


lista_inicio.agregar_inicio(
    "Albert Einstein"
)


# Inicialmente:
#
# cabeza
# ↓
# None
#
#
# Creamos:
#
# Einstein
# ↓
# None
#
#
# Ahora:
#
# cabeza
# ↓
# Einstein


lista_inicio.agregar_inicio(
    "Nikola Tesla"
)


# Antes:
#
# cabeza
# ↓
# Einstein
#
#
# Nuevo nodo:
#
# Tesla
#
#
# hacemos:
#
# Tesla.siguiente = Einstein
#
#
# y luego:
#
# cabeza = Tesla
#
#
# Resultado:
#
# Tesla
# ↓
# Einstein
# ↓
# None


# ============================================================
# 15. RECORRER LA LISTA
# ============================================================

actual = lista_inicio.cabeza


while actual is not None:

    print(
        actual.valor
    )

    actual = actual.siguiente


# Resultado:
#
# Nikola Tesla
# Albert Einstein
#
#
# Tesla aparece primero porque fue agregado
# al inicio después de Einstein.


# ============================================================
# 16. AGREGAR AL FINAL
# ============================================================

# En muchos casos queremos mantener:
#
# Einstein
# ↓
# Tesla
# ↓
# Turing
#
#
# según el orden en que fueron agregados.


class ListaEnlazadaCompleta:

    def __init__(self):
        self.cabeza = None

    def agregar_final(
        self,
        valor
    ):

        nuevo_nodo = Nodo(
            valor
        )

        # Si la lista está vacía:
        if self.cabeza is None:

            self.cabeza = nuevo_nodo

            return

        # Si ya existen nodos:
        actual = self.cabeza

        while (
            actual.siguiente
            is not None
        ):

            actual = (
                actual.siguiente
            )

        actual.siguiente = (
            nuevo_nodo
        )


# ============================================================
# 17. ENTENDER agregar_final()
# ============================================================

# Tenemos:
#
# Einstein
# ↓
# Tesla
# ↓
# None
#
#
# Queremos agregar:
#
# Turing
#
#
# Empezamos desde la cabeza.
#
# Mientras exista:
#
# actual.siguiente
#
# avanzamos.
#
#
# Cuando encontramos:
#
# siguiente = None
#
# significa:
#
# llegamos al último nodo.
#
#
# Entonces:
#
# actual.siguiente = nuevo_nodo


# ============================================================
# 18. UTILIZAR agregar_final()
# ============================================================

lista_cientificos = (
    ListaEnlazadaCompleta()
)


lista_cientificos.agregar_final(
    "Albert Einstein"
)

lista_cientificos.agregar_final(
    "Nikola Tesla"
)

lista_cientificos.agregar_final(
    "Alan Turing"
)


# Estructura:
#
# Einstein
# ↓
# Tesla
# ↓
# Turing
# ↓
# None


# ============================================================
# 19. MÉTODO PARA RECORRER
# ============================================================

# Podemos incorporar el recorrido dentro de la clase.


class ListaEnlazadaRecorrible:

    def __init__(self):
        self.cabeza = None

    def agregar_final(
        self,
        valor
    ):

        nuevo_nodo = Nodo(
            valor
        )

        if self.cabeza is None:

            self.cabeza = nuevo_nodo

            return

        actual = self.cabeza

        while (
            actual.siguiente
            is not None
        ):

            actual = (
                actual.siguiente
            )

        actual.siguiente = (
            nuevo_nodo
        )

    def mostrar(self):

        actual = self.cabeza

        while actual is not None:

            print(
                actual.valor
            )

            actual = (
                actual.siguiente
            )


lista_programadores = (
    ListaEnlazadaRecorrible()
)


lista_programadores.agregar_final(
    "Ada Lovelace"
)

lista_programadores.agregar_final(
    "Alan Turing"
)

lista_programadores.agregar_final(
    "Grace Hopper"
)


lista_programadores.mostrar()


# ============================================================
# 20. BUSCAR UN VALOR
# ============================================================

# Podemos utilizar exactamente el mismo patrón
# de recorrido para buscar.


class ListaEnlazadaBusqueda:

    def __init__(self):
        self.cabeza = None

    def agregar_final(
        self,
        valor
    ):

        nuevo_nodo = Nodo(
            valor
        )

        if self.cabeza is None:

            self.cabeza = nuevo_nodo

            return

        actual = self.cabeza

        while (
            actual.siguiente
            is not None
        ):

            actual = (
                actual.siguiente
            )

        actual.siguiente = (
            nuevo_nodo
        )

    def contiene(
        self,
        valor_buscado
    ):

        actual = self.cabeza

        while actual is not None:

            if (
                actual.valor
                == valor_buscado
            ):

                return True

            actual = (
                actual.siguiente
            )

        return False


lista_busqueda = (
    ListaEnlazadaBusqueda()
)


lista_busqueda.agregar_final(
    "Albert Einstein"
)

lista_busqueda.agregar_final(
    "Carl Sagan"
)

lista_busqueda.agregar_final(
    "Stephen Hawking"
)


print(
    lista_busqueda.contiene(
        "Carl Sagan"
    )
)


print(
    lista_busqueda.contiene(
        "Nikola Tesla"
    )
)


# Resultado:
#
# True
# False


# ============================================================
# 21. POR QUÉ LA BÚSQUEDA RECORRE LOS NODOS
# ============================================================

# No tenemos algo equivalente a:
#
# lista[5]
#
# para saltar directamente a un nodo arbitrario
# de esta implementación.
#
#
# Empezamos desde:
#
# cabeza
#
# y seguimos:
#
# siguiente
# siguiente
# siguiente
#
# hasta:
#
# encontrar el dato
#
# o:
#
# llegar a None.


# ============================================================
# 22. EJEMPLO REAL: CADENA DE TAREAS
# ============================================================

tarea_uno = Nodo(
    "Validar solicitud"
)


tarea_dos = Nodo(
    "Procesar solicitud"
)


tarea_tres = Nodo(
    "Registrar resultado"
)


tarea_uno.siguiente = (
    tarea_dos
)


tarea_dos.siguiente = (
    tarea_tres
)


tarea_actual = tarea_uno


while tarea_actual is not None:

    print(
        "Procesando:",
        tarea_actual.valor
    )

    tarea_actual = (
        tarea_actual.siguiente
    )


# Estructura:
#
# Validar solicitud
# ↓
# Procesar solicitud
# ↓
# Registrar resultado
# ↓
# None


# ============================================================
# 23. EJEMPLO CON AUTOS CLÁSICOS
# ============================================================

auto_uno = Nodo(
    "Chevrolet Bel Air"
)

auto_dos = Nodo(
    "Ford Mustang"
)

auto_tres = Nodo(
    "Chevrolet Camaro 1967"
)


auto_uno.siguiente = auto_dos
auto_dos.siguiente = auto_tres


auto_actual = auto_uno


while auto_actual is not None:

    print(
        auto_actual.valor
    )

    auto_actual = (
        auto_actual.siguiente
    )


# ============================================================
# 24. QUÉ HEMOS COMBINADO
# ============================================================

# Para construir una lista enlazada utilizamos:
#
# POO
# → clase Nodo
#
# atributos
# → valor / siguiente
#
# None
# → final de la estructura
#
# referencias
# → siguiente nodo
#
# while
# → recorrido
#
# condicionales
# → comprobar lista vacía
#
# métodos
# → agregar / buscar / mostrar
#
#
# Esto demuestra cómo los conocimientos anteriores
# comienzan a combinarse.


# ============================================================
# 25. ¿POR QUÉ ESTUDIAR ESTO EN PYTHON?
# ============================================================

# En Python normalmente utilizaremos:
#
# list
# deque
# dict
# set
#
# para la mayoría de aplicaciones.
#
#
# No es habitual implementar manualmente
# una lista enlazada para tareas normales.
#
#
# Sin embargo, estudiarla es útil porque permite
# comprender:
#
# - referencias;
# - estructuras conectadas;
# - nodos;
# - recorridos;
# - relaciones entre elementos.
#
#
# Estos conceptos serán fundamentales en:
#
# árboles
# grafos
# algunos algoritmos


# ============================================================
# 26. LISTA ENLAZADA SIMPLE
# ============================================================

# La estructura que estamos estudiando se denomina:
#
# lista simplemente enlazada
#
#
# Porque cada nodo conoce solamente:
#
# siguiente
#
#
# Nodo
# ↓
# Nodo
# ↓
# Nodo
#
#
# Existe también:
#
# lista doblemente enlazada
#
# donde cada nodo podría tener:
#
# anterior
# siguiente
#
#
# Pero NO necesitamos estudiarla ahora.


# ============================================================
# 27. NO CONFUNDIR CON list
# ============================================================

# Python:
#
# lista = [
#     "A",
#     "B",
#     "C"
# ]
#
# es un objeto list incorporado.
#
#
# Una lista enlazada:
#
# Nodo A
# ↓
# Nodo B
# ↓
# Nodo C
#
# es otra estructura diferente.
#
#
# Aunque ambas pueden almacenar
# una secuencia de datos.


# ============================================================
# 28. CONCEPTO CLAVE: REFERENCIA
# ============================================================

# Cuando hacemos:
#
# nodo_uno.siguiente = nodo_dos
#
#
# no estamos copiando solamente:
#
# nodo_dos.valor
#
#
# Estamos guardando una referencia
# al objeto nodo_dos.
#
#
# Por eso después podemos hacer:
#
# nodo_uno.siguiente.valor
#
# y acceder al dato del segundo nodo.


# ============================================================
# 29. LA CABEZA ES EL PUNTO DE ENTRADA
# ============================================================

# Una lista enlazada necesita normalmente
# una referencia al primer nodo:
#
# cabeza
#
#
# Si perdemos la referencia a la cabeza,
# ya no tenemos nuestro punto normal de entrada
# para recorrer toda la estructura.
#
#
# Por eso una clase ListaEnlazada suele contener:
#
# self.cabeza


# ============================================================
# 30. PATRÓN MÁS IMPORTANTE DEL ARCHIVO
# ============================================================

# Este patrón debes reconocer:


# actual = cabeza
#
# while actual is not None:
#
#     usar(actual.valor)
#
#     actual = actual.siguiente


# Significa:
#
# empezar
# ↓
# usar nodo
# ↓
# avanzar
# ↓
# usar nodo
# ↓
# avanzar
# ↓
# ...
# ↓
# None
# ↓
# terminar


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# LISTA ENLAZADA:
#
# conjunto de nodos conectados.
#
#
# ------------------------------------------------------------
#
# NODO:
#
# contiene:
#
# valor
# +
# siguiente
#
#
# ------------------------------------------------------------
#
# EJEMPLO:
#
# Einstein
# ↓
# Tesla
# ↓
# Turing
# ↓
# None
#
#
# ------------------------------------------------------------
#
# CLASE BÁSICA:
#
# class Nodo:
#
#     def __init__(self, valor):
#
#         self.valor = valor
#         self.siguiente = None
#
#
# ------------------------------------------------------------
#
# CONECTAR:
#
# nodo_uno.siguiente = nodo_dos
#
#
# ------------------------------------------------------------
#
# CABEZA:
#
# referencia al primer nodo.
#
#
# ------------------------------------------------------------
#
# RECORRER:
#
# actual = cabeza
#
# while actual is not None:
#
#     print(actual.valor)
#
#     actual = actual.siguiente
#
#
# ------------------------------------------------------------
#
# None:
#
# representa el final
# de la lista.
#
#
# ------------------------------------------------------------
#
# CONCEPTO MÁS IMPORTANTE:
#
# cada nodo conoce al siguiente.
#
#
# ------------------------------------------------------------
#
# SIGUIENTE TEMA:
#
# ÁRBOLES
#
# donde un nodo podrá tener
# múltiples nodos hijos.