# ============================================================
# SENTENCIAS CONDICIONALES EN PYTHON
# ============================================================
#
# Las sentencias condicionales permiten ejecutar distintos
# bloques de código dependiendo de si una condición se evalúa
# como verdadera o falsa.
#
# Las principales estructuras son:
#
# if
# if - else
# if - elif - else
#
# Para construir condiciones utilizaremos conceptos ya
# estudiados:
#
# - operadores de comparación
# - operadores lógicos
# - valores booleanos
#
# Estas estructuras serán fundamentales para implementar
# validaciones, permisos, estados y reglas de negocio.


# ------------------------------------------------------------
# 1. INDENTACIÓN
# ------------------------------------------------------------

# Python utiliza indentación para identificar qué instrucciones
# pertenecen a un bloque.
#
# Por convención se utilizan 4 espacios.
#
# Después de if, elif y else se utilizan dos puntos (:).

usuario_activo = True

if usuario_activo:
    print("El usuario está activo.")

print("El programa continúa.")


# En este ejemplo:
#
# print("El usuario está activo.")
#
# pertenece al bloque del if porque está indentado.
#
# print("El programa continúa.")
#
# está fuera del bloque y se ejecutará independientemente
# del resultado de la condición.


# ------------------------------------------------------------
# 2. CONDICIONAL if
# ------------------------------------------------------------

# if ejecuta un bloque únicamente cuando su condición
# se evalúa como verdadera.

estado_ticket = "Nuevo"

if estado_ticket == "Nuevo":
    print("El ticket debe ser revisado.")


# Si la condición fuera falsa, simplemente se omitiría
# el bloque indentado.


# ------------------------------------------------------------
# 3. if - else
# ------------------------------------------------------------

# else permite definir qué debe ocurrir cuando la condición
# del if no se cumple.

ticket_cerrado = False

if ticket_cerrado:
    print("El ticket está cerrado.")
else:
    print("El ticket todavía está disponible.")


# Solo uno de los dos bloques será ejecutado.


# ------------------------------------------------------------
# 4. if - elif - else
# ------------------------------------------------------------

# elif permite comprobar condiciones adicionales.
#
# Python evalúa las condiciones de arriba hacia abajo.
#
# Cuando encuentra la primera condición verdadera,
# ejecuta ese bloque y deja de evaluar los siguientes.

prioridad = "Alta"

if prioridad == "Crítica":
    print("Atención inmediata.")
elif prioridad == "Alta":
    print("Atención prioritaria.")
elif prioridad == "Media":
    print("Atención normal.")
else:
    print("Prioridad baja.")


# ------------------------------------------------------------
# 5. COMPARACIONES DENTRO DE CONDICIONALES
# ------------------------------------------------------------

tiempo_resolucion = 3.5
tiempo_sla = 4.0

if tiempo_resolucion <= tiempo_sla:
    print("El ticket fue resuelto dentro del tiempo permitido.")
else:
    print("El ticket superó el tiempo permitido.")


# Aquí utilizamos el operador <= estudiado anteriormente.


# ------------------------------------------------------------
# 6. OPERADORES LÓGICOS EN CONDICIONES
# ------------------------------------------------------------

usuario_autenticado = True
es_tecnico = True
ticket_cerrado = False

if usuario_autenticado and es_tecnico and not ticket_cerrado:
    print("El usuario puede gestionar el ticket.")
else:
    print("El usuario no puede gestionar el ticket.")


# La condición anterior puede leerse como:
#
# usuario autenticado
# Y
# es técnico
# Y
# el ticket NO está cerrado


# ------------------------------------------------------------
# 7. USAR or DENTRO DE UNA CONDICIÓN
# ------------------------------------------------------------

es_tecnico = False
es_supervisor = True

if es_tecnico or es_supervisor:
    print("El usuario tiene permisos de gestión.")
else:
    print("El usuario no tiene permisos de gestión.")


# Basta con que una de las dos condiciones sea verdadera.


# ------------------------------------------------------------
# 8. CONDICIONALES ANIDADOS
# ------------------------------------------------------------

# Un condicional puede contener otro condicional.
#
# Esto puede ser útil cuando una segunda comprobación
# solo tiene sentido después de cumplir la primera.

usuario_activo = True
rol_usuario = "Técnico"

if usuario_activo:
    print("Usuario activo.")

    if rol_usuario == "Técnico":
        print("Acceso al área técnica permitido.")
    else:
        print("El usuario no pertenece al área técnica.")
else:
    print("Usuario inactivo.")


# La segunda condición solamente se evalúa si usuario_activo
# es verdadero.


# ------------------------------------------------------------
# 9. EVITAR COMPARACIONES INNECESARIAS CON True Y False
# ------------------------------------------------------------

cuenta_activa = True


# Aunque esto funciona:
#
# if cuenta_activa == True:
#     print("Cuenta activa")


# Normalmente es más claro escribir:

if cuenta_activa:
    print("Cuenta activa.")


# Para comprobar el caso contrario podemos utilizar not:

cuenta_bloqueada = False

if not cuenta_bloqueada:
    print("La cuenta no está bloqueada.")


# ------------------------------------------------------------
# 10. ORDEN DE LAS CONDICIONES
# ------------------------------------------------------------

# El orden de if y elif importa.
#
# Debemos comprobar primero los casos más específicos
# cuando una condición puede incluir a otra.

tiempo_respuesta = 15

if tiempo_respuesta <= 15:
    print("Respuesta excelente.")
elif tiempo_respuesta <= 30:
    print("Respuesta aceptable.")
else:
    print("Respuesta lenta.")


# Si tiempo_respuesta vale 15, Python entra en el primer bloque
# y ya no evalúa los siguientes.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# if
# → ejecuta código si una condición se cumple.
#
# else
# → ejecuta una alternativa cuando el if no se cumple.
#
# elif
# → permite evaluar condiciones adicionales.
#
# Python evalúa las condiciones en orden.
#
# Los bloques se definen mediante indentación.
#
# Los operadores de comparación y operadores lógicos permiten
# construir condiciones más completas.
#
# Estos conceptos serán esenciales posteriormente para trabajar
# con reglas de negocio, validaciones y estados de tickets.