# ============================================================
# CICLOS EN PYTHON
# ============================================================
#
# Los ciclos permiten repetir un bloque de código sin escribir
# las mismas instrucciones una y otra vez.
#
# En este módulo estudiaremos:
#
# while
# for
# range()
# break
# continue
#
# Los ciclos serán útiles posteriormente para recorrer datos,
# procesar elementos y repetir operaciones.


# ------------------------------------------------------------
# 1. CICLO while
# ------------------------------------------------------------

# while repite un bloque mientras una condición se mantenga
# verdadera.

contador = 1

while contador <= 3:
    print("Contador:", contador)
    contador += 1

print("Fin del while.")


# Proceso:
#
# contador = 1
# contador = 2
# contador = 3
#
# Cuando contador pasa a 4:
#
# contador <= 3
#
# resulta False y el ciclo termina.


# ------------------------------------------------------------
# 2. EVITAR CICLOS INFINITOS
# ------------------------------------------------------------

# Cuando utilizamos while debemos asegurarnos de que exista
# alguna forma de que la condición eventualmente deje de
# cumplirse.

contador = 1

while contador <= 3:
    print(contador)

    # Modificamos la variable de control.
    contador += 1


# Si elimináramos:
#
# contador += 1
#
# contador seguiría siendo 1 y la condición nunca cambiaría.
#
# El ciclo podría ejecutarse indefinidamente.


# ------------------------------------------------------------
# 3. CICLO for
# ------------------------------------------------------------

# for permite recorrer elementos de un iterable.
#
# Un iterable es un objeto cuyos elementos pueden recorrerse
# uno por uno.
#
# Por ahora utilizaremos strings y range().
#
# Más adelante estudiaremos listas, tuplas, diccionarios
# y sets en profundidad.


# Ejemplo recorriendo un string:

estado = "Nuevo"

for caracter in estado:
    print(caracter)


# En cada iteración la variable caracter toma uno de los
# caracteres del string.


# ------------------------------------------------------------
# 4. range()
# ------------------------------------------------------------

# range() genera una secuencia de números que puede utilizarse
# con for.

for numero in range(5):
    print(numero)


# Resultado:
#
# 0
# 1
# 2
# 3
# 4
#
# El límite final no se incluye.


# ------------------------------------------------------------
# 5. range(inicio, fin)
# ------------------------------------------------------------

for numero in range(1, 6):
    print(numero)


# Resultado:
#
# 1
# 2
# 3
# 4
# 5


# ------------------------------------------------------------
# 6. range(inicio, fin, paso)
# ------------------------------------------------------------

# El tercer valor indica cuánto debe avanzar el rango.

for numero in range(0, 10, 2):
    print(numero)


# Resultado:
#
# 0
# 2
# 4
# 6
# 8


# ------------------------------------------------------------
# 7. ACUMULADORES
# ------------------------------------------------------------

# Una variable puede utilizarse para acumular resultados
# durante las iteraciones.

total = 0

for numero in range(1, 4):
    total += numero

print("Total:", total)


# Proceso:
#
# total = 0
#
# total = 0 + 1
# total = 1 + 2
# total = 3 + 3
#
# resultado:
#
# 6


# ------------------------------------------------------------
# 8. CONTADORES
# ------------------------------------------------------------

# También podemos utilizar una variable para contar
# cuántas veces ocurre algo.

cantidad = 0

for numero in range(5):
    cantidad += 1

print("Cantidad de iteraciones:", cantidad)


# ------------------------------------------------------------
# 9. break
# ------------------------------------------------------------

# break termina inmediatamente el ciclo actual.

for numero in range(1, 6):
    print("Número:", numero)

    if numero == 3:
        print("Se encontró el número 3.")
        break

print("Fin del ciclo.")


# El ciclo termina cuando numero vale 3.
#
# Los valores 4 y 5 ya no se procesan.


# ------------------------------------------------------------
# 10. continue
# ------------------------------------------------------------

# continue interrumpe únicamente la iteración actual
# y pasa directamente a la siguiente.

for numero in range(1, 6):

    if numero == 3:
        continue

    print(numero)


# Resultado:
#
# 1
# 2
# 4
# 5
#
# El número 3 fue omitido.


# ------------------------------------------------------------
# 11. while CON break
# ------------------------------------------------------------

contador = 1

while True:
    print("Iteración:", contador)

    if contador == 3:
        break

    contador += 1


# while True crea intencionalmente un ciclo cuya condición
# siempre es verdadera.
#
# Por eso necesitamos una condición interna que ejecute break.


# ------------------------------------------------------------
# 12. COMBINAR CICLOS Y CONDICIONALES
# ------------------------------------------------------------

# Los ciclos suelen utilizarse junto con if.

for numero in range(1, 6):

    if numero % 2 == 0:
        print(numero, "es par")
    else:
        print(numero, "es impar")


# Aquí utilizamos:
#
# for
# range()
# if
# else
# %
# ==


# Es un ejemplo de cómo los conceptos estudiados comienzan
# a combinarse.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# while
# → repite mientras una condición sea verdadera.
#
# for
# → recorre los elementos de un iterable.
#
# range()
# → genera una secuencia de números.
#
# break
# → termina completamente el ciclo.
#
# continue
# → salta la iteración actual y continúa con la siguiente.
#
# Los ciclos suelen combinarse con:
#
# - variables
# - operadores
# - comparaciones
# - condicionales
#
# Más adelante los utilizaremos especialmente para recorrer
# colecciones y procesar datos.