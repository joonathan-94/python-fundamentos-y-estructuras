# ============================================================
# STRINGS EN PYTHON
# ============================================================
#
# Un string (str) representa una cadena de caracteres.
#
# En Python los strings son inmutables:
# una operación sobre un string no modifica el objeto original.
#
# Algunos métodos devuelven un nuevo string, mientras que otros
# pueden devolver números, booleanos, listas u otros tipos de datos.


# ------------------------------------------------------------
# 1. CREACIÓN DE STRINGS
# ------------------------------------------------------------

nombre = "Neo"
serie = 'The Sopranos'

print(nombre)
print(serie)


# ------------------------------------------------------------
# 2. COMILLAS SIMPLES Y DOBLES
# ------------------------------------------------------------

# Ambas formas crean valores de tipo str.
# Podemos elegir una u otra según facilite la escritura del texto.

frase_1 = "Walter White dijo: 'Yo soy el peligro'"
frase_2 = 'El personaje se llama "Neo"'

print(frase_1)
print(frase_2)


# ------------------------------------------------------------
# 3. LONGITUD DE UN STRING
# ------------------------------------------------------------

# len() devuelve la cantidad de caracteres de una cadena.

titulo_ticket = "Problema de conexión"

print(len(titulo_ticket))


# ------------------------------------------------------------
# 4. ACCESO MEDIANTE ÍNDICES
# ------------------------------------------------------------

# Los caracteres de un string poseen posiciones.
# Los índices comienzan en 0.

personaje = "Goku"

print(personaje[0])   # G
print(personaje[1])   # o

# También existen índices negativos.

print(personaje[-1])  # u


# ------------------------------------------------------------
# 5. SLICING
# ------------------------------------------------------------

# El slicing permite obtener una parte de una cadena.
#
# sintaxis:
#
# string[inicio:fin]
#
# El índice de inicio se incluye.
# El índice final no se incluye.

tecnologia = "Python"

print(tecnologia[0:3])  # Pyt
print(tecnologia[3:6])  # hon
print(tecnologia[:3])   # Pyt
print(tecnologia[3:])   # hon


# ------------------------------------------------------------
# 6. INMUTABILIDAD
# ------------------------------------------------------------

estado = "Nuevo"

# Esto NO es válido:
#
# estado[0] = "n"
#
# Los strings no permiten modificar caracteres individuales.

# Sin embargo, podemos crear otro string:

estado_normalizado = estado.lower()

print("Original:", estado)
print("Nuevo:", estado_normalizado)


# ------------------------------------------------------------
# 7. MAYÚSCULAS Y MINÚSCULAS
# ------------------------------------------------------------

texto = "hOla MUnDo deL deSArroLlo WeB"

print("Original:", texto)

# lower()
# Devuelve un nuevo string en minúsculas.

print("lower():", texto.lower())

# upper()
# Devuelve un nuevo string en mayúsculas.

print("upper():", texto.upper())

# capitalize()
# Convierte el primer carácter a mayúscula y el resto a minúsculas.

print("capitalize():", texto.capitalize())

# title()
# Convierte el comienzo de cada palabra al formato de título.
#
# No debe asumirse que title() siempre produce nombres propios
# lingüísticamente correctos; es una transformación automática.

print("title():", texto.title())


# ------------------------------------------------------------
# 8. ELIMINACIÓN DE ESPACIOS
# ------------------------------------------------------------

# strip()
# Elimina espacios en blanco al inicio y al final.

usuario_ingresado = "   Homer Simpson   "

usuario_limpio = usuario_ingresado.strip()

print(f"Original: '{usuario_ingresado}'")
print(f"Limpio:   '{usuario_limpio}'")


# lstrip()
# Elimina espacios del lado izquierdo.

print(f"lstrip(): '{usuario_ingresado.lstrip()}'")


# rstrip()
# Elimina espacios del lado derecho.

print(f"rstrip(): '{usuario_ingresado.rstrip()}'")


# ------------------------------------------------------------
# 9. BÚSQUEDA Y PERTENENCIA
# ------------------------------------------------------------

descripcion = "Error de conexión con servidor PostgreSQL"

# in
# Comprueba si una subcadena está presente.
# Devuelve True o False.

print("PostgreSQL" in descripcion)


# count()
# Cuenta cuántas veces aparece una subcadena.

registro = "error warning error info error"

cantidad_errores = registro.count("error")

print("Cantidad de errores:", cantidad_errores)


# find()
# Devuelve el índice donde comienza la primera coincidencia.
# Si no encuentra la subcadena devuelve -1.

posicion = descripcion.find("servidor")

print("Posición de 'servidor':", posicion)


# ------------------------------------------------------------
# 10. COMPROBAR INICIO Y FINAL
# ------------------------------------------------------------

archivo = "reporte_tickets.csv"

print(archivo.startswith("reporte"))
print(archivo.endswith(".csv"))


# ------------------------------------------------------------
# 11. REEMPLAZAR TEXTO
# ------------------------------------------------------------

descripcion = "El ticket está Abierto"

descripcion_actualizada = descripcion.replace(
    "Abierto",
    "En progreso"
)

print(descripcion_actualizada)


# ------------------------------------------------------------
# 12. SPLIT
# ------------------------------------------------------------

# split() divide un string y devuelve una lista.

etiquetas = "red,hardware,servidor"

lista_etiquetas = etiquetas.split(",")

print(lista_etiquetas)
print(type(lista_etiquetas))


# ------------------------------------------------------------
# 13. JOIN
# ------------------------------------------------------------

# join() construye un string uniendo varios strings mediante
# el separador sobre el cual se llama el método.

tecnicos = [
    "Elliot Alderson",
    "Neo",
    "Tony Soprano"
]

tecnicos_texto = ", ".join(tecnicos)

print(tecnicos_texto)


# ------------------------------------------------------------
# 14. CONCATENACIÓN
# ------------------------------------------------------------

nombre = "Homer"
apellido = "Simpson"

nombre_completo = nombre + " " + apellido

print(nombre_completo)


# ------------------------------------------------------------
# 15. F-STRINGS
# ------------------------------------------------------------

# Las f-strings permiten insertar valores dentro de strings
# de forma clara y legible.

ticket_id = 25
estado = "Nuevo"

mensaje = f"El ticket #{ticket_id} se encuentra en estado {estado}."

print(mensaje)