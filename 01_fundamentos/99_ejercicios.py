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