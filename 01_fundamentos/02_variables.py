# ============================================================
# VARIABLES EN PYTHON
# ============================================================
#
# Una variable es un nombre que referencia un objeto.
#
# En Python no es necesario declarar previamente el tipo
# de una variable. El tipo pertenece al objeto al que
# la variable hace referencia.


# ------------------------------------------------------------
# 1. ASIGNACIÓN DE VARIABLES
# ------------------------------------------------------------

# El operador = se utiliza para asignar un valor a un nombre.

nombre = "Jonathan"
edad = 32
altura = 1.63
activo = True

print(nombre)
print(edad)
print(altura)
print(activo)


# ------------------------------------------------------------
# 2. USAR VARIABLES
# ------------------------------------------------------------

# Una variable puede utilizarse posteriormente para realizar
# operaciones o construir nuevos valores.

personaje = "Neo"

bienvenida = f"Hola {personaje}, ¿cómo estás?"

print(bienvenida)


# ------------------------------------------------------------
# 3. NOMBRES DESCRIPTIVOS
# ------------------------------------------------------------

# Los nombres de variables deberían indicar claramente
# qué información representan.

ticket_id = 25
titulo_ticket = "Problema de conexión"
prioridad_ticket = "Alta"
tecnico_responsable = None

print(ticket_id)
print(titulo_ticket)
print(prioridad_ticket)
print(tecnico_responsable)


# ------------------------------------------------------------
# 4. SNAKE_CASE
# ------------------------------------------------------------

# La convención habitual en Python para nombres de variables
# es snake_case:
#
# palabras en minúsculas separadas por guiones bajos.

nombre_usuario = "Elliot Alderson"
cantidad_tickets = 5
fecha_creacion = "2026-09-22"

# Evitaremos estilos como:
#
# nombreUsuario
# CantidadTickets
#
# aunque algunos sean técnicamente válidos.


# ------------------------------------------------------------
# 5. REASIGNACIÓN
# ------------------------------------------------------------

# Una variable puede hacer referencia a otro valor posteriormente.

estado_ticket = "Nuevo"

print("Estado inicial:", estado_ticket)

estado_ticket = "En progreso"

print("Estado actualizado:", estado_ticket)


# ------------------------------------------------------------
# 6. TIPADO DINÁMICO
# ------------------------------------------------------------

# Python utiliza tipado dinámico.
#
# Una misma variable puede referenciar objetos de distintos
# tipos durante la ejecución del programa.

dato = 10
print(dato, type(dato))

dato = "Walter White"
print(dato, type(dato))

# Aunque Python lo permite, cambiar constantemente el significado
# y el tipo de una variable puede dificultar la lectura del código.
# Conviene mantener nombres y propósitos claros.


# ------------------------------------------------------------
# 7. ASIGNACIÓN MÚLTIPLE
# ------------------------------------------------------------

# Python permite asignar varios valores en una misma línea.

nombre, rol, activo = "Tony Soprano", "Solicitante", True

print(nombre)
print(rol)
print(activo)


# También puede asignarse el mismo valor a varias variables.

estado_anterior = estado_actual = "Nuevo"

print(estado_anterior)
print(estado_actual)


# ------------------------------------------------------------
# 8. INTERCAMBIO DE VALORES
# ------------------------------------------------------------

# Python permite intercambiar los valores de dos variables
# sin necesitar una variable temporal.

tecnico_principal = "Neo"
tecnico_secundario = "Morpheus"

tecnico_principal, tecnico_secundario = (
    tecnico_secundario,
    tecnico_principal
)

print("Principal:", tecnico_principal)
print("Secundario:", tecnico_secundario)


# ------------------------------------------------------------
# 9. REGLAS PARA NOMBRAR VARIABLES
# ------------------------------------------------------------

# Un nombre de variable puede contener:
#
# - Letras
# - Números
# - Guion bajo (_)
#
# Pero no puede comenzar con un número.

usuario_1 = "Homer Simpson"
_usuario_interno = "Rick Sanchez"

# Ejemplos inválidos:
#
# 1_usuario = "Neo"
# nombre-usuario = "Neo"
#
# Tampoco pueden utilizarse palabras reservadas de Python:
#
# if = 10
# for = 20
# class = "Ticket"


# ------------------------------------------------------------
# 10. CONSTANTES POR CONVENCIÓN
# ------------------------------------------------------------

# Python no posee constantes estrictas como otros lenguajes.
#
# Por convención, un nombre escrito completamente en mayúsculas
# indica que ese valor no debería modificarse durante el programa.

MAX_INTENTOS_LOGIN = 5
TIEMPO_SESION_MINUTOS = 30

print(MAX_INTENTOS_LOGIN)
print(TIEMPO_SESION_MINUTOS)