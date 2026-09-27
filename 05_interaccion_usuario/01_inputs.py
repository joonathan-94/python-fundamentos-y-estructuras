# ============================================================
# ENTRADA DE DATOS CON input()
# ============================================================
#
# Hasta ahora nuestros programas han trabajado principalmente
# con valores definidos directamente en el código.
#
# Ejemplo:
#
# nombre = "Pikachu"
# edad = 25
#
# input() permite que un usuario entregue información mientras
# el programa se está ejecutando.
#
# Esto es útil en:
#
# - aplicaciones de consola;
# - scripts interactivos;
# - herramientas administrativas;
# - automatizaciones que requieren parámetros;
# - menús;
# - formularios simples de terminal.
#
# Más adelante, en aplicaciones web, los datos llegarán por
# otros medios, como formularios HTTP o APIs.
#
# Comprender input() ayuda a entender un principio general:
#
#     recibir datos externos
#     ↓
#     validarlos / transformarlos
#     ↓
#     utilizarlos


# ------------------------------------------------------------
# 1. input()
# ------------------------------------------------------------

# input() detiene temporalmente la ejecución del programa
# y espera que el usuario escriba un valor.
#
# Cuando el usuario presiona Enter, Python devuelve
# el texto ingresado.

nombre_usuario = input("Ingresa tu nombre: ")

print("Nombre ingresado:", nombre_usuario)


# ------------------------------------------------------------
# 2. input() SIEMPRE DEVUELVE str
# ------------------------------------------------------------

# Este punto es fundamental.
#
# Aunque el usuario escriba:
#
# 25
#
# Python recibe:
#
# "25"
#
# es decir, un string.

edad_ingresada = input("Ingresa tu edad: ")

print(edad_ingresada)
print(type(edad_ingresada))


# Si el usuario escribe:
#
# 31
#
# type(edad_ingresada) será:
#
# <class 'str'>


# ------------------------------------------------------------
# 3. CONVERTIR UN INPUT A int
# ------------------------------------------------------------

# Si necesitamos realizar operaciones matemáticas,
# debemos convertir el string.

anio_auto = input("Ingresa el año de fabricación del auto: ")

anio_auto_numero = int(anio_auto)

print("Año registrado:", anio_auto_numero)
print(type(anio_auto_numero))


# También podemos hacerlo directamente:

cantidad_tickets = int(
    input("¿Cuántos tickets deseas procesar?: ")
)

print("Tickets:", cantidad_tickets)


# ------------------------------------------------------------
# 4. CONVERTIR UN INPUT A float
# ------------------------------------------------------------

# float() se utiliza cuando necesitamos números decimales.

precio_corvette = float(
    input("Ingresa el precio estimado del Corvette: ")
)

print("Precio registrado:", precio_corvette)


# Ejemplo:
#
# usuario escribe:
#
# 42500.50
#
# Python lo convierte a:
#
# 42500.5


# ------------------------------------------------------------
# 5. QUÉ PASA SI LA CONVERSIÓN NO ES VÁLIDA
# ------------------------------------------------------------

# Si hacemos:
#
# edad = int(input("Edad: "))
#
# y el usuario escribe:
#
# treinta
#
# int("treinta")
#
# no puede convertirse a un entero.
#
# Python produce:
#
# ValueError
#
#
# Por ahora NO manejaremos ese error.
#
# El tratamiento correcto de este tipo de situaciones se
# estudiará en:
#
# 08_manejo_excepciones
#
# Lo importante por ahora es comprender que los datos externos
# no siempre serán válidos.


# ------------------------------------------------------------
# 6. LIMPIAR ESPACIOS CON strip()
# ------------------------------------------------------------

# Como input() devuelve un string, podemos utilizar los métodos
# de strings que ya estudiamos.

nombre_pokemon = input(
    "Ingresa el nombre del Pokémon: "
)

nombre_pokemon = nombre_pokemon.strip()

print(nombre_pokemon)


# Si el usuario escribe:
#
# "   Totodile   "
#
# strip() produce:
#
# "Totodile"


# ------------------------------------------------------------
# 7. NORMALIZAR TEXTO
# ------------------------------------------------------------

# También podemos combinar strip() con lower().

estado_ingresado = input(
    "Ingresa el estado del ticket: "
)

estado_normalizado = estado_ingresado.strip().lower()

print(estado_normalizado)


# Ejemplos:
#
# "NUEVO"
# " Nuevo "
# "nuevo"
#
# terminan convertidos en:
#
# "nuevo"
#
# Esto facilita posteriormente realizar comparaciones.


# ------------------------------------------------------------
# 8. INPUT + CONDICIONALES
# ------------------------------------------------------------

# Podemos utilizar inmediatamente el dato ingresado
# dentro de nuestra lógica.

prioridad_ingresada = input(
    "Ingresa la prioridad del ticket: "
).strip().lower()


if prioridad_ingresada == "critica":
    print("El ticket requiere atención inmediata.")

elif prioridad_ingresada == "alta":
    print("El ticket requiere atención prioritaria.")

else:
    print("El ticket seguirá el flujo normal.")


# Aquí estamos combinando:
#
# input()
# strings
# strip()
# lower()
# if / elif / else


# ------------------------------------------------------------
# 9. INPUT + OPERACIONES MATEMÁTICAS
# ------------------------------------------------------------

cantidad_repuestos = int(
    input("Cantidad de repuestos: ")
)

precio_unitario = float(
    input("Precio por repuesto: ")
)

total_compra = cantidad_repuestos * precio_unitario

print(f"Total: ${total_compra}")


# El patrón es:
#
# recibir
# ↓
# convertir
# ↓
# procesar
# ↓
# mostrar resultado


# ------------------------------------------------------------
# 10. VARIOS DATOS PARA CONSTRUIR UNA ESTRUCTURA
# ------------------------------------------------------------

# Podemos utilizar distintos inputs para construir un
# diccionario.

nombre_dinosaurio = input(
    "Nombre del dinosaurio: "
).strip()

periodo_dinosaurio = input(
    "Período geológico: "
).strip()

dinosaurio_registrado = {
    "nombre": nombre_dinosaurio,
    "periodo": periodo_dinosaurio
}

print(dinosaurio_registrado)


# Este patrón aparecerá constantemente:
#
# datos externos
# ↓
# variables
# ↓
# estructura de datos
#
# En una aplicación web ocurre algo conceptualmente parecido,
# aunque los datos normalmente llegan desde formularios,
# peticiones HTTP o APIs en lugar de input().


# ------------------------------------------------------------
# 11. INPUT DENTRO DE UN CICLO
# ------------------------------------------------------------

# También podemos solicitar información repetidamente.

comando_usuario = ""

while comando_usuario != "salir":

    comando_usuario = input(
        "Escribe un comando o 'salir': "
    ).strip().lower()

    print("Comando recibido:", comando_usuario)


# Cuando el usuario escribe:
#
# salir
#
# la condición del while deja de cumplirse.


# ------------------------------------------------------------
# 12. EJEMPLO PRÁCTICO: REGISTRO SIMPLE DE TICKET
# ------------------------------------------------------------

print("\n--- Registro de ticket ---")


titulo_registro = input(
    "Título del ticket: "
).strip()

solicitante_registro = input(
    "Solicitante: "
).strip()

prioridad_registro = input(
    "Prioridad: "
).strip().capitalize()


ticket_registrado = {
    "titulo": titulo_registro,
    "solicitante": solicitante_registro,
    "prioridad": prioridad_registro,
    "estado": "Nuevo"
}


print("\nTicket registrado:")

for campo_ticket, valor_ticket in ticket_registrado.items():
    print(f"{campo_ticket}: {valor_ticket}")


# Este ejemplo reúne conceptos ya estudiados:
#
# input()
# strings
# variables
# diccionarios
# for
#
# Todavía no estamos construyendo WorkDesk.
#
# El ejemplo simplemente representa un caso realista de captura
# de información mediante consola.


# ------------------------------------------------------------
# 13. NO UTILIZAR eval() PARA CONVERTIR INPUTS
# ------------------------------------------------------------

# No debemos hacer:
#
# valor = eval(input("Ingresa un valor: "))
#
# para convertir datos recibidos del usuario.
#
# eval() interpreta el contenido como código Python y puede
# ejecutar expresiones no deseadas.
#
# Para conversiones simples utilizaremos herramientas
# específicas:
#
# int()
# float()
# str()
#
# y posteriormente validaciones y manejo de excepciones.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# input()
# → recibe información del usuario.
#
# El resultado de input() es siempre un str.
#
#
# Si necesitamos un entero:
#
# int(input(...))
#
#
# Si necesitamos un decimal:
#
# float(input(...))
#
#
# Para limpiar texto:
#
# input(...).strip()
#
#
# Para normalizar:
#
# input(...).strip().lower()
#
#
# Patrón fundamental:
#
# entrada
# ↓
# transformación
# ↓
# validación
# ↓
# procesamiento
# ↓
# salida
#
#
# Más adelante aprenderemos a manejar entradas inválidas
# utilizando excepciones.