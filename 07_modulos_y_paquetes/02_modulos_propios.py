# ============================================================
# MÓDULOS PROPIOS EN PYTHON
# ============================================================
#
# Python no solamente permite importar módulos de su
# biblioteca estándar.
#
# También podemos importar archivos .py creados por nosotros.
#
#
# Tenemos:
#
# operaciones.py
#
# con funciones como:
#
# sumar()
# calcular_total()
# normalizar_codigo()
# crear_resumen_ticket()
#
#
# Desde este archivo aprenderemos distintas formas
# de utilizarlas.


# ------------------------------------------------------------
# 1. IMPORTAR NUESTRO MÓDULO COMPLETO
# ------------------------------------------------------------

import operaciones


# Ahora operaciones representa nuestro archivo:
#
# operaciones.py
#
# Podemos acceder a sus funciones mediante:
#
# operaciones.funcion()


resultado_suma = operaciones.sumar(
    20,
    10
)

print(resultado_suma)


# ------------------------------------------------------------
# 2. UTILIZAR OTRA FUNCIÓN DEL MISMO MÓDULO
# ------------------------------------------------------------

total_compra = operaciones.calcular_total(
    cantidad=3,
    precio_unitario=15000
)

print(total_compra)


# Esta sintaxis deja muy claro de dónde viene la función:
#
# operaciones.calcular_total()
#
#          ↑
#          módulo
#
#
#                         ↑
#                         función


# ------------------------------------------------------------
# 3. IMPORTAR UNA FUNCIÓN ESPECÍFICA
# ------------------------------------------------------------

from operaciones import normalizar_codigo


codigo_normalizado = normalizar_codigo(
    "   wd-1001   "
)

print(codigo_normalizado)


# En este caso ya no necesitamos escribir:
#
# operaciones.normalizar_codigo()
#
# porque importamos directamente:
#
# normalizar_codigo


# ------------------------------------------------------------
# 4. IMPORTAR VARIAS FUNCIONES
# ------------------------------------------------------------

from operaciones import (
    calcular_total,
    crear_resumen_ticket
)


precio_servicio = calcular_total(
    4,
    12500
)

print(precio_servicio)


ticket_creado = crear_resumen_ticket(
    id_ticket="WD-2001",
    titulo_ticket="Usuario sin acceso"
)

print(ticket_creado)


# ------------------------------------------------------------
# 5. USAR ALIAS CON UN MÓDULO PROPIO
# ------------------------------------------------------------

import operaciones as ops


resultado_alias = ops.sumar(
    100,
    50
)

print(resultado_alias)


# Python permite alias exactamente igual que con módulos
# de la biblioteca estándar.
#
# operaciones
# ↓
# ops


# No significa que debamos hacerlo siempre.
#
# En este caso:
#
# import operaciones
#
# probablemente es más claro.
#
# El alias solamente sirve para demostrar que también
# podemos hacerlo con módulos propios.


# ------------------------------------------------------------
# 6. EL ARCHIVO NO SE COPIA
# ------------------------------------------------------------

# Al hacer:
#
# import operaciones
#
# no copiamos manualmente las funciones dentro de este archivo.
#
# Python carga el módulo y nos permite acceder a sus nombres.
#
#
# Esto significa que la lógica sigue definida en:
#
# operaciones.py
#
# y podemos reutilizarla desde diferentes archivos.


# ------------------------------------------------------------
# 7. POR QUÉ ESTO ES ÚTIL
# ------------------------------------------------------------

# Imagina un programa con:
#
# crear_ticket.py
# editar_ticket.py
# reportes.py
#
#
# Los tres necesitan normalizar IDs.
#
# Sería mala idea copiar esto en cada archivo:
#
# codigo.strip().upper()
#
#
# Podemos crear una sola función:
#
# normalizar_codigo()
#
# en un módulo reutilizable.


# ------------------------------------------------------------
# 8. CAMBIAR LA LÓGICA EN UN SOLO LUGAR
# ------------------------------------------------------------

# Si mañana cambia la forma en que normalizamos códigos,
# modificamos:
#
# operaciones.py
#
# y todos los archivos que utilicen esa función podrán
# beneficiarse del cambio.
#
#
# Esto reduce duplicación.


# ------------------------------------------------------------
# 9. __name__
# ------------------------------------------------------------

# Todos los módulos de Python tienen una variable especial:
#
# __name__
#
#
# En este archivo podemos observarla:

print(__name__)


# Si ejecutamos directamente:
#
# 02_modulos_propios.py
#
# normalmente veremos:
#
# __main__


# ------------------------------------------------------------
# 10. __name__ DENTRO DEL MÓDULO IMPORTADO
# ------------------------------------------------------------

print(operaciones.__name__)


# Como operaciones fue importado, veremos:
#
# operaciones


# ------------------------------------------------------------
# 11. POR QUÉ EXISTE EL PATRÓN __main__
# ------------------------------------------------------------

# En operaciones.py tenemos:
#
# if __name__ == "__main__":
#     ...
#
#
# Cuando ejecutamos operaciones.py directamente:
#
# __name__
# vale:
#
# "__main__"
#
#
# Por eso el bloque se ejecuta.


# Pero cuando hacemos:
#
# import operaciones
#
# dentro de este archivo:
#
# operaciones.__name__
#
# vale:
#
# "operaciones"
#
#
# Por eso el bloque protegido NO se ejecuta.


# ------------------------------------------------------------
# 12. EJEMPLO SIN PROTECCIÓN
# ------------------------------------------------------------

# Supongamos que operaciones.py tuviera directamente:
#
# print("Hola")
#
# sin:
#
# if __name__ == "__main__":
#
#
# Al hacer:
#
# import operaciones
#
# ese print también se ejecutaría.
#
#
# Python ejecuta las sentencias de nivel superior de un módulo
# la primera vez que lo importa durante la ejecución
# del programa.


# ------------------------------------------------------------
# 13. QUÉ DEBERÍA IR NORMALMENTE EN UN MÓDULO
# ------------------------------------------------------------

# Un módulo puede contener:
#
# - funciones;
# - clases;
# - constantes;
# - estructuras relacionadas;
#
# pero debería existir alguna relación lógica entre ellas.


# Por ejemplo:
#
# calculos.py
#
# calcular_total()
# calcular_promedio()
# calcular_impuesto()
#
#
# texto.py
#
# normalizar_codigo()
# limpiar_nombre()
# construir_slug()
#
#
# Esto comienza a separar responsabilidades.


# ------------------------------------------------------------
# 14. EJEMPLO DE ORGANIZACIÓN
# ------------------------------------------------------------

# Un proyecto podría evolucionar desde:
#
# programa.py
#
#
# hasta:
#
# programa.py
# calculos.py
# validaciones.py
# archivos.py
# reportes.py
#
#
# El archivo principal coordina las operaciones y los
# demás módulos contienen responsabilidades específicas.


# ------------------------------------------------------------
# 15. RELACIÓN CON FUNCIONES
# ------------------------------------------------------------

# En el módulo anterior aprendimos:
#
# función
# → organiza comportamiento.
#
#
# Ahora:
#
# módulo
# → organiza funciones y otros elementos relacionados.
#
#
# Podemos visualizarlo:
#
# PROGRAMA
# │
# ├── módulo
# │   ├── función
# │   ├── función
# │   └── función
# │
# └── módulo
#     ├── función
#     └── función


# ------------------------------------------------------------
# 16. EJEMPLO CON WORKDESK
# ------------------------------------------------------------

# Sin diseñar todavía la arquitectura real de WorkDesk,
# conceptualmente podríamos tener:
#
# tickets.py
# usuarios.py
# reportes.py
#
#
# tickets.py podría contener funciones relacionadas
# específicamente con tickets.
#
#
# usuarios.py podría contener funciones relacionadas
# con usuarios.
#
#
# Esto sería mucho más mantenible que colocar absolutamente
# todo dentro de:
#
# app.py


# ------------------------------------------------------------
# 17. EJEMPLO CON AUTOMATIZACIÓN
# ------------------------------------------------------------

# Podríamos tener:
#
# respaldos.py
# archivos.py
# notificaciones.py
#
#
# y luego un archivo principal:
#
# ejecutar_respaldo.py
#
# que importe las funciones necesarias.


# ------------------------------------------------------------
# 18. EJEMPLO CON DATOS
# ------------------------------------------------------------

# También:
#
# cargar_datos.py
# limpiar_datos.py
# calcular_metricas.py
#
#
# permite separar las distintas etapas de un proceso.


# ------------------------------------------------------------
# 19. EVITAR IMPORTACIONES CON *
# ------------------------------------------------------------

# Igual que con módulos estándar, evitaremos:
#
# from operaciones import *
#
#
# Preferimos:
#
# import operaciones
#
# o:
#
# from operaciones import calcular_total
#
#
# porque queda claro qué estamos utilizando.


# ------------------------------------------------------------
# 20. CUIDADO CON LOS NOMBRES DE ARCHIVOS
# ------------------------------------------------------------

# Evita crear archivos con nombres iguales a módulos
# estándar que quieras importar.
#
#
# Por ejemplo, dentro de un proyecto no sería buena idea
# crear:
#
# random.py
#
# si también quieres:
#
# import random
#
#
# porque puedes generar conflictos sobre qué archivo
# debe importar Python.


# ------------------------------------------------------------
# 21. ERROR ModuleNotFoundError
# ------------------------------------------------------------

# Si Python no encuentra un módulo:
#
# import modulo_que_no_existe
#
# producirá:
#
# ModuleNotFoundError
#
#
# En nuestros ejemplos, operaciones.py está en la misma
# carpeta que este archivo, por lo que puede importarse
# directamente.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# Nuestro archivo:
#
# operaciones.py
#
# es un módulo.
#
#
# Podemos hacer:
#
# import operaciones
#
# operaciones.sumar(10, 5)
#
#
# O:
#
# from operaciones import sumar
#
# sumar(10, 5)
#
#
# Las funciones permanecen definidas en un único archivo
# y pueden reutilizarse desde otros módulos.
#
#
# __name__
#
# identifica cómo se está utilizando el módulo.
#
#
# if __name__ == "__main__":
#
# permite ejecutar cierto código únicamente cuando el archivo
# se ejecuta directamente.
#
#
# RELACIÓN:
#
# función
# ↓
# organiza lógica
#
# módulo
# ↓
# organiza funciones y otros elementos relacionados
#
# paquete
# ↓
# organizará varios módulos relacionados
#
#
# Ese último nivel será nuestro siguiente paso.