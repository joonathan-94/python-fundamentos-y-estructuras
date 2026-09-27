# ============================================================
# PAQUETES EN PYTHON
# ============================================================
#
# Ya aprendimos:
#
# función
# → bloque reutilizable de lógica
#
# módulo
# → archivo .py que puede contener funciones y otros elementos
#
#
# Ahora agregamos:
#
# paquete
# → carpeta que organiza módulos relacionados
#
#
# Nuestra estructura:
#
# utilidades/
# ├── __init__.py
# ├── calculos.py
# └── texto.py
#
#
# utilidades
# → paquete
#
# calculos
# → módulo
#
# texto
# → módulo


# ------------------------------------------------------------
# 1. IMPORTAR DESDE UN PAQUETE
# ------------------------------------------------------------

from utilidades.calculos import calcular_promedio


promedio_obtenido = calcular_promedio(
    10,
    20
)

print(promedio_obtenido)


# Podemos leer:
#
# from utilidades.calculos import calcular_promedio
#
# como:
#
# desde el paquete:
#
# utilidades
#
# entra al módulo:
#
# calculos
#
# e importa:
#
# calcular_promedio


# ------------------------------------------------------------
# 2. VISUALIZACIÓN DE LA RUTA
# ------------------------------------------------------------

# Código:
#
# from utilidades.calculos import calcular_promedio
#
#
# Representación:
#
# utilidades/
#     ↓
# calculos.py
#     ↓
# calcular_promedio()


# ------------------------------------------------------------
# 3. IMPORTAR DESDE OTRO MÓDULO DEL PAQUETE
# ------------------------------------------------------------

from utilidades.texto import normalizar_codigo


codigo_ticket = normalizar_codigo(
    "   wd-3001   "
)

print(codigo_ticket)


# Resultado:
#
# WD-3001


# ------------------------------------------------------------
# 4. IMPORTAR VARIAS FUNCIONES
# ------------------------------------------------------------

from utilidades.texto import (
    normalizar_codigo,
    normalizar_nombre
)


codigo_normalizado = normalizar_codigo(
    "  srv-001  "
)

nombre_normalizado = normalizar_nombre(
    "   stephen hawking   "
)


print(codigo_normalizado)
print(nombre_normalizado)


# Resultado:
#
# SRV-001
#
# Stephen Hawking


# ------------------------------------------------------------
# 5. EJEMPLO CON CIENTÍFICOS
# ------------------------------------------------------------

cientificos = [
    "   stephen hawking   ",
    "  carl sagan ",
    "   galileo galilei",
    "jose maza   "
]


cientificos_normalizados = []


for cientifico in cientificos:

    nombre_limpio = normalizar_nombre(
        cientifico
    )

    cientificos_normalizados.append(
        nombre_limpio
    )


print(cientificos_normalizados)


# Aquí reutilizamos una función definida en:
#
# utilidades/texto.py
#
# para transformar varios datos.


# ------------------------------------------------------------
# 6. UTILIZAR OTRO CÁLCULO DEL PAQUETE
# ------------------------------------------------------------

from utilidades.calculos import calcular_diferencia


anio_publicacion_inicial = 1988
anio_publicacion_final = 2001


diferencia_anios = calcular_diferencia(
    anio_publicacion_inicial,
    anio_publicacion_final
)


print(diferencia_anios)


# No importa demasiado qué representan los datos.
#
# calcular_diferencia() contiene una operación reutilizable.


# ------------------------------------------------------------
# 7. POR QUÉ UTILIZAR PAQUETES
# ------------------------------------------------------------

# Supongamos que nuestro proyecto comienza a crecer.
#
# Podríamos tener muchos módulos:
#
# calculos.py
# texto.py
# archivos.py
# fechas.py
#
#
# En lugar de dejarlos todos mezclados, podemos agruparlos:
#
# utilidades/
# ├── calculos.py
# ├── texto.py
# ├── archivos.py
# └── fechas.py
#
#
# El paquete ayuda a organizar módulos relacionados.


# ------------------------------------------------------------
# 8. FUNCIÓN → MÓDULO → PAQUETE
# ------------------------------------------------------------

# Esta relación es el concepto principal del tema.
#
#
# FUNCIÓN
#
# def normalizar_codigo():
#     ...
#
#
# vive dentro de:
#
# texto.py
#
#
# texto.py es:
#
# MÓDULO
#
#
# texto.py vive dentro de:
#
# utilidades/
#
#
# utilidades es:
#
# PAQUETE


# ------------------------------------------------------------
# 9. EJEMPLO CON UN PROYECTO MÁS GRANDE
# ------------------------------------------------------------

# Conceptualmente un programa podría crecer hacia algo así:
#
# proyecto/
# │
# ├── usuarios/
# │   ├── usuarios.py
# │   └── validaciones.py
# │
# ├── tickets/
# │   ├── tickets.py
# │   └── prioridades.py
# │
# └── utilidades/
#     ├── texto.py
#     └── calculos.py
#
#
# No estamos construyendo esta arquitectura todavía.
#
# El ejemplo solamente muestra cómo los paquetes ayudan
# a separar áreas relacionadas.


# ------------------------------------------------------------
# 10. RELACIÓN CON WORKDESK
# ------------------------------------------------------------

# Cuando WorkDesk crezca no querremos tener:
#
# app.py
#
# con miles de líneas.
#
#
# Utilizaremos diferentes archivos y carpetas para separar
# responsabilidades.
#
# Los módulos y paquetes son parte de esa base conceptual.
#
# La arquitectura real se estudiará cuando corresponda.


# ------------------------------------------------------------
# 11. RELACIÓN CON ANÁLISIS DE DATOS
# ------------------------------------------------------------

# Lo mismo aplica fuera del desarrollo web.
#
# Por ejemplo:
#
# analisis/
# ├── carga.py
# ├── limpieza.py
# └── metricas.py
#
#
# Podríamos importar:
#
# from analisis.metricas import calcular_promedio
#
#
# Por eso módulos y paquetes no son algo exclusivo
# de Flask o aplicaciones web.


# ------------------------------------------------------------
# 12. RELACIÓN CON AUTOMATIZACIÓN
# ------------------------------------------------------------

# También podríamos tener:
#
# automatizacion/
# ├── archivos.py
# ├── respaldos.py
# └── notificaciones.py
#
#
# Un script principal podría utilizar esas funciones
# mediante imports.


# ------------------------------------------------------------
# 13. NO NECESITAMOS ENTENDER TODO AHORA
# ------------------------------------------------------------

# A este nivel no necesitas conocer:
#
# - arquitecturas complejas;
# - paquetes distribuibles;
# - publicación en PyPI;
# - imports relativos avanzados;
# - configuración avanzada de rutas.
#
#
# Eso tendrá sentido cuando construyamos proyectos mayores.
#
# Por ahora necesitamos comprender solamente la estructura.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# FUNCIÓN
#
# def calcular_promedio():
#     ...
#
# organiza una tarea.
#
#
# MÓDULO
#
# calculos.py
#
# organiza código relacionado.
#
#
# PAQUETE
#
# utilidades/
#
# organiza módulos relacionados.
#
#
# IMPORTACIÓN:
#
# from utilidades.calculos import calcular_promedio
#
#
# se puede leer:
#
# paquete
# ↓
# módulo
# ↓
# función
#
#
# utilidades
# ↓
# calculos
# ↓
# calcular_promedio
#
#
# Ese es el conocimiento fundamental que necesitamos
# consolidar en este punto.