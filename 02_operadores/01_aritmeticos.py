# ============================================================
# OPERADORES ARITMÉTICOS EN PYTHON
# ============================================================
#
# Los operadores aritméticos permiten realizar operaciones
# matemáticas con valores numéricos.
#
# Los principales operadores son:
#
# +   suma
# -   resta
# *   multiplicación
# /   división
# //  división entera
# %   módulo o resto
# **  potencia
#
# Estos operadores aparecerán frecuentemente al trabajar con:
#
# - cantidades
# - tiempos
# - precios
# - porcentajes
# - contadores
# - estadísticas
# - distribución de elementos


# ------------------------------------------------------------
# 1. SUMA
# ------------------------------------------------------------

# El operador + suma dos valores numéricos.

tickets_nuevos = 12
tickets_reabiertos = 3

total_tickets = tickets_nuevos + tickets_reabiertos

print("Total tickets:", total_tickets)


# ------------------------------------------------------------
# 2. RESTA
# ------------------------------------------------------------

# El operador - permite restar un valor de otro.

tickets_totales = 20
tickets_resueltos = 7

tickets_pendientes = tickets_totales - tickets_resueltos

print("Tickets pendientes:", tickets_pendientes)


# ------------------------------------------------------------
# 3. MULTIPLICACIÓN
# ------------------------------------------------------------

# El operador * multiplica dos valores.

costo_mensual = 15
cantidad_meses = 12

costo_anual = costo_mensual * cantidad_meses

print("Costo anual:", costo_anual)


# ------------------------------------------------------------
# 4. DIVISIÓN
# ------------------------------------------------------------

# El operador / realiza una división normal.
#
# En Python, el resultado de / es normalmente un float,
# incluso cuando la división es exacta.

total = 12
cantidad = 6

division = total / cantidad

print("División:", division)
print("Tipo:", type(division))


# Resultado:
#
# 2.0


# ------------------------------------------------------------
# 5. DIVISIÓN ENTERA
# ------------------------------------------------------------

# El operador // realiza una división entera o floor division.
#
# Con números positivos podemos pensar inicialmente que
# conserva la parte entera del resultado.

tickets = 12
tecnicos = 5

tickets_por_tecnico = tickets // tecnicos

print("Tickets por técnico:", tickets_por_tecnico)


# 12 / 5
# → 2.4
#
# 12 // 5
# → 2


# IMPORTANTE:
#
# Técnicamente // redondea hacia abajo.
#
# Esto se nota especialmente con números negativos.
#
# Por ejemplo:
#
# -12 // 5
#
# produce:
#
# -3
#
# y no -2.


# ------------------------------------------------------------
# 6. MÓDULO O RESTO
# ------------------------------------------------------------

# El operador % devuelve el resto de una división.

tickets = 12
tecnicos = 5

tickets_sobrantes = tickets % tecnicos

print("Tickets sobrantes:", tickets_sobrantes)


# Si distribuimos:
#
# 12 tickets
# entre
# 5 técnicos
#
# cada técnico recibe 2 tickets:
#
# 5 * 2 = 10
#
# y sobran:
#
# 2 tickets


# ------------------------------------------------------------
# 7. POTENCIA
# ------------------------------------------------------------

# El operador ** permite elevar un número a una potencia.

base = 2
exponente = 3

resultado = base ** exponente

print("Potencia:", resultado)


# 2 ** 3
#
# equivale a:
#
# 2 * 2 * 2
#
# resultado:
#
# 8


# ------------------------------------------------------------
# 8. OPERADORES DE ASIGNACIÓN COMPUESTA
# ------------------------------------------------------------

# Podemos realizar una operación y reasignar el resultado
# a la misma variable.

cantidad_tickets = 10

cantidad_tickets += 2

print("Después de += 2:", cantidad_tickets)


# Esto:

# cantidad_tickets += 2

# equivale conceptualmente a:

# cantidad_tickets = cantidad_tickets + 2


# También existen:

# +=
# -=
# *=
# /=
# //=
# %=
# **=


# Ejemplo con resta:

tickets_pendientes = 10

tickets_pendientes -= 1

print("Tickets pendientes:", tickets_pendientes)


# ------------------------------------------------------------
# 9. PRECEDENCIA DE OPERADORES
# ------------------------------------------------------------

# Python no evalúa todas las operaciones simplemente
# de izquierda a derecha.
#
# Los operadores tienen distintos niveles de prioridad.
#
# Para los operadores estudiados aquí, una simplificación útil es:
#
# 1. ()
# 2. **
# 3. *  /  //  %
# 4. +  -
#
# Ejemplo:

resultado = 2 + 3 * 4

print(resultado)  # 14


# Primero:
#
# 3 * 4 = 12
#
# Después:
#
# 2 + 12 = 14


# Los paréntesis permiten cambiar explícitamente el orden:

resultado_con_parentesis = (2 + 3) * 4

print(resultado_con_parentesis)  # 20


# Cuando una expresión pueda resultar difícil de leer,
# utilizar paréntesis mejora la claridad del código.


# ------------------------------------------------------------
# 10. EJEMPLO APLICADO A TICKETS
# ------------------------------------------------------------

tickets_pendientes = 85
cantidad_tecnicos = 4

tickets_por_tecnico = tickets_pendientes // cantidad_tecnicos
tickets_sobrantes = tickets_pendientes % cantidad_tecnicos

print("Tickets por técnico:", tickets_por_tecnico)
print("Tickets sin distribuir:", tickets_sobrantes)


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# +   suma
# -   resta
# *   multiplicación
# /   división normal
# //  división entera
# %   resto de una división
# **  potencia
#
# También podemos combinar operaciones con asignación:
#
# +=
# -=
# *=
# etc.
#
# Cuando existen varias operaciones en una expresión,
# debemos considerar su precedencia o utilizar paréntesis
# para hacer explícito el orden deseado.