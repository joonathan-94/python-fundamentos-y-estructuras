# ============================================================
# STRINGS EN PYTHON
# ============================================================
#
# Un string (str) representa una cadena de caracteres.
#
# Ejemplos:
#
# "Python"
# "WorkDesk"
# "Problema de conexión"
#
# En Python, los strings son inmutables:
# una operación sobre un string NO modifica el objeto original.
#
# Dependiendo de la operación realizada, podemos obtener:
#
# - otro string
# - un número entero
# - un booleano
# - una lista
#
# Los strings son uno de los tipos de datos más utilizados,
# especialmente al trabajar con:
#
# - nombres
# - títulos
# - descripciones
# - mensajes
# - formularios
# - archivos
# - datos recibidos desde usuarios
# - información proveniente de APIs o bases de datos


# ------------------------------------------------------------
# 1. CREACIÓN DE STRINGS
# ------------------------------------------------------------

# Podemos crear strings utilizando comillas dobles o simples.

nombre = "Neo"
serie = 'The Sopranos'

print(nombre)
print(serie)

# Ambos valores son de tipo str.

print(type(nombre))
print(type(serie))


# ------------------------------------------------------------
# 2. COMILLAS SIMPLES Y DOBLES
# ------------------------------------------------------------

# Ambas formas crean exactamente el mismo tipo de dato.
#
# Podemos elegir la que facilite escribir el contenido
# de la cadena.

frase_1 = "Walter White dijo: 'Yo soy el peligro'"
frase_2 = 'El personaje se llama "Neo"'

print(frase_1)
print(frase_2)


# ------------------------------------------------------------
# 3. SECUENCIAS DE ESCAPE
# ------------------------------------------------------------

# Algunas combinaciones especiales comienzan con una barra
# invertida (\).
#
# Se conocen como secuencias de escape.

# \n -> salto de línea

mensaje = "Ticket creado\nTicket asignado"

print(mensaje)


# \t -> tabulación

datos_ticket = "ID:\t25\nEstado:\tNuevo"

print(datos_ticket)


# \" -> permite incluir comillas dobles
# dentro de un string delimitado por comillas dobles.

frase = "El estado del ticket es \"Nuevo\""

print(frase)


# \\ -> representa una barra invertida.

ruta_ejemplo = "C:\\usuarios\\documentos"

print(ruta_ejemplo)


# ------------------------------------------------------------
# 4. STRINGS MULTILÍNEA
# ------------------------------------------------------------

# Las triples comillas permiten crear strings que contienen
# varias líneas.

descripcion_ticket = """
El usuario informa que no puede acceder al sistema.
El problema comenzó durante la mañana.
Se solicita revisión del equipo.
"""

print(descripcion_ticket)


# ------------------------------------------------------------
# 5. LONGITUD DE UN STRING
# ------------------------------------------------------------

# len() devuelve la cantidad de caracteres de una cadena.
#
# El resultado es un número entero (int).

titulo_ticket = "Problema de conexión"

cantidad_caracteres = len(titulo_ticket)

print(cantidad_caracteres)
print(type(cantidad_caracteres))


# ------------------------------------------------------------
# 6. ACCESO MEDIANTE ÍNDICES
# ------------------------------------------------------------

# Cada carácter dentro de un string posee una posición.
#
# En Python, los índices comienzan desde 0.

personaje = "Goku"

# Posiciones:
#
# G   o   k   u
# 0   1   2   3

print(personaje[0])  # G
print(personaje[1])  # o


# También existen índices negativos.
#
# Estos comienzan desde el final del string.
#
# G   o   k   u
# -4 -3  -2  -1

print(personaje[-1])  # u
print(personaje[-2])  # k


# IMPORTANTE:
#
# Intentar acceder a una posición que no existe genera
# un IndexError.
#
# Ejemplo inválido:
#
# personaje[20]


# ------------------------------------------------------------
# 7. SLICING
# ------------------------------------------------------------

# El slicing permite obtener una parte de un string.
#
# Sintaxis básica:
#
# string[inicio:fin]
#
# El índice inicial SE incluye.
# El índice final NO se incluye.

tecnologia = "Python"

print(tecnologia[0:3])  # Pyt
print(tecnologia[3:6])  # hon


# Podemos omitir el índice inicial.

print(tecnologia[:3])   # Pyt


# También podemos omitir el índice final.

print(tecnologia[3:])   # hon


# Si omitimos ambos obtenemos todo el string.

print(tecnologia[:])    # Python


# ------------------------------------------------------------
# 8. SLICING CON PASO
# ------------------------------------------------------------

# La sintaxis completa del slicing es:
#
# string[inicio:fin:paso]
#
# El paso indica cuántas posiciones avanzamos.

codigo = "WD-2026-0042"

print(codigo[::2])


# Un paso negativo permite recorrer el string
# desde el final hacia el comienzo.

texto = "Python"

texto_invertido = texto[::-1]

print(texto_invertido)  # nohtyP


# ------------------------------------------------------------
# 9. INMUTABILIDAD
# ------------------------------------------------------------

# Los strings son inmutables.
#
# Esto significa que una vez creado un objeto str,
# sus caracteres individuales no pueden modificarse.

estado = "Nuevo"

# Esto produciría un error:
#
# estado[0] = "n"


# Una operación sobre el string puede devolver
# un NUEVO string.

estado_normalizado = estado.lower()

print("Original:", estado)
print("Nuevo:", estado_normalizado)


# El string original continúa siendo:

print(estado)  # Nuevo


# También podríamos reasignar la variable:

estado = estado.lower()

print(estado)  # nuevo


# Aquí NO modificamos el string original.
#
# La variable "estado" simplemente pasa a referenciar
# el nuevo string generado por lower().


# ------------------------------------------------------------
# 10. MAYÚSCULAS Y MINÚSCULAS
# ------------------------------------------------------------

texto = "hOla MUnDo deL deSArroLlo WeB"

print("Original:", texto)


# lower()
#
# Devuelve un nuevo string en minúsculas.

print("lower():", texto.lower())


# upper()
#
# Devuelve un nuevo string en mayúsculas.

print("upper():", texto.upper())


# capitalize()
#
# Convierte el primer carácter a mayúscula
# y el resto del string a minúsculas.

print("capitalize():", texto.capitalize())


# title()
#
# Aplica formato de título a las palabras.

print("title():", texto.title())


# IMPORTANTE:
#
# title() realiza una transformación automática.
# No garantiza que nombres propios o textos complejos queden
# lingüísticamente escritos de forma perfecta.


# ------------------------------------------------------------
# 11. ELIMINACIÓN DE ESPACIOS
# ------------------------------------------------------------

usuario_ingresado = "   Homer Simpson   "


# strip()
#
# Elimina espacios en blanco al comienzo y al final.
#
# NO elimina espacios internos.

usuario_limpio = usuario_ingresado.strip()

print(f"Original: '{usuario_ingresado}'")
print(f"Limpio:   '{usuario_limpio}'")


# lstrip()
#
# Elimina espacios únicamente del lado izquierdo.

print(f"lstrip(): '{usuario_ingresado.lstrip()}'")


# rstrip()
#
# Elimina espacios únicamente del lado derecho.

print(f"rstrip(): '{usuario_ingresado.rstrip()}'")


# ------------------------------------------------------------
# 12. OPERADORES DE PERTENENCIA: in Y not in
# ------------------------------------------------------------

descripcion = "Error de conexión con servidor PostgreSQL"


# in
#
# Comprueba si una subcadena existe dentro del string.
#
# Devuelve True o False.

contiene_postgresql = "PostgreSQL" in descripcion

print(contiene_postgresql)


# not in
#
# Comprueba que una subcadena NO esté presente.

contiene_mysql = "MySQL" in descripcion
no_contiene_mysql = "MySQL" not in descripcion

print(contiene_mysql)
print(no_contiene_mysql)


# Las búsquedas distinguen mayúsculas y minúsculas.

print("postgresql" in descripcion)  # False


# Podemos normalizar ambos textos antes de comparar.

descripcion_normalizada = descripcion.lower()

print("postgresql" in descripcion_normalizada)  # True


# ------------------------------------------------------------
# 13. count()
# ------------------------------------------------------------

# count() indica cuántas veces aparece una subcadena.
#
# Devuelve un int.

registro = "error warning error info error"

cantidad_errores = registro.count("error")

print("Cantidad de errores:", cantidad_errores)


# ------------------------------------------------------------
# 14. find()
# ------------------------------------------------------------

# find() busca una subcadena dentro de otra cadena.
#
# Si la encuentra:
# devuelve el índice donde comienza la primera coincidencia.
#
# Si NO la encuentra:
# devuelve -1.

descripcion = "Error de conexión con servidor PostgreSQL"

posicion_servidor = descripcion.find("servidor")

print("Posición de 'servidor':", posicion_servidor)


posicion_oracle = descripcion.find("Oracle")

print("Posición de 'Oracle':", posicion_oracle)  # -1


# ------------------------------------------------------------
# 15. startswith() Y endswith()
# ------------------------------------------------------------

# startswith()
#
# Comprueba si un string comienza con determinado texto.

codigo_ticket = "WD-2026-0042"

print(codigo_ticket.startswith("WD"))


# endswith()
#
# Comprueba si un string termina con determinado texto.

archivo = "captura_error.png"

print(archivo.endswith(".png"))


# Ambos métodos devuelven valores booleanos.


# ------------------------------------------------------------
# 16. replace()
# ------------------------------------------------------------

# replace() devuelve un nuevo string reemplazando
# una parte del texto por otra.
#
# El string original no se modifica.

mensaje_estado = "El ticket está Nuevo"

mensaje_actualizado = mensaje_estado.replace(
    "Nuevo",
    "En progreso"
)

print("Original:", mensaje_estado)
print("Actualizado:", mensaje_actualizado)


# ------------------------------------------------------------
# 17. split()
# ------------------------------------------------------------

# split() divide un string y devuelve una LISTA.
#
# Podemos indicar qué texto se utilizará como separador.

etiquetas = "red,hardware,servidor"

lista_etiquetas = etiquetas.split(",")

print(lista_etiquetas)
print(type(lista_etiquetas))


# Si no indicamos un separador, split() divide el texto
# utilizando espacios en blanco.

descripcion = "Error conexión servidor"

palabras = descripcion.split()

print(palabras)


# IMPORTANTE:
#
# Aquí utilizamos una lista únicamente para observar el resultado
# de split().
#
# Las listas se estudiarán en profundidad posteriormente.


# ------------------------------------------------------------
# 18. join()
# ------------------------------------------------------------

# join() realiza una operación complementaria a split():
#
# une diferentes strings utilizando un separador.
#
# Sintaxis:
#
# separador.join(elementos)

tecnicos = [
    "Elliot Alderson",
    "Neo",
    "Tony Soprano"
]

tecnicos_texto = " | ".join(tecnicos)

print(tecnicos_texto)


# Resultado:
#
# Elliot Alderson | Neo | Tony Soprano


# IMPORTANTE:
#
# Los elementos que se unen mediante join()
# deben ser strings.


# ------------------------------------------------------------
# 19. CONCATENACIÓN
# ------------------------------------------------------------

# El operador + permite concatenar strings.

nombre = "Homer"
apellido = "Simpson"

nombre_completo = nombre + " " + apellido

print(nombre_completo)


# Los operandos deben ser strings.
#
# Esto produciría un TypeError:
#
# edad = 40
# texto = "Edad: " + edad
#
# Más adelante estudiaremos conversión de tipos.


# ------------------------------------------------------------
# 20. REPETICIÓN DE STRINGS
# ------------------------------------------------------------

# El operador * permite repetir un string.

separador = "-" * 30

print(separador)


# Otro ejemplo:

alerta = "ERROR " * 3

print(alerta)


# ------------------------------------------------------------
# 21. F-STRINGS
# ------------------------------------------------------------

# Las f-strings permiten insertar valores dentro de strings
# utilizando llaves {}.
#
# Son una forma clara y legible de construir mensajes.

id_ticket = 25
estado = "Nuevo"

mensaje = f"El ticket #{id_ticket} se encuentra en estado {estado}."

print(mensaje)


# Los valores insertados no tienen que ser necesariamente strings.

cantidad_tickets = 5
usuario_activo = True

resumen = (
    f"Tickets: {cantidad_tickets} | "
    f"Usuario activo: {usuario_activo}"
)

print(resumen)


# ------------------------------------------------------------
# 22. MÉTODOS BÁSICOS DE VALIDACIÓN
# ------------------------------------------------------------

# Algunos métodos permiten comprobar qué tipo de caracteres
# contiene un string.
#
# Todos estos métodos devuelven True o False.


# isdigit()
#
# Comprueba si los caracteres representan dígitos.

numero_ticket = "0042"

print(numero_ticket.isdigit())  # True


# isalpha()
#
# Comprueba si todos los caracteres son letras.

nombre = "Jonathan"

print(nombre.isalpha())  # True


# Un espacio hace que el resultado sea False.

nombre_completo = "Homer Simpson"

print(nombre_completo.isalpha())  # False


# isalnum()
#
# Comprueba si todos los caracteres son letras o números.

codigo = "WD2026"

print(codigo.isalnum())  # True


# isspace()
#
# Comprueba si el string contiene únicamente espacios
# u otros caracteres considerados espacios en blanco.

espacios = "   "

print(espacios.isspace())  # True


# ------------------------------------------------------------
# 23. RESUMEN DE TIPOS DEVUELTOS
# ------------------------------------------------------------

# No todos los métodos de strings devuelven strings.
#
# Algunos ejemplos:


texto = "Python Python"


# Devuelve str

print(type(texto.lower()))
print(type(texto.upper()))
print(type(texto.replace("Python", "Flask")))


# Devuelve int

print(type(len(texto)))
print(type(texto.count("Python")))
print(type(texto.find("Python")))


# Devuelve bool

print(type("Python" in texto))
print(type(texto.startswith("Python")))
print(type(texto.endswith("Python")))
print(type(texto.isalpha()))


# Devuelve list

print(type(texto.split()))


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# Los strings son estructuras fundamentales para trabajar
# con información textual.
#
# Debemos recordar especialmente:
#
# 1. Son inmutables.
#
# 2. Podemos acceder a caracteres mediante índices.
#
# 3. Podemos extraer partes mediante slicing.
#
# 4. Existen métodos para limpiar, buscar, transformar,
#    dividir y validar texto.
#
# 5. Los métodos no siempre devuelven otro string.
#
# 6. split() devuelve una lista.
#
# 7. join() permite construir un string a partir de varios strings.
#
# 8. Las f-strings son una herramienta habitual para construir
#    mensajes con valores almacenados en variables.
#
# Estos conceptos aparecerán constantemente al trabajar
# posteriormente con formularios, APIs, bases de datos,
# validaciones y nuestro futuro sistema de tickets.