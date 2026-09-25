# ============================================================
# OPERADORES DE COMPARACIÓN EN PYTHON
# ============================================================
#
# Los operadores de comparación permiten comparar valores.
#
# Los principales son:
#
# ==  igual a
# !=  distinto de
# >   mayor que
# <   menor que
# >=  mayor o igual que
# <=  menor o igual que
#
# En los ejemplos habituales de este archivo, el resultado
# de una comparación será:
#
# True
#
# o:
#
# False
#
# Estos operadores serán fundamentales cuando posteriormente
# estudiemos condiciones con if, elif y else.


# ------------------------------------------------------------
# 1. IGUALDAD ==
# ------------------------------------------------------------

# == comprueba si dos valores son iguales.

estado_actual = "Nuevo"
estado_esperado = "Nuevo"

son_iguales = estado_actual == estado_esperado

print("¿Los estados son iguales?:", son_iguales)


# IMPORTANTE:
#
# =  significa asignación
#
# == significa comparación


# Ejemplo:

estado = "Nuevo"          # asignación
resultado = estado == "Nuevo"  # comparación

print(resultado)


# ------------------------------------------------------------
# 2. DESIGUALDAD !=
# ------------------------------------------------------------

# != comprueba si dos valores son diferentes.

prioridad_actual = "Alta"
prioridad_anterior = "Media"

son_diferentes = prioridad_actual != prioridad_anterior

print("¿Las prioridades son diferentes?:", son_diferentes)


# ------------------------------------------------------------
# 3. MAYOR QUE >
# ------------------------------------------------------------

tickets_abiertos = 15
limite_tickets = 10

supera_limite = tickets_abiertos > limite_tickets

print("¿Supera el límite?:", supera_limite)


# ------------------------------------------------------------
# 4. MENOR QUE <
# ------------------------------------------------------------

tiempo_resolucion = 2.5
tiempo_maximo = 4.0

dentro_del_tiempo = tiempo_resolucion < tiempo_maximo

print("¿Está bajo el tiempo máximo?:", dentro_del_tiempo)


# ------------------------------------------------------------
# 5. MAYOR O IGUAL QUE >=
# ------------------------------------------------------------

tickets_actuales = 10
limite = 10

alcanzo_limite = tickets_actuales >= limite

print("¿Alcanzó o superó el límite?:", alcanzo_limite)


# ------------------------------------------------------------
# 6. MENOR O IGUAL QUE <=
# ------------------------------------------------------------

tiempo_resolucion = 4
tiempo_sla = 4

cumple_tiempo = tiempo_resolucion <= tiempo_sla

print("¿Cumple el tiempo establecido?:", cumple_tiempo)


# ------------------------------------------------------------
# 7. COMPARACIONES DE STRINGS
# ------------------------------------------------------------

# Los strings también pueden compararse.

estado = "Nuevo"

print(estado == "Nuevo")  # True


# Las mayúsculas y minúsculas importan.

print("Nuevo" == "nuevo")  # False


# Si necesitamos comparar textos sin importar su formato,
# podemos normalizarlos primero con los conocimientos
# estudiados en strings.

estado_usuario = "NUEVO"

estado_normalizado = estado_usuario.lower()

print(estado_normalizado == "nuevo")  # True


# ------------------------------------------------------------
# 8. COMPARACIONES ENCADENADAS
# ------------------------------------------------------------

# Python permite encadenar comparaciones.

tiempo_resolucion = 3

dentro_del_rango = 0 < tiempo_resolucion <= 4

print("¿Tiempo dentro del rango?:", dentro_del_rango)


# Podemos leerlo como:
#
# tiempo_resolucion es mayor que 0
#
# Y
#
# tiempo_resolucion es menor o igual que 4
#
# Más adelante veremos esta relación con el operador lógico and.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# ==  igual
# !=  diferente
# >   mayor
# <   menor
# >=  mayor o igual
# <=  menor o igual
#
# Debemos recordar especialmente:
#
# =  asigna un valor
#
# == compara dos valores
#
# Las comparaciones serán utilizadas constantemente cuando
# estudiemos control de flujo y reglas de negocio.