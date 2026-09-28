# ============================================================
# ELSE, FINALLY, RAISE Y BUENAS PRÁCTICAS
# ============================================================
#
# Ya conocemos:
#
# try
# except
#
# Ahora agregaremos:
#
# else
# finally
# raise
#
#
# Estructura completa:
#
# try:
#     operación que podría fallar
#
# except TipoDeExcepcion:
#     respuesta ante el error
#
# else:
#     código que se ejecuta si NO hubo excepción
#
# finally:
#     código que se ejecuta siempre


# ------------------------------------------------------------
# 1. ELSE
# ------------------------------------------------------------

# El bloque else se ejecuta solamente si el bloque try
# termina correctamente y no ocurre ninguna excepción.


try:
    edad_usuario = int("31")

except ValueError:
    print("La edad no es válida.")

else:
    print(f"Edad registrada: {edad_usuario}")


# Como "31" puede convertirse correctamente a int:
#
# try
# → funciona
#
# except
# → se omite
#
# else
# → se ejecuta


# ------------------------------------------------------------
# 2. EJEMPLO DE ELSE CON INPUT
# ------------------------------------------------------------

try:
    cantidad_estrellas = int(
        input("Cantidad de estrellas observadas: ")
    )

except ValueError:
    print("Debes ingresar un número entero.")

else:
    print(
        f"Cantidad registrada: {cantidad_estrellas}"
    )


# Si el usuario escribe:
#
# 25
#
# se ejecuta else.
#
#
# Si escribe:
#
# veinticinco
#
# se ejecuta except.


# ------------------------------------------------------------
# 3. POR QUÉ UTILIZAR ELSE
# ------------------------------------------------------------

# Podríamos escribir todo dentro del try:

try:
    distancia = float("4.24")

    print(
        f"Distancia registrada: {distancia}"
    )

except ValueError:
    print("Distancia inválida.")


# Pero también podemos separar:
#
# operación que puede fallar
#
# de:
#
# código que debe ejecutarse solamente si todo funcionó.


try:
    distancia_parsecs = float("4.24")

except ValueError:
    print("Distancia inválida.")

else:
    print(
        f"Distancia registrada: {distancia_parsecs}"
    )


# Esto puede mejorar la claridad.


# ------------------------------------------------------------
# 4. FINALLY
# ------------------------------------------------------------

# finally se ejecuta al terminar el try,
# independientemente de si ocurrió una excepción.


try:
    numero = int("50")

except ValueError:
    print("Número inválido.")

finally:
    print("Proceso terminado.")


# Resultado:
#
# el try funciona
# ↓
# finally se ejecuta igualmente


# ------------------------------------------------------------
# 5. FINALLY CUANDO OCURRE UNA EXCEPCIÓN
# ------------------------------------------------------------

try:
    numero_invalido = int("Galileo")

except ValueError:
    print("No fue posible realizar la conversión.")

finally:
    print("Intento de conversión finalizado.")


# Aunque ocurrió ValueError:
#
# finally
#
# también se ejecutó.


# ------------------------------------------------------------
# 6. PARA QUÉ SIRVE FINALLY
# ------------------------------------------------------------

# finally es especialmente útil cuando necesitamos realizar
# una acción independientemente del resultado.
#
# Por ejemplo:
#
# - cerrar recursos;
# - liberar recursos;
# - realizar limpieza;
# - finalizar determinados procesos.
#
#
# Más adelante tendrá más sentido cuando trabajemos
# con archivos, conexiones y otros recursos.


# ------------------------------------------------------------
# 7. ESTRUCTURA COMPLETA
# ------------------------------------------------------------

try:
    divisor = int(
        input("Ingresa un divisor: ")
    )

    resultado = 100 / divisor

except ValueError:
    print("Debes ingresar un número entero.")

except ZeroDivisionError:
    print("No puedes dividir por cero.")

else:
    print(f"Resultado: {resultado}")

finally:
    print("Operación de división finalizada.")


# Podemos interpretar:
#
# try
# → intenta la operación
#
# except
# → responde ante errores conocidos
#
# else
# → se ejecuta si no hubo errores
#
# finally
# → se ejecuta siempre


# ------------------------------------------------------------
# 8. NO NECESITAMOS USAR TODO SIEMPRE
# ------------------------------------------------------------

# No todas las estructuras necesitan:
#
# try
# except
# else
# finally
#
# al mismo tiempo.
#
#
# Muchas veces bastará con:

try:
    numero_simple = int("10")

except ValueError:
    print("Dato inválido.")


# Debemos utilizar únicamente las partes que aporten valor.


# ------------------------------------------------------------
# 9. GUARDAR LA EXCEPCIÓN CON "as"
# ------------------------------------------------------------

# Podemos guardar el objeto de la excepción en una variable.

try:
    numero_cientifico = int("Stephen Hawking")

except ValueError as error:
    print("Ocurrió un ValueError.")
    print(error)


# La variable:
#
# error
#
# contiene información sobre la excepción producida.


# ------------------------------------------------------------
# 10. CUÁNDO UTILIZAR "as"
# ------------------------------------------------------------

# Puede ser útil cuando necesitamos:
#
# - conocer más detalles;
# - registrar información;
# - diagnosticar problemas.
#
#
# Por ahora basta con reconocer esta sintaxis:
#
# except ValueError as error:
#
# No necesitamos utilizarla en todos los except.


# ------------------------------------------------------------
# 11. RAISE
# ------------------------------------------------------------

# Hasta ahora las excepciones eran generadas automáticamente
# por Python.
#
# También podemos generar una excepción nosotros mismos
# utilizando:
#
# raise


def validar_edad(edad):

    if edad < 0:
        raise ValueError(
            "La edad no puede ser negativa."
        )

    return edad


edad_correcta = validar_edad(31)

print(edad_correcta)


# Si ejecutáramos:
#
# validar_edad(-5)
#
# nuestra propia función produciría:
#
# ValueError


# ------------------------------------------------------------
# 12. QUÉ SIGNIFICA RAISE
# ------------------------------------------------------------

# Podemos pensar:
#
# raise
#
# → "esta situación no es válida;
#    genera una excepción".
#
#
# Ejemplo:
#
# if valor_invalido:
#     raise ValueError("Mensaje")


# ------------------------------------------------------------
# 13. RAISE PARA VALIDAR DATOS
# ------------------------------------------------------------

def validar_prioridad(prioridad):

    prioridades_validas = [
        "Baja",
        "Media",
        "Alta"
    ]

    if prioridad not in prioridades_validas:
        raise ValueError(
            "La prioridad indicada no es válida."
        )

    return prioridad


prioridad_correcta = validar_prioridad(
    "Alta"
)

print(prioridad_correcta)


# La función establece una regla:
#
# solamente acepta prioridades conocidas.


# ------------------------------------------------------------
# 14. CAPTURAR UNA EXCEPCIÓN GENERADA CON RAISE
# ------------------------------------------------------------

try:
    prioridad_ticket = validar_prioridad(
        "Urgentísima"
    )

except ValueError as error:
    print(f"Error: {error}")


# Flujo:
#
# validar_prioridad()
# ↓
# detecta valor inválido
# ↓
# raise ValueError
# ↓
# except ValueError
# ↓
# responde de forma controlada


# ------------------------------------------------------------
# 15. EJEMPLO CON CIENTÍFICOS
# ------------------------------------------------------------

def validar_anio_nacimiento(anio):

    if anio <= 0:
        raise ValueError(
            "El año debe ser mayor que cero."
        )

    return anio


try:
    anio_hawking = validar_anio_nacimiento(
        1942
    )

except ValueError as error:
    print(error)

else:
    print(
        f"Año registrado: {anio_hawking}"
    )


# ------------------------------------------------------------
# 16. RAISE NO ES LO MISMO QUE PRINT
# ------------------------------------------------------------

# Esto:

def validar_cantidad_menos_util(cantidad):

    if cantidad < 0:
        print("Cantidad inválida.")

    return cantidad


# solamente muestra un mensaje.
#
#
# En cambio:


def validar_cantidad(cantidad):

    if cantidad < 0:
        raise ValueError(
            "La cantidad no puede ser negativa."
        )

    return cantidad


# raise comunica al programa que ocurrió una situación
# excepcional.
#
# Otro código puede decidir posteriormente cómo manejarla.


# ------------------------------------------------------------
# 17. SEPARAR VALIDACIÓN Y RESPUESTA
# ------------------------------------------------------------

def validar_nivel_prioridad(nivel):

    if nivel < 1 or nivel > 3:
        raise ValueError(
            "La prioridad debe estar entre 1 y 3."
        )

    return nivel


try:
    nivel_ticket = validar_nivel_prioridad(
        2
    )

except ValueError as error:
    print(error)

else:
    print(
        f"Nivel aceptado: {nivel_ticket}"
    )


# Observa las responsabilidades:
#
# validar_nivel_prioridad()
# → aplica la regla
#
# try/except
# → decide cómo responder si la regla falla


# ------------------------------------------------------------
# 18. NO USAR EXCEPCIONES PARA TODO
# ------------------------------------------------------------

# No toda condición necesita una excepción.
#
# Por ejemplo:

edad_persona = 17

if edad_persona >= 18:
    print("Mayor de edad.")

else:
    print("Menor de edad.")


# Esto es simplemente una decisión normal del programa.
#
# No necesitamos:
#
# raise ValueError
#
# solo porque una persona sea menor de edad.


# Las excepciones representan situaciones que impiden
# continuar normalmente con una determinada operación.


# ------------------------------------------------------------
# 19. VALIDACIÓN NORMAL VS EXCEPCIÓN
# ------------------------------------------------------------

# CONDICIONAL:
#
# if estado == "Nuevo":
#     ...
#
# representa lógica normal.
#
#
# EXCEPCIÓN:
#
# if cantidad < 0:
#     raise ValueError(...)
#
# puede representar un dato que consideramos inválido.


# ------------------------------------------------------------
# 20. EVITAR EXCEPT VACÍOS
# ------------------------------------------------------------

# Evitaremos patrones como:
#
# try:
#     operacion()
#
# except:
#     pass
#
#
# porque pueden ocultar completamente un problema.
#
#
# Si ocurre un error, debemos:
#
# - manejarlo;
# - informar;
# - devolver una respuesta adecuada;
#
# o dejar que el error continúe si no sabemos solucionarlo.


# ------------------------------------------------------------
# 21. EVITAR CAPTURAR DEMASIADO
# ------------------------------------------------------------

# EVITAR como costumbre:

# try:
#     muchas_lineas_de_codigo()
# except Exception:
#     print("Error")


# PREFERIR:

try:
    cantidad_usuarios = int("25")

except ValueError:
    print("Cantidad inválida.")


# Capturamos exactamente el problema que conocemos.


# ------------------------------------------------------------
# 22. NO CONFUNDIR ERROR CON VALIDACIÓN DE NEGOCIO
# ------------------------------------------------------------

# Una aplicación puede tener reglas.
#
# Por ejemplo:
#
# un ticket solamente puede tener ciertas prioridades.
#
# Una función puede detectar un dato inválido:

def normalizar_prioridad(prioridad):

    prioridad_limpia = prioridad.strip().title()

    prioridades_validas = [
        "Baja",
        "Media",
        "Alta"
    ]

    if prioridad_limpia not in prioridades_validas:
        raise ValueError(
            "Prioridad no reconocida."
        )

    return prioridad_limpia


try:
    prioridad_normalizada = normalizar_prioridad(
        " alta "
    )

except ValueError as error:
    print(error)

else:
    print(prioridad_normalizada)


# Este ejemplo es solamente pedagógico.
#
# La lógica real de WorkDesk se diseñará posteriormente.


# ------------------------------------------------------------
# 23. EJEMPLO CON FUNCIÓN DE DIVISIÓN
# ------------------------------------------------------------

def calcular_promedio_por_elementos(
    total,
    cantidad
):

    if cantidad == 0:
        raise ValueError(
            "La cantidad debe ser mayor que cero."
        )

    return total / cantidad


try:
    promedio = calcular_promedio_por_elementos(
        total=500,
        cantidad=5
    )

except ValueError as error:
    print(error)

else:
    print(f"Promedio: {promedio}")


# Aquí evitamos realizar una operación inválida antes de
# llegar a una división por cero.


# ------------------------------------------------------------
# 24. EJEMPLO COMPLETO
# ------------------------------------------------------------

def calcular_costo(
    cantidad,
    precio_unitario
):

    if cantidad < 0:
        raise ValueError(
            "La cantidad no puede ser negativa."
        )

    if precio_unitario < 0:
        raise ValueError(
            "El precio no puede ser negativo."
        )

    return cantidad * precio_unitario


try:
    costo_total = calcular_costo(
        cantidad=3,
        precio_unitario=15000
    )

except ValueError as error:
    print(f"Datos inválidos: {error}")

else:
    print(
        f"Costo calculado: {costo_total}"
    )

finally:
    print("Proceso de cálculo terminado.")


# Este ejemplo reúne:
#
# función
# parámetros
# condicionales
# raise
# ValueError
# try
# except
# else
# finally


# ------------------------------------------------------------
# 25. BUENAS PRÁCTICAS BÁSICAS
# ------------------------------------------------------------

# 1.
# Capturar excepciones específicas.
#
#
# 2.
# No envolver innecesariamente todo el programa
# dentro de un try.
#
#
# 3.
# No ocultar errores con except vacío.
#
#
# 4.
# Utilizar mensajes comprensibles.
#
#
# 5.
# Utilizar raise cuando una función detecta una
# situación que considera inválida.
#
#
# 6.
# No utilizar excepciones para reemplazar todos
# los if y else.
#
#
# 7.
# Manejar solamente los errores que realmente
# sabemos cómo tratar.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# TRY
#
# intenta una operación que podría fallar.
#
#
# EXCEPT
#
# responde ante una excepción determinada.
#
#
# ELSE
#
# se ejecuta cuando el try termina correctamente.
#
#
# FINALLY
#
# se ejecuta independientemente de si hubo
# una excepción o no.
#
#
# RAISE
#
# permite generar una excepción intencionalmente.
#
#
# EJEMPLO:
#
# if edad < 0:
#     raise ValueError("Edad inválida")
#
#
# CAPTURAR INFORMACIÓN:
#
# except ValueError as error:
#     print(error)
#
#
# ESTRUCTURA COMPLETA:
#
# try:
#     ...
#
# except ValueError:
#     ...
#
# else:
#     ...
#
# finally:
#     ...
#
#
# No necesitamos utilizar las cuatro secciones siempre.
#
#
# REGLA GENERAL:
#
# operación riesgosa
# ↓
# try
#
# error conocido
# ↓
# except
#
# ejecución correcta opcional
# ↓
# else
#
# acción que debe ocurrir siempre
# ↓
# finally
#
#
# Cuando nuestra propia lógica detecta un dato inválido:
#
# raise
#
#
# El objetivo del manejo de excepciones no es ocultar errores.
#
# El objetivo es permitir que nuestros programas respondan
# de manera controlada ante situaciones previsibles.