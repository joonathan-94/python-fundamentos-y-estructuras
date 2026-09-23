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
# VARIABLES
# ============================================================

print('EJERCICIOS SOBRE VARIABLES')

# ------------------------------------------------------------
# VAR-01 - DATOS DE UN USUARIO
# ------------------------------------------------------------
#
# Crea variables para representar los siguientes datos:
#
# Nombre: "Elliot Alderson"
# Rol: "Técnico"
# Edad: 28
# Usuario activo: True
#
# Utiliza nombres descriptivos siguiendo la convención snake_case.
#
# Imprime cada variable.
#
# Tu código aquí:

print('Ejercicio de variables nro 1')

nombre = 'Elliot Alderson'
rol = 'Tecnico'
edad = 28
usuario_activo = True

print(nombre)
print(rol)
print(edad)
print(usuario_activo)

# ------------------------------------------------------------
# VAR-02 - DATOS DE UN TICKET
# ------------------------------------------------------------
#
# Representa mediante variables los siguientes datos:
#
# ID: 42
# Título: "Error al iniciar sesión"
# Prioridad: "Alta"
# Estado: "Nuevo"
# Solicitante: "Homer Simpson"
# Técnico responsable: todavía ninguno
#
# Utiliza nombres descriptivos siguiendo snake_case.
#
# Imprime todos los valores.
#
# Tu código aquí:

print('Ejercicio de variables nro 2')

identificador_ticket = 42
titulo_ticket = 'Error de inicio de sesión'
prioridad_ticket = 'Alta'
estado = 'nuevo'
solicitante = 'Homer Simpson'
tecnico_responsable = None

print(identificador_ticket)
print(titulo_ticket)
print(prioridad_ticket)
print(estado)
print(solicitante)
print(tecnico_responsable)


# ------------------------------------------------------------
# VAR-03 - REASIGNACIÓN DE ESTADO
# ------------------------------------------------------------
#
# Crea una variable llamada estado_ticket cuyo valor inicial
# sea "Nuevo".
#
# 1. Imprime el estado inicial.
# 2. Reasigna la variable con el valor "Asignado".
# 3. Imprime nuevamente el estado.
# 4. Reasigna la variable con el valor "En progreso".
# 5. Imprime el estado final.
#
# El objetivo es observar cómo una variable puede referenciar
# distintos valores durante la ejecución.
#
# Tu código aquí:

print('Ejercicio de variables nro 3')

estado_ticket = 'Nuevo'
print(estado_ticket)
estado_ticket = 'Asignado'
print(estado_ticket)
estado_ticket = 'En progreso'
print(estado_ticket)

# ------------------------------------------------------------
# VAR-04 - ASIGNACIÓN MÚLTIPLE
# ------------------------------------------------------------
#
# Utilizando una sola línea de asignación, crea las variables:
#
# tecnico
# grupo
# disponible
#
# con los valores:
#
# "Neo"
# "Infraestructura"
# True
#
# Después imprime las tres variables.
#
# Tu código aquí:

print('Ejercicio de variables nro 4')

tecnico, grupo, disponible = 'neo', 'infraestructura', True
print(tecnico)
print(grupo)
print(disponible)


# ------------------------------------------------------------
# VAR-05 - INTERCAMBIO DE VALORES
# ------------------------------------------------------------
#
# Tienes:
#
# tecnico_principal = "Walter White"
# tecnico_secundario = "Jesse Pinkman"
#
# Intercambia sus valores sin crear una tercera variable.
#
# Después imprime ambos valores para comprobar el resultado.
#
# Tu código aquí:

print('Ejercicio de variables nro 5')

tecnico_principal = "Walter White"
tecnico_secundario = "Jesse Pinkman"

print(tecnico_principal)
print(tecnico_secundario)

tecnico_principal, tecnico_secundario = (tecnico_secundario, tecnico_principal)

print(tecnico_principal)
print(tecnico_secundario)


# ------------------------------------------------------------
# DESAFÍO VAR - CICLO BÁSICO DE UN TICKET
# ------------------------------------------------------------
#
# Crea variables para representar:
#
# ID del ticket: 100
# Título: "Impresora sin conexión"
# Prioridad: "Media"
# Estado inicial: "Nuevo"
# Solicitante: "Michael Corleone"
# Técnico responsable: None
#
# Después:
#
# 1. Imprime los datos iniciales.
# 2. Reasigna el estado a "Asignado".
# 3. Asigna como técnico responsable a "Elliot Alderson".
# 4. Reasigna nuevamente el estado a "En progreso".
# 5. Imprime el estado final y el técnico responsable.
#
# Utiliza nombres descriptivos y snake_case.
#
# Tu código aquí:

print('Ejercicio: Desafio variables')

id_ticket = 100
titulo_ticket = "Impresora sin conexión"
prioridad = 'Media'
estado_ticket = 'Nuevo'
solicitante_ticket = 'Michael Corleone'
tecnico_responsable = None

print(id_ticket)
print(titulo_ticket)
print(prioridad)
print(estado_ticket)
print(solicitante_ticket)
print(tecnico_responsable)

tecnico_responsable = 'Elliot Alderson'
estado_ticket = 'En progreso'
print(estado_ticket)
print(tecnico_responsable)