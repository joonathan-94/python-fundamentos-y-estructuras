# ============================================================
# EJERCICIOS - ARCHIVOS Y DATOS
# ============================================================
#
# Objetivo:
#
# Practicar los conceptos esenciales del bloque:
#
# - escribir archivos;
# - leer archivos;
# - utilizar JSON;
# - trabajar nuevamente con estructuras Python.
#
# Los ejercicios son deliberadamente básicos.


# ------------------------------------------------------------
# ARCH-01 - GUARDAR Y LEER UN ARCHIVO DE TEXTO
# ------------------------------------------------------------
#
# Crea una variable:
#
# ruta_archivo
#
# con esta ruta:
#
# "09_archivos_y_datos/datos/ejercicio_cientificos.txt"
#
#
# Luego:
#
# 1. Abre el archivo en modo escritura "w".
#
# 2. Utiliza:
#
#    encoding="utf-8"
#
# 3. Escribe estas tres líneas:
#
# Albert Einstein
# Stephen Hawking
# Nikola Tesla
#
# Recuerda utilizar:
#
# \n
#
# para los saltos de línea.
#
#
# 4. Cierra el bloque de escritura.
#
# 5. Abre nuevamente el mismo archivo,
#    esta vez utilizando "r".
#
# 6. Lee todo el contenido utilizando:
#
#    read()
#
# 7. Guarda el resultado en:
#
#    contenido_archivo
#
# 8. Imprime el contenido.
#
#
# El resultado debería mostrar:
#
# Albert Einstein
# Stephen Hawking
# Nikola Tesla
#
#
# Tu código aquí:

ruta_archivo = "09_archivos_y_datos/datos/ejercicio_cientificos.txt"

with open(
    ruta_archivo,
    "w",
    encoding="utf-8"
) as nuevo_archivo:
    nuevo_archivo.write("Albert Einstein\n")
    nuevo_archivo.write("Stephen Hawking\n")
    nuevo_archivo.write("Nikola Tesla\n")


with open(
    ruta_archivo,
    "r",
    encoding="utf-8"
) as archivo:
    contenido_archivo = archivo.read()

print("Contenido de archivo de texto:")
print(contenido_archivo)


# ------------------------------------------------------------
# ARCH-02 - GUARDAR Y LEER JSON
# ------------------------------------------------------------
#
# Primero importa:
#
# json
#
#
# Crea este diccionario:
#
# cientifico = {
#     "nombre": "Alan Turing",
#     "area": "Computación",
#     "anio_nacimiento": 1912
# }
#
#
# Crea la ruta:
#
# ruta_json =
# "09_archivos_y_datos/datos/ejercicio_cientifico.json"
#
#
# Luego:
#
# 1. Abre el archivo utilizando "w".
#
# 2. Guarda el diccionario utilizando:
#
#    json.dump()
#
# Utiliza:
#
#    indent=4
#    ensure_ascii=False
#
#
# 3. Después abre nuevamente el archivo
#    utilizando "r".
#
# 4. Recupera los datos utilizando:
#
#    json.load()
#
# 5. Guarda el resultado en:
#
#    cientifico_cargado
#
# 6. Imprime:
#
#    cientifico_cargado["nombre"]
#
#    cientifico_cargado["area"]
#
#
# Resultado esperado:
#
# Alan Turing
# Computación
#
#
# Tu código aquí:

import json


cientifico = {
    "nombre": "Alan Turing",
    "area": "Computación",
    "anio_nacimiento": 1912
}

ruta_json = (
    "09_archivos_y_datos/datos/"
    "ejercicio_cientifico.json"
)


with open(
    ruta_json,
    "w",
    encoding="utf-8"
) as archivo:
    json.dump(
        cientifico,
        archivo,
        indent=4,
        ensure_ascii=False
    )


with open(
    ruta_json,
    "r",
    encoding="utf-8"
) as archivo:
    cientifico_cargado = json.load(archivo)


print(cientifico_cargado["nombre"])
print(cientifico_cargado["area"])