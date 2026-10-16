# ============================================================
# BÚSQUEDAS EN PYTHON
# ============================================================
#
# Buscar significa:
#
# encontrar un elemento
# dentro de una colección.
#
#
# Ejemplos:
#
# encontrar un usuario por nombre;
# encontrar un ticket por ID;
# encontrar un número;
# encontrar un producto;
# encontrar un archivo;
# encontrar un registro.
#
#
# En este archivo estudiaremos:
#
# - búsqueda lineal;
# - búsqueda binaria;
# - diferencias entre ambas;
# - índices;
# - uso de enumerate();
# - uso de while;
# - cálculo del punto medio;
# - importancia de tener datos ordenados;
# - relación con Big O;
# - cuándo conviene utilizar cada estrategia.
#
#
# Complejidades principales:
#
# búsqueda lineal
# → O(n)
#
#
# búsqueda binaria
# → O(log n)


# ============================================================
# 1. ¿QUÉ SIGNIFICA BUSCAR?
# ============================================================

# Supongamos que tenemos:

cientificos = [
    "Albert Einstein",
    "Nikola Tesla",
    "Alan Turing",
    "Grace Hopper"
]


# Queremos encontrar:
#
# "Alan Turing"
#
#
# Una forma natural sería revisar:
#
# Albert Einstein
# ↓
# Nikola Tesla
# ↓
# Alan Turing
#
#
# hasta encontrarlo.
#
#
# Eso es una:
#
# BÚSQUEDA LINEAL.


# ============================================================
# 2. BÚSQUEDA LINEAL
# ============================================================

# La búsqueda lineal revisa los elementos
# uno por uno.
#
#
# No necesita que la colección
# esté ordenada.
#
#
# Ejemplo:

autos_clasicos = [
    "Chevrolet Bel Air",
    "Ford Mustang",
    "Chevrolet Camaro",
    "Chevrolet Corvette"
]


objetivo = "Chevrolet Camaro"


for auto in autos_clasicos:

    if auto == objetivo:

        print(
            "Auto encontrado:",
            auto
        )

        break


# ============================================================
# 3. ¿QUÉ ESTÁ OCURRIENDO?
# ============================================================

# Python revisa:
#
# Chevrolet Bel Air
#
# ¿es Chevrolet Camaro?
# → no
#
#
# Ford Mustang
#
# ¿es Chevrolet Camaro?
# → no
#
#
# Chevrolet Camaro
#
# ¿es Chevrolet Camaro?
# → sí
#
#
# Entonces:
#
# encontramos el dato
# y usamos break.


# ============================================================
# 4. BÚSQUEDA LINEAL EN UNA FUNCIÓN
# ============================================================

def buscar_auto(
    autos,
    auto_buscado
):

    for auto in autos:

        if auto == auto_buscado:

            return True

    return False


resultado = buscar_auto(
    autos_clasicos,
    "Ford Mustang"
)


print(
    "¿Existe el auto?",
    resultado
)


# ============================================================
# 5. ¿POR QUÉ RETURN Y NO BREAK?
# ============================================================

# Dentro de una función:
#
# return
#
# no solamente termina el ciclo.
#
#
# También termina la función
# y devuelve un resultado.
#
#
# Ejemplo:
#
# si encontramos:
#
# "Ford Mustang"
#
# hacemos:
#
# return True
#
#
# y la función termina inmediatamente.


# ============================================================
# 6. SI NO ENCONTRAMOS EL ELEMENTO
# ============================================================

# Observa:
#
# return False
#
# está FUERA del for.


def existe_cientifico(
    nombres,
    buscado
):

    for nombre in nombres:

        if nombre == buscado:

            return True

    return False


# Si recorremos todo
# y nunca encontramos coincidencia:
#
# termina el for
#
# y recién entonces:
#
# return False


print(
    existe_cientifico(
        cientificos,
        "Carl Sagan"
    )
)


# ============================================================
# 7. BÚSQUEDA LINEAL Y BIG O
# ============================================================

# Supongamos:
#
# ["A", "B", "C", "D", "E"]
#
#
# buscamos:
#
# "A"
#
#
# encontramos inmediatamente.
#
#
# Pero si buscamos:
#
# "E"
#
# debemos revisar:
#
# A
# B
# C
# D
# E
#
#
# Y si buscamos:
#
# "Z"
#
# debemos revisar toda la colección.
#
#
# En el peor caso:
#
# revisamos n elementos.
#
#
# Por eso:
#
# búsqueda lineal
# → O(n)


# ============================================================
# 8. BUSCAR TAMBIÉN LA POSICIÓN
# ============================================================

# A veces no queremos solamente saber:
#
# "¿existe?"
#
#
# También queremos saber:
#
# "¿en qué posición está?"
#
#
# Para eso podemos utilizar:
#
# enumerate()


lenguajes = [
    "Python",
    "JavaScript",
    "Java",
    "C"
]


for indice, lenguaje in enumerate(
    lenguajes
):

    print(
        indice,
        lenguaje
    )


# Resultado conceptual:
#
# 0 Python
# 1 JavaScript
# 2 Java
# 3 C


# ============================================================
# 9. BÚSQUEDA LINEAL DEVOLVIENDO ÍNDICE
# ============================================================

def buscar_indice(
    elementos,
    objetivo
):

    for indice, elemento in enumerate(
        elementos
    ):

        if elemento == objetivo:

            return indice

    return None


indice_python = buscar_indice(
    lenguajes,
    "Python"
)


print(
    "Índice:",
    indice_python
)


# Si encontramos Python:
#
# devuelve:
#
# 0
#
#
# Si no encontramos el elemento:
#
# devuelve:
#
# None


# ============================================================
# 10. ¿POR QUÉ NONE?
# ============================================================

# None representa:
#
# ausencia de valor.
#
#
# Es mejor que utilizar:
#
# 0
#
# para indicar "no encontrado",
#
# porque:
#
# 0
#
# es un índice perfectamente válido.


resultado_busqueda = buscar_indice(
    lenguajes,
    "Ruby"
)


print(
    resultado_busqueda
)


# Resultado:
#
# None


# ============================================================
# 11. CUIDADO CON ESTA COMPROBACIÓN
# ============================================================

# Si buscamos un elemento
# que está en índice 0:
#
# buscar_indice(...)
#
# devuelve:
#
# 0
#
#
# Pero:
#
# bool(0)
#
# es:
#
# False.
#
#
# Por eso NO conviene hacer:

# if resultado_busqueda:
#     ...


# Para este caso es mejor:

if resultado_busqueda is not None:

    print(
        "Elemento encontrado"
    )


# Este detalle conecta con:
#
# truthiness
# y
# None
#
# que ya estudiaste anteriormente.


# ============================================================
# 12. PYTHON YA TIENE FORMAS DE BUSCAR
# ============================================================

# Para muchas situaciones reales
# no necesitamos escribir manualmente
# una búsqueda lineal.
#
#
# Podemos utilizar:
#
# in


peliculas = [
    "The Godfather",
    "The Matrix",
    "Goodfellas"
]


print(
    "The Matrix"
    in peliculas
)


# Esto devuelve:
#
# True
#
# o:
#
# False


# ============================================================
# 13. MÉTODO index()
# ============================================================

# También existe:
#
# list.index()
#
#
# Devuelve el índice
# de la primera coincidencia.


indice_matrix = peliculas.index(
    "The Matrix"
)


print(
    indice_matrix
)


# IMPORTANTE:
#
# si el elemento NO existe:
#
# index()
#
# genera:
#
# ValueError.
#
#
# Por eso debemos conocer
# el comportamiento del método
# antes de utilizarlo.


# ============================================================
# 14. ¿ENTONCES PARA QUÉ IMPLEMENTAMOS LA BÚSQUEDA?
# ============================================================

# Porque nuestro objetivo ahora
# no es reemplazar:
#
# in
#
# ni:
#
# index()
#
#
# Nuestro objetivo es entender:
#
# qué ocurre conceptualmente
# cuando buscamos información.
#
#
# Más adelante normalmente utilizaremos
# las herramientas apropiadas de Python.


# ============================================================
# 15. EL PROBLEMA DE BUSCAR UNO POR UNO
# ============================================================

# Imaginemos:
#
# 1_000_000 registros.
#
#
# Una búsqueda lineal podría necesitar
# revisar una enorme cantidad de ellos.
#
#
# Pregunta:
#
# ¿podemos aprovechar alguna propiedad
# de los datos para buscar mejor?
#
#
# Sí:
#
# si los datos están ORDENADOS.


# ============================================================
# 16. BÚSQUEDA BINARIA
# ============================================================

# La búsqueda binaria funciona sobre
# una colección ordenada.
#
#
# La idea principal es:
#
# mirar el elemento del medio
#
# y descartar aproximadamente
# la mitad de la colección.


numeros_ordenados = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90
]


# Queremos encontrar:
#
# 70


# ============================================================
# 17. IDEA VISUAL DE LA BÚSQUEDA BINARIA
# ============================================================

# Tenemos:
#
# 10 20 30 40 50 60 70 80 90
#
#
#              ↑
#             50
#
#
# buscamos:
#
# 70
#
#
# Preguntamos:
#
# ¿70 == 50?
#
# no.
#
#
# ¿70 > 50?
#
# sí.
#
#
# Entonces sabemos que:
#
# 10 20 30 40 50
#
# ya NO pueden contener la respuesta.
#
#
# Nos quedamos con:
#
# 60 70 80 90
#
#
# Acabamos de descartar
# aproximadamente la mitad
# con una sola comparación.


# ============================================================
# 18. NECESITAMOS CONTROLAR UN RANGO
# ============================================================

# Para implementar búsqueda binaria
# manejaremos tres posiciones:
#
# inicio
#
# fin
#
# medio
#
#
# Ejemplo:
#
# índice:
#
# 0  1  2  3  4
#
#
# inicio:
#
# 0
#
#
# fin:
#
# 4
#
#
# medio:
#
# 2


# ============================================================
# 19. CALCULAR LA POSICIÓN CENTRAL
# ============================================================

inicio = 0

fin = 8


medio = (
    inicio + fin
) // 2


print(
    "Posición central:",
    medio
)


# Usamos:
#
# //
#
# división entera.
#
#
# Ejemplo:
#
# 8 / 2
# → 4.0
#
#
# 8 // 2
# → 4
#
#
# Necesitamos un entero
# porque los índices de una lista
# son números enteros.


# ============================================================
# 20. RECORDATORIO SOBRE //
# ============================================================

print(
    9 // 2
)


# Resultado:
#
# 4
#
#
# La parte decimal se descarta.
#
#
# Esto es útil para calcular
# una posición central.


# ============================================================
# 21. IMPLEMENTACIÓN DE BÚSQUEDA BINARIA
# ============================================================

def busqueda_binaria(
    numeros,
    objetivo
):

    inicio = 0

    fin = len(numeros) - 1


    while inicio <= fin:

        medio = (
            inicio + fin
        ) // 2

        valor_medio = numeros[medio]


        if valor_medio == objetivo:

            return medio


        if valor_medio < objetivo:

            inicio = medio + 1

        else:

            fin = medio - 1


    return None


# ============================================================
# 22. PROBAR LA FUNCIÓN
# ============================================================

indice_encontrado = busqueda_binaria(
    numeros_ordenados,
    70
)


print(
    "Índice encontrado:",
    indice_encontrado
)


# 70 está en:
#
# índice 6


# ============================================================
# 23. EXPLICAR LA FUNCIÓN PASO A PASO
# ============================================================

# Empezamos con:

# inicio = 0

# fin = len(numeros) - 1


# Si tenemos 9 elementos:
#
# len(numeros)
#
# devuelve:
#
# 9
#
#
# pero los índices son:
#
# 0 1 2 3 4 5 6 7 8
#
#
# por eso:
#
# fin = 9 - 1
#
# fin = 8


# ============================================================
# 24. POR QUÉ while
# ============================================================

# Utilizamos:
#
# while inicio <= fin
#
#
# porque seguimos buscando
# mientras exista una zona válida
# donde podría encontrarse
# el objetivo.
#
#
# Cuando:
#
# inicio > fin
#
# significa que ya no quedan
# posiciones por revisar.


# ============================================================
# 25. PRIMERA ITERACIÓN
# ============================================================

# Lista:
#
# 10 20 30 40 50 60 70 80 90
#
#
# índices:
#
# 0  1  2  3  4  5  6  7  8
#
#
# inicio:
#
# 0
#
#
# fin:
#
# 8
#
#
# medio:
#
# (0 + 8) // 2
#
# =
#
# 4
#
#
# numeros[4]
#
# =
#
# 50


# ============================================================
# 26. COMPARACIÓN
# ============================================================

# Buscamos:
#
# 70
#
#
# valor medio:
#
# 50
#
#
# Tenemos:
#
# 50 < 70
#
#
# Por lo tanto:
#
# el objetivo debe estar
# a la DERECHA.


# ============================================================
# 27. MOVER EL INICIO
# ============================================================

# Hacemos:
#
# inicio = medio + 1
#
#
# medio era:
#
# 4
#
#
# ahora:
#
# inicio = 5
#
#
# Hemos descartado:
#
# índices:
#
# 0 1 2 3 4
#
#
# Ya no necesitamos revisarlos.


# ============================================================
# 28. SEGUNDA ITERACIÓN
# ============================================================

# Ahora:
#
# inicio = 5
#
# fin = 8
#
#
# medio:
#
# (5 + 8) // 2
#
# =
#
# 6
#
#
# numeros[6]
#
# =
#
# 70
#
#
# encontramos:
#
# objetivo == valor_medio
#
#
# entonces:
#
# return 6


# ============================================================
# 29. CUANDO EL OBJETIVO ES MENOR
# ============================================================

# Supongamos que buscamos:
#
# 20.
#
#
# Primera comparación:
#
# medio:
#
# 50
#
#
# tenemos:
#
# 50 > 20
#
#
# entonces el objetivo,
# si existe,
# debe estar a la IZQUIERDA.
#
#
# Hacemos:
#
# fin = medio - 1


# ============================================================
# 30. LAS TRES POSIBILIDADES
# ============================================================

# valor_medio == objetivo
#
# → encontrado
#
#
# valor_medio < objetivo
#
# → buscar a la derecha
#
#
# valor_medio > objetivo
#
# → buscar a la izquierda


# ============================================================
# 31. DIAGRAMA MENTAL
# ============================================================

#                    valor medio
#                        |
#             ┌──────────┼──────────┐
#             |          |          |
#           menor      igual      mayor
#             |          |          |
#             v          v          v
#          derecha    encontrado   izquierda
#
#
# Más precisamente:
#
# si valor_medio < objetivo
# → derecha
#
#
# si valor_medio > objetivo
# → izquierda


# ============================================================
# 32. ¿POR QUÉ ES MÁS EFICIENTE?
# ============================================================

# Búsqueda lineal:
#
# puede eliminar:
#
# 1 elemento por comparación.
#
#
# Búsqueda binaria:
#
# puede eliminar:
#
# aproximadamente la mitad
# del espacio de búsqueda
# por comparación.


# ============================================================
# 33. EJEMPLO CON MUCHOS ELEMENTOS
# ============================================================

# Supongamos:
#
# 1_024 elementos.
#
#
# Búsqueda lineal:
#
# podría revisar hasta:
#
# 1_024 elementos.
#
#
# Búsqueda binaria:
#
# aproximadamente:
#
# 1_024
# ↓
# 512
# ↓
# 256
# ↓
# 128
# ↓
# 64
# ↓
# 32
# ↓
# 16
# ↓
# 8
# ↓
# 4
# ↓
# 2
# ↓
# 1
#
#
# alrededor de:
#
# 10 reducciones.


# ============================================================
# 34. COMPLEJIDAD
# ============================================================

# BÚSQUEDA LINEAL:
#
# O(n)
#
#
# BÚSQUEDA BINARIA:
#
# O(log n)


# ============================================================
# 35. REQUISITO FUNDAMENTAL
# ============================================================

# Búsqueda binaria necesita:
#
# DATOS ORDENADOS.
#
#
# Esto:
#
# [10, 20, 30, 40, 50]
#
# funciona.
#
#
# Esto:
#
# [30, 10, 50, 20, 40]
#
# NO cumple el requisito.


# ============================================================
# 36. ¿POR QUÉ DEBEN ESTAR ORDENADOS?
# ============================================================

# Supongamos:
#
# [10, 20, 30, 40, 50]
#
#
# miramos:
#
# 30
#
#
# si buscamos 50:
#
# sabemos que debemos ir
# hacia la derecha.
#
#
# Podemos saberlo porque:
#
# los valores están ordenados.
#
#
# En una colección desordenada:
#
# [50, 10, 30, 20, 40]
#
#
# saber que:
#
# objetivo > valor_medio
#
# NO nos permite saber
# en qué lado está el objetivo.


# ============================================================
# 37. EJEMPLO CON STRINGS
# ============================================================

# La búsqueda binaria
# no funciona solamente con números.
#
#
# Puede trabajar con valores
# que tengan un orden comparable.


nombres_ordenados = [
    "Ada Lovelace",
    "Alan Turing",
    "Albert Einstein",
    "Grace Hopper",
    "Nikola Tesla"
]


indice_nombre = busqueda_binaria(
    nombres_ordenados,
    "Grace Hopper"
)


print(
    "Nombre encontrado en índice:",
    indice_nombre
)


# Python puede comparar strings
# siguiendo su orden lexicográfico.


# ============================================================
# 38. ORDENAR SOLO PARA BUSCAR UNA VEZ
# ============================================================

# Aquí aparece una idea importante.
#
#
# Supongamos que tenemos
# una lista desordenada.
#
#
# Podemos pensar:
#
# "la ordeno y después
# hago búsqueda binaria".
#
#
# Pero ordenar también tiene un costo.
#
#
# Ordenamiento:
#
# aproximadamente O(n log n)
#
#
# Búsqueda binaria:
#
# O(log n)
#
#
# Si solamente queremos realizar
# UNA búsqueda:
#
# ordenar toda la colección
# puede ser trabajo innecesario.


# ============================================================
# 39. EJEMPLO DE DECISIÓN
# ============================================================

# Situación:
#
# 100 elementos desordenados.
#
#
# Necesitamos buscar:
#
# una sola vez.
#
#
# Una búsqueda lineal:
#
# O(n)
#
# puede ser completamente razonable.
#
#
# No necesitamos:
#
# ordenar
# +
# búsqueda binaria
#
# solamente porque O(log n)
# parece mejor.


# ============================================================
# 40. CUÁNDO PUEDE SER ÚTIL LA BÚSQUEDA BINARIA
# ============================================================

# Tiene más sentido cuando:
#
# - los datos ya están ordenados;
#
# - realizaremos muchas búsquedas;
#
# - la colección es suficientemente grande;
#
# - podemos acceder a posiciones directamente.


# ============================================================
# 41. ELEGIR LA ESTRUCTURA PUEDE SER TODAVÍA MEJOR
# ============================================================

# Supongamos que necesitamos
# encontrar tickets constantemente
# mediante su ID.
#
#
# Podríamos utilizar:
#
# lista
#
# +
# búsqueda lineal.
#
#
# Pero también podemos diseñar:
#
# dict


tickets_por_id = {
    "TK-001": {
        "titulo": "Crear usuario"
    },

    "TK-002": {
        "titulo": "Servidor caído"
    },

    "TK-003": {
        "titulo": "Actualizar software"
    }
}


print(
    tickets_por_id["TK-002"]
)


# Consulta por clave:
#
# O(1) en promedio.
#
#
# Esto vuelve a demostrar:
#
# no siempre necesitamos
# "un algoritmo más complicado".
#
#
# A veces necesitamos:
#
# una estructura de datos
# más apropiada.


# ============================================================
# 42. LISTA VS SET
# ============================================================

# Si solamente necesitamos comprobar:
#
# "¿existe este elemento?"
#
# muchas veces:
#
# set
#
# puede ser una buena opción.


usuarios_activos = {
    "Einstein",
    "Turing",
    "Hopper"
}


print(
    "Turing"
    in usuarios_activos
)


# En un set:
#
# comprobar pertenencia
#
# suele ser:
#
# O(1) en promedio.
#
#
# En una lista:
#
# "elemento" in lista
#
# normalmente requiere:
#
# O(n)


# ============================================================
# 43. MISMO PROBLEMA, DISTINTA ESTRUCTURA
# ============================================================

# LISTA:
#
# usuarios = [
#     "Einstein",
#     "Turing",
#     "Hopper"
# ]
#
#
# buscar existencia:
#
# O(n)
#
#
# ------------------------------------------------------------
#
# SET:
#
# usuarios = {
#     "Einstein",
#     "Turing",
#     "Hopper"
# }
#
#
# buscar existencia:
#
# O(1) promedio.
#
#
# ------------------------------------------------------------
#
# La elección depende
# de lo que necesitemos hacer
# con los datos.


# ============================================================
# 44. ¿LISTA O SET?
# ============================================================

# Si necesitamos:
#
# orden
# posiciones
# duplicados
#
# list puede ser adecuada.
#
#
# Si necesitamos principalmente:
#
# elementos únicos
# +
# comprobar pertenencia
#
# set puede ser más apropiado.


# ============================================================
# 45. ¿LISTA O DICT?
# ============================================================

# Si tenemos registros y necesitamos:
#
# buscar constantemente por un identificador,
#
# dict puede representar mejor
# el problema.
#
#
# Ejemplo:
#
# ticket_id
# ↓
# datos del ticket


# ============================================================
# 46. BÚSQUEDA LINEAL NO ES "MALA"
# ============================================================

# Esto es muy importante.
#
#
# O(n)
#
# NO significa:
#
# "código malo".
#
#
# Una búsqueda lineal puede ser:
#
# sencilla
# correcta
# legible
# suficiente
#
#
# especialmente para:
#
# colecciones pequeñas
# datos desordenados
# búsquedas ocasionales


# ============================================================
# 47. BÚSQUEDA BINARIA NO SIEMPRE ES LA RESPUESTA
# ============================================================

# O(log n)
#
# escala mejor que:
#
# O(n)
#
#
# pero necesita ciertas condiciones.
#
#
# No debemos pensar:
#
# "búsqueda binaria siempre es mejor".
#
#
# Debemos pensar:
#
# "¿mi problema cumple las condiciones
# donde tiene sentido utilizarla?"


# ============================================================
# 48. DUPLICADOS
# ============================================================

# Supongamos:
#
# [10, 20, 20, 20, 30]
#
#
# Si buscamos:
#
# 20
#
#
# una búsqueda binaria puede encontrar
# alguno de los 20.
#
#
# No necesariamente:
#
# el primero.
#
#
# Encontrar específicamente:
#
# primera aparición
#
# última aparición
#
# todas las apariciones
#
# requiere lógica adicional.
#
#
# No necesitamos estudiar esa variante ahora.


# ============================================================
# 49. MÓDULO bisect
# ============================================================

# Python posee el módulo:
#
# bisect
#
#
# que ofrece herramientas relacionadas
# con búsquedas e inserciones
# en secuencias ordenadas.
#
#
# No necesitamos estudiarlo
# en profundidad todavía.
#
#
# Lo importante ahora es comprender
# el algoritmo y su razonamiento.


# ============================================================
# 50. RESUMEN: BÚSQUEDA LINEAL
# ============================================================

# BÚSQUEDA LINEAL:
#
# revisa uno por uno.
#
#
# Ventajas:
#
# simple;
# funciona con datos desordenados;
# fácil de implementar.
#
#
# Complejidad:
#
# O(n)
#
#
# Ejemplo mental:
#
# abrir cajones
# uno por uno
# hasta encontrar algo.


# ============================================================
# 51. RESUMEN: BÚSQUEDA BINARIA
# ============================================================

# BÚSQUEDA BINARIA:
#
# mira el centro
# y descarta una parte grande
# de la búsqueda.
#
#
# Requisito principal:
#
# datos ordenados.
#
#
# Complejidad:
#
# O(log n)
#
#
# Ejemplo mental:
#
# buscar una palabra
# en un diccionario ordenado.
#
#
# No comenzarías necesariamente
# desde la primera página.
#
# Puedes aproximarte
# utilizando el orden.


# ============================================================
# 52. COMPARACIÓN
# ============================================================

# ------------------------------------------------------------
# BÚSQUEDA LINEAL
# ------------------------------------------------------------
#
# Datos ordenados:
#
# NO obligatorio.
#
#
# Estrategia:
#
# revisar uno por uno.
#
#
# Complejidad:
#
# O(n)
#
#
# ------------------------------------------------------------
# BÚSQUEDA BINARIA
# ------------------------------------------------------------
#
# Datos ordenados:
#
# SÍ.
#
#
# Estrategia:
#
# dividir el espacio de búsqueda.
#
#
# Complejidad:
#
# O(log n)


# ============================================================
# 53. FORMA DE PENSAR EL PROBLEMA
# ============================================================

# Antes de buscar algo,
# pregúntate:
#
# ¿los datos están ordenados?
#
# ¿la colección es grande?
#
# ¿buscaré una vez o muchas veces?
#
# ¿solo necesito comprobar existencia?
#
# ¿necesito obtener una posición?
#
# ¿existe una estructura mejor
# para representar estos datos?
#
#
# Estas preguntas son más importantes
# que memorizar un algoritmo.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# BÚSQUEDA LINEAL:
#
# uno por uno
#
# O(n)
#
#
# ------------------------------------------------------------
#
# BÚSQUEDA BINARIA:
#
# dividir aproximadamente
# el espacio de búsqueda
# en cada paso
#
# O(log n)
#
#
# ------------------------------------------------------------
#
# CONDICIÓN:
#
# búsqueda binaria necesita
# datos ordenados.
#
#
# ------------------------------------------------------------
#
# DETALLE IMPORTANTE:
#
# inicio
# ↓
# fin
# ↓
# medio
#
#
# medio:
#
# (inicio + fin) // 2
#
#
# ------------------------------------------------------------
#
# SI:
#
# valor_medio == objetivo
#
# → encontrado
#
#
# SI:
#
# valor_medio < objetivo
#
# → buscar a la derecha
#
#
# SI:
#
# valor_medio > objetivo
#
# → buscar a la izquierda
#
#
# ------------------------------------------------------------
#
# COMO PROGRAMADOR:
#
# no preguntarse solamente:
#
# "¿qué algoritmo puedo utilizar?"
#
#
# también:
#
# "¿qué estructura de datos
# representa mejor el problema?"
#
#
# ------------------------------------------------------------
#
# SIGUIENTE TEMA:
#
# ordenamiento y eficiencia