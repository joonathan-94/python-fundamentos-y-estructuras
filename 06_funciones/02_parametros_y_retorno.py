# ============================================================
# PARÁMETROS, ARGUMENTOS Y RETORNO EN PYTHON
# ============================================================
#
# Las funciones se vuelven realmente útiles cuando pueden:
#
# - recibir información;
# - trabajar con esa información;
# - devolver un resultado.
#
# Ejemplo general:
#
# def calcular_total(cantidad, precio):
#     return cantidad * precio
#
# resultado = calcular_total(3, 15000)
#
#
# En este ejemplo:
#
# cantidad y precio
# → son PARÁMETROS.
#
# 3 y 15000
# → son ARGUMENTOS.
#
#
# PARÁMETRO
# → nombre definido dentro de la función.
#
# ARGUMENTO
# → valor entregado cuando llamamos a la función.


# ------------------------------------------------------------
# 1. PARÁMETROS
# ------------------------------------------------------------

def mostrar_auto(modelo_auto):
    print(f"Auto registrado: {modelo_auto}")


# modelo_auto es un parámetro.


# ------------------------------------------------------------
# 2. ARGUMENTOS
# ------------------------------------------------------------

mostrar_auto("Camaro 1967")
mostrar_auto("Corvette Stingray")
mostrar_auto("Chevrolet Bel Air")


# Los strings anteriores son argumentos.
#
# La misma función trabaja con distintos valores.


# ------------------------------------------------------------
# 3. VARIOS PARÁMETROS
# ------------------------------------------------------------

def mostrar_ficha_auto(modelo_auto, anio_fabricacion):
    print(f"Modelo: {modelo_auto}")
    print(f"Año: {anio_fabricacion}")


mostrar_ficha_auto(
    "Ford Mustang",
    1969
)


# Una función puede recibir varios parámetros.


# ------------------------------------------------------------
# 4. ARGUMENTOS POSICIONALES
# ------------------------------------------------------------

# Por defecto, Python asocia los argumentos según
# la posición en la llamada.

def registrar_pokemon(nombre_pokemon, tipo_pokemon):
    print(f"Nombre: {nombre_pokemon}")
    print(f"Tipo: {tipo_pokemon}")


registrar_pokemon(
    "Totodile",
    "Agua"
)


# Python interpreta:
#
# "Totodile"
# → nombre_pokemon
#
# "Agua"
# → tipo_pokemon


# El orden importa.

registrar_pokemon(
    "Agua",
    "Totodile"
)


# El programa funciona, pero los datos quedaron asociados
# a parámetros incorrectos.
#
# Python no conoce el significado de los valores.
#
# Solamente respeta la posición.


# ------------------------------------------------------------
# 5. ARGUMENTOS POR NOMBRE
# ------------------------------------------------------------

# Podemos indicar explícitamente a qué parámetro corresponde
# cada argumento.

def mostrar_dinosaurio(nombre_dinosaurio, periodo_geologico):
    print(f"Dinosaurio: {nombre_dinosaurio}")
    print(f"Periodo: {periodo_geologico}")


mostrar_dinosaurio(
    periodo_geologico="Cretácico",
    nombre_dinosaurio="Tyrannosaurus rex"
)


# En este caso el orden deja de ser importante porque
# indicamos explícitamente los nombres de los parámetros.


# ------------------------------------------------------------
# 6. POSICIONALES VS ARGUMENTOS POR NOMBRE
# ------------------------------------------------------------

# Los argumentos posicionales son cómodos cuando la llamada
# es corta y resulta evidente qué representa cada valor.

def calcular_area(ancho, alto):
    return ancho * alto


area_rectangulo = calcular_area(10, 5)

print(area_rectangulo)


# Cuando una llamada tiene varios valores similares,
# los argumentos por nombre pueden mejorar la claridad.

def calcular_costo_servicio(
    horas_trabajadas,
    valor_hora,
    costo_materiales
):
    return (
        horas_trabajadas * valor_hora
        + costo_materiales
    )


costo_servicio = calcular_costo_servicio(
    horas_trabajadas=2.5,
    valor_hora=18000,
    costo_materiales=12000
)

print(costo_servicio)


# Al leer la llamada sabemos inmediatamente qué significa
# cada valor.


# ------------------------------------------------------------
# 7. MEZCLAR ARGUMENTOS POSICIONALES Y POR NOMBRE
# ------------------------------------------------------------

def registrar_usuario(nombre_usuario, rol_usuario, activo):
    print(nombre_usuario)
    print(rol_usuario)
    print(activo)


registrar_usuario(
    "Walter White",
    rol_usuario="Administrador",
    activo=True
)


# Los argumentos posicionales deben aparecer antes de los
# argumentos enviados mediante nombre.
#
# Esta llamada sería inválida:
#
# registrar_usuario(
#     nombre_usuario="Walter White",
#     "Administrador",
#     True
# )
#
# porque aparecen argumentos posicionales después de uno
# enviado mediante nombre.


# ------------------------------------------------------------
# 8. VALORES PREDETERMINADOS
# ------------------------------------------------------------

# Un parámetro puede tener un valor por defecto.

def crear_ticket(titulo_ticket, estado_ticket="Nuevo"):
    return {
        "titulo": titulo_ticket,
        "estado": estado_ticket
    }


ticket_impresora = crear_ticket(
    "Impresora sin conexión"
)

print(ticket_impresora)


# Como no indicamos estado_ticket, Python utiliza:
#
# "Nuevo"


# También podemos reemplazar el valor predeterminado.

ticket_resuelto = crear_ticket(
    "Contraseña restablecida",
    "Resuelto"
)

print(ticket_resuelto)


# ------------------------------------------------------------
# 9. PARÁMETROS OBLIGATORIOS Y OPCIONALES
# ------------------------------------------------------------

# Podemos pensar inicialmente:
#
# parámetro sin valor predeterminado
# → obligatorio
#
# parámetro con valor predeterminado
# → opcional


def registrar_vehiculo(
    modelo_vehiculo,
    anio_vehiculo,
    disponible=True
):
    return {
        "modelo": modelo_vehiculo,
        "anio": anio_vehiculo,
        "disponible": disponible
    }


vehiculo_disponible = registrar_vehiculo(
    "Chevrolet Bel Air",
    1957
)

print(vehiculo_disponible)


vehiculo_no_disponible = registrar_vehiculo(
    "Corvette Stingray",
    1963,
    False
)

print(vehiculo_no_disponible)


# ------------------------------------------------------------
# 10. ORDEN DE PARÁMETROS CON VALORES PREDETERMINADOS
# ------------------------------------------------------------

# Los parámetros obligatorios deben aparecer antes de los
# parámetros que tienen valores predeterminados.


# Correcto:

def crear_usuario(nombre_usuario, activo=True):
    return {
        "nombre": nombre_usuario,
        "activo": activo
    }


# Incorrecto:
#
# def crear_usuario(activo=True, nombre_usuario):
#     ...
#
# Python produciría un SyntaxError.


# ------------------------------------------------------------
# 11. return CON UN VALOR
# ------------------------------------------------------------

def obtener_nombre_completo(nombre, apellido):
    nombre_completo = f"{nombre} {apellido}"

    return nombre_completo


nombre_persona = obtener_nombre_completo(
    "Tony",
    "Soprano"
)

print(nombre_persona)


# return entrega el resultado al código que llamó
# a la función.


# ------------------------------------------------------------
# 12. UTILIZAR DIRECTAMENTE EL VALOR DEVUELTO
# ------------------------------------------------------------

def convertir_minutos(minutos_totales):
    return minutos_totales / 60


print(convertir_minutos(180))


# No siempre necesitamos guardar primero el resultado
# en una variable.
#
# Sin embargo, utilizar una variable puede mejorar la
# legibilidad cuando el resultado será utilizado nuevamente.


# ------------------------------------------------------------
# 13. RETORNAR VARIOS VALORES
# ------------------------------------------------------------

# Python permite devolver varios valores.

def obtener_medidas():
    ancho = 1920
    alto = 1080

    return ancho, alto


resolucion = obtener_medidas()

print(resolucion)
print(type(resolucion))


# El resultado es una tupla:
#
# (1920, 1080)


# Técnicamente Python está empaquetando los valores
# dentro de una tupla.


# ------------------------------------------------------------
# 14. DESEMPAQUETAR VARIOS VALORES DEVUELTOS
# ------------------------------------------------------------

def obtener_coordenadas():
    latitud = 29.9792
    longitud = 31.1342

    return latitud, longitud


latitud_giza, longitud_giza = obtener_coordenadas()

print(latitud_giza)
print(longitud_giza)


# Estamos combinando:
#
# función
# return
# tupla
# desempaquetado


# ------------------------------------------------------------
# 15. EJEMPLO REAL: CALCULAR ESTADÍSTICAS SIMPLES
# ------------------------------------------------------------

def calcular_resumen(valor_minimo, valor_maximo):
    diferencia = valor_maximo - valor_minimo
    promedio = (valor_minimo + valor_maximo) / 2

    return diferencia, promedio


diferencia_temperatura, promedio_temperatura = (
    calcular_resumen(18.5, 27.5)
)

print("Diferencia:", diferencia_temperatura)
print("Promedio:", promedio_temperatura)


# Este patrón puede aparecer posteriormente en:
#
# - procesamiento de datos;
# - automatizaciones;
# - reportes;
# - análisis de información.


# ------------------------------------------------------------
# 16. UNA FUNCIÓN PUEDE DEVOLVER UNA LISTA
# ------------------------------------------------------------

def obtener_iniciales_kanto():
    return [
        "Bulbasaur",
        "Charmander",
        "Squirtle"
    ]


iniciales_kanto = obtener_iniciales_kanto()

print(iniciales_kanto)


# return puede devolver cualquier tipo de objeto:
#
# str
# int
# float
# bool
# list
# tuple
# dict
# set
# None
#
# y posteriormente objetos creados por nosotros mismos.


# ------------------------------------------------------------
# 17. RETORNAR UN DICCIONARIO
# ------------------------------------------------------------

# Esto será especialmente frecuente en muchos tipos
# de programas Python.

def construir_ficha_dinosaurio(
    nombre_especie,
    periodo_especie
):
    ficha_dinosaurio = {
        "nombre": nombre_especie,
        "periodo": periodo_especie
    }

    return ficha_dinosaurio


ficha_triceratops = construir_ficha_dinosaurio(
    "Triceratops",
    "Cretácico"
)

print(ficha_triceratops)


# Una función puede procesar información y devolver
# una estructura organizada.


# ------------------------------------------------------------
# 18. EJEMPLO REALISTA: CREAR DATOS DE UN TICKET
# ------------------------------------------------------------

def construir_ticket(
    id_ticket,
    titulo_ticket,
    prioridad_ticket,
    estado_ticket="Nuevo"
):
    ticket_construido = {
        "id": id_ticket,
        "titulo": titulo_ticket,
        "prioridad": prioridad_ticket,
        "estado": estado_ticket
    }

    return ticket_construido


ticket_creado = construir_ticket(
    id_ticket="WD-8001",
    titulo_ticket="Usuario sin acceso",
    prioridad_ticket="Alta"
)

print(ticket_creado)


# Resultado conceptual:
#
# {
#     "id": "WD-8001",
#     "titulo": "Usuario sin acceso",
#     "prioridad": "Alta",
#     "estado": "Nuevo"
# }


# Este es un buen ejemplo de cómo una función puede:
#
# recibir datos
# ↓
# organizarlos
# ↓
# devolver una estructura


# ------------------------------------------------------------
# 19. EJEMPLO REALISTA: TRANSFORMAR DATOS
# ------------------------------------------------------------

# Las funciones no sirven solamente para cálculos.
#
# También pueden transformar datos.

def normalizar_codigo(codigo_recibido):
    codigo_limpio = codigo_recibido.strip()
    codigo_normalizado = codigo_limpio.upper()

    return codigo_normalizado


codigo_ticket = normalizar_codigo(
    "   wd-9001   "
)

print(codigo_ticket)


# Resultado:
#
# WD-9001


# Este tipo de función puede ser útil en:
#
# - backend;
# - integraciones;
# - importaciones de archivos;
# - procesamiento de datos;
# - automatizaciones.


# ------------------------------------------------------------
# 20. FUNCIÓN UTILIZANDO OTRA FUNCIÓN
# ------------------------------------------------------------

# Una función puede utilizar el resultado de otra.

def calcular_subtotal(cantidad, precio):
    return cantidad * precio


def calcular_total_con_impuesto(cantidad, precio):
    subtotal_calculado = calcular_subtotal(
        cantidad,
        precio
    )

    total_calculado = subtotal_calculado * 1.19

    return total_calculado


total_repuestos = calcular_total_con_impuesto(
    3,
    20000
)

print(total_repuestos)


# Aquí empezamos a dividir una operación en responsabilidades.
#
# calcular_subtotal()
# → calcula el subtotal.
#
# calcular_total_con_impuesto()
# → utiliza ese resultado y agrega otra regla.


# ------------------------------------------------------------
# 21. CUIDADO CON VALORES MUTABLES COMO PREDETERMINADOS
# ------------------------------------------------------------

# Esta es una advertencia importante de Python.
#
# Evitaremos utilizar una lista o diccionario mutable
# directamente como valor predeterminado.


# EVITAR:

# def agregar_elemento(elemento, elementos=[]):
#     elementos.append(elemento)
#     return elementos


# La lista utilizada como valor predeterminado se crea una vez
# cuando Python define la función.
#
# Por eso podría conservar información entre llamadas.


# Una alternativa segura es utilizar None.

def agregar_elemento(elemento, elementos=None):

    if elementos is None:
        elementos = []

    elementos.append(elemento)

    return elementos


primera_lista = agregar_elemento("Pikachu")
segunda_lista = agregar_elemento("Gengar")

print(primera_lista)
print(segunda_lista)


# Resultado:
#
# ["Pikachu"]
# ["Gengar"]
#
# Cada llamada crea una nueva lista cuando no entregamos
# una lista explícitamente.


# No necesitas memorizar este patrón todavía.
#
# Lo importante es recordar:
#
# cuidado con:
#
# parametro=[]
# parametro={}
#
# como valores predeterminados.


# ------------------------------------------------------------
# 22. NO MODIFICAR DATOS SIN NECESIDAD
# ------------------------------------------------------------

# Cuando una función recibe una colección mutable puede
# modificar el objeto original.

def agregar_tecnico(lista_tecnicos, tecnico_nuevo):
    lista_tecnicos.append(tecnico_nuevo)


tecnicos_disponibles = [
    "Morpheus",
    "Trinity"
]

agregar_tecnico(
    tecnicos_disponibles,
    "Neo"
)

print(tecnicos_disponibles)


# La lista original fue modificada.
#
# Esto no es necesariamente incorrecto.
#
# Pero debemos saber que está ocurriendo.
#
# Más adelante aprenderemos a diseñar funciones considerando
# claramente si deben:
#
# - modificar un objeto existente;
# - devolver un objeto nuevo.


# ------------------------------------------------------------
# 23. EJEMPLO: BACKEND
# ------------------------------------------------------------

def preparar_respuesta_usuario(
    nombre_usuario,
    rol_usuario,
    activo=True
):
    respuesta_usuario = {
        "nombre": nombre_usuario,
        "rol": rol_usuario,
        "activo": activo
    }

    return respuesta_usuario


datos_usuario = preparar_respuesta_usuario(
    nombre_usuario="Jesse Pinkman",
    rol_usuario="Técnico"
)

print(datos_usuario)


# Una función con este tipo de estructura podría aparecer
# posteriormente al preparar información para:
#
# - una API;
# - una respuesta del backend;
# - un proceso interno;
# - una transformación de datos.
#
# El ejemplo todavía es simplificado.


# ------------------------------------------------------------
# 24. EJEMPLO: MONEYDESK
# ------------------------------------------------------------

def calcular_saldo(
    ingresos_totales,
    gastos_totales
):
    saldo_actual = (
        ingresos_totales
        - gastos_totales
    )

    return saldo_actual


saldo_mensual = calcular_saldo(
    ingresos_totales=850000,
    gastos_totales=630000
)

print("Saldo:", saldo_mensual)


# Aquí la función representa una operación clara:
#
# ingresos
# -
# gastos
# =
# saldo


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# PARÁMETRO
#
# def funcion(parametro):
#
# Es el nombre utilizado dentro de la definición.
#
#
# ARGUMENTO
#
# funcion(valor)
#
# Es el valor entregado durante la llamada.
#
#
# ARGUMENTOS POSICIONALES
#
# funcion("valor", 10)
#
# Se relacionan según su posición.
#
#
# ARGUMENTOS POR NOMBRE
#
# funcion(
#     nombre="valor",
#     cantidad=10
# )
#
# Indican explícitamente a qué parámetro corresponde
# cada valor.
#
#
# VALOR PREDETERMINADO
#
# def funcion(estado="Nuevo"):
#
# permite omitir ese argumento durante la llamada.
#
#
# return
#
# devuelve información al código que llamó la función.
#
#
# VARIOS VALORES
#
# return valor_a, valor_b
#
# produce conceptualmente una tupla.
#
#
# Una función puede devolver prácticamente cualquier
# tipo de objeto Python.
#
#
# REGLA IMPORTANTE:
#
# evitar valores mutables como:
#
# []
# {}
#
# directamente como parámetros predeterminados.
#
#
# La finalidad de parámetros y return es poder construir
# funciones reutilizables que trabajen con datos diferentes
# sin duplicar la lógica.