# ============================================================
# TIPOS DE DATOS BÁSICOS EN PYTHON
# ============================================================

# Python utiliza distintos tipos de datos para representar
# diferentes clases de información.


# ------------------------------------------------------------
# STR - CADENAS DE TEXTO
# ------------------------------------------------------------

# Los strings (str) representan cadenas de texto.
# Pueden escribirse utilizando comillas dobles o simples.

texto_comillas_dobles = "string"
texto_comillas_simples = 'string'

print(type(texto_comillas_dobles))
print(type(texto_comillas_simples))


# ------------------------------------------------------------
# INT - NÚMEROS ENTEROS
# ------------------------------------------------------------

# Los enteros (int) representan números sin parte decimal.
# Pueden ser positivos, negativos o cero.

print(type(10))
print(type(-25))
print(type(0))


# ------------------------------------------------------------
# FLOAT - NÚMEROS DECIMALES
# ------------------------------------------------------------

# Los números de punto flotante (float) representan
# números que poseen parte decimal.

print(type(10.5))
print(type(3.14))


# ------------------------------------------------------------
# BOOL - VALORES LÓGICOS
# ------------------------------------------------------------

# Los booleanos (bool) representan valores lógicos.
# Solamente pueden tomar los valores True o False.

print(type(True))
print(type(False))


# ------------------------------------------------------------
# NONE - AUSENCIA DE VALOR
# ------------------------------------------------------------

# None representa la ausencia de un valor.
# Su tipo es NoneType.

print(type(None))