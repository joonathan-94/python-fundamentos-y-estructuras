# ============================================================
# EJERCICIOS - FUNDAMENTOS DE PYTHON
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 1 - IDENTIFICAR TIPOS
# ------------------------------------------------------------

print("Ejercicio 1:")

nombre_personaje = "Tony Soprano"
edad = 39
altura = 1.85
activo = False
alias = "T"

print("Nombre:", type(nombre_personaje))
print("Edad:", type(edad))
print("Altura:", type(altura))
print("Activo:", type(activo))
print("Alias:", type(alias))


# ------------------------------------------------------------
# EJERCICIO 2 - DETECTAR LA DIFERENCIA ENTRE TIPOS
# ------------------------------------------------------------

print("\nEjercicio 2:")

print(type(10))
print(type("10"))
print(type(10.0))
print(type(True))
print(type(None))

print(10 + 10)
print("10" + "10")


# ------------------------------------------------------------
# EJERCICIO 3 - DATOS DE UN TICKET
# ------------------------------------------------------------

print("\nEjercicio 3:")

ticket_id = 25
titulo = "Problema de conexión"
prioridad = "Crítica"
ticket_activo = True
tecnico_responsable = None

print("ID:", type(ticket_id))
print("Título:", type(titulo))
print("Prioridad:", type(prioridad))
print("Activo:", type(ticket_activo))
print("Técnico responsable:", type(tecnico_responsable))

# ============================================================
# STRINGS
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 4 - LIMPIAR EL TÍTULO DE UN TICKET
# ------------------------------------------------------------
#
# Un usuario ingresó el siguiente título:
#
# titulo = "    ERROR DE CONEXIÓN CON SERVIDOR    "
#
# 1. Elimina los espacios sobrantes al inicio y al final.
# 2. Convierte el texto completo a minúsculas.
# 3. Guarda el resultado en una variable llamada titulo_limpio.
# 4. Imprime el título original y el título limpio.
#
# Tu código aquí:


# ------------------------------------------------------------
# EJERCICIO 5 - COMPROBAR EXTENSIÓN DE UN ARCHIVO
# ------------------------------------------------------------
#
# Un ticket contiene el siguiente archivo adjunto:
#
# archivo = "captura_error.png"
#
# Utiliza un método de strings para comprobar si el archivo
# termina en ".png".
#
# Guarda el resultado booleano en:
#
# es_imagen_png
#
# Imprime el resultado.
#
# Tu código aquí:


# ------------------------------------------------------------
# EJERCICIO 6 - BUSCAR INFORMACIÓN EN UNA DESCRIPCIÓN
# ------------------------------------------------------------
#
# Un usuario llamado Walter White creó el siguiente ticket:
#
# descripcion = "El computador presenta un error de red al iniciar sesión"
#
# 1. Comprueba si la palabra "red" aparece en la descripción.
# 2. Guarda el resultado en una variable llamada contiene_red.
# 3. Busca en qué posición comienza la palabra "error".
# 4. Guarda esa posición en una variable llamada posicion_error.
# 5. Imprime ambos resultados.
#
# Tu código aquí:


# ------------------------------------------------------------
# EJERCICIO 7 - ACTUALIZAR TEXTO DE ESTADO
# ------------------------------------------------------------
#
# Tienes el siguiente mensaje:
#
# mensaje = "El ticket #25 actualmente está Nuevo"
#
# Utiliza replace() para cambiar:
#
# "Nuevo"
#
# por:
#
# "En progreso"
#
# Guarda el resultado en una nueva variable.
# No modifiques directamente el string original.
#
# Imprime ambos valores para observar la inmutabilidad.
#
# Tu código aquí:


# ------------------------------------------------------------
# EJERCICIO 8 - PROCESAR ETIQUETAS
# ------------------------------------------------------------
#
# Un ticket posee sus etiquetas almacenadas temporalmente
# como un único string:
#
# etiquetas = "red,hardware,critico,servidor"
#
# 1. Utiliza split() para convertirlo en una lista.
# 2. Guarda el resultado en lista_etiquetas.
# 3. Imprime lista_etiquetas.
# 4. Comprueba utilizando type() qué tipo de dato devolvió split().
#
# Tu código aquí:


# ------------------------------------------------------------
# EJERCICIO 9 - MOSTRAR TÉCNICOS ASIGNADOS
# ------------------------------------------------------------
#
# Tienes la siguiente lista:
#
# tecnicos = ["Elliot Alderson", "Neo", "Tony Soprano"]
#
# Utiliza join() para obtener exactamente un string similar a:
#
# "Elliot Alderson | Neo | Tony Soprano"
#
# Guarda el resultado en:
#
# tecnicos_asignados
#
# Imprime el resultado.
#
# Tu código aquí:


# ------------------------------------------------------------
# EJERCICIO 10 - GENERAR RESUMEN DE TICKET
# ------------------------------------------------------------
#
# Tienes estas variables:
#
# ticket_id = 42
# solicitante = "Homer Simpson"
# prioridad = "Alta"
# estado = "Nuevo"
#
# Utiliza una f-string para generar un mensaje con este formato:
#
# Ticket #42 | Solicitante: Homer Simpson | Prioridad: Alta | Estado: Nuevo
#
# Guarda el resultado en:
#
# resumen_ticket
#
# Imprime el mensaje.
#
# Tu código aquí:


# ------------------------------------------------------------
# DESAFÍO - NORMALIZAR DATOS DE UN TICKET
# ------------------------------------------------------------
#
# Tienes:
#
# titulo = "    FaLLa De RED EN OfiCIna    "
# solicitante = "   neo   "
#
# Utilizando únicamente operaciones y métodos de strings:
#
# 1. Elimina los espacios sobrantes de ambos valores.
# 2. Convierte el título completamente a minúsculas.
# 3. Convierte el nombre del solicitante a formato título.
# 4. Construye mediante una f-string el siguiente mensaje:
#
# Solicitante: Neo | Ticket: falla de red en oficina
#
# No modifiques los valores originales.
#
# Tu código aquí:

