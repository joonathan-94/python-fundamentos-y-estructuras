# ============================================================
# EXCEPCIONES Y TRY / EXCEPT EN PYTHON
# ============================================================
#
# Un programa puede estar escrito correctamente y aun así
# encontrar problemas durante su ejecución.
#
# Ejemplo:
#
# numero = int("hola")
#
# La sintaxis es válida.
#
# Pero Python no puede convertir:
#
# "hola"
#
# a un número entero.
#
# Por eso ocurre:
#
# ValueError
#
#
# A este tipo de situaciones las llamamos excepciones.
#
#
# El manejo de excepciones nos permite responder de manera
# controlada ante determinados errores.


# ------------------------------------------------------------
# 1. UNA EXCEPCIÓN
# ------------------------------------------------------------

# Este código produciría un error:
#
# numero = int("treinta")
#
#
# Python mostraría algo similar a:
#
# ValueError: invalid literal for int()
#
#
# ValueError identifica el TIPO de excepción.


# ------------------------------------------------------------
# 2. LEER EL ERROR
# ------------------------------------------------------------

# Cuando Python muestra un error, una de las partes más
# importantes se encuentra normalmente al final.
#
# Ejemplo:
#
# ValueError: invalid literal for int() with base 10: 'hola'
#
#
# Podemos interpretar:
#
# ValueError
# → tipo de excepción
#
# invalid literal...
# → información sobre lo ocurrido
#
#
# Aprender a leer el tipo de excepción nos ayuda a saber
# qué problema debemos investigar.


# ------------------------------------------------------------
# 3. ValueError
# ------------------------------------------------------------

# ValueError ocurre cuando el tipo de operación es válido,
# pero el valor recibido no sirve para esa operación.
#
#
# Ejemplo:
#
# int("25")
#
# funciona.
#
#
# Pero:
#
# int("veinticinco")
#
# produce ValueError.


numero_correcto = int("25")

print(numero_correcto)


# Dejamos comentado el ejemplo que fallaría:
#
# numero_incorrecto = int("veinticinco")


# ------------------------------------------------------------
# 4. ZeroDivisionError
# ------------------------------------------------------------

# No podemos dividir un número por cero.
#
# Ejemplo:
#
# resultado = 100 / 0
#
# produce:
#
# ZeroDivisionError


resultado_valido = 100 / 5

print(resultado_valido)


# ------------------------------------------------------------
# 5. TypeError
# ------------------------------------------------------------

# TypeError aparece cuando una operación recibe tipos
# incompatibles para lo que intenta hacer.
#
#
# Ejemplo:
#
# "Edad: " + 31
#
# intenta sumar:
#
# str + int
#
# y produciría TypeError.


mensaje_correcto = "Edad: " + str(31)

print(mensaje_correcto)


# ------------------------------------------------------------
# 6. KeyError
# ------------------------------------------------------------

# Los diccionarios pueden producir KeyError cuando intentamos
# acceder directamente a una clave que no existe.


cientifico = {
    "nombre": "Stephen Hawking",
    "area": "Física"
}


print(cientifico["nombre"])


# Esto fallaría:
#
# print(cientifico["nacionalidad"])
#
# porque "nacionalidad" no existe.
#
# Python produciría:
#
# KeyError


# Recuerda que ya conocemos una alternativa cuando una clave
# puede no existir:

nacionalidad = cientifico.get(
    "nacionalidad",
    "No registrada"
)

print(nacionalidad)


# Esto también demuestra algo importante:
#
# no todos los problemas necesitan try/except.
#
# A veces el propio tipo de dato ya ofrece una herramienta
# adecuada para manejar la situación.


# ------------------------------------------------------------
# 7. IndexError
# ------------------------------------------------------------

# Una lista produce IndexError cuando intentamos acceder
# a una posición inexistente.


astronomos = [
    "Galileo Galilei",
    "Carl Sagan",
    "José Maza"
]


print(astronomos[0])


# Esto fallaría:
#
# print(astronomos[10])
#
# porque ese índice no existe.
#
# Resultado:
#
# IndexError


# ------------------------------------------------------------
# 8. try / except
# ------------------------------------------------------------

# Ahora llegamos al concepto principal.
#
#
# Estructura:
#
# try:
#     operación que podría fallar
#
# except TipoDeExcepcion:
#     qué hacer si ocurre esa excepción


try:
    edad_usuario = int(
        input("Ingresa tu edad: ")
    )

except ValueError:
    print("Debes ingresar un número entero.")


# Si escribes:
#
# 31
#
# int() funciona y except no se ejecuta.
#
#
# Si escribes:
#
# treinta
#
# ocurre ValueError y Python ejecuta:
#
# except ValueError


# ------------------------------------------------------------
# 9. FLUJO DE TRY / EXCEPT
# ------------------------------------------------------------

# Podemos visualizarlo:
#
#
# try
# ↓
# intenta ejecutar el código
#
#
# ¿todo funciona?
#
# SÍ
# ↓
# except se omite
#
#
# ¿ocurre ValueError?
#
# SÍ
# ↓
# se ejecuta except ValueError
#
#
# Después el programa puede continuar.


print("El programa continúa.")


# ------------------------------------------------------------
# 10. SOLO SE INTERRUMPE EL RESTO DEL TRY
# ------------------------------------------------------------

try:
    numero_ingresado = int(
        input("Ingresa un número: ")
    )

    print("Conversión realizada.")

except ValueError:
    print("No se pudo convertir el valor.")


# Si int() produce ValueError:
#
# Python NO alcanza:
#
# print("Conversión realizada.")
#
#
# Salta directamente al except correspondiente.


# ------------------------------------------------------------
# 11. CAPTURAR LA EXCEPCIÓN CORRECTA
# ------------------------------------------------------------

# Debemos capturar la excepción que realmente esperamos.


try:
    divisor = int(
        input("Ingresa un divisor: ")
    )

    resultado_division = 100 / divisor

    print(resultado_division)

except ValueError:
    print("El divisor debe ser un número entero.")

except ZeroDivisionError:
    print("No puedes dividir por cero.")


# Aquí existen DOS operaciones que pueden producir
# excepciones distintas:
#
#
# int(...)
# → ValueError
#
# 100 / divisor
# → ZeroDivisionError


# ------------------------------------------------------------
# 12. VARIOS EXCEPT
# ------------------------------------------------------------

# Un try puede tener varios bloques except.
#
# Python utilizará el manejador correspondiente al tipo
# de excepción que ocurrió.


try:
    posicion = int(
        input("Selecciona una posición de 0 a 2: ")
    )

    cientificos = [
        "Marie Curie",
        "Albert Einstein",
        "Stephen Hawking"
    ]

    print(cientificos[posicion])

except ValueError:
    print("Debes ingresar un número.")

except IndexError:
    print("La posición indicada no existe.")


# Ejemplo:
#
# usuario escribe:
#
# hola
#
# → ValueError
#
#
# usuario escribe:
#
# 9
#
# → IndexError


# ------------------------------------------------------------
# 13. CAPTURAR VARIAS EXCEPCIONES JUNTAS
# ------------------------------------------------------------

# Si queremos responder exactamente igual ante varios tipos,
# podemos agruparlos en una tupla.


try:
    indice_ingresado = int(
        input("Selecciona un científico: ")
    )

    nombres_cientificos = [
        "Isaac Newton",
        "Galileo Galilei",
        "Carl Sagan"
    ]

    print(nombres_cientificos[indice_ingresado])

except (ValueError, IndexError):
    print("La selección ingresada no es válida.")


# Aquí utilizamos algo que ya estudiamos:
#
# (ValueError, IndexError)
#
# es una tupla de tipos de excepción.


# ------------------------------------------------------------
# 14. NO CAPTURAR TODO SIN NECESIDAD
# ------------------------------------------------------------

# Python permite hacer cosas como:
#
# try:
#     ...
#
# except:
#     ...
#
#
# Pero evitaremos acostumbrarnos a esto.
#
# El problema es que podríamos ocultar errores que no
# esperábamos.


# Preferimos:

try:
    cantidad = int("20")

except ValueError:
    print("Cantidad inválida.")


# Esto comunica claramente:
#
# "Sé que esta conversión puede producir ValueError
# y sé cómo responder ante ese problema."


# ------------------------------------------------------------
# 15. Exception TAMBIÉN ES MUY AMPLIO
# ------------------------------------------------------------

# También existe:
#
# except Exception:
#
# que puede capturar una gran cantidad de excepciones.
#
# Tiene usos válidos, pero NO será nuestra opción automática.
#
# Para comenzar preferiremos:
#
# except ValueError
# except ZeroDivisionError
# except KeyError
#
# etc.
#
#
# Es mejor manejar de forma específica los errores que
# realmente sabemos resolver.


# ------------------------------------------------------------
# 16. NO TODO ERROR DEBE SER OCULTADO
# ------------------------------------------------------------

# Supongamos que escribimos incorrectamente una variable:
#
# print(nombre_inexistente)
#
#
# Esto produce:
#
# NameError
#
#
# Generalmente eso representa un error en nuestro código.
#
# No tendría sentido ocultarlo simplemente con:
#
# except:
#     print("Algo salió mal")
#
#
# Como programadores necesitamos ver ciertos errores
# para poder corregirlos.


# ------------------------------------------------------------
# 17. TRY DEBE PROTEGER EL CÓDIGO NECESARIO
# ------------------------------------------------------------

# Evitaremos colocar enormes cantidades de código dentro
# de un único try si solamente una operación es riesgosa.


# MENOS CLARO:
#
# try:
#     muchas instrucciones
#     muchos cálculos
#     conversiones
#     varias operaciones
#     ...
# except ValueError:
#     ...


# MÁS CLARO:

try:
    cantidad_repuestos = int("5")

except ValueError:
    print("Cantidad inválida.")


# Así resulta más fácil identificar qué operación podía
# producir la excepción.


# ------------------------------------------------------------
# 18. EJEMPLO CON INPUT
# ------------------------------------------------------------

try:
    anio_nacimiento = int(
        input("Ingresa tu año de nacimiento: ")
    )

    edad_aproximada = 2026 - anio_nacimiento

    print(
        f"Edad aproximada: {edad_aproximada}"
    )

except ValueError:
    print(
        "El año debe ser ingresado como un número entero."
    )


# Antes, un dato inválido terminaba el programa.
#
# Ahora tenemos una respuesta controlada.


# ------------------------------------------------------------
# 19. EJEMPLO CON UNA FUNCIÓN
# ------------------------------------------------------------

def dividir_valores(dividendo, divisor):

    try:
        resultado = dividendo / divisor

        return resultado

    except ZeroDivisionError:
        return None


resultado_correcto = dividir_valores(
    100,
    4
)

resultado_invalido = dividir_valores(
    100,
    0
)


print(resultado_correcto)
print(resultado_invalido)


# Este ejemplo combina:
#
# funciones
# parámetros
# return
# try
# except
# None


# No significa que siempre debamos devolver None.
#
# La respuesta correcta dependerá del programa.
#
# Por ahora solamente estamos practicando el mecanismo.


# ------------------------------------------------------------
# 20. EJEMPLO CON DICCIONARIO
# ------------------------------------------------------------

datos_astronomo = {
    "nombre": "José Maza",
    "profesion": "Astrónomo"
}


try:
    institucion = datos_astronomo["institucion"]

    print(institucion)

except KeyError:
    print("La institución no se encuentra registrada.")


# Este ejemplo funciona.
#
# Sin embargo, si simplemente queremos obtener un valor
# opcional de un diccionario, probablemente sería más
# sencillo utilizar:
#
# datos_astronomo.get(...)
#
#
# try/except no reemplaza las demás herramientas
# que ya conocemos.


# ------------------------------------------------------------
# 21. EJEMPLO CON LISTAS
# ------------------------------------------------------------

aportes_cientificos = [
    "Relatividad",
    "Radiación de Hawking",
    "Leyes del movimiento"
]


try:
    aporte = aportes_cientificos[1]

    print(aporte)

except IndexError:
    print("El aporte solicitado no existe.")


# En programas reales el índice podría venir desde:
#
# - un usuario;
# - datos externos;
# - otro cálculo.
#
# Allí puede tener más sentido proteger el acceso.


# ------------------------------------------------------------
# 22. VALIDAR INPUT HASTA QUE SEA CORRECTO
# ------------------------------------------------------------

# Podemos combinar:
#
# while
# try
# except
# break
#
# Todos estos conceptos ya fueron estudiados.


while True:

    try:
        cantidad_estrellas = int(
            input("Ingresa una cantidad de estrellas: ")
        )

        break

    except ValueError:
        print(
            "Debes ingresar un número entero. Intenta nuevamente."
        )


print(
    f"Cantidad registrada: {cantidad_estrellas}"
)


# Funcionamiento:
#
# usuario escribe algo inválido
# ↓
# ValueError
# ↓
# except muestra mensaje
# ↓
# while vuelve a intentarlo
#
#
# usuario escribe un entero válido
# ↓
# conversión correcta
# ↓
# break
# ↓
# termina el ciclo


# ------------------------------------------------------------
# 23. EXCEPCIÓN ESPERADA VS ERROR DE PROGRAMACIÓN
# ------------------------------------------------------------

# Este criterio es importante.
#
#
# Usuario escribe:
#
# "hola"
#
# cuando esperamos un int.
#
# → situación previsible.
#
#
# Intentamos utilizar una variable que nunca definimos.
#
# → probablemente tenemos un error de programación.
#
#
# No debemos utilizar try/except simplemente para ocultar
# cualquier problema.
#
# Debemos manejar situaciones que realmente sabemos
# reconocer y resolver.


# ------------------------------------------------------------
# 24. EJEMPLO SIMPLIFICADO DE WORKDESK
# ------------------------------------------------------------

# Imaginemos que recibimos una prioridad numérica
# desde una entrada externa.


try:
    nivel_prioridad = int(
        input("Nivel de prioridad (1-3): ")
    )

    prioridades = [
        "Baja",
        "Media",
        "Alta"
    ]

    prioridad_seleccionada = prioridades[
        nivel_prioridad - 1
    ]

    print(
        f"Prioridad: {prioridad_seleccionada}"
    )

except ValueError:
    print(
        "El nivel de prioridad debe ser numérico."
    )

except IndexError:
    print(
        "El nivel indicado está fuera del rango permitido."
    )


# Este ejemplo combina conocimientos anteriores sin intentar
# diseñar todavía la lógica real de WorkDesk.


# ------------------------------------------------------------
# 25. QUÉ NO VEREMOS TODAVÍA
# ------------------------------------------------------------

# En el siguiente archivo estudiaremos:
#
# else
# finally
# raise
#
# y algunas buenas prácticas adicionales.
#
#
# Por ahora queremos consolidar solamente:
#
# excepción
# try
# except
# tipos específicos de excepción


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# EXCEPCIÓN
#
# problema detectado durante la ejecución.
#
#
# EJEMPLOS:
#
# ValueError
# → valor incorrecto para una operación.
#
# TypeError
# → tipos incompatibles.
#
# ZeroDivisionError
# → división por cero.
#
# KeyError
# → clave inexistente en un diccionario.
#
# IndexError
# → posición inexistente en una secuencia.
#
#
# ESTRUCTURA:
#
# try:
#     codigo_que_puede_fallar()
#
# except TipoDeExcepcion:
#     respuesta_al_error()
#
#
# VARIOS ERRORES:
#
# try:
#     ...
#
# except ValueError:
#     ...
#
# except ZeroDivisionError:
#     ...
#
#
# MISMA RESPUESTA PARA VARIOS:
#
# except (ValueError, IndexError):
#     ...
#
#
# REGLA IMPORTANTE:
#
# capturar de forma específica los errores que sabemos
# manejar.
#
#
# NO UTILIZAR try/except PARA:
#
# - ocultar errores;
# - ignorar problemas de programación;
# - envolver todo el programa sin necesidad.
#
#
# PATRÓN GENERAL:
#
# operación que puede fallar
# ↓
# try
#
# excepción que sabemos manejar
# ↓
# except
#
# respuesta controlada
# ↓
# el programa puede continuar