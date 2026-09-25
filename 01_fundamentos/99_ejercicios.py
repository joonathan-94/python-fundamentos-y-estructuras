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


# ============================================================
# STRINGS
# ============================================================


# ------------------------------------------------------------
# STR-01 - NORMALIZAR DATOS DE UN TICKET
# ------------------------------------------------------------
#
# Un usuario ingresó los siguientes datos:
#
# titulo = "   ERROR DE CONEXIÓN CON SERVIDOR   "
# solicitante = "   elliot alderson   "
#
# Realiza lo siguiente:
#
# 1. Elimina los espacios sobrantes de titulo.
# 2. Convierte titulo completamente a minúsculas.
# 3. Guarda el resultado en titulo_normalizado.
#
# 4. Elimina los espacios sobrantes de solicitante.
# 5. Convierte solicitante a formato título.
# 6. Guarda el resultado en solicitante_normalizado.
#
# 7. Imprime los valores originales y los normalizados.
#
# El objetivo es practicar:
#
# - strip()
# - lower()
# - title()
# - inmutabilidad de los strings
#
# Tu código aquí:

titulo = '   ERROR DE CONEXIÓN CON SERVIDOR   '
solicitante = '   elliot alderson   '
print(f'titulo original: {titulo}')
titulo_normalizado = titulo.lower().strip()
print(f'titulo normalizado: {titulo_normalizado}')

print(f'solicitante original: {solicitante}')
solicitante_normalizado = solicitante.title().strip()
print(f'solicitante normalizado: {solicitante_normalizado}')

# ------------------------------------------------------------
# STR-02 - ANALIZAR UN CÓDIGO DE TICKET
# ------------------------------------------------------------
#
# Tienes:
#
# codigo_ticket = "WD-2026-0042"
#
# Utilizando índices, slicing y métodos de strings:
#
# 1. Obtén el prefijo "WD".
# 2. Obtén el año "2026".
# 3. Obtén el número "0042".
# 4. Comprueba si el código comienza con "WD".
# 5. Comprueba si el número contiene únicamente dígitos.
#
# Guarda cada resultado en una variable descriptiva.
#
# Imprime todos los resultados.
#
# El objetivo es practicar:
#
# - índices
# - slicing
# - startswith()
# - isdigit()
#
# Tu código aquí:

codigo_ticket = "WD-2026-0042"

# 1. Obtén el prefijo "WD" (índices 0 al 2, sin incluir el 2)
prefijo = codigo_ticket[:2]

# 2. Obtén el año "2026" (índices 3 al 7)
anio = codigo_ticket[3:7]

# 3. Obtén el número "0042" (índices 8 en adelante)
numero = codigo_ticket[8:]

# 4. Comprueba si el código comienza con "WD"
empieza_con_wd = codigo_ticket.startswith("WD")

# 5. Comprueba si el número contiene únicamente dígitos
numero_es_digito = numero.isdigit()

# Imprimir resultados
print(f"Prefijo: {prefijo}")
print(f"Año: {anio}")
print(f"Número: {numero}")
print(f"¿Comienza con 'WD'?: {empieza_con_wd}")
print(f"¿El número es solo dígitos?: {numero_es_digito}")

# ------------------------------------------------------------
# STR-03 - DESAFÍO: PROCESAR INFORMACIÓN DE UN TICKET
# ------------------------------------------------------------
#
# Tienes:
#
# codigo_ticket = "   WD-2026-0100   "
# titulo = "   FaLLa DE RED EN SERVIDOR   "
# descripcion = "El usuario reporta un ERROR de RED"
# archivo = "captura_error.png"
# tecnico = "   neo   "
#
# Utilizando únicamente conceptos estudiados hasta ahora:
#
# 1. Limpia codigo_ticket eliminando espacios sobrantes.
#
# 2. Normaliza titulo:
#    - elimina espacios sobrantes
#    - conviértelo a minúsculas
#
# 3. Normaliza tecnico:
#    - elimina espacios sobrantes
#    - utiliza title()
#
# 4. Comprueba si descripcion contiene la palabra "error"
#    sin importar las mayúsculas o minúsculas.
#
# 5. Comprueba si archivo termina en ".png".
#
# 6. Utilizando slicing, extrae desde codigo_ticket:
#
#    prefijo
#    anio
#    numero
#
# 7. Construye una f-string con un resumen similar a:
#
# Ticket: WD-2026-0100
# Técnico: Neo
# Título: falla de red en servidor
# Contiene error: True
# Archivo PNG: True
#
# 8. Imprime el resumen.
#
# IMPORTANTE:
#
# No utilices todavía:
#
# - if
# - for
# - while
# - funciones
#
# Tu código aquí:

# ------------------------------------------------------------
# STR-03 - DESAFÍO: PROCESAR INFORMACIÓN DE UN TICKET
# ------------------------------------------------------------

codigo_ticket = "   WD-2026-0100   "
titulo = "   FaLLa DE RED EN SERVIDOR   "
descripcion = "El usuario reporta un ERROR de RED"
archivo = "captura_error.png"
tecnico = "   neo   "

# 1. Limpiar codigo_ticket
codigo_ticket_limpio = codigo_ticket.strip()

# 2. Normalizar titulo (eliminar espacios y convertir a minúsculas)
titulo_normalizado = titulo.strip().lower()

# 3. Normalizar tecnico (eliminar espacios y aplicar title)
tecnico_normalizado = tecnico.strip().title()

# 4. Comprobar si descripcion contiene "error" (convertimos a minúsculas para comparar)
contiene_error = "error" in descripcion.lower()

# 5. Comprobar si archivo termina en ".png"
es_png = archivo.endswith(".png")

# 6. Extraer partes de codigo_ticket usando slicing
prefijo = codigo_ticket_limpio[:2]
anio = codigo_ticket_limpio[3:7]
numero = codigo_ticket_limpio[8:]

# 7. Construir la f-string con el resumen
resumen = f"""Ticket: {codigo_ticket_limpio}
Técnico: {tecnico_normalizado}
Título: {titulo_normalizado}
Contiene error: {contiene_error}
Archivo PNG: {es_png}"""

# 8. Imprimir el resumen
print(resumen)

# ============================================================
# CONVERSIÓN DE TIPOS EN PYTHON
# ============================================================
#
# En Python podemos convertir valores de un tipo de dato
# a otro utilizando funciones incorporadas.
#
# Algunas de las conversiones más comunes son:
#
# str()   -> convierte a string
# int()   -> convierte a entero
# float() -> convierte a número decimal
# bool()  -> convierte a booleano
#
# La conversión debe ser válida.
#
# Por ejemplo:
#
# int("25")
#
# funciona porque "25" representa un número entero.
#
# En cambio:
#
# int("Neo")
#
# produciría un error porque "Neo" no puede interpretarse
# como un número entero.


# ------------------------------------------------------------
# 1. COMPROBAR EL TIPO ORIGINAL
# ------------------------------------------------------------

edad = "31"

print(edad)
print(type(edad))

# Aunque visualmente vemos 31, el valor es un string.


# ------------------------------------------------------------
# 2. CONVERTIR A int
# ------------------------------------------------------------

# int() permite obtener un número entero cuando el valor
# recibido puede convertirse correctamente.

edad_texto = "31"

edad_numero = int(edad_texto)

print(edad_numero)
print(type(edad_numero))


# Otro ejemplo relacionado con tickets:

id_ticket_texto = "100"

id_ticket = int(id_ticket_texto)

print(id_ticket)
print(type(id_ticket))


# ------------------------------------------------------------
# 3. CONVERTIR A float
# ------------------------------------------------------------

# float() permite crear un número decimal.

horas_texto = "2.5"

horas = float(horas_texto)

print(horas)
print(type(horas))


# Un entero también puede convertirse a float.

cantidad = 5

cantidad_decimal = float(cantidad)

print(cantidad_decimal)
print(type(cantidad_decimal))


# ------------------------------------------------------------
# 4. CONVERTIR A str
# ------------------------------------------------------------

# str() permite convertir otros valores a texto.

id_ticket = 42

id_ticket_texto = str(id_ticket)

print(id_ticket_texto)
print(type(id_ticket_texto))


# También podemos convertir booleanos:

estado_activo = True

estado_texto = str(estado_activo)

print(estado_texto)
print(type(estado_texto))


# ------------------------------------------------------------
# 5. CONVERTIR float A int
# ------------------------------------------------------------

# Al convertir un float a int, Python elimina
# la parte decimal.
#
# NO debemos pensar que int() redondea.

tiempo = 3.9

tiempo_entero = int(tiempo)

print(tiempo_entero)  # 3


# Otro ejemplo:

valor = 7.8

print(int(valor))  # 7


# ------------------------------------------------------------
# 6. CONVERSIONES INVÁLIDAS
# ------------------------------------------------------------

# No cualquier string puede convertirse a número.

# Esto funcionaría:

numero = int("25")

print(numero)


# Esto produciría ValueError:
#
# numero = int("Tony Soprano")


# Tampoco podemos convertir directamente este string
# decimal utilizando int():
#
# numero = int("10.5")
#
# porque "10.5" no representa directamente un entero.


# En ese caso podríamos convertir primero a float:

numero_decimal = float("10.5")

print(numero_decimal)


# ------------------------------------------------------------
# 7. CONVERTIR A bool
# ------------------------------------------------------------

# bool() convierte un valor en True o False.
#
# Algunos valores considerados falsos incluyen:
#
# 0
# 0.0
# ""
# None
# False

print(bool(0))       # False
print(bool(0.0))     # False
print(bool(""))      # False
print(bool(None))    # False


# Otros valores normalmente se consideran verdaderos.

print(bool(1))        # True
print(bool(25))       # True
print(bool("Python")) # True


# ------------------------------------------------------------
# 8. CUIDADO CON STRINGS Y bool()
# ------------------------------------------------------------

# Un string NO vacío se considera verdadero.
#
# Por eso:

valor = "False"

resultado = bool(valor)

print(resultado)  # True


# Aunque el texto diga "False", sigue siendo un string
# que contiene caracteres.
#
# Esto es diferente de:

valor_booleano = False

print(bool(valor_booleano))  # False


# ------------------------------------------------------------
# 9. COMPROBAR LA CONVERSIÓN CON type()
# ------------------------------------------------------------

numero_texto = "50"

print(type(numero_texto))

numero = int(numero_texto)

print(type(numero))


# Podemos comprobar claramente:
#
# antes  -> str
# después -> int


# ------------------------------------------------------------
# 10. EJEMPLO RELACIONADO CON UN TICKET
# ------------------------------------------------------------

id_ticket_recibido = "250"
horas_resolucion_recibidas = "1.5"

id_ticket = int(id_ticket_recibido)
horas_resolucion = float(horas_resolucion_recibidas)

print(id_ticket)
print(type(id_ticket))

print(horas_resolucion)
print(type(horas_resolucion))


# ============================================================
# CONVERSIÓN DE TIPOS
# ============================================================


# ------------------------------------------------------------
# CONV-01 - CONVERTIR DATOS BÁSICOS
# ------------------------------------------------------------
#
# Tienes:
#
# edad = "31"
# horas = "2.5"
# id_ticket = 100
#
# Convierte:
#
# edad       -> int
# horas      -> float
# id_ticket  -> str
#
# Guarda cada resultado en una nueva variable.
#
# Imprime el resultado y su tipo utilizando type().
#
# Tu código aquí:

edad = "31"
horas = "2.5"
id_ticket = 100

edad_int = int(edad)
horas_float = float(horas)
id_ticket_str = str(id_ticket)

print(edad_int, type(edad_int))
print(horas_float, type(horas_float))
print(id_ticket_str, type(id_ticket_str))


# ------------------------------------------------------------
# CONV-02 - DATOS DE UN TICKET
# ------------------------------------------------------------
#
# Imagina que recibimos:
#
# id_ticket = "250"
# tiempo_resolucion = "3.5"
#
# Convierte:
#
# id_ticket         -> int
# tiempo_resolucion -> float
#
# Imprime ambos valores y sus tipos.
#
# Tu código aquí:

id_ticket = "250"
tiempo_resolucion = "3.5"

id_ticket_int = int(id_ticket)
tiempo_resolucion_float = float(tiempo_resolucion)

print('id ticket (original): ', id_ticket)
print('id ticket (original): ', type(id_ticket))
print('id ticket (int): ', id_ticket_int)
print('id ticket (int): ', type(id_ticket_int))
print('Tiempo de resolución (original): ', tiempo_resolucion)
print('Tiempo de resolución (original): ', type(tiempo_resolucion))
print('Tiempo de resolución (float): ', tiempo_resolucion_float)
print('Tiempo de resolución (float): ', type(tiempo_resolucion_float))

# ------------------------------------------------------------
# CONV-03 - CONVERSIÓN A BOOLEANO
# ------------------------------------------------------------
#
# Tienes:
#
# valor_1 = 0
# valor_2 = 1
# valor_3 = ""
# valor_4 = "False"
#
# Convierte cada valor utilizando bool().
#
# Guarda los resultados en variables descriptivas
# e imprímelos.
#
# Observa especialmente qué ocurre con "False".
#
# Tu código aquí:

valor_1 = 0
valor_2 = 1
valor_3 = ""
valor_4 = "False"

bool_1 = bool(valor_1)
bool_2 = bool(valor_2)
bool_3 = bool(valor_3)
bool_4 = bool(valor_4)

print("valor_1 (0):", bool_1)
print("valor_2 (1):", bool_2)
print("valor_3 (''):", bool_3)
print("valor_4 ('False'):", bool_4)