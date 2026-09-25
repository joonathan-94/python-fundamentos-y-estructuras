# ============================================================
# CONVERSIÓN DE TIPOS EN PYTHON
# ============================================================
#
# En Python podemos convertir valores de un tipo de dato
# a otro utilizando funciones incorporadas.
#
# Algunas de las conversiones más comunes son:
#
# str()   -> convierte a string
# int()   -> convierte a entero
# float() -> convierte a número decimal
# bool()  -> convierte a booleano
#
# La conversión debe ser válida.
#
# Por ejemplo:
#
# int("25")
#
# funciona porque "25" representa un número entero.
#
# En cambio:
#
# int("Neo")
#
# produciría un error porque "Neo" no puede interpretarse
# como un número entero.


# ------------------------------------------------------------
# 1. COMPROBAR EL TIPO ORIGINAL
# ------------------------------------------------------------

edad = "31"

print(edad)
print(type(edad))

# Aunque visualmente vemos 31, el valor es un string.


# ------------------------------------------------------------
# 2. CONVERTIR A int
# ------------------------------------------------------------

# int() permite obtener un número entero cuando el valor
# recibido puede convertirse correctamente.

edad_texto = "31"

edad_numero = int(edad_texto)

print(edad_numero)
print(type(edad_numero))


# Otro ejemplo relacionado con tickets:

id_ticket_texto = "100"

id_ticket = int(id_ticket_texto)

print(id_ticket)
print(type(id_ticket))


# ------------------------------------------------------------
# 3. CONVERTIR A float
# ------------------------------------------------------------

# float() permite crear un número decimal.

horas_texto = "2.5"

horas = float(horas_texto)

print(horas)
print(type(horas))


# Un entero también puede convertirse a float.

cantidad = 5

cantidad_decimal = float(cantidad)

print(cantidad_decimal)
print(type(cantidad_decimal))


# ------------------------------------------------------------
# 4. CONVERTIR A str
# ------------------------------------------------------------

# str() permite convertir otros valores a texto.

id_ticket = 42

id_ticket_texto = str(id_ticket)

print(id_ticket_texto)
print(type(id_ticket_texto))


# También podemos convertir booleanos:

estado_activo = True

estado_texto = str(estado_activo)

print(estado_texto)
print(type(estado_texto))


# ------------------------------------------------------------
# 5. CONVERTIR float A int
# ------------------------------------------------------------

# Al convertir un float a int, Python elimina
# la parte decimal.
#
# NO debemos pensar que int() redondea.

tiempo = 3.9

tiempo_entero = int(tiempo)

print(tiempo_entero)  # 3


# Otro ejemplo:

valor = 7.8

print(int(valor))  # 7


# ------------------------------------------------------------
# 6. CONVERSIONES INVÁLIDAS
# ------------------------------------------------------------

# No cualquier string puede convertirse a número.

# Esto funcionaría:

numero = int("25")

print(numero)


# Esto produciría ValueError:
#
# numero = int("Tony Soprano")


# Tampoco podemos convertir directamente este string
# decimal utilizando int():
#
# numero = int("10.5")
#
# porque "10.5" no representa directamente un entero.


# En ese caso podríamos convertir primero a float:

numero_decimal = float("10.5")

print(numero_decimal)


# ------------------------------------------------------------
# 7. CONVERTIR A bool
# ------------------------------------------------------------

# bool() convierte un valor en True o False.
#
# Algunos valores considerados falsos incluyen:
#
# 0
# 0.0
# ""
# None
# False

print(bool(0))       # False
print(bool(0.0))     # False
print(bool(""))      # False
print(bool(None))    # False


# Otros valores normalmente se consideran verdaderos.

print(bool(1))        # True
print(bool(25))       # True
print(bool("Python")) # True


# ------------------------------------------------------------
# 8. CUIDADO CON STRINGS Y bool()
# ------------------------------------------------------------

# Un string NO vacío se considera verdadero.
#
# Por eso:

valor = "False"

resultado = bool(valor)

print(resultado)  # True


# Aunque el texto diga "False", sigue siendo un string
# que contiene caracteres.
#
# Esto es diferente de:

valor_booleano = False

print(bool(valor_booleano))  # False


# ------------------------------------------------------------
# 9. COMPROBAR LA CONVERSIÓN CON type()
# ------------------------------------------------------------

numero_texto = "50"

print(type(numero_texto))

numero = int(numero_texto)

print(type(numero))


# Podemos comprobar claramente:
#
# antes  -> str
# después -> int


# ------------------------------------------------------------
# 10. EJEMPLO RELACIONADO CON UN TICKET
# ------------------------------------------------------------

id_ticket_recibido = "250"
horas_resolucion_recibidas = "1.5"

id_ticket = int(id_ticket_recibido)
horas_resolucion = float(horas_resolucion_recibidas)

print(id_ticket)
print(type(id_ticket))

print(horas_resolucion)
print(type(horas_resolucion))


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# Debemos recordar:
#
# str()   -> convierte a texto
#
# int()   -> convierte a entero cuando el valor lo permite
#
# float() -> convierte a número decimal cuando el valor
#            lo permite
#
# bool()  -> convierte utilizando las reglas de verdad
#            de Python
#
# int() aplicado sobre un float elimina la parte decimal;
# no realiza un redondeo tradicional.
#
# Una conversión inválida puede producir un error.
#
# Más adelante aprenderemos a controlar estos errores
# cuando estudiemos manejo de excepciones.