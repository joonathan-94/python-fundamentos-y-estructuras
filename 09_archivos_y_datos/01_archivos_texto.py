# ============================================================
# ARCHIVOS DE TEXTO EN PYTHON
# ============================================================
#
# Hasta ahora la mayoría de nuestros datos existían solamente
# mientras el programa estaba ejecutándose.
#
# Por ejemplo:
#
# cientifico = "Albert Einstein"
#
# Cuando el programa termina, esa variable desaparece.
#
#
# Los archivos permiten almacenar información fuera de la
# ejecución del programa.
#
# Esto introduce una idea importante:
#
# PERSISTENCIA
#
# programa
# ↓
# guarda información
# ↓
# archivo
# ↓
# la información continúa existiendo después de finalizar
# el programa


# ------------------------------------------------------------
# 1. open()
# ------------------------------------------------------------

# Python incorpora la función:
#
# open()
#
# que permite abrir archivos.
#
#
# Ejemplo conceptual:
#
# open("archivo.txt")
#
#
# Normalmente debemos indicar:
#
# - ruta del archivo;
# - modo de apertura;
# - codificación.


# ------------------------------------------------------------
# 2. MODOS PRINCIPALES
# ------------------------------------------------------------

# Los modos que utilizaremos inicialmente son:
#
# "r"
# → read
# → leer
#
# "w"
# → write
# → escribir
#
# "a"
# → append
# → agregar contenido al final
#
#
# Debemos tener especial cuidado con:
#
# "w"
#
# porque reemplaza el contenido anterior del archivo.


# ------------------------------------------------------------
# 3. RUTA DEL ARCHIVO
# ------------------------------------------------------------

ruta_cientificos = (
    "09_archivos_y_datos/datos/cientificos.txt"
)


# Esta es una ruta relativa.
#
# En estos ejemplos asumimos que ejecutamos Python desde
# la raíz del repositorio:
#
# python-fundamentos-y-estructuras/


# ------------------------------------------------------------
# 4. ESCRIBIR UN ARCHIVO
# ------------------------------------------------------------

# Utilizaremos:
#
# with open(...)
#
# para abrir el archivo.
#
# Al terminar el bloque "with", Python se encarga de cerrar
# correctamente el archivo.


with open(
    ruta_cientificos,
    "w",
    encoding="utf-8"
) as archivo:

    archivo.write("Albert Einstein\n")
    archivo.write("Stephen Hawking\n")
    archivo.write("Galileo Galilei\n")


# Después de ejecutar este bloque:
#
# cientificos.txt
#
# tendrá:
#
# Albert Einstein
# Stephen Hawking
# Galileo Galilei


# ------------------------------------------------------------
# 5. POR QUÉ UTILIZAMOS \n
# ------------------------------------------------------------

# \n representa un salto de línea.
#
# Por ejemplo:
#
# archivo.write("Nikola Tesla\n")
#
# permite que el siguiente texto aparezca en otra línea.


# ------------------------------------------------------------
# 6. encoding="utf-8"
# ------------------------------------------------------------

# Indicamos:
#
# encoding="utf-8"
#
# para trabajar correctamente con caracteres como:
#
# José Maza
# Física
# Astronomía
#
# y otros caracteres propios de distintos idiomas.
#
# Para nuestros archivos de texto utilizaremos normalmente
# UTF-8.


# ------------------------------------------------------------
# 7. LEER TODO EL ARCHIVO
# ------------------------------------------------------------

with open(
    ruta_cientificos,
    "r",
    encoding="utf-8"
) as archivo:

    contenido_completo = archivo.read()


print("Contenido completo:")
print(contenido_completo)


# read()
#
# lee todo el contenido disponible y devuelve un string.


print(type(contenido_completo))


# Resultado:
#
# <class 'str'>


# ------------------------------------------------------------
# 8. AGREGAR INFORMACIÓN CON "a"
# ------------------------------------------------------------

# El modo:
#
# "a"
#
# agrega contenido al final sin eliminar lo anterior.


with open(
    ruta_cientificos,
    "a",
    encoding="utf-8"
) as archivo:

    archivo.write("Nikola Tesla\n")
    archivo.write("José Maza\n")


# Ahora el archivo contiene:
#
# Albert Einstein
# Stephen Hawking
# Galileo Galilei
# Nikola Tesla
# José Maza


# ------------------------------------------------------------
# 9. DIFERENCIA ENTRE "w" Y "a"
# ------------------------------------------------------------

# "w"
#
# reemplaza el contenido.
#
#
# "a"
#
# agrega contenido al final.
#
#
# Resumen:
#
# quiero comenzar/reemplazar un archivo
# → "w"
#
# quiero conservar lo existente y agregar
# → "a"


# ------------------------------------------------------------
# 10. readline()
# ------------------------------------------------------------

# readline()
#
# lee una sola línea.


with open(
    ruta_cientificos,
    "r",
    encoding="utf-8"
) as archivo:

    primera_linea = archivo.readline()


print("Primera línea:")
print(primera_linea)


# La línea normalmente incluye:
#
# \n
#
# al final.


# Podemos limpiarla:

primera_linea_limpia = primera_linea.strip()

print(primera_linea_limpia)


# Aquí reutilizamos:
#
# strings
# strip()


# ------------------------------------------------------------
# 11. readlines()
# ------------------------------------------------------------

# readlines()
#
# devuelve todas las líneas dentro de una lista.


with open(
    ruta_cientificos,
    "r",
    encoding="utf-8"
) as archivo:

    lineas_cientificos = archivo.readlines()


print(lineas_cientificos)

print(type(lineas_cientificos))


# Conceptualmente obtenemos algo parecido a:
#
# [
#     "Albert Einstein\n",
#     "Stephen Hawking\n",
#     ...
# ]
#
#
# Es una lista de strings.


# ------------------------------------------------------------
# 12. LIMPIAR LAS LÍNEAS
# ------------------------------------------------------------

cientificos_limpios = []


for linea in lineas_cientificos:

    nombre_limpio = linea.strip()

    cientificos_limpios.append(
        nombre_limpio
    )


print(cientificos_limpios)


# Estamos combinando:
#
# archivo
# ↓
# readlines()
# ↓
# lista
# ↓
# for
# ↓
# strip()
# ↓
# nueva lista


# ------------------------------------------------------------
# 13. RECORRER DIRECTAMENTE UN ARCHIVO
# ------------------------------------------------------------

# También podemos recorrer directamente el archivo
# utilizando un for.


with open(
    ruta_cientificos,
    "r",
    encoding="utf-8"
) as archivo:

    for linea in archivo:

        nombre_cientifico = linea.strip()

        print(
            f"Científico: {nombre_cientifico}"
        )


# Para muchos casos esta forma es muy cómoda porque podemos
# procesar cada línea individualmente.


# ------------------------------------------------------------
# 14. LEER Y BUSCAR INFORMACIÓN
# ------------------------------------------------------------

cientifico_buscado = "Stephen Hawking"


with open(
    ruta_cientificos,
    "r",
    encoding="utf-8"
) as archivo:

    for linea in archivo:

        nombre_actual = linea.strip()

        if nombre_actual == cientifico_buscado:
            print(
                f"Encontrado: {nombre_actual}"
            )


# Aquí combinamos conocimientos anteriores:
#
# archivos
# strings
# for
# if


# ------------------------------------------------------------
# 15. CONTAR REGISTROS
# ------------------------------------------------------------

cantidad_cientificos = 0


with open(
    ruta_cientificos,
    "r",
    encoding="utf-8"
) as archivo:

    for linea in archivo:

        if linea.strip() != "":
            cantidad_cientificos += 1


print(
    f"Cantidad de científicos: {cantidad_cientificos}"
)


# ------------------------------------------------------------
# 16. ESCRIBIR DATOS DESDE UNA LISTA
# ------------------------------------------------------------

cientificos_destacados = [
    "Werner Heisenberg",
    "Carl Sagan",
    "Alan Turing",
    "Ada Lovelace",
    "Grace Hopper"
]


# Podríamos escribir esta información en un archivo
# recorriendo la lista.


ruta_seleccion = (
    "09_archivos_y_datos/datos/"
    "seleccion_cientificos.txt"
)


with open(
    ruta_seleccion,
    "w",
    encoding="utf-8"
) as archivo:

    for cientifico in cientificos_destacados:

        archivo.write(
            f"{cientifico}\n"
        )


# Python creará:
#
# seleccion_cientificos.txt
#
# si todavía no existe.


# ------------------------------------------------------------
# 17. LEER EL ARCHIVO GENERADO
# ------------------------------------------------------------

with open(
    ruta_seleccion,
    "r",
    encoding="utf-8"
) as archivo:

    seleccion_guardada = archivo.read()


print("Selección guardada:")
print(seleccion_guardada)


# ------------------------------------------------------------
# 18. ARCHIVO INEXISTENTE
# ------------------------------------------------------------

# Si intentamos abrir en modo lectura un archivo que no existe:
#
# open("archivo_inexistente.txt", "r")
#
# Python produce:
#
# FileNotFoundError
#
#
# Esta es una excepción.
#
# Podemos aplicar lo que acabamos de estudiar.


try:

    with open(
        "archivo_que_no_existe.txt",
        "r",
        encoding="utf-8"
    ) as archivo:

        contenido = archivo.read()

except FileNotFoundError:
    print("El archivo solicitado no existe.")


# Esto conecta directamente:
#
# manejo de archivos
# +
# manejo de excepciones


# ------------------------------------------------------------
# 19. "w" PUEDE CREAR UN ARCHIVO
# ------------------------------------------------------------

# Si abrimos:
#
# open("nuevo_archivo.txt", "w")
#
# y el archivo no existe:
#
# Python puede crearlo.
#
#
# En cambio:
#
# "r"
#
# requiere que el archivo exista.


# ------------------------------------------------------------
# 20. "a" TAMBIÉN PUEDE CREARLO
# ------------------------------------------------------------

# Si utilizamos:
#
# "a"
#
# y el archivo no existe, Python también puede crearlo.
#
# Si existe, agrega información al final.


# ------------------------------------------------------------
# 21. NO NECESITAMOS close() CON with
# ------------------------------------------------------------

# También existe la forma:
#
# archivo = open(...)
# ...
# archivo.close()
#
#
# Pero nosotros preferiremos:
#
# with open(...) as archivo:
#     ...
#
#
# porque el archivo se cierra automáticamente cuando
# abandonamos el bloque.


# ------------------------------------------------------------
# 22. EJEMPLO: REGISTRO DE OBSERVACIONES
# ------------------------------------------------------------

ruta_observaciones = (
    "09_archivos_y_datos/datos/observaciones.txt"
)


observaciones = [
    "Galileo Galilei - observaciones telescópicas",
    "Carl Sagan - divulgación científica",
    "Stephen Hawking - cosmología y agujeros negros"
]


with open(
    ruta_observaciones,
    "w",
    encoding="utf-8"
) as archivo:

    for observacion in observaciones:
        archivo.write(
            f"{observacion}\n"
        )


# Este ejemplo representa un almacenamiento muy simple.
#
# Todavía no estamos utilizando una base de datos.
#
# Simplemente persistimos información en un archivo.


# ------------------------------------------------------------
# 23. ARCHIVOS COMO FUENTE DE DATOS
# ------------------------------------------------------------

# Un programa puede:
#
# leer datos
# ↓
# procesarlos
# ↓
# producir nuevos resultados
# ↓
# escribir esos resultados
#
#
# Este patrón aparecerá en:
#
# automatizaciones
# importaciones
# exportaciones
# procesamiento de datos
# reportes
# integraciones


# ------------------------------------------------------------
# 24. EJEMPLO CON UN PERSONAJE FICTICIO
# ------------------------------------------------------------

# También podemos almacenar cualquier tipo de información
# textual.
#
# Por ejemplo:
#
# Rick Sanchez
#
# es un personaje ficticio de Rick and Morty.
#
# Lo usamos solamente como dato de ejemplo.


personaje_ficticio = "Rick Sanchez"

print(personaje_ficticio)


# ------------------------------------------------------------
# 25. QUÉ DEBEMOS RECORDAR
# ------------------------------------------------------------

# open()
# → abre un archivo.
#
#
# "r"
# → leer.
#
#
# "w"
# → escribir y reemplazar.
#
#
# "a"
# → agregar al final.
#
#
# read()
# → todo el contenido como string.
#
#
# readline()
# → una línea.
#
#
# readlines()
# → lista de líneas.
#
#
# with open(...)
# → forma recomendada para trabajar con el archivo y
#   cerrarlo correctamente.
#
#
# encoding="utf-8"
# → codificación que utilizaremos para nuestros textos.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# Hasta ahora:
#
# datos
# ↓
# variables
# ↓
# desaparecían al terminar el programa
#
#
# Ahora:
#
# programa
# ↓
# archivo
# ↓
# información persistente
#
#
# PATRÓN BÁSICO DE LECTURA:
#
# with open(
#     ruta,
#     "r",
#     encoding="utf-8"
# ) as archivo:
#     contenido = archivo.read()
#
#
# PATRÓN BÁSICO DE ESCRITURA:
#
# with open(
#     ruta,
#     "w",
#     encoding="utf-8"
# ) as archivo:
#     archivo.write("Contenido")
#
#
# PATRÓN PARA AGREGAR:
#
# with open(
#     ruta,
#     "a",
#     encoding="utf-8"
# ) as archivo:
#     archivo.write("Nuevo contenido")
#
#
# Los archivos representan nuestro primer mecanismo sencillo
# para conservar información fuera de la ejecución del
# programa.