# ============================================================
# EJERCICIOS - OPERADORES
# ============================================================
#
# Este archivo contiene ejercicios breves correspondientes
# al módulo de operadores.
#
# El objetivo es comprobar la comprensión de los conceptos
# principales sin agregar complejidad innecesaria.


# ------------------------------------------------------------
# OP-01 - DISTRIBUIR TICKETS
# ------------------------------------------------------------
#
# Tienes:
#
# tickets_pendientes = 85
# tecnicos_disponibles = 4
#
# Utilizando operadores aritméticos:
#
# 1. Calcula cuántos tickets puede recibir cada técnico
#    utilizando división entera //.
#
# 2. Calcula cuántos tickets sobran utilizando %.
#
# Guarda los resultados en:
#
# tickets_por_tecnico
# tickets_sobrantes
#
# Imprime ambos resultados.
#
# Tu código aquí:

tickets_pendientes = 85
tecnicos_disponibles = 4

tickets_por_tecnico = tickets_pendientes // tecnicos_disponibles
tickets_sobrantes = tickets_pendientes % tecnicos_disponibles

print(tickets_por_tecnico)
print(tickets_sobrantes)


# ------------------------------------------------------------
# OP-02 - COMPARAR DATOS DE UN TICKET
# ------------------------------------------------------------
#
# Tienes:
#
# tiempo_resolucion = 3.5
# tiempo_sla = 4.0
#
# estado_actual = "En progreso"
# estado_esperado = "En progreso"
#
# Realiza dos comparaciones:
#
# 1. Comprueba si tiempo_resolucion es menor o igual
#    que tiempo_sla.
#
# 2. Comprueba si estado_actual es igual
#    a estado_esperado.
#
# Guarda los resultados en:
#
# cumple_sla
# estado_correcto
#
# Imprime ambos valores.
#
# Tu código aquí:

tiempo_resolucion = 3.5
tiempo_sla = 4.0

estado_actual = "En progreso"
estado_esperado = "En progreso"

cumple_sla = tiempo_resolucion <= tiempo_sla
estado_correcto = estado_actual == estado_esperado

print(cumple_sla)
print(estado_correcto)


# ------------------------------------------------------------
# OP-03 - VALIDAR PERMISO DE GESTIÓN
# ------------------------------------------------------------
#
# Tienes:
#
# usuario_autenticado = True
# es_tecnico = True
# es_supervisor = False
# ticket_cerrado = False
#
# Un usuario puede gestionar el ticket solamente si:
#
# - está autenticado
#
# Y
#
# - es técnico O supervisor
#
# Y
#
# - el ticket NO está cerrado
#
# Construye una expresión utilizando:
#
# and
# or
# not
#
# Guarda el resultado en:
#
# puede_gestionar_ticket
#
# Imprime el resultado.
#
# Tu código aquí:

usuario_autenticado = True
es_tecnico = True
es_supervisor = False
ticket_cerrado = False

puede_gestionar_ticket = usuario_autenticado and (es_tecnico or es_supervisor) and not ticket_cerrado

print(puede_gestionar_ticket)