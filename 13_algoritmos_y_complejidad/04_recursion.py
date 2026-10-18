# ============================================================
# RECURSIÓN
# ============================================================
#
# Recursión:
#
# una función se llama a sí misma
# para resolver una versión más pequeña
# del mismo problema.
#
#
# Una función recursiva necesita:
#
# 1. caso base;
# 2. caso recursivo;
# 3. avanzar hacia el caso base.


# ============================================================
# 1. EJEMPLO BÁSICO
# ============================================================

def cuenta_regresiva(numero):

    if numero == 0:
        print("Fin")
        return

    print(numero)

    cuenta_regresiva(
        numero - 1
    )


cuenta_regresiva(3)


# Resultado:
#
# 3
# 2
# 1
# Fin


# ============================================================
# 2. CASO BASE
# ============================================================

# El caso base indica cuándo
# debe detenerse la recursión.
#
#
# En el ejemplo:
#
# numero == 0
#
# significa:
#
# ya no necesitamos continuar.


def ejemplo_base(numero):

    if numero == 0:
        return

    ejemplo_base(
        numero - 1
    )


# ============================================================
# 3. CASO RECURSIVO
# ============================================================

# Esta llamada:
#
# ejemplo_base(numero - 1)
#
# es el caso recursivo.
#
#
# La función vuelve a llamarse,
# pero con un problema más pequeño.
#
#
# 3
# ↓
# 2
# ↓
# 1
# ↓
# 0


# ============================================================
# 4. PROGRESO HACIA EL CASO BASE
# ============================================================

# La llamada recursiva debe acercarse
# al caso base.
#
#
# Correcto:
#
# numero - 1
#
#
# porque:
#
# 3 → 2 → 1 → 0
#
#
# Incorrecto:
#
# llamar siempre con el mismo número,
#
# porque nunca alcanzaríamos
# la condición de salida.


# ============================================================
# 5. CADA LLAMADA ES INDEPENDIENTE
# ============================================================

# Al ejecutar:
#
# cuenta_regresiva(3)
#
# conceptualmente tenemos:
#
# cuenta_regresiva(3)
# ↓
# cuenta_regresiva(2)
# ↓
# cuenta_regresiva(1)
# ↓
# cuenta_regresiva(0)
#
#
# Cada llamada posee su propio
# valor de numero.


# ============================================================
# 6. PILA DE LLAMADAS
# ============================================================

# Las llamadas anteriores esperan
# mientras se ejecuta una nueva llamada.
#
#
# Conceptualmente:
#
# ┌─────────────────────┐
# │ cuenta_regresiva(0) │
# ├─────────────────────┤
# │ cuenta_regresiva(1) │
# ├─────────────────────┤
# │ cuenta_regresiva(2) │
# ├─────────────────────┤
# │ cuenta_regresiva(3) │
# └─────────────────────┘
#
#
# Cuando llegamos al caso base,
# las llamadas comienzan a terminar.


# ============================================================
# 7. RECURSIÓN CON RETURN
# ============================================================

def sumar_hasta(numero):

    if numero == 0:
        return 0

    return numero + sumar_hasta(
        numero - 1
    )


resultado_suma = sumar_hasta(3)


print(
    "Resultado:",
    resultado_suma
)


# Desarrollo:
#
# sumar_hasta(3)
#
# 3 + sumar_hasta(2)
#
# 3 + 2 + sumar_hasta(1)
#
# 3 + 2 + 1 + sumar_hasta(0)
#
# 3 + 2 + 1 + 0
#
# 6


# ============================================================
# 8. LAS LLAMADAS TAMBIÉN DEVUELVEN VALORES
# ============================================================

# sumar_hasta(0)
# → 0
#
# sumar_hasta(1)
# → 1 + 0
# → 1
#
# sumar_hasta(2)
# → 2 + 1
# → 3
#
# sumar_hasta(3)
# → 3 + 3
# → 6


# ============================================================
# 9. EJEMPLO REAL: CARPETAS
# ============================================================

documentos = {
    "nombre": "Documentos",
    "subcarpetas": [
        {
            "nombre": "Trabajo",
            "subcarpetas": [
                {
                    "nombre": "Informes",
                    "subcarpetas": []
                },
                {
                    "nombre": "Proyectos",
                    "subcarpetas": []
                }
            ]
        },
        {
            "nombre": "Personal",
            "subcarpetas": [
                {
                    "nombre": "Fotos",
                    "subcarpetas": []
                }
            ]
        }
    ]
}


def mostrar_carpetas(
    carpeta,
    nivel=0
):

    print(
        "  " * nivel
        + carpeta["nombre"]
    )

    for subcarpeta in carpeta["subcarpetas"]:

        mostrar_carpetas(
            subcarpeta,
            nivel + 1
        )


mostrar_carpetas(
    documentos
)


# Resultado conceptual:
#
# Documentos
#   Trabajo
#     Informes
#     Proyectos
#   Personal
#     Fotos


# ============================================================
# 10. ¿POR QUÉ LA RECURSIÓN ENCAJA AQUÍ?
# ============================================================

# Una carpeta:
#
# contiene subcarpetas.
#
#
# Cada subcarpeta:
#
# vuelve a ser una carpeta.
#
#
# Por eso podemos resolver:
#
# mostrar carpeta
# ↓
# mostrar cada subcarpeta
# ↓
# aplicar nuevamente
# mostrar_carpetas()


# ============================================================
# 11. RELACIÓN CON ÁRBOLES
# ============================================================

class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.hijos = []


def mostrar_arbol(nodo):

    print(
        nodo.valor
    )

    for hijo in nodo.hijos:

        mostrar_arbol(
            hijo
        )


# Cada hijo vuelve a ser:
#
# un Nodo.
#
#
# Por eso podemos ejecutar
# exactamente la misma operación
# sobre él.


# ============================================================
# 12. RECURSIÓN VS ITERACIÓN
# ============================================================

# Iteración:
#
# for
# while
#
#
# Recursión:
#
# una función vuelve
# a llamarse a sí misma.
#
#
# Para secuencias sencillas,
# normalmente un ciclo es más directo.
#
#
# Para estructuras jerárquicas
# o anidadas,
# la recursión puede ser natural.


# ============================================================
# 13. EJEMPLO ITERATIVO
# ============================================================

def cuenta_iterativa(numero):

    while numero > 0:

        print(numero)

        numero -= 1

    print("Fin")


# ============================================================
# 14. EJEMPLO RECURSIVO
# ============================================================

def cuenta_recursiva(numero):

    if numero == 0:
        print("Fin")
        return

    print(numero)

    cuenta_recursiva(
        numero - 1
    )


# Ambos pueden resolver
# la misma cuenta regresiva.
#
#
# No utilizamos recursión
# solamente porque podamos hacerlo.


# ============================================================
# 15. RECURSIÓN INFINITA
# ============================================================

# Esto sería incorrecto:
#
#
# def ejemplo(numero):
#
#     ejemplo(numero)
#
#
# El argumento nunca cambia
# y nunca existe una condición
# que detenga correctamente
# el proceso.


# ============================================================
# 16. RECURSIONERROR
# ============================================================

# Python limita la profundidad
# de recursión.
#
#
# Si realizamos demasiadas llamadas
# recursivas podemos obtener:
#
# RecursionError
#
#
# No debemos aumentar ese límite
# simplemente para corregir
# una recursión mal diseñada.


# ============================================================
# 17. COMPLEJIDAD BÁSICA
# ============================================================

# En:
#
# cuenta_regresiva(n)
#
# realizamos aproximadamente
# una llamada por cada valor:
#
# n
# n - 1
# n - 2
# ...
# 0
#
#
# Tiempo:
#
# O(n)
#
#
# También se acumulan llamadas
# en la pila:
#
# espacio adicional
# aproximadamente O(n).


# ============================================================
# 18. CÓMO ANALIZAR RECURSIÓN
# ============================================================

# Preguntas importantes:
#
# ¿Cuál es el caso base?
#
# ¿Dónde se llama nuevamente
# la función?
#
# ¿Cómo cambia el argumento?
#
# ¿Se acerca al caso base?
#
# ¿Qué devuelve cada llamada?


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# RECURSIÓN:
#
# una función se llama
# a sí misma.
#
#
# CASO BASE:
#
# detiene la recursión.
#
#
# CASO RECURSIVO:
#
# vuelve a llamar
# a la función.
#
#
# PROGRESO:
#
# cada llamada debe acercarse
# al caso base.
#
#
# Ejemplo:
#
# 3
# ↓
# 2
# ↓
# 1
# ↓
# 0
# ↓
# terminar
#
#
# Regla práctica:
#
# estructura lineal sencilla
# → ciclo
#
# estructura naturalmente
# jerárquica o anidada
# → considerar recursión