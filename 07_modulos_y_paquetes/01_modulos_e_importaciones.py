# ============================================================
# MÓDULOS E IMPORTACIONES EN PYTHON
# ============================================================
#
# A medida que un programa crece, resulta poco práctico
# mantener todo el código dentro de un solo archivo.
#
# Python permite dividir el código en distintos archivos.
#
# Un archivo .py puede actuar como un módulo.
#
# Ejemplo:
#
# operaciones.py
#
# puede contener:
#
# funciones
# variables
# clases
# constantes
#
# y luego otro archivo puede importar ese contenido.
#
#
# IDEA GENERAL:
#
# archivo_a.py
#     ↓
# contiene código reutilizable
#
# archivo_b.py
#     ↓
# importa y utiliza ese código


# ------------------------------------------------------------
# 1. QUÉ ES UN MÓDULO
# ------------------------------------------------------------

# Un módulo es, de forma sencilla, un archivo de Python.
#
# Ejemplos:
#
# math
# random
# datetime
#
# son módulos disponibles en Python.
#
# También podemos crear nuestros propios módulos:
#
# operaciones.py
# validaciones.py
# reportes.py
#
#
# Esto permite organizar mejor un programa.


# ------------------------------------------------------------
# 2. import
# ------------------------------------------------------------

# Para utilizar un módulo podemos usar:
#
# import nombre_modulo
#
#
# Ejemplo:

import math


# math es un módulo de la biblioteca estándar de Python.


# ------------------------------------------------------------
# 3. UTILIZAR ALGO DEL MÓDULO
# ------------------------------------------------------------

# Después de importar un módulo, podemos acceder a sus
# elementos utilizando:
#
# nombre_modulo.elemento


raiz_cuadrada = math.sqrt(81)

print(raiz_cuadrada)


# Resultado:
#
# 9.0
#
#
# Aquí:
#
# math
# → módulo
#
# sqrt
# → función perteneciente al módulo math


# ------------------------------------------------------------
# 4. POR QUÉ SE UTILIZA modulo.funcion()
# ------------------------------------------------------------

# Cuando hacemos:
#
# import math
#
# Python agrega el nombre:
#
# math
#
# al espacio de nombres actual.
#
# Las funciones del módulo continúan perteneciendo a math.
#
# Por eso escribimos:
#
# math.sqrt()
#
# math.floor()
#
# math.ceil()


numero_decimal = 7.8

redondeo_inferior = math.floor(numero_decimal)
redondeo_superior = math.ceil(numero_decimal)

print(redondeo_inferior)
print(redondeo_superior)


# Esto tiene una ventaja:
#
# cuando vemos:
#
# math.sqrt()
#
# sabemos inmediatamente de dónde viene sqrt().


# ------------------------------------------------------------
# 5. IMPORTAR ELEMENTOS ESPECÍFICOS
# ------------------------------------------------------------

# También podemos importar directamente una función:
#
# from modulo import elemento


from math import sqrt


resultado_raiz = sqrt(144)

print(resultado_raiz)


# Ahora podemos utilizar:
#
# sqrt()
#
# directamente.
#
# Ya no necesitamos escribir:
#
# math.sqrt()


# ------------------------------------------------------------
# 6. import modulo VS from modulo import elemento
# ------------------------------------------------------------

# FORMA 1:

import math

resultado_uno = math.sqrt(64)

print(resultado_uno)


# FORMA 2:

from math import sqrt

resultado_dos = sqrt(64)

print(resultado_dos)


# Ambas son válidas.
#
# La diferencia principal es cómo quedan disponibles
# los nombres en nuestro archivo.
#
#
# import math
#
# → agrega el nombre math.
#
#
# from math import sqrt
#
# → agrega directamente el nombre sqrt.


# ------------------------------------------------------------
# 7. IMPORTAR VARIOS ELEMENTOS
# ------------------------------------------------------------

from math import floor, ceil


valor_prueba = 15.7

valor_floor = floor(valor_prueba)
valor_ceil = ceil(valor_prueba)

print(valor_floor)
print(valor_ceil)


# Podemos importar varios elementos del mismo módulo.


# ------------------------------------------------------------
# 8. ALIAS CON as
# ------------------------------------------------------------

# Python permite asignar un nombre alternativo a un módulo.

import math as matematica


resultado_alias = matematica.sqrt(225)

print(resultado_alias)


# Aquí:
#
# math
#
# fue importado con el nombre:
#
# matematica
#
#
# Esto se denomina alias.


# ------------------------------------------------------------
# 9. ALIAS EN ELEMENTOS ESPECÍFICOS
# ------------------------------------------------------------

from math import sqrt as raiz


resultado_raiz_alias = raiz(169)

print(resultado_raiz_alias)


# En este caso:
#
# sqrt
#
# se encuentra disponible con el nombre:
#
# raiz


# ------------------------------------------------------------
# 10. CUÁNDO TIENE SENTIDO USAR UN ALIAS
# ------------------------------------------------------------

# Los alias pueden utilizarse cuando:
#
# - el nombre original es largo;
# - existe una convención conocida;
# - necesitamos evitar un conflicto de nombres;
# - mejora realmente la lectura.
#
#
# No conviene crear alias innecesarios o confusos.
#
# Por ejemplo:
#
# import math as x
#
# funciona, pero "x" no explica qué representa.


# ------------------------------------------------------------
# 11. EJEMPLO CON random
# ------------------------------------------------------------

import random


numero_aleatorio = random.randint(1, 10)

print(numero_aleatorio)


# randint(1, 10)
#
# devuelve un entero aleatorio entre 1 y 10,
# incluyendo ambos extremos.
#
#
# De nuevo:
#
# random
# → módulo
#
# randint
# → función del módulo


# ------------------------------------------------------------
# 12. EJEMPLO PRÁCTICO CON UNA LISTA
# ------------------------------------------------------------

pokemones_disponibles = [
    "Bulbasaur",
    "Charmander",
    "Squirtle"
]


pokemon_seleccionado = random.choice(
    pokemones_disponibles
)

print(pokemon_seleccionado)


# random.choice()
#
# selecciona un elemento de una secuencia.


# ------------------------------------------------------------
# 13. EJEMPLO CON datetime
# ------------------------------------------------------------

# Algunos módulos contienen clases.
#
# Podemos importar directamente una de ellas.

from datetime import date


fecha_actual = date.today()

print(fecha_actual)


# Aquí:
#
# datetime
# → módulo
#
# date
# → clase disponible dentro del módulo
#
# today()
# → método de la clase date
#
#
# No necesitas profundizar todavía en clases.
# Las veremos posteriormente en POO.


# ------------------------------------------------------------
# 14. IMPORTACIONES AL COMIENZO DEL ARCHIVO
# ------------------------------------------------------------

# Normalmente los imports se colocan al comienzo del archivo.
#
# Ejemplo:
#
# import math
# import random
# from datetime import date
#
#
# Esto permite que al abrir el archivo podamos identificar
# rápidamente qué dependencias utiliza.


# ------------------------------------------------------------
# 15. EVITAR from modulo import *
# ------------------------------------------------------------

# Python permite técnicamente hacer:
#
# from math import *
#
# pero evitaremos esta práctica.


# ¿Por qué?
#
# Porque introduce muchos nombres directamente en nuestro
# espacio de nombres.
#
# Después podría ser difícil saber:
#
# - de dónde viene una función;
# - qué nombres fueron importados;
# - si existe un conflicto con otro nombre.


# Preferimos:

# import math

# o:

# from math import sqrt


# porque son opciones explícitas.


# ------------------------------------------------------------
# 16. CONFLICTOS DE NOMBRES
# ------------------------------------------------------------

# Supongamos que importamos:

from math import floor


# y luego definimos algo con el mismo nombre:

# floor = "otro valor"
#
# En ese caso estaríamos reemplazando el nombre importado
# dentro de nuestro espacio de nombres actual.
#
# Por eso debemos usar nombres claros y evitar colisiones.


resultado_floor = floor(9.9)

print(resultado_floor)


# ------------------------------------------------------------
# 17. UN MÓDULO TIENE SU PROPIO ESPACIO DE NOMBRES
# ------------------------------------------------------------

# Cuando utilizamos:
#
# import math
#
# las funciones y nombres del módulo viven dentro
# del espacio de nombres de math.
#
# Por ejemplo:
#
# math.sqrt
# math.floor
# math.ceil
#
#
# Esto ayuda a organizar el código y evitar conflictos.


# ------------------------------------------------------------
# 18. UN MÓDULO PUEDE CONTENER MÁS QUE FUNCIONES
# ------------------------------------------------------------

# Un módulo puede contener:
#
# - funciones;
# - variables;
# - constantes;
# - clases;
# - código ejecutable.
#
#
# En nuestros primeros ejemplos utilizaremos principalmente
# funciones porque es lo que acabamos de estudiar.


# ------------------------------------------------------------
# 19. EJEMPLO CON UNA CONSTANTE DEL MÓDULO math
# ------------------------------------------------------------

valor_pi = math.pi

print(valor_pi)


# pi es un valor disponible dentro del módulo math.
#
# No todo lo que importamos tiene que ser una función.


# ------------------------------------------------------------
# 20. EJEMPLO PRÁCTICO: CÁLCULO GEOMÉTRICO
# ------------------------------------------------------------

radio_circulo = 5

area_circulo = (
    math.pi
    * radio_circulo ** 2
)

print(area_circulo)


# Aquí utilizamos:
#
# módulo
# constante
# operadores
# variables
#
# en conjunto.


# ------------------------------------------------------------
# 21. MODULOS DE LA BIBLIOTECA ESTÁNDAR
# ------------------------------------------------------------

# Python incluye una gran cantidad de módulos disponibles
# sin necesidad de instalarlos manualmente.
#
# Algunos ejemplos:
#
# math
# random
# datetime
# pathlib
# statistics
# json
# csv
#
#
# Esto forma parte de la biblioteca estándar de Python.
#
# No significa que debamos memorizar todos los módulos.
#
# Lo importante es saber:
#
# "Python probablemente ya tiene herramientas para resolver
# muchas tareas comunes".


# ------------------------------------------------------------
# 22. EJEMPLO CON statistics
# ------------------------------------------------------------

import statistics


tiempos_respuesta = [
    12.5,
    15.0,
    9.8,
    14.2
]


promedio_respuesta = statistics.mean(
    tiempos_respuesta
)

print(promedio_respuesta)


# Este tipo de módulo podría utilizarse posteriormente
# en procesamiento o análisis básico de datos.


# ------------------------------------------------------------
# 23. EJEMPLO CON pathlib
# ------------------------------------------------------------

from pathlib import Path


ruta_archivo = Path("datos") / "tickets.csv"

print(ruta_archivo)


# pathlib facilita trabajar con rutas de archivos.
#
# Más adelante tendrá mucho más sentido cuando estudiemos:
#
# 09_archivos_y_datos


# ------------------------------------------------------------
# 24. IMPORTAR NO SIGNIFICA COPIAR CÓDIGO MANUALMENTE
# ------------------------------------------------------------

# Cuando hacemos:
#
# import math
#
# no estamos copiando manualmente todo el contenido del módulo
# dentro de nuestro archivo.
#
# Estamos pidiendo a Python que cargue el módulo y nos permita
# acceder a sus nombres.


# ------------------------------------------------------------
# 25. LOS MÓDULOS AYUDAN A EVITAR DUPLICACIÓN
# ------------------------------------------------------------

# Imagina que tenemos una función:
#
# calcular_total()
#
# que necesitamos en:
#
# ventas.py
# reportes.py
# facturacion.py
#
#
# No queremos copiar la misma función tres veces.
#
# Podemos colocarla en:
#
# operaciones.py
#
# y luego importarla desde los demás archivos.
#
#
# Ese será exactamente el siguiente paso del módulo.


# ------------------------------------------------------------
# 26. EJEMPLO CON BACKEND
# ------------------------------------------------------------

# En un proyecto backend podríamos tener módulos como:
#
# usuarios.py
# tickets.py
# autenticacion.py
# reportes.py
#
#
# Cada archivo puede contener funciones relacionadas
# con una responsabilidad determinada.
#
# Posteriormente otros módulos pueden utilizar esas funciones.


# ------------------------------------------------------------
# 27. EJEMPLO CON AUTOMATIZACIÓN
# ------------------------------------------------------------

# También podríamos tener:
#
# archivos.py
# respaldos.py
# validaciones.py
#
#
# y reutilizar sus funciones desde un script principal.
#
#
# Esto permite construir programas más organizados.


# ------------------------------------------------------------
# 28. EJEMPLO CON PROCESAMIENTO DE DATOS
# ------------------------------------------------------------

# Un proyecto podría separarse en:
#
# carga_datos.py
# limpieza_datos.py
# calculos.py
# reportes.py
#
#
# Cada módulo tendría una responsabilidad concreta.
#
# Esta organización comienza a ser importante a medida
# que crece el código.


# ------------------------------------------------------------
# 29. ERROR CUANDO EL MÓDULO NO EXISTE
# ------------------------------------------------------------

# Si intentamos:
#
# import modulo_inexistente
#
# Python no podrá encontrarlo y producirá:
#
# ModuleNotFoundError
#
#
# Más adelante veremos con más detalle cómo Python busca
# los módulos.
#
# Por ahora basta con reconocer este error.


# ------------------------------------------------------------
# 30. QUÉ FORMA DE IMPORT USAR
# ------------------------------------------------------------

# No existe una única forma correcta para todos los casos.
#
# Podemos utilizar:
#
# import modulo
#
# cuando queremos mantener claro el origen:
#
# math.sqrt()
#
#
# Podemos utilizar:
#
# from modulo import funcion
#
# cuando necesitamos una función concreta y la llamada
# sigue siendo clara:
#
# sqrt()
#
#
# Podemos utilizar:
#
# import modulo as alias
#
# cuando existe una razón clara para utilizar un alias.


# ------------------------------------------------------------
# 31. RESUMEN VISUAL
# ------------------------------------------------------------

# FORMA 1
#
# import math
#
# math.sqrt(81)
#
#
# FORMA 2
#
# from math import sqrt
#
# sqrt(81)
#
#
# FORMA 3
#
# import math as matematica
#
# matematica.sqrt(81)
#
#
# FORMA 4
#
# from math import sqrt as raiz
#
# raiz(81)


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# MÓDULO
#
# archivo de Python que puede contener código reutilizable.
#
#
# IMPORTAR UN MÓDULO:
#
# import modulo
#
# uso:
#
# modulo.funcion()
#
#
# IMPORTAR UN ELEMENTO:
#
# from modulo import funcion
#
# uso:
#
# funcion()
#
#
# ALIAS:
#
# import modulo as alias
#
# from modulo import funcion as alias
#
#
# EVITAREMOS:
#
# from modulo import *
#
# porque hace menos explícito el origen de los nombres.
#
#
# Los módulos permiten:
#
# - dividir programas grandes;
# - organizar responsabilidades;
# - reutilizar código;
# - evitar duplicación;
# - mantener archivos más manejables.
#
#
# Nuestro siguiente paso será crear e importar
# un módulo escrito por nosotros mismos.