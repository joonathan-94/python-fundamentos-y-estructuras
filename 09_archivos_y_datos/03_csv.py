# ============================================================
# ARCHIVOS CSV EN PYTHON
# ============================================================
#
# CSV significa:
#
# Comma-Separated Values
#
# Es un formato de texto utilizado para representar
# información tabular.
#
# Ejemplo:
#
# nombre,area,anio
# Albert Einstein,Física,1879
# Stephen Hawking,Cosmología,1942
# Carl Sagan,Astronomía,1934
#
#
# Podemos imaginarlo como una tabla:
#
# nombre             area          anio
# ------------------------------------------------
# Albert Einstein    Física        1879
# Stephen Hawking    Cosmología    1942
# Carl Sagan         Astronomía    1934
#
#
# CSV es muy utilizado en:
#
# - exportaciones;
# - importaciones;
# - sistemas ERP;
# - sistemas WMS;
# - reportes;
# - automatizaciones;
# - procesamiento de datos;
# - análisis de datos.
#
#
# Python incluye el módulo:
#
# csv
#
# dentro de su biblioteca estándar.


import csv


# ------------------------------------------------------------
# 1. RUTA DEL ARCHIVO
# ------------------------------------------------------------

ruta_mediciones = (
    "09_archivos_y_datos/datos/mediciones.csv"
)


# Igual que en los ejemplos anteriores, utilizamos
# una ruta relativa desde la raíz del repositorio.


# ------------------------------------------------------------
# 2. ESCRIBIR UN CSV CON csv.writer()
# ------------------------------------------------------------

# Primero vamos a crear información tabular.
#
# Cada lista representa una FILA.


encabezado = [
    "cientifico",
    "area",
    "anio_nacimiento"
]


fila_einstein = [
    "Albert Einstein",
    "Física",
    1879
]


fila_hawking = [
    "Stephen Hawking",
    "Cosmología",
    1942
]


fila_sagan = [
    "Carl Sagan",
    "Astronomía",
    1934
]


# Abrimos el archivo en modo escritura.


with open(
    ruta_mediciones,
    "w",
    encoding="utf-8",
    newline=""
) as archivo:

    escritor = csv.writer(archivo)

    escritor.writerow(encabezado)
    escritor.writerow(fila_einstein)
    escritor.writerow(fila_hawking)
    escritor.writerow(fila_sagan)


# El archivo generado tendrá aproximadamente:
#
# cientifico,area,anio_nacimiento
# Albert Einstein,Física,1879
# Stephen Hawking,Cosmología,1942
# Carl Sagan,Astronomía,1934


# ------------------------------------------------------------
# 3. writerow()
# ------------------------------------------------------------

# writerow()
#
# escribe UNA fila.
#
#
# Ejemplo:
#
# escritor.writerow(
#     ["Galileo Galilei", "Astronomía", 1564]
# )


# ------------------------------------------------------------
# 4. writerows()
# ------------------------------------------------------------

# Si tenemos varias filas dentro de una lista,
# podemos utilizar:
#
# writerows()


cientificos_adicionales = [
    [
        "Werner Heisenberg",
        "Física",
        1901
    ],
    [
        "Nikola Tesla",
        "Ingeniería eléctrica",
        1856
    ],
    [
        "Galileo Galilei",
        "Astronomía",
        1564
    ],
    [
        "Alan Turing",
        "Computación",
        1912
    ]
]


# Agregaremos estas filas utilizando modo "a".


with open(
    ruta_mediciones,
    "a",
    encoding="utf-8",
    newline=""
) as archivo:

    escritor = csv.writer(archivo)

    escritor.writerows(
        cientificos_adicionales
    )


# ------------------------------------------------------------
# 5. ¿POR QUÉ newline=""?
# ------------------------------------------------------------

# Cuando utilizamos el módulo csv es recomendable abrir
# el archivo utilizando:
#
# newline=""
#
# para permitir que el módulo csv controle correctamente
# los saltos de línea.
#
#
# Para nuestros ejemplos utilizaremos normalmente:
#
# encoding="utf-8"
# newline=""


# ------------------------------------------------------------
# 6. LEER UN CSV CON csv.reader()
# ------------------------------------------------------------

# Ahora podemos leer el archivo.


with open(
    ruta_mediciones,
    "r",
    encoding="utf-8",
    newline=""
) as archivo:

    lector = csv.reader(archivo)

    for fila in lector:
        print(fila)


# Cada fila se obtiene como una lista.
#
#
# Ejemplo:
#
# [
#     "Albert Einstein",
#     "Física",
#     "1879"
# ]


# ------------------------------------------------------------
# 7. LOS DATOS LEÍDOS SON STRINGS
# ------------------------------------------------------------

# Este detalle es importante.
#
# Aunque en el CSV tengamos:
#
# 1879
#
# al leerlo obtendremos:
#
# "1879"
#
#
# Si necesitamos utilizarlo matemáticamente,
# debemos convertirlo.


with open(
    ruta_mediciones,
    "r",
    encoding="utf-8",
    newline=""
) as archivo:

    lector = csv.reader(archivo)

    encabezado_leido = next(lector)

    print("Encabezado:")
    print(encabezado_leido)

    for fila in lector:

        nombre = fila[0]
        area = fila[1]
        anio = int(fila[2])

        print(nombre)
        print(area)
        print(anio)
        print(type(anio))


# Aquí reutilizamos:
#
# listas
# índices
# int()
# for


# ------------------------------------------------------------
# 8. next()
# ------------------------------------------------------------

# En el ejemplo anterior utilizamos:
#
# next(lector)
#
# para obtener la primera fila.
#
# En nuestro CSV esa primera fila corresponde
# al encabezado:
#
# cientifico,area,anio_nacimiento
#
#
# Luego el for continúa desde la fila siguiente.


# ------------------------------------------------------------
# 9. csv.DictReader
# ------------------------------------------------------------

# csv.reader() entrega cada fila como una lista.
#
# También podemos utilizar:
#
# csv.DictReader
#
# para obtener cada fila como un diccionario.
#
#
# Esto conecta directamente con los diccionarios
# que ya estudiamos.


with open(
    ruta_mediciones,
    "r",
    encoding="utf-8",
    newline=""
) as archivo:

    lector_diccionarios = csv.DictReader(
        archivo
    )

    for registro in lector_diccionarios:

        print(registro)


# Una fila se verá conceptualmente así:
#
# {
#     "cientifico": "Albert Einstein",
#     "area": "Física",
#     "anio_nacimiento": "1879"
# }


# ------------------------------------------------------------
# 10. ACCEDER POR CLAVE
# ------------------------------------------------------------

with open(
    ruta_mediciones,
    "r",
    encoding="utf-8",
    newline=""
) as archivo:

    lector = csv.DictReader(archivo)

    for cientifico in lector:

        nombre = cientifico["cientifico"]
        area = cientifico["area"]

        print(
            f"{nombre} - {area}"
        )


# En lugar de:
#
# fila[0]
# fila[1]
#
# podemos utilizar:
#
# registro["cientifico"]
# registro["area"]
#
#
# Esto suele hacer el código más descriptivo.


# ------------------------------------------------------------
# 11. CONVERTIR DATOS
# ------------------------------------------------------------

# DictReader también devuelve strings.
#
# Por eso:
#
# cientifico["anio_nacimiento"]
#
# contiene algo como:
#
# "1942"
#
# y no:
#
# 1942


with open(
    ruta_mediciones,
    "r",
    encoding="utf-8",
    newline=""
) as archivo:

    lector = csv.DictReader(archivo)

    for cientifico in lector:

        nombre = cientifico["cientifico"]

        anio_nacimiento = int(
            cientifico["anio_nacimiento"]
        )

        print(
            f"{nombre}: {anio_nacimiento}"
        )


# ------------------------------------------------------------
# 12. PROCESAR INFORMACIÓN DEL CSV
# ------------------------------------------------------------

# Podemos realizar cálculos con los datos.


with open(
    ruta_mediciones,
    "r",
    encoding="utf-8",
    newline=""
) as archivo:

    lector = csv.DictReader(archivo)

    for cientifico in lector:

        nombre = cientifico["cientifico"]

        anio_nacimiento = int(
            cientifico["anio_nacimiento"]
        )

        antiguedad_historica = (
            2026 - anio_nacimiento
        )

        print(
            f"{nombre}: {antiguedad_historica} años "
            f"desde su nacimiento"
        )


# Este ejemplo demuestra un flujo muy común:
#
# CSV
# ↓
# leer
# ↓
# convertir datos
# ↓
# procesar
# ↓
# generar información


# ------------------------------------------------------------
# 13. FILTRAR DATOS
# ------------------------------------------------------------

# También podemos combinar CSV con condicionales.


with open(
    ruta_mediciones,
    "r",
    encoding="utf-8",
    newline=""
) as archivo:

    lector = csv.DictReader(archivo)

    for cientifico in lector:

        if cientifico["area"] == "Astronomía":

            print(
                "Astrónomo encontrado:",
                cientifico["cientifico"]
            )


# Aquí combinamos:
#
# archivo
# CSV
# diccionario
# for
# if


# ------------------------------------------------------------
# 14. csv.DictWriter
# ------------------------------------------------------------

# También podemos escribir diccionarios utilizando:
#
# csv.DictWriter
#
#
# Primero indicamos qué columnas tendrá el archivo.


ruta_aportes = (
    "09_archivos_y_datos/datos/"
    "aportes_cientificos.csv"
)


columnas = [
    "nombre",
    "campo",
    "aporte"
]


registros = [
    {
        "nombre": "Alan Turing",
        "campo": "Computación",
        "aporte": "Fundamentos de la computación"
    },
    {
        "nombre": "Ada Lovelace",
        "campo": "Computación",
        "aporte": "Algoritmos para la máquina analítica"
    },
    {
        "nombre": "Grace Hopper",
        "campo": "Computación",
        "aporte": "Desarrollo de compiladores"
    }
]


with open(
    ruta_aportes,
    "w",
    encoding="utf-8",
    newline=""
) as archivo:

    escritor = csv.DictWriter(
        archivo,
        fieldnames=columnas
    )

    escritor.writeheader()

    escritor.writerows(
        registros
    )


# ------------------------------------------------------------
# 15. writeheader()
# ------------------------------------------------------------

# writeheader()
#
# escribe los nombres de las columnas.
#
#
# En nuestro ejemplo:
#
# nombre,campo,aporte


# ------------------------------------------------------------
# 16. DictWriter + DICCIONARIOS
# ------------------------------------------------------------

# Esta combinación resulta muy natural:
#
# lista
# ↓
# diccionarios
# ↓
# DictWriter
# ↓
# archivo CSV


# ------------------------------------------------------------
# 17. LEER EL CSV QUE ACABAMOS DE CREAR
# ------------------------------------------------------------

with open(
    ruta_aportes,
    "r",
    encoding="utf-8",
    newline=""
) as archivo:

    lector = csv.DictReader(archivo)

    for aporte in lector:

        print(
            aporte["nombre"],
            "-",
            aporte["aporte"]
        )


# ------------------------------------------------------------
# 18. CSV Y DATOS TABULARES
# ------------------------------------------------------------

# CSV funciona especialmente bien cuando los registros
# comparten las mismas columnas.
#
#
# Por ejemplo:
#
# id,nombre,estado
# 1,Albert Einstein,Activo
# 2,Stephen Hawking,Activo
# 3,Alan Turing,Activo
#
#
# Cada fila representa un registro.
#
# Cada columna representa un atributo.


# ------------------------------------------------------------
# 19. CSV VS JSON
# ------------------------------------------------------------

# CSV:
#
# datos tabulares
# filas y columnas
#
#
# JSON:
#
# estructuras más flexibles
# listas
# objetos
# datos anidados
#
#
# Ejemplo CSV:
#
# nombre,area,anio
# Carl Sagan,Astronomía,1934
#
#
# Ejemplo JSON:
#
# {
#     "nombre": "Carl Sagan",
#     "area": "Astronomía",
#     "anio": 1934
# }


# ------------------------------------------------------------
# 20. CSV NO ES EXCEL
# ------------------------------------------------------------

# Un archivo:
#
# .csv
#
# NO es lo mismo que:
#
# .xlsx
#
#
# Excel puede abrir archivos CSV,
# pero CSV es simplemente un formato de texto tabular.
#
#
# No contiene directamente:
#
# - fórmulas complejas;
# - múltiples hojas;
# - gráficos;
# - estilos;
# - colores.
#
#
# Para archivos Excel reales necesitaremos posteriormente
# otras herramientas.


# ------------------------------------------------------------
# 21. EJEMPLO DE INTEGRACIÓN
# ------------------------------------------------------------

# Muchos sistemas permiten exportar información como CSV.
#
# Por ejemplo:
#
# ERP
# ↓
# ordenes.csv
# ↓
# Python
# ↓
# procesa / valida / transforma
# ↓
# otro sistema
#
#
# Este patrón es común en integraciones empresariales.


# ------------------------------------------------------------
# 22. EJEMPLO DE ANÁLISIS DE DATOS
# ------------------------------------------------------------

# También podemos recibir:
#
# mediciones.csv
#
# temperatura,humedad
# 22.5,50
# 23.1,52
# 21.8,48
#
#
# Python podría:
#
# leer
# ↓
# convertir a números
# ↓
# calcular promedios
# ↓
# detectar valores
# ↓
# generar resultados
#
#
# Más adelante herramientas especializadas pueden facilitar
# este trabajo, pero el principio básico será el mismo.


# ------------------------------------------------------------
# 23. RICK SANCHEZ COMO DATO FICTICIO
# ------------------------------------------------------------

# Rick Sanchez es un personaje ficticio.
#
# Si apareciera en un CSV de ejemplo:
#
# nombre,tipo
# Rick Sanchez,Personaje ficticio
#
# seguiría siendo simplemente información textual para
# nuestro programa.


# ------------------------------------------------------------
# 24. MANEJO DE ARCHIVO INEXISTENTE
# ------------------------------------------------------------

ruta_inexistente = (
    "09_archivos_y_datos/datos/"
    "datos_inexistentes.csv"
)


try:

    with open(
        ruta_inexistente,
        "r",
        encoding="utf-8",
        newline=""
    ) as archivo:

        lector = csv.reader(archivo)

        for fila in lector:
            print(fila)

except FileNotFoundError:
    print("El archivo CSV no existe.")


# Nuevamente conectamos:
#
# archivos
# +
# módulos
# +
# excepciones


# ------------------------------------------------------------
# 25. QUÉ UTILIZAREMOS MÁS
# ------------------------------------------------------------

# Para comenzar:
#
# csv.reader()
# → filas como listas.
#
#
# csv.writer()
# → escribir filas desde listas.
#
#
# csv.DictReader()
# → filas como diccionarios.
#
#
# csv.DictWriter()
# → escribir utilizando diccionarios.
#
#
# Personalmente, cuando existen encabezados claros,
# DictReader y DictWriter suelen resultar especialmente
# cómodos porque podemos trabajar con nombres de columnas.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# CSV
#
# representa información tabular:
#
# filas
# +
# columnas
#
#
# LEER COMO LISTAS:
#
# lector = csv.reader(archivo)
#
#
# ESCRIBIR LISTAS:
#
# escritor = csv.writer(archivo)
#
#
# LEER COMO DICCIONARIOS:
#
# lector = csv.DictReader(archivo)
#
#
# ESCRIBIR DICCIONARIOS:
#
# escritor = csv.DictWriter(
#     archivo,
#     fieldnames=columnas
# )
#
#
# Al leer CSV:
#
# los valores llegan inicialmente como strings.
#
# Si necesitamos números:
#
# int(...)
# float(...)
#
#
# FLUJO COMÚN:
#
# archivo CSV
# ↓
# lectura
# ↓
# listas o diccionarios
# ↓
# conversión
# ↓
# procesamiento
# ↓
# resultado
#
#
# CSV será especialmente útil posteriormente para:
#
# automatización
# integraciones
# importaciones
# exportaciones
# procesamiento de datos
# análisis de datos