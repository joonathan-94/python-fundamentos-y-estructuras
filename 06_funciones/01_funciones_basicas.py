# ============================================================
# FUNCIONES BÁSICAS EN PYTHON
# ============================================================
#
# Una función es un bloque de código que realiza una tarea
# determinada y que puede ejecutarse cuando sea necesario.
#
# Las funciones permiten:
#
# - organizar el código;
# - evitar repetir lógica;
# - dividir problemas grandes en partes más pequeñas;
# - reutilizar comportamiento;
# - facilitar pruebas y mantenimiento;
# - separar responsabilidades.
#
# En programas pequeños podemos escribir instrucciones una
# detrás de otra.
#
# A medida que una aplicación crece, esa forma de trabajar
# comienza a ser difícil de mantener.
#
# Las funciones permiten agrupar comportamiento bajo un nombre.
#
# Sintaxis básica:
#
# def nombre_funcion():
#     instrucciones
#
#
# "def" indica que estamos definiendo una función.
#
# El código dentro de la función debe estar indentado.


# ------------------------------------------------------------
# 1. DEFINIR UNA FUNCIÓN
# ------------------------------------------------------------

def mostrar_bienvenida():
    print("Sistema iniciado correctamente.")


# En este punto la función está DEFINIDA.
#
# Python conoce la función, pero todavía no ha ejecutado
# el código que contiene.


# ------------------------------------------------------------
# 2. LLAMAR UNA FUNCIÓN
# ------------------------------------------------------------

# Para ejecutar una función escribimos su nombre seguido
# de paréntesis.

mostrar_bienvenida()


# Resultado:
#
# Sistema iniciado correctamente.


# Podemos llamarla nuevamente:

mostrar_bienvenida()


# La misma lógica se ejecuta otra vez sin tener que repetir
# el print manualmente.


# ------------------------------------------------------------
# 3. DEFINIR NO ES LO MISMO QUE EJECUTAR
# ------------------------------------------------------------

def mostrar_estado_servidor():
    print("Servidor operativo.")


# La línea anterior solamente define la función.
#
# Para ejecutar el bloque debemos llamarla:

mostrar_estado_servidor()


# Esta diferencia es importante:
#
# definir:
#
# def mostrar_estado_servidor():
#     ...
#
#
# ejecutar:
#
# mostrar_estado_servidor()


# ------------------------------------------------------------
# 4. FUNCIONES QUE RECIBEN INFORMACIÓN
# ------------------------------------------------------------

# Una función puede recibir valores para trabajar con ellos.
#
# Estos valores permiten reutilizar la misma lógica con
# información diferente.

def mostrar_pokemon(nombre_pokemon):
    print(f"Pokémon registrado: {nombre_pokemon}")


mostrar_pokemon("Totodile")
mostrar_pokemon("Gengar")
mostrar_pokemon("Blaziken")


# La función es la misma.
#
# Lo que cambia es la información que recibe.
#
# Estudiaremos parámetros y argumentos con mayor profundidad
# en el siguiente archivo.


# ------------------------------------------------------------
# 5. EJEMPLO REAL: MOSTRAR UN TICKET
# ------------------------------------------------------------

def mostrar_ticket(id_ticket, estado_ticket):
    print(f"{id_ticket} - {estado_ticket}")


mostrar_ticket("WD-1001", "Nuevo")
mostrar_ticket("WD-1002", "En progreso")


# Sin funciones podríamos terminar repitiendo muchas veces
# estructuras similares.
#
# Una función permite centralizar esa lógica.


# ------------------------------------------------------------
# 6. return
# ------------------------------------------------------------

# Una función puede DEVOLVER un resultado utilizando return.
#
# Esto es uno de los conceptos más importantes de este módulo.

def calcular_total(cantidad_productos, precio_unitario):
    total_calculado = cantidad_productos * precio_unitario

    return total_calculado


resultado_compra = calcular_total(4, 2500)

print(resultado_compra)


# Proceso:
#
# calcular_total(4, 2500)
#
# cantidad_productos = 4
# precio_unitario = 2500
#
# total_calculado = 10000
#
# return 10000
#
# resultado_compra recibe:
#
# 10000


# ------------------------------------------------------------
# 7. return VS print()
# ------------------------------------------------------------

# Esta diferencia es FUNDAMENTAL.


# FUNCIÓN QUE SOLAMENTE IMPRIME

def mostrar_suma(valor_a, valor_b):
    print(valor_a + valor_b)


mostrar_suma(10, 5)


# Esta función muestra el resultado en consola.
#
# Pero no está entregando ese resultado al resto del programa.


# FUNCIÓN QUE DEVUELVE EL RESULTADO

def sumar_valores(numero_a, numero_b):
    resultado_suma = numero_a + numero_b

    return resultado_suma


suma_obtenida = sumar_valores(10, 5)

print(suma_obtenida)


# Ahora el valor puede reutilizarse.

resultado_doble = suma_obtenida * 2

print(resultado_doble)


# ------------------------------------------------------------
# 8. POR QUÉ return SUELE SER MÁS REUTILIZABLE
# ------------------------------------------------------------

def calcular_precio_final(cantidad_repuestos, valor_repuesto):
    return cantidad_repuestos * valor_repuesto


precio_final = calcular_precio_final(3, 15990)


# Podemos decidir posteriormente qué hacer con el resultado.

print(precio_final)


# También podríamos:
#
# - almacenarlo;
# - compararlo;
# - enviarlo a otra función;
# - guardarlo posteriormente en una base de datos;
# - incluirlo en una respuesta de una API;
# - utilizarlo en otro cálculo.
#
# La función no necesita decidir cómo mostrar el resultado.
#
# Su responsabilidad es calcularlo.


# ------------------------------------------------------------
# 9. EJEMPLO: AUTOMATIZACIÓN
# ------------------------------------------------------------

def generar_nombre_respaldo(nombre_sistema, fecha_respaldo):
    nombre_archivo = (
        f"backup_{nombre_sistema}_{fecha_respaldo}.zip"
    )

    return nombre_archivo


archivo_respaldo = generar_nombre_respaldo(
    "workdesk",
    "2026-09-27"
)

print(archivo_respaldo)


# Resultado:
#
# backup_workdesk_2026-09-27.zip
#
#
# Una función como esta podría utilizarse posteriormente
# dentro de un script real de automatización.


# ------------------------------------------------------------
# 10. EJEMPLO: PROCESAMIENTO DE DATOS
# ------------------------------------------------------------

def calcular_promedio(valor_uno, valor_dos, valor_tres):
    suma_mediciones = valor_uno + valor_dos + valor_tres
    promedio_mediciones = suma_mediciones / 3

    return promedio_mediciones


promedio_temperatura = calcular_promedio(
    23.5,
    25.0,
    24.0
)

print(promedio_temperatura)


# En análisis o procesamiento de datos, las funciones permiten
# encapsular transformaciones o cálculos para reutilizarlos.


# ------------------------------------------------------------
# 11. return TERMINA LA EJECUCIÓN DE LA FUNCIÓN
# ------------------------------------------------------------

# Cuando Python ejecuta return, la función termina.

def comprobar_numero(numero_recibido):

    if numero_recibido < 0:
        return "Negativo"

    return "Cero o positivo"


clasificacion_negativa = comprobar_numero(-5)
clasificacion_positiva = comprobar_numero(10)

print(clasificacion_negativa)
print(clasificacion_positiva)


# Si numero_recibido es menor que 0:
#
# return "Negativo"
#
# termina inmediatamente la función.
#
# Python no continúa ejecutando las instrucciones posteriores
# dentro de esa llamada.


# ------------------------------------------------------------
# 12. FUNCIÓN SIN return
# ------------------------------------------------------------

def registrar_evento():
    print("Evento registrado.")


resultado_evento = registrar_evento()

print(resultado_evento)


# La función imprime:
#
# Evento registrado.
#
# Pero resultado_evento contiene:
#
# None
#
#
# Cuando una función termina sin ejecutar un return con valor,
# Python devuelve None.


# ------------------------------------------------------------
# 13. return SIN EXPRESIÓN
# ------------------------------------------------------------

# También podemos utilizar return sin indicar un valor.

def validar_estado(estado_recibido):

    if estado_recibido == "":
        return

    print(f"Estado recibido: {estado_recibido}")


resultado_validacion = validar_estado("")

print(resultado_validacion)


# return sin valor también devuelve None.
#
# En este caso se utiliza para terminar anticipadamente
# la función.


# ------------------------------------------------------------
# 14. REUTILIZACIÓN
# ------------------------------------------------------------

def convertir_minutos_a_horas(minutos_totales):
    horas_calculadas = minutos_totales / 60

    return horas_calculadas


duracion_tarea = convertir_minutos_a_horas(120)
duracion_reunion = convertir_minutos_a_horas(90)
duracion_proceso = convertir_minutos_a_horas(45)

print(duracion_tarea)
print(duracion_reunion)
print(duracion_proceso)


# Una sola función puede trabajar con muchos valores.
#
# Si posteriormente necesitamos cambiar la fórmula,
# tenemos un único lugar donde modificar la lógica.


# ------------------------------------------------------------
# 15. EVITAR REPETICIÓN
# ------------------------------------------------------------

# Sin función podríamos terminar haciendo:

precio_corvette = 45000 * 1.19
precio_camaro = 38000 * 1.19
precio_bel_air = 52000 * 1.19


# Si la lógica se repite, podemos encapsularla.

def aplicar_impuesto(precio_base):
    return precio_base * 1.19


corvette_con_impuesto = aplicar_impuesto(45000)
camaro_con_impuesto = aplicar_impuesto(38000)
bel_air_con_impuesto = aplicar_impuesto(52000)

print(corvette_con_impuesto)
print(camaro_con_impuesto)
print(bel_air_con_impuesto)


# La segunda versión centraliza la regla de cálculo.


# ------------------------------------------------------------
# 16. UNA FUNCIÓN DEBE TENER UN PROPÓSITO CLARO
# ------------------------------------------------------------

# Es preferible crear funciones con nombres que expliquen
# claramente qué hacen.

def calcular_area_rectangulo(ancho_rectangulo, alto_rectangulo):
    return ancho_rectangulo * alto_rectangulo


area_calculada = calcular_area_rectangulo(10, 5)

print(area_calculada)


# El nombre:
#
# calcular_area_rectangulo
#
# comunica claramente la intención.


# Evitaremos nombres ambiguos como:
#
# funcion1()
# hacer_cosa()
# proceso()
# ejecutar()
#
# cuando podemos expresar mejor la responsabilidad.


# ------------------------------------------------------------
# 17. NOMBRES DE FUNCIONES
# ------------------------------------------------------------

# Utilizaremos snake_case.
#
# Ejemplos adecuados:
#
# calcular_total()
# validar_usuario()
# generar_reporte()
# obtener_ticket()
# procesar_archivo()
# calcular_promedio()
#
#
# Los nombres suelen comenzar con un verbo porque una función
# representa una acción o comportamiento.


# ------------------------------------------------------------
# 18. EJEMPLO REALISTA: CALCULAR COSTO DE UN TICKET
# ------------------------------------------------------------

def calcular_costo_servicio(horas_trabajadas, valor_hora):
    costo_servicio = horas_trabajadas * valor_hora

    return costo_servicio


costo_ticket = calcular_costo_servicio(
    2.5,
    18000
)


print(f"Costo del servicio: ${costo_ticket}")


# Esta función:
#
# recibe datos
# ↓
# realiza una operación
# ↓
# devuelve el resultado
#
#
# No solicita datos con input().
#
# Tampoco decide necesariamente dónde guardar el resultado.
#
# Esto ayuda a separar responsabilidades.


# ------------------------------------------------------------
# 19. SEPARAR ENTRADA, LÓGICA Y SALIDA
# ------------------------------------------------------------

# Un patrón que empezaremos a aplicar es:
#
# ENTRADA
# ↓
# LÓGICA
# ↓
# SALIDA


# Entrada:

horas_ingresadas = 3
tarifa_ingresada = 15000


# Lógica:

def obtener_costo_total(horas_servicio, tarifa_hora):
    return horas_servicio * tarifa_hora


costo_obtenido = obtener_costo_total(
    horas_ingresadas,
    tarifa_ingresada
)


# Salida:

print(f"Total calculado: ${costo_obtenido}")


# Esta separación será cada vez más importante cuando
# avancemos hacia:
#
# - programas de consola;
# - backend;
# - APIs;
# - automatizaciones;
# - testing;
# - WorkDesk;
# - MoneyDesk.


# ------------------------------------------------------------
# 20. EJEMPLO CON UNA REGLA SIMPLE
# ------------------------------------------------------------

def obtener_categoria_prioridad(nivel_prioridad):

    if nivel_prioridad >= 4:
        return "Alta"

    if nivel_prioridad >= 2:
        return "Media"

    return "Baja"


prioridad_servidor = obtener_categoria_prioridad(4)

print(prioridad_servidor)


# Aquí una función encapsula una pequeña regla.
#
# En aplicaciones reales este tipo de lógica puede aparecer
# para:
#
# - clasificaciones;
# - validaciones;
# - cálculos;
# - transformaciones;
# - decisiones de negocio.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# DEFINIR:
#
# def nombre_funcion():
#     ...
#
#
# EJECUTAR:
#
# nombre_funcion()
#
#
# RECIBIR INFORMACIÓN:
#
# def funcion(valor):
#     ...
#
#
# DEVOLVER INFORMACIÓN:
#
# def funcion(valor):
#     resultado = ...
#     return resultado
#
#
# Una función puede entenderse inicialmente como:
#
# entrada
# ↓
# procesamiento
# ↓
# resultado
#
#
# print()
# → muestra información.
#
# return
# → devuelve información al código que llamó la función.
#
#
# Si una función no devuelve explícitamente un valor:
#
# → devuelve None.
#
#
# Una buena función debería tener:
#
# - un propósito claro;
# - un nombre descriptivo;
# - lógica comprensible;
# - una responsabilidad bien definida.
#
#
# Las funciones permiten comenzar a transformar scripts
# lineales en programas mejor organizados y reutilizables.