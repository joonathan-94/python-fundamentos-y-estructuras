# ============================================================
# PATHLIB Y DATETIME
# ============================================================
#
# En este archivo estudiaremos dos herramientas
# muy utilizadas de la biblioteca estándar:
#
# pathlib
# → rutas, carpetas y archivos
#
# datetime
# → fechas, horas y diferencias de tiempo
#
#
# IDEA PRINCIPAL:
#
# Path
# → representa una ruta como un objeto.
#
#
# datetime
# → representa una fecha y hora.
#
#
# timedelta
# → representa una duración o diferencia temporal.


# ============================================================
# PATHLIB
# ============================================================


# ------------------------------------------------------------
# 1. IMPORTAR Path
# ------------------------------------------------------------

from pathlib import Path


# Path pertenece al módulo:
#
# pathlib
#
#
# Nos permite trabajar con rutas sin depender
# tanto de strings construidos manualmente.


# ------------------------------------------------------------
# 2. CREAR UNA RUTA
# ------------------------------------------------------------

ruta_simple = Path(
    "11_python_intermedio"
)


print(ruta_simple)


# Path NO significa necesariamente que el archivo
# o carpeta ya exista.
#
# Simplemente estamos creando un objeto que
# representa esa ruta.


# ------------------------------------------------------------
# 3. COMBINAR RUTAS
# ------------------------------------------------------------

ruta_archivo = (
    Path("11_python_intermedio")
    / "ejemplo_pathlib.txt"
)


print(ruta_archivo)


# El operador:
#
# /
#
# tiene aquí un significado especial.
#
# Permite unir partes de una ruta.
#
#
# Conceptualmente:
#
# carpeta
# /
# archivo
#
# ↓
#
# ruta completa


# ------------------------------------------------------------
# 4. VENTAJA FRENTE A STRINGS
# ------------------------------------------------------------

# Con strings podríamos escribir:
#
# "11_python_intermedio/ejemplo_pathlib.txt"
#
#
# Con Path:
#
# Path("11_python_intermedio")
# / "ejemplo_pathlib.txt"
#
#
# Path facilita:
#
# - construir rutas;
# - consultar archivos;
# - crear carpetas;
# - leer y escribir;
# - obtener extensiones;
# - recorrer directorios.


# ------------------------------------------------------------
# 5. RUTA DEL ARCHIVO PYTHON ACTUAL
# ------------------------------------------------------------

# Python proporciona:
#
# __file__
#
# dentro de archivos .py.
#
# Representa la ruta del archivo Python
# que se está ejecutando.


archivo_actual = Path(__file__)


print(archivo_actual)


# ------------------------------------------------------------
# 6. CARPETA DEL ARCHIVO ACTUAL
# ------------------------------------------------------------

carpeta_actual = Path(
    __file__
).parent


print(carpeta_actual)


# Esto es muy útil.
#
# En lugar de depender de:
#
# "desde qué carpeta ejecuté Python"
#
# podemos construir rutas relativas al propio
# archivo .py.


# ------------------------------------------------------------
# 7. CREAR UNA CARPETA PARA DATOS
# ------------------------------------------------------------

ruta_datos = (
    carpeta_actual
    / "datos_intermedio"
)


ruta_datos.mkdir(
    exist_ok=True
)


print(ruta_datos)


# mkdir()
#
# crea una carpeta.
#
#
# exist_ok=True
#
# significa:
#
# "si ya existe, no produzcas un error".


# ------------------------------------------------------------
# 8. parents=True
# ------------------------------------------------------------

ruta_anidada = (
    ruta_datos
    / "reportes"
    / "temporales"
)


ruta_anidada.mkdir(
    parents=True,
    exist_ok=True
)


# parents=True
#
# permite crear también las carpetas
# intermedias que no existan.


# ------------------------------------------------------------
# 9. CREAR UNA RUTA A UN ARCHIVO
# ------------------------------------------------------------

ruta_cientificos = (
    ruta_datos
    / "cientificos.txt"
)


print(ruta_cientificos)


# Todavía simplemente tenemos una ruta.
#
# Ahora podemos utilizarla para escribir.


# ------------------------------------------------------------
# 10. write_text()
# ------------------------------------------------------------

ruta_cientificos.write_text(
    (
        "Albert Einstein\n"
        "Alan Turing\n"
        "Grace Hopper\n"
    ),
    encoding="utf-8"
)


# write_text()
#
# permite escribir texto directamente.
#
#
# IMPORTANTE:
#
# reemplaza el contenido existente,
# de forma similar al modo "w" de open().


# ------------------------------------------------------------
# 11. read_text()
# ------------------------------------------------------------

contenido = ruta_cientificos.read_text(
    encoding="utf-8"
)


print(contenido)


# Para operaciones sencillas:
#
# Path.read_text()
# Path.write_text()
#
# pueden resultar muy cómodos.
#
#
# Para operaciones más específicas podemos
# seguir utilizando:
#
# with open(...)


# ------------------------------------------------------------
# 12. Path TAMBIÉN FUNCIONA CON open()
# ------------------------------------------------------------

with open(
    ruta_cientificos,
    "r",
    encoding="utf-8"
) as archivo:

    for linea in archivo:
        print(
            linea.strip()
        )


# Path puede entregarse directamente a:
#
# open()
#
# No necesitamos convertirlo manualmente a str.


# ------------------------------------------------------------
# 13. COMPROBAR SI UNA RUTA EXISTE
# ------------------------------------------------------------

print(
    ruta_cientificos.exists()
)


# exists()
#
# pregunta:
#
# ¿esta ruta existe?


# ------------------------------------------------------------
# 14. ARCHIVO O CARPETA
# ------------------------------------------------------------

print(
    ruta_cientificos.is_file()
)


print(
    ruta_datos.is_dir()
)


# is_file()
#
# → ¿es un archivo?
#
#
# is_dir()
#
# → ¿es una carpeta?


# ------------------------------------------------------------
# 15. INFORMACIÓN DE UNA RUTA
# ------------------------------------------------------------

print(
    ruta_cientificos.name
)


print(
    ruta_cientificos.stem
)


print(
    ruta_cientificos.suffix
)


print(
    ruta_cientificos.parent
)


# Para:
#
# cientificos.txt
#
#
# name
# → cientificos.txt
#
# stem
# → cientificos
#
# suffix
# → .txt
#
# parent
# → carpeta que contiene el archivo


# ------------------------------------------------------------
# 16. EJEMPLO CON EXTENSIONES
# ------------------------------------------------------------

ruta_reporte = (
    ruta_datos
    / "reporte.csv"
)


print(
    ruta_reporte.suffix
)


# Resultado:
#
# .csv


# ------------------------------------------------------------
# 17. RECORRER ARCHIVOS DE UNA CARPETA
# ------------------------------------------------------------

for elemento in ruta_datos.iterdir():

    print(
        elemento.name
    )


# iterdir()
#
# permite recorrer los elementos existentes
# dentro de una carpeta.


# ------------------------------------------------------------
# 18. BUSCAR POR PATRÓN CON glob()
# ------------------------------------------------------------

for archivo_txt in ruta_datos.glob(
    "*.txt"
):

    print(
        archivo_txt.name
    )


# "*.txt"
#
# significa:
#
# todos los elementos cuyo nombre termine en .txt
#
#
# Esto puede ser útil para:
#
# reportes
# archivos importados
# procesamiento masivo
# automatizaciones


# ------------------------------------------------------------
# 19. EJEMPLO REAL DE RUTAS
# ------------------------------------------------------------

ruta_exportaciones = (
    carpeta_actual
    / "datos_intermedio"
    / "exportaciones"
)


ruta_exportaciones.mkdir(
    parents=True,
    exist_ok=True
)


ruta_reporte_tickets = (
    ruta_exportaciones
    / "tickets.txt"
)


ruta_reporte_tickets.write_text(
    (
        "TK-001 - Nuevo\n"
        "TK-002 - En progreso\n"
        "TK-003 - Cerrado\n"
    ),
    encoding="utf-8"
)


print(
    ruta_reporte_tickets
)


# Conceptualmente:
#
# carpeta base
# ↓
# datos
# ↓
# exportaciones
# ↓
# archivo
#
#
# Cada parte puede construirse claramente
# mediante Path.


# ============================================================
# DATETIME
# ============================================================


# ------------------------------------------------------------
# 20. IMPORTAR HERRAMIENTAS
# ------------------------------------------------------------

from datetime import date
from datetime import datetime
from datetime import timedelta


# Utilizaremos:
#
# date
# → fecha
#
# datetime
# → fecha + hora
#
# timedelta
# → duración


# ------------------------------------------------------------
# 21. FECHA ACTUAL
# ------------------------------------------------------------

fecha_actual = date.today()


print(fecha_actual)


# Ejemplo:
#
# 2026-10-01
#
#
# La salida depende del día en que
# ejecutemos el programa.


# ------------------------------------------------------------
# 22. ACCEDER A PARTES DE UNA FECHA
# ------------------------------------------------------------

print(
    fecha_actual.year
)

print(
    fecha_actual.month
)

print(
    fecha_actual.day
)


# Podemos obtener:
#
# año
# mes
# día


# ------------------------------------------------------------
# 23. CREAR UNA FECHA MANUALMENTE
# ------------------------------------------------------------

fecha_nacimiento_turing = date(
    1912,
    6,
    23
)


print(
    fecha_nacimiento_turing
)


# Orden:
#
# date(
#     año,
#     mes,
#     día
# )


# ------------------------------------------------------------
# 24. FECHA Y HORA ACTUAL
# ------------------------------------------------------------

fecha_hora_actual = datetime.now()


print(
    fecha_hora_actual
)


# datetime incluye:
#
# año
# mes
# día
# hora
# minuto
# segundo
# microsegundo


# ------------------------------------------------------------
# 25. ACCEDER A SUS COMPONENTES
# ------------------------------------------------------------

print(
    fecha_hora_actual.hour
)

print(
    fecha_hora_actual.minute
)


# Igual que con date podemos acceder
# a diferentes componentes.


# ------------------------------------------------------------
# 26. CREAR UN datetime MANUALMENTE
# ------------------------------------------------------------

fecha_ticket = datetime(
    2026,
    10,
    1,
    9,
    30
)


print(
    fecha_ticket
)


# Tenemos:
#
# año
# mes
# día
# hora
# minuto


# ------------------------------------------------------------
# 27. timedelta
# ------------------------------------------------------------

# timedelta representa una cantidad
# de tiempo.


tres_dias = timedelta(
    days=3
)


print(
    tres_dias
)


# ------------------------------------------------------------
# 28. SUMAR TIEMPO
# ------------------------------------------------------------

fecha_creacion = datetime.now()


fecha_limite = (
    fecha_creacion
    + timedelta(days=3)
)


print(
    fecha_creacion
)

print(
    fecha_limite
)


# Conceptualmente:
#
# creación
# ↓
# + 3 días
# ↓
# vencimiento


# ------------------------------------------------------------
# 29. RESTAR TIEMPO
# ------------------------------------------------------------

ayer = (
    datetime.now()
    - timedelta(days=1)
)


print(ayer)


# También podemos utilizar:
#
# hours
# minutes
# seconds


# ------------------------------------------------------------
# 30. timedelta CON HORAS
# ------------------------------------------------------------

dos_horas_despues = (
    datetime.now()
    + timedelta(hours=2)
)


print(
    dos_horas_despues
)


# ------------------------------------------------------------
# 31. DIFERENCIA ENTRE DOS FECHAS
# ------------------------------------------------------------

inicio = datetime(
    2026,
    10,
    1,
    10,
    0
)


fin = datetime(
    2026,
    10,
    1,
    12,
    30
)


duracion = (
    fin
    - inicio
)


print(
    duracion
)


# Resultado:
#
# 2:30:00


# ------------------------------------------------------------
# 32. days Y total_seconds()
# ------------------------------------------------------------

print(
    duracion.days
)


print(
    duracion.total_seconds()
)


# total_seconds()
#
# devuelve la duración completa
# expresada en segundos.


# ------------------------------------------------------------
# 33. COMPARAR FECHAS
# ------------------------------------------------------------

fecha_uno = date(
    2026,
    10,
    1
)


fecha_dos = date(
    2026,
    10,
    5
)


print(
    fecha_uno < fecha_dos
)


# Resultado:
#
# True
#
#
# Las fechas pueden compararse.


# ------------------------------------------------------------
# 34. EJEMPLO DE VENCIMIENTO
# ------------------------------------------------------------

ahora = datetime.now()


vencimiento = (
    ahora
    - timedelta(hours=2)
)


if ahora > vencimiento:

    print(
        "El plazo está vencido."
    )

else:

    print(
        "El plazo sigue vigente."
    )


# Este patrón será útil posteriormente para:
#
# vencimientos
# sesiones
# tareas
# SLA
# fechas límite


# ------------------------------------------------------------
# 35. FORMATEAR UNA FECHA
# ------------------------------------------------------------

# datetime normalmente representa una fecha
# de forma técnica.
#
#
# Podemos convertirla a texto mediante:
#
# strftime()


fecha_formateada = (
    datetime.now().strftime(
        "%d-%m-%Y"
    )
)


print(
    fecha_formateada
)


# Por ejemplo:
#
# 01-10-2026


# ------------------------------------------------------------
# 36. FECHA Y HORA FORMATEADAS
# ------------------------------------------------------------

fecha_hora_formateada = (
    datetime.now().strftime(
        "%d-%m-%Y %H:%M"
    )
)


print(
    fecha_hora_formateada
)


# Algunos códigos frecuentes:
#
# %d
# → día
#
# %m
# → mes
#
# %Y
# → año con cuatro dígitos
#
# %H
# → hora 24 horas
#
# %M
# → minutos


# ------------------------------------------------------------
# 37. TEXTO A datetime
# ------------------------------------------------------------

# También podemos hacer la operación inversa.
#
# strptime()
#
# convierte un string a datetime.


fecha_texto = (
    "15-10-2026 18:30"
)


fecha_convertida = (
    datetime.strptime(
        fecha_texto,
        "%d-%m-%Y %H:%M"
    )
)


print(
    fecha_convertida
)


print(
    type(fecha_convertida)
)


# Antes:
#
# str
#
# Después:
#
# datetime


# ------------------------------------------------------------
# 38. strftime VS strptime
# ------------------------------------------------------------

# strftime:
#
# datetime
# ↓
# string
#
#
# strptime:
#
# string
# ↓
# datetime


# ------------------------------------------------------------
# 39. EJEMPLO PRÁCTICO CON TICKET
# ------------------------------------------------------------

ticket = {
    "id": "TK-1001",
    "titulo": "Servidor sin conexión",
    "creado_en": datetime.now()
}


print(
    ticket["id"]
)


print(
    ticket["creado_en"]
)


# En una aplicación real es muy habitual
# almacenar fechas asociadas a registros.


# ------------------------------------------------------------
# 40. CALCULAR UNA FECHA LÍMITE
# ------------------------------------------------------------

ticket["vence_en"] = (
    ticket["creado_en"]
    + timedelta(hours=4)
)


print(
    ticket["vence_en"]
)


# Podemos representar:
#
# creado_en
# ↓
# + 4 horas
# ↓
# vence_en


# ------------------------------------------------------------
# 41. COMPROBAR SI ESTÁ VENCIDO
# ------------------------------------------------------------

esta_vencido = (
    datetime.now()
    > ticket["vence_en"]
)


print(
    esta_vencido
)


# ------------------------------------------------------------
# 42. FORMATEAR PARA MOSTRAR AL USUARIO
# ------------------------------------------------------------

fecha_visible = (
    ticket["creado_en"].strftime(
        "%d-%m-%Y %H:%M"
    )
)


print(
    fecha_visible
)


# Internamente:
#
# datetime
#
#
# Para mostrar:
#
# string formateado
#
#
# Es importante no confundir ambas cosas.


# ------------------------------------------------------------
# 43. NO GUARDAR TODO COMO STRINGS
# ------------------------------------------------------------

# Supongamos:
#
# "01-10-2026"
#
# Es un string.
#
#
# Podemos mostrarlo fácilmente,
# pero realizar cálculos temporales será
# mucho menos práctico.
#
#
# Para cálculos:
#
# date
# datetime
#
#
# Para presentación:
#
# strftime()


# ------------------------------------------------------------
# 44. EJEMPLO CON ARCHIVO Y FECHA
# ------------------------------------------------------------

fecha_reporte = (
    datetime.now().strftime(
        "%Y-%m-%d"
    )
)


nombre_reporte = (
    f"reporte_{fecha_reporte}.txt"
)


ruta_reporte_fecha = (
    ruta_exportaciones
    / nombre_reporte
)


ruta_reporte_fecha.write_text(
    "Reporte generado correctamente.",
    encoding="utf-8"
)


print(
    ruta_reporte_fecha
)


# Resultado conceptual:
#
# reporte_2026-10-01.txt
#
#
# Aquí combinamos:
#
# datetime
# +
# strings
# +
# pathlib


# ------------------------------------------------------------
# 45. EJEMPLO REALISTA INTEGRADO
# ------------------------------------------------------------

class Ticket:

    def __init__(
        self,
        codigo,
        titulo
    ):
        self.codigo = codigo
        self.titulo = titulo
        self.creado_en = datetime.now()

    def obtener_vencimiento(
        self,
        horas
    ):

        return (
            self.creado_en
            + timedelta(hours=horas)
        )

    def obtener_fecha_formateada(self):

        return (
            self.creado_en.strftime(
                "%d-%m-%Y %H:%M"
            )
        )


ticket_servidor = Ticket(
    "TK-2001",
    "Servidor principal sin conexión"
)


print(
    ticket_servidor.codigo
)


print(
    ticket_servidor.obtener_fecha_formateada()
)


print(
    ticket_servidor.obtener_vencimiento(
        4
    )
)


# Aquí combinamos:
#
# POO
# +
# datetime
# +
# timedelta
#
#
# Esto se acerca bastante más al tipo
# de código que encontraremos posteriormente
# en aplicaciones reales.


# ------------------------------------------------------------
# 46. SOBRE ZONAS HORARIAS
# ------------------------------------------------------------

# datetime también puede manejar zonas horarias.
#
# Sin embargo, ese tema requiere decisiones adicionales
# según el tipo de aplicación.
#
#
# No profundizaremos todavía.
#
# Lo estudiaremos cuando exista una necesidad real
# en una aplicación backend.


# ------------------------------------------------------------
# 47. REGLA PRÁCTICA CON Path
# ------------------------------------------------------------

# Evitar cuando sea posible:
#
# carpeta + "/" + archivo
#
#
# Preferir:
#
# Path(carpeta) / archivo
#
#
# porque representa mejor una ruta
# y proporciona herramientas específicas
# para trabajar con ella.


# ------------------------------------------------------------
# 48. REGLA PRÁCTICA CON datetime
# ------------------------------------------------------------

# Mantener las fechas como:
#
# date
# datetime
#
# mientras necesitemos:
#
# calcular
# comparar
# sumar
# restar
#
#
# Convertirlas a string principalmente
# cuando necesitemos mostrarlas o
# generar determinados textos.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# PATHLIB
#
# Path(...)
# → representa una ruta.
#
#
# Path(...) / "archivo.txt"
# → combina rutas.
#
#
# exists()
# → comprueba existencia.
#
#
# is_file()
# → comprueba archivo.
#
#
# is_dir()
# → comprueba carpeta.
#
#
# mkdir()
# → crea carpetas.
#
#
# read_text()
# → lee texto.
#
#
# write_text()
# → escribe texto.
#
#
# glob()
# → busca rutas según un patrón.
#
#
# ------------------------------------------------------------
#
# DATETIME
#
# date
# → fecha.
#
#
# datetime
# → fecha + hora.
#
#
# timedelta
# → duración.
#
#
# datetime.now()
# → fecha y hora actuales.
#
#
# date.today()
# → fecha actual.
#
#
# fecha + timedelta(...)
# → calcular fecha futura.
#
#
# fecha - timedelta(...)
# → calcular fecha anterior.
#
#
# fecha_a - fecha_b
# → obtener duración.
#
#
# ------------------------------------------------------------
#
# strftime()
#
# datetime
# ↓
# string
#
#
# strptime()
#
# string
# ↓
# datetime
#
#
# ------------------------------------------------------------
#
# EJEMPLO REAL:
#
# ruta
# ↓
# Path
#
# archivo generado
# ↓
# reporte_2026-10-01.txt
#
#
# ticket
# ↓
# creado_en
# ↓
# datetime
#
# + timedelta
# ↓
# vencimiento
#
#
# ------------------------------------------------------------
#
# REGLA PRINCIPAL:
#
# Path
# → rutas y archivos.
#
# datetime
# → fechas y horas.
#
# timedelta
# → cálculos de tiempo.