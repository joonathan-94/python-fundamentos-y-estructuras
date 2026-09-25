# ============================================================
# OPERADORES LÓGICOS EN PYTHON
# ============================================================
#
# Los operadores lógicos permiten combinar o negar
# expresiones según su valor de verdad.
#
# Los tres operadores principales son:
#
# and
# or
# not
#
# Serán especialmente importantes cuando estudiemos:
#
# - if
# - elif
# - while
# - validaciones
# - permisos
# - reglas de negocio
#
# Por ahora trabajaremos principalmente con valores booleanos
# y comparaciones.


# ------------------------------------------------------------
# 1. OPERADOR and
# ------------------------------------------------------------

# Cuando trabajamos con valores booleanos:
#
# and permite expresar que ambas condiciones
# deben cumplirse.

usuario_autenticado = True
es_tecnico = True

puede_gestionar_ticket = usuario_autenticado and es_tecnico

print(
    "¿Puede gestionar el ticket?:",
    puede_gestionar_ticket
)


# Ejemplos básicos:
#
# True  and True   -> True
# True  and False  -> False
# False and True   -> False
# False and False  -> False


# ------------------------------------------------------------
# 2. OPERADOR or
# ------------------------------------------------------------

# or permite expresar que al menos una de las condiciones
# debe cumplirse.

es_tecnico = True
es_supervisor = False

tiene_permiso_gestion = es_tecnico or es_supervisor

print(
    "¿Tiene permiso de gestión?:",
    tiene_permiso_gestion
)


# Ejemplos básicos:
#
# True  or True   -> True
# True  or False  -> True
# False or True   -> True
# False or False  -> False


# ------------------------------------------------------------
# 3. OPERADOR not
# ------------------------------------------------------------

# not invierte el valor de verdad.
#
# True  -> False
# False -> True

ticket_cerrado = False

ticket_disponible = not ticket_cerrado

print(
    "¿Ticket disponible?:",
    ticket_disponible
)


# ------------------------------------------------------------
# 4. COMBINAR COMPARACIONES CON and
# ------------------------------------------------------------

tickets_asignados = 5
limite_tickets = 10
usuario_activo = True

puede_recibir_tickets = (
    tickets_asignados < limite_tickets
    and usuario_activo
)

print(
    "¿Puede recibir más tickets?:",
    puede_recibir_tickets
)


# ------------------------------------------------------------
# 5. COMBINAR and, or Y not
# ------------------------------------------------------------

usuario_autenticado = True

es_tecnico = True
es_supervisor = False

ticket_cerrado = False

puede_gestionar_ticket = (
    usuario_autenticado
    and (es_tecnico or es_supervisor)
    and not ticket_cerrado
)

print(
    "¿Puede gestionar el ticket?:",
    puede_gestionar_ticket
)


# Esta expresión puede leerse como:
#
# El usuario:
#
# 1. debe estar autenticado
#
# Y
#
# 2. debe ser técnico O supervisor
#
# Y
#
# 3. el ticket NO debe estar cerrado


# ------------------------------------------------------------
# 6. PRECEDENCIA DE OPERADORES LÓGICOS
# ------------------------------------------------------------

# Entre los operadores lógicos estudiados, el orden
# de prioridad es:
#
# 1. not
# 2. and
# 3. or
#
# Las comparaciones como:
#
# >
# <
# ==
# >=
# <=
#
# tienen mayor prioridad que estos operadores lógicos.


# Aunque Python conozca estas reglas, utilizar paréntesis
# suele hacer que una expresión compleja sea más fácil de leer.

resultado = True or False and False

print(resultado)


# Python interpreta primero:

# False and False

# y después:

# True or False


# Podemos hacer explícita nuestra intención:

resultado = True or (False and False)

print(resultado)


# ------------------------------------------------------------
# 7. EVALUACIÓN DE CORTOCIRCUITO
# ------------------------------------------------------------

# and y or utilizan evaluación de cortocircuito.
#
# Esto significa que Python puede dejar de evaluar
# una expresión cuando ya conoce su resultado lógico.


# Con and:
#
# si el primer valor resulta falso, no es necesario
# evaluar los siguientes para determinar que la condición
# completa no puede cumplirse.


# Con or:
#
# si el primer valor resulta verdadero, no es necesario
# evaluar los siguientes para saber que ya existe una
# condición verdadera.


# Este comportamiento será más importante posteriormente
# cuando trabajemos con condiciones y funciones.


# ------------------------------------------------------------
# 8. PRECISIÓN TÉCNICA SOBRE and Y or
# ------------------------------------------------------------

# Aunque normalmente utilizaremos and y or para construir
# condiciones, técnicamente estos operadores no están
# obligados a devolver True o False.
#
# Pueden devolver uno de los operandos evaluados.

valor = "" or "Sin título"

print(valor)


# Como "" es considerado falso,
# Python devuelve el segundo valor:
#
# "Sin título"


# En cambio, not sí devuelve siempre un booleano.

resultado_not = not "Python"

print(resultado_not)  # False


# No es necesario utilizar esta característica avanzada
# todavía.
#
# Lo importante por ahora es reconocer que:
#
# and
# or
#
# trabajan con el valor de verdad de sus operandos.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# and
# → normalmente representa que deben cumplirse varias
#   condiciones.
#
# or
# → normalmente representa que basta con que se cumpla
#   alguna condición.
#
# not
# → niega o invierte una condición.
#
# Precedencia:
#
# not
# ↓
# and
# ↓
# or
#
# Los paréntesis ayudan a hacer explícita la lógica.
#
# Estos operadores adquirirán especial importancia en
# el siguiente módulo cuando estudiemos control de flujo.