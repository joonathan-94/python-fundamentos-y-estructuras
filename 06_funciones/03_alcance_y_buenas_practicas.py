# ============================================================
# ALCANCE Y BUENAS PRÁCTICAS EN FUNCIONES
# ============================================================
#
# Cuando trabajamos con funciones no basta con conocer:
#
# def
# parámetros
# argumentos
# return
#
# También necesitamos entender:
#
# - dónde existen las variables;
# - qué información debería recibir una función;
# - qué información debería devolver;
# - cómo documentarla;
# - cómo escribir funciones fáciles de mantener.
#
# Estas decisiones comienzan a ser importantes cuando un
# programa crece y deja de ser un script pequeño.


# ------------------------------------------------------------
# 1. ALCANCE DE UNA VARIABLE
# ------------------------------------------------------------

# El alcance (scope) determina desde qué parte del programa
# podemos acceder a un nombre.


def mostrar_modelo():
    modelo_local = "Corvette Stingray"

    print(modelo_local)


mostrar_modelo()


# modelo_local fue creada dentro de la función.
#
# Es una variable local.
#
# Esto NO funcionaría fuera de la función:
#
# print(modelo_local)
#
# produciría:
#
# NameError


# ------------------------------------------------------------
# 2. VARIABLES LOCALES
# ------------------------------------------------------------

def calcular_total():
    cantidad_local = 4
    precio_local = 2500

    total_local = cantidad_local * precio_local

    return total_local


resultado_total = calcular_total()

print(resultado_total)


# cantidad_local
# precio_local
# total_local
#
# pertenecen al ámbito local de calcular_total().
#
# Sus nombres existen durante la ejecución de esa función.


# ------------------------------------------------------------
# 3. CADA LLAMADA TIENE SU PROPIO ÁMBITO LOCAL
# ------------------------------------------------------------

def mostrar_pokemon(nombre_pokemon):
    mensaje_local = f"Pokémon: {nombre_pokemon}"

    print(mensaje_local)


mostrar_pokemon("Totodile")
mostrar_pokemon("Gengar")


# Cada llamada trabaja con sus propios valores locales.
#
# Una llamada no utiliza automáticamente los valores locales
# creados por otra llamada.


# ------------------------------------------------------------
# 4. VARIABLES GLOBALES
# ------------------------------------------------------------

# Una variable definida fuera de una función pertenece
# al ámbito global del módulo.

nombre_sistema = "WorkDesk"


def mostrar_nombre_sistema():
    print(nombre_sistema)


mostrar_nombre_sistema()


# La función puede LEER nombre_sistema porque el nombre existe
# en un ámbito exterior.


# ------------------------------------------------------------
# 5. EVITAR DEPENDER INNECESARIAMENTE DE VARIABLES GLOBALES
# ------------------------------------------------------------

# Esto funciona:

impuesto_global = 0.19


def calcular_precio_global(precio_base):
    return precio_base * (1 + impuesto_global)


precio_final_global = calcular_precio_global(10000)

print(precio_final_global)


# Pero la función depende de una variable externa.
#
# Para entender completamente la función tenemos que buscar
# información fuera de ella.


# Muchas veces es más explícito recibir la información:

def calcular_precio(precio_base, porcentaje_impuesto):
    return precio_base * (1 + porcentaje_impuesto)


precio_final = calcular_precio(
    precio_base=10000,
    porcentaje_impuesto=0.19
)

print(precio_final)


# Ahora la función declara claramente qué necesita para
# realizar su trabajo.


# ------------------------------------------------------------
# 6. global
# ------------------------------------------------------------

contador_global = 0


def incrementar_contador_global():
    global contador_global

    contador_global += 1


incrementar_contador_global()

print(contador_global)


# La palabra global indica que queremos modificar el nombre
# existente en el ámbito global.
#
# Sin global, una asignación dentro de la función normalmente
# crearía una variable local.


# IMPORTANTE:
#
# global existe y es válido.
#
# Pero no deberíamos utilizarlo como solución automática.
#
# Una dependencia excesiva de variables globales puede hacer
# que el código sea:
#
# - más difícil de seguir;
# - más difícil de probar;
# - más difícil de reutilizar;
# - más propenso a efectos secundarios inesperados.


# ------------------------------------------------------------
# 7. ALTERNATIVA A MODIFICAR UNA GLOBAL
# ------------------------------------------------------------

def incrementar_contador(valor_actual):
    return valor_actual + 1


contador_actual = 0

contador_actual = incrementar_contador(contador_actual)

print(contador_actual)


# En este caso la función:
#
# recibe el estado actual
# ↓
# calcula un nuevo valor
# ↓
# lo devuelve
#
# La modificación queda visible en el código que llama
# a la función.


# ------------------------------------------------------------
# 8. UNA FUNCIÓN DEBE EXPLICAR QUÉ NECESITA
# ------------------------------------------------------------

# Menos claro:

configuracion_global = {
    "tarifa_hora": 15000
}


def calcular_servicio_menos_claro(horas):
    return horas * configuracion_global["tarifa_hora"]


# Más explícito:

def calcular_servicio(horas_trabajadas, tarifa_hora):
    return horas_trabajadas * tarifa_hora


costo_servicio = calcular_servicio(
    horas_trabajadas=3,
    tarifa_hora=15000
)

print(costo_servicio)


# La segunda función puede reutilizarse con cualquier tarifa.


# ------------------------------------------------------------
# 9. SEPARAR ENTRADA DE DATOS Y LÓGICA
# ------------------------------------------------------------

# EVITAR, cuando sea posible, mezclar toda la interacción
# dentro de una función de cálculo.


def calcular_saldo(ingresos, gastos):
    return ingresos - gastos


# Los datos pueden provenir de cualquier lugar:
#
# input()
# archivo
# API
# base de datos
# pruebas automatizadas
#
# La función no necesita saberlo.


ingresos_mes = 850000
gastos_mes = 630000

saldo_mes = calcular_saldo(
    ingresos_mes,
    gastos_mes
)

print(saldo_mes)


# Esto hace la función más reutilizable.


# ------------------------------------------------------------
# 10. EJEMPLO MENOS REUTILIZABLE
# ------------------------------------------------------------

def calcular_saldo_desde_consola():
    ingresos = float(
        input("Ingresa los ingresos: ")
    )

    gastos = float(
        input("Ingresa los gastos: ")
    )

    return ingresos - gastos


# Esta función puede servir en un script pequeño.
#
# Pero queda directamente acoplada a la consola.
#
# Para reutilizar la lógica en:
#
# - Flask;
# - una API;
# - un test;
# - una automatización;
#
# tendríamos que modificarla.


# ------------------------------------------------------------
# 11. SEPARAR RESPONSABILIDADES
# ------------------------------------------------------------

# Una función debería tener un propósito claro.


def normalizar_id_ticket(id_recibido):
    return id_recibido.strip().upper()


def construir_resumen_ticket(
    id_ticket,
    titulo_ticket
):
    return {
        "id": id_ticket,
        "titulo": titulo_ticket
    }


id_normalizado = normalizar_id_ticket(
    "   wd-1001 "
)

resumen_ticket = construir_resumen_ticket(
    id_ticket=id_normalizado,
    titulo_ticket="Error de acceso"
)

print(resumen_ticket)


# Tenemos dos responsabilidades:
#
# normalizar_id_ticket()
# → normaliza un identificador.
#
# construir_resumen_ticket()
# → construye una estructura.
#
#
# Evitamos crear una función enorme que haga absolutamente
# todo.


# ------------------------------------------------------------
# 12. FUNCIONES PEQUEÑAS, PERO CON SENTIDO
# ------------------------------------------------------------

# "Una función debe ser pequeña" no significa dividir cada
# línea en una función diferente.
#
# La división debe representar responsabilidades útiles.


def calcular_subtotal(cantidad, precio_unitario):
    return cantidad * precio_unitario


def calcular_impuesto(subtotal, tasa_impuesto):
    return subtotal * tasa_impuesto


def calcular_total_compra(
    cantidad,
    precio_unitario,
    tasa_impuesto
):
    subtotal = calcular_subtotal(
        cantidad,
        precio_unitario
    )

    impuesto = calcular_impuesto(
        subtotal,
        tasa_impuesto
    )

    return subtotal + impuesto


total_compra = calcular_total_compra(
    cantidad=3,
    precio_unitario=20000,
    tasa_impuesto=0.19
)

print(total_compra)


# Aquí cada función tiene una responsabilidad comprensible.


# ------------------------------------------------------------
# 13. EVITAR REPETICIÓN INNECESARIA
# ------------------------------------------------------------

# Si una misma regla aparece muchas veces, una función puede
# centralizarla.


def normalizar_nombre(nombre_recibido):
    return nombre_recibido.strip().title()


nombre_entrenador = normalizar_nombre(
    "   misty   "
)

nombre_solicitante = normalizar_nombre(
    "   tony soprano   "
)

nombre_propietario = normalizar_nombre(
    "   walter white   "
)

print(nombre_entrenador)
print(nombre_solicitante)
print(nombre_propietario)


# Si cambia la regla de normalización, tenemos un solo lugar
# donde modificarla.


# ------------------------------------------------------------
# 14. DOCSTRINGS
# ------------------------------------------------------------

# Una docstring documenta el propósito de una función.
#
# Se escribe como la primera instrucción dentro de la función.

def calcular_area_rectangulo(ancho, alto):
    """Calcula y devuelve el área de un rectángulo."""

    return ancho * alto


area_rectangulo = calcular_area_rectangulo(
    10,
    5
)

print(area_rectangulo)


# Una docstring NO es simplemente un comentario cualquiera.
#
# Python la asocia a la función.


print(calcular_area_rectangulo.__doc__)


# ------------------------------------------------------------
# 15. DOCSTRING DE VARIAS LÍNEAS
# ------------------------------------------------------------

def calcular_costo_mantenimiento(
    horas_trabajadas,
    tarifa_hora
):
    """
    Calcula el costo de un mantenimiento.

    Multiplica las horas trabajadas por la tarifa
    correspondiente a una hora de trabajo.
    """

    return horas_trabajadas * tarifa_hora


costo_mantenimiento = calcular_costo_mantenimiento(
    4,
    18000
)

print(costo_mantenimiento)


# No todas las funciones pequeñas necesitan una explicación
# extensa.
#
# La documentación debe aportar información útil y no repetir
# innecesariamente lo que el código ya expresa con claridad.


# ------------------------------------------------------------
# 16. COMENTARIO VS DOCSTRING
# ------------------------------------------------------------

# COMENTARIO:
#
# explica decisiones o detalles del código.
#
# DOCSTRING:
#
# documenta el propósito y comportamiento de una función,
# clase o módulo.


def convertir_segundos_a_minutos(segundos):
    """Convierte segundos a minutos."""

    # Un minuto contiene 60 segundos.
    return segundos / 60


minutos_convertidos = convertir_segundos_a_minutos(180)

print(minutos_convertidos)


# ------------------------------------------------------------
# 17. TYPE HINTS
# ------------------------------------------------------------

# Python permite agregar anotaciones de tipo.
#
# Ejemplo:

def calcular_precio_total(
    cantidad: int,
    precio_unitario: float
) -> float:
    return cantidad * precio_unitario


precio_calculado = calcular_precio_total(
    3,
    15990.0
)

print(precio_calculado)


# Podemos leerlo así:
#
# cantidad
# → se espera int
#
# precio_unitario
# → se espera float
#
# -> float
# → esperamos que la función devuelva float


# ------------------------------------------------------------
# 18. LOS TYPE HINTS NO CAMBIAN EL TIPADO DE PYTHON
# ------------------------------------------------------------

# Las anotaciones ayudan a:
#
# - documentar;
# - comprender interfaces;
# - IDEs;
# - analizadores estáticos;
# - herramientas de calidad.
#
# Pero Python normalmente NO obliga en tiempo de ejecución
# a respetar estas anotaciones.


def mostrar_generacion(
    generacion: int
) -> str:
    return f"Generación: {generacion}"


print(mostrar_generacion(2))


# Las anotaciones expresan intención.
#
# No debemos interpretarlas como una validación automática.


# ------------------------------------------------------------
# 19. TYPE HINTS CON COLECCIONES BÁSICAS
# ------------------------------------------------------------

def contar_tickets(
    tickets_recibidos: list
) -> int:
    return len(tickets_recibidos)


tickets_abiertos = [
    "WD-1001",
    "WD-1002",
    "WD-1003"
]

cantidad_tickets = contar_tickets(
    tickets_abiertos
)

print(cantidad_tickets)


# Más adelante veremos formas de tipado más específicas.
#
# Por ahora basta con comprender la sintaxis básica.


# ------------------------------------------------------------
# 20. COMBINAR DOCSTRING Y TYPE HINTS
# ------------------------------------------------------------

def calcular_antiguedad_auto(
    anio_actual: int,
    anio_fabricacion: int
) -> int:
    """Calcula los años transcurridos desde la fabricación."""

    return anio_actual - anio_fabricacion


antiguedad_camaro = calcular_antiguedad_auto(
    anio_actual=2026,
    anio_fabricacion=1967
)

print(antiguedad_camaro)


# Esto mejora la información disponible para quien lea
# o utilice la función.


# ------------------------------------------------------------
# 21. NOMBRES DESCRIPTIVOS
# ------------------------------------------------------------

# EVITAR:

def calc(a, b):
    return a * b


# PREFERIR, cuando el dominio lo permite:

def calcular_costo_repuestos(
    cantidad_repuestos,
    precio_repuesto
):
    return cantidad_repuestos * precio_repuesto


costo_repuestos = calcular_costo_repuestos(
    cantidad_repuestos=4,
    precio_repuesto=12500
)

print(costo_repuestos)


# Un buen nombre reduce la necesidad de comentarios.


# ------------------------------------------------------------
# 22. snake_case
# ------------------------------------------------------------

# Para funciones y variables utilizaremos snake_case.


def obtener_estado_ticket():
    return "Nuevo"


# Preferimos:
#
# obtener_estado_ticket()
#
# y evitamos para código Python nuevo:
#
# obtenerEstadoTicket()


# ------------------------------------------------------------
# 23. EVITAR FUNCIONES CON RESPONSABILIDADES MEZCLADAS
# ------------------------------------------------------------

# Supongamos que necesitamos procesar un ID y calcular
# una prioridad.
#
# Podemos separar ambas reglas.


def limpiar_id(id_recibido):
    return id_recibido.strip().upper()


def clasificar_prioridad(nivel):
    if nivel >= 4:
        return "Alta"

    if nivel >= 2:
        return "Media"

    return "Baja"


codigo_limpio = limpiar_id(
    " wd-5001 "
)

prioridad_calculada = clasificar_prioridad(4)

print(codigo_limpio)
print(prioridad_calculada)


# Cada función puede cambiar independientemente.


# ------------------------------------------------------------
# 24. EFECTOS SECUNDARIOS
# ------------------------------------------------------------

# Un efecto secundario ocurre cuando una función produce
# cambios fuera de su valor retornado.
#
# Por ejemplo, modificar una lista recibida.

def agregar_modelo(
    modelos_existentes,
    modelo_nuevo
):
    modelos_existentes.append(modelo_nuevo)


autos_clasicos = [
    "Corvette Stingray",
    "Camaro 1967"
]

agregar_modelo(
    autos_clasicos,
    "Chevrolet Bel Air"
)

print(autos_clasicos)


# La función modificó el objeto original.
#
# Esto puede ser completamente válido.
#
# Lo importante es saber y dejar claro que la función
# produce ese efecto.


# ------------------------------------------------------------
# 25. ALTERNATIVA SIN MODIFICAR LA LISTA ORIGINAL
# ------------------------------------------------------------

def obtener_lista_con_modelo(
    modelos_existentes,
    modelo_nuevo
):
    nuevos_modelos = modelos_existentes.copy()

    nuevos_modelos.append(modelo_nuevo)

    return nuevos_modelos


modelos_originales = [
    "Ford Mustang",
    "Dodge Charger"
]

modelos_actualizados = obtener_lista_con_modelo(
    modelos_originales,
    "Pontiac GTO"
)


print("Original:", modelos_originales)
print("Nueva:", modelos_actualizados)


# Ninguna de las dos formas es universalmente correcta.
#
# La función debe expresar claramente si modifica datos
# existentes o devuelve un nuevo resultado.


# ------------------------------------------------------------
# 26. EJEMPLO REALISTA: LÓGICA DE BACKEND
# ------------------------------------------------------------

def normalizar_prioridad(
    prioridad_recibida: str
) -> str:
    """Normaliza el texto utilizado como prioridad."""

    return prioridad_recibida.strip().capitalize()


def construir_ticket_basico(
    id_ticket: str,
    titulo_ticket: str,
    prioridad_ticket: str
) -> dict:
    """Construye y devuelve los datos básicos de un ticket."""

    return {
        "id": id_ticket,
        "titulo": titulo_ticket,
        "prioridad": prioridad_ticket,
        "estado": "Nuevo"
    }


prioridad_normalizada = normalizar_prioridad(
    "   alta   "
)

ticket_backend = construir_ticket_basico(
    id_ticket="WD-7001",
    titulo_ticket="Error de conexión",
    prioridad_ticket=prioridad_normalizada
)

print(ticket_backend)


# Observa la separación:
#
# normalizar_prioridad()
# → transforma un dato.
#
# construir_ticket_basico()
# → construye una estructura.
#
# Ninguna función solicita input().
#
# Por eso la misma lógica podría utilizarse posteriormente
# desde una consola, una API o una aplicación web.


# ------------------------------------------------------------
# 27. EJEMPLO REALISTA: AUTOMATIZACIÓN
# ------------------------------------------------------------

def construir_nombre_archivo(
    sistema: str,
    fecha: str
) -> str:
    """Construye el nombre de un archivo de respaldo."""

    sistema_normalizado = sistema.strip().lower()

    return f"backup_{sistema_normalizado}_{fecha}.zip"


nombre_backup = construir_nombre_archivo(
    sistema="MoneyDesk",
    fecha="2026-09-27"
)

print(nombre_backup)


# La función no realiza todavía el backup.
#
# Tiene una responsabilidad concreta:
#
# generar el nombre.


# ------------------------------------------------------------
# 28. EJEMPLO REALISTA: PROCESAMIENTO DE DATOS
# ------------------------------------------------------------

def calcular_promedio(
    valores: list
) -> float:
    """Calcula el promedio de una lista de valores."""

    suma_valores = 0

    for valor_actual in valores:
        suma_valores += valor_actual

    return suma_valores / len(valores)


mediciones_cpu = [
    45.2,
    70.5,
    63.1
]

promedio_cpu = calcular_promedio(
    mediciones_cpu
)

print(promedio_cpu)


# Más adelante aprenderemos a manejar casos como:
#
# []
#
# donde no podríamos dividir por cero.
#
# Eso corresponde al estudio de validaciones y excepciones.


# ------------------------------------------------------------
# 29. QUÉ DEBERÍAMOS BUSCAR AL CREAR UNA FUNCIÓN
# ------------------------------------------------------------

# Antes de crear una función podemos preguntarnos:
#
# ¿Qué tarea realiza?
#
# ¿Qué datos necesita?
#
# ¿Qué resultado debería devolver?
#
# ¿Está modificando algo fuera de ella?
#
# ¿Su nombre explica claramente qué hace?
#
# ¿Estoy mezclando responsabilidades diferentes?
#
# ¿Podría reutilizar esta lógica en otro contexto?


# ------------------------------------------------------------
# 30. NO BUSCAR PERFECCIÓN PREMATURAMENTE
# ------------------------------------------------------------

# Tampoco debemos convertir un programa pequeño en decenas
# de funciones innecesarias.
#
# Nuestro objetivo inicial es:
#
# código claro
# +
# responsabilidades razonables
# +
# reutilización cuando tenga sentido
#
#
# A medida que construyamos proyectos reales aprenderemos
# cuándo conviene dividir más el código.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# VARIABLE LOCAL
#
# existe dentro del ámbito de una función.
#
#
# VARIABLE GLOBAL
#
# pertenece al ámbito del módulo.
#
#
# global
#
# permite reasignar un nombre del ámbito global,
# pero no debe utilizarse innecesariamente.
#
#
# BUENA PRÁCTICA GENERAL
#
# preferir funciones que reciban claramente lo que necesitan:
#
# def calcular(valor, configuracion):
#     ...
#
# en lugar de depender ocultamente de muchos datos globales.
#
#
# DOCSTRING
#
# def funcion():
#     """Describe qué hace la función."""
#
#
# TYPE HINT
#
# def sumar(a: int, b: int) -> int:
#     return a + b
#
#
# Los type hints ayudan a documentar y analizar el código,
# pero Python no los impone automáticamente en tiempo
# de ejecución.
#
#
# FUNCIONES MANTENIBLES
#
# - nombres descriptivos;
# - snake_case;
# - propósito claro;
# - parámetros explícitos;
# - return para entregar resultados;
# - evitar dependencias globales innecesarias;
# - separar entrada/salida de la lógica cuando tenga sentido;
# - conocer los efectos secundarios;
# - documentar cuando aporte valor.
#
#
# El objetivo no es escribir funciones perfectas desde el
# comienzo.
#
# El objetivo es aprender a dividir un programa en piezas
# comprensibles, reutilizables y fáciles de modificar.