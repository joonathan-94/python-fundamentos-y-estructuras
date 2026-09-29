# ============================================================
# PROGRAMACIÓN ORIENTADA A OBJETOS - CLASES BÁSICAS
# ============================================================
#
# Hasta ahora hemos trabajado principalmente con:
#
# variables
# funciones
# listas
# diccionarios
# módulos
# archivos
#
# La Programación Orientada a Objetos (POO) agrega otra forma
# de organizar nuestros programas.
#
#
# La idea principal es agrupar:
#
# DATOS
# +
# COMPORTAMIENTO
#
# dentro de objetos relacionados.
#
#
# Ejemplo conceptual:
#
# Científico
#
# datos:
# - nombre
# - área
# - año de nacimiento
#
# comportamientos:
# - presentarse
# - mostrar información
#
#
# En Python podemos representar este concepto mediante
# una CLASE.


# ------------------------------------------------------------
# 1. QUÉ ES UNA CLASE
# ------------------------------------------------------------

# Una clase puede entenderse inicialmente como una plantilla
# utilizada para crear objetos.
#
#
# Por ejemplo:
#
# clase Cientifico
# ↓
# permite crear
#
# Albert Einstein
# Stephen Hawking
# Nikola Tesla
#
#
# Cada uno puede almacenar información diferente, pero todos
# fueron creados utilizando la misma estructura.


# ------------------------------------------------------------
# 2. DEFINIR UNA CLASE
# ------------------------------------------------------------

class Cientifico:
    pass


# Utilizamos:
#
# class
#
# para definir una clase.
#
#
# Cientifico
#
# es el nombre de la clase.
#
#
# pass
#
# significa que por ahora el bloque no realiza ninguna acción.
#
#
# Observa también la convención del nombre:
#
# Cientifico
#
# Las clases normalmente utilizan PascalCase / CapWords.
#
# Ejemplos:
#
# Cientifico
# Ticket
# Usuario
# CuentaBancaria
# RegistroAstronomico
#
#
# En cambio, variables y funciones continúan utilizando:
#
# snake_case


# ------------------------------------------------------------
# 3. CREAR UN OBJETO
# ------------------------------------------------------------

cientifico_vacio = Cientifico()


print(cientifico_vacio)


# Acabamos de crear un OBJETO utilizando la clase Cientifico.
#
#
# Podemos expresarlo así:
#
# Cientifico
# → clase
#
# cientifico_vacio
# → objeto
#
#
# También podemos decir:
#
# cientifico_vacio
#
# es una INSTANCIA de Cientifico.
#
#
# En este contexto:
#
# objeto
# e
# instancia
#
# se utilizan prácticamente para referirse al mismo concepto.


# ------------------------------------------------------------
# 4. CLASE VS OBJETO
# ------------------------------------------------------------

# Esta diferencia es fundamental.
#
#
# CLASE:
#
# define la estructura.
#
#
# OBJETO:
#
# representa una instancia concreta de esa estructura.
#
#
# Podemos pensar:
#
# plano de una casa
# → clase
#
# casa construida
# → objeto
#
#
# O:
#
# modelo de automóvil
# → clase
#
# automóvil concreto
# → objeto


# ------------------------------------------------------------
# 5. VARIOS OBJETOS DE LA MISMA CLASE
# ------------------------------------------------------------

cientifico_uno = Cientifico()
cientifico_dos = Cientifico()
cientifico_tres = Cientifico()


print(cientifico_uno)
print(cientifico_dos)
print(cientifico_tres)


# Son objetos diferentes.
#
# Aunque todos fueron creados desde:
#
# Cientifico


# ------------------------------------------------------------
# 6. __init__()
# ------------------------------------------------------------

# Normalmente queremos que nuestros objetos tengan información
# desde el momento en que son creados.
#
# Para eso utilizamos:
#
# __init__()
#
#
# __init__ es un método especial que se ejecuta cuando
# inicializamos una nueva instancia.
#
#
# Para nuestro nivel actual puedes pensar:
#
# __init__()
# → configura los datos iniciales del objeto


class Astronomo:

    def __init__(self, nombre):
        self.nombre = nombre


# Aquí aparece uno de los conceptos más importantes de POO:
#
# self


# ------------------------------------------------------------
# 7. QUÉ ES self
# ------------------------------------------------------------

# Inicialmente piensa:
#
# self
# → el objeto concreto con el que estamos trabajando
#
#
# Cuando creamos:
#
# Astronomo("Carl Sagan")
#
# Python crea un objeto y ese objeto es representado por:
#
# self
#
# dentro de __init__.


astronomo_sagan = Astronomo(
    "Carl Sagan"
)


print(astronomo_sagan.nombre)


# Resultado:
#
# Carl Sagan


# ------------------------------------------------------------
# 8. QUÉ OCURRE EN ESTA LÍNEA
# ------------------------------------------------------------

# Tenemos:
#
# self.nombre = nombre
#
#
# El lado derecho:
#
# nombre
#
# es el parámetro recibido.
#
#
# El lado izquierdo:
#
# self.nombre
#
# es un atributo que guardamos dentro del objeto.
#
#
# Podemos visualizar:
#
# nombre
# ↓
# "Carl Sagan"
#
# self.nombre
# ↓
# atributo del objeto


# ------------------------------------------------------------
# 9. ATRIBUTOS
# ------------------------------------------------------------

# Un atributo es información asociada a un objeto.
#
#
# Podemos crear una clase con varios atributos.


class Fisico:

    def __init__(
        self,
        nombre,
        area,
        anio_nacimiento
    ):
        self.nombre = nombre
        self.area = area
        self.anio_nacimiento = anio_nacimiento


# Ahora cada objeto Fisico tendrá:
#
# nombre
# area
# anio_nacimiento


# ------------------------------------------------------------
# 10. CREAR UNA INSTANCIA CON DATOS
# ------------------------------------------------------------

fisico_einstein = Fisico(
    "Albert Einstein",
    "Física teórica",
    1879
)


print(fisico_einstein.nombre)
print(fisico_einstein.area)
print(fisico_einstein.anio_nacimiento)


# ------------------------------------------------------------
# 11. OTRO OBJETO DE LA MISMA CLASE
# ------------------------------------------------------------

fisico_hawking = Fisico(
    "Stephen Hawking",
    "Cosmología",
    1942
)


print(fisico_hawking.nombre)
print(fisico_hawking.area)
print(fisico_hawking.anio_nacimiento)


# Tenemos:
#
# fisico_einstein
#
# y:
#
# fisico_hawking
#
# Ambos son objetos de:
#
# Fisico
#
# pero mantienen valores diferentes.


# ------------------------------------------------------------
# 12. CADA INSTANCIA TIENE SUS PROPIOS DATOS
# ------------------------------------------------------------

print(
    fisico_einstein.nombre
)

print(
    fisico_hawking.nombre
)


# Resultado:
#
# Albert Einstein
# Stephen Hawking
#
#
# La clase es la misma.
#
# Los objetos son diferentes.


# ------------------------------------------------------------
# 13. VISUALIZACIÓN DEL CONCEPTO
# ------------------------------------------------------------

# CLASE:
#
# Fisico
#
# define:
#
# nombre
# area
# anio_nacimiento
#
#
# OBJETO 1:
#
# fisico_einstein
#
# nombre = Albert Einstein
# area = Física teórica
# anio_nacimiento = 1879
#
#
# OBJETO 2:
#
# fisico_hawking
#
# nombre = Stephen Hawking
# area = Cosmología
# anio_nacimiento = 1942


# ------------------------------------------------------------
# 14. ACCEDER A UN ATRIBUTO
# ------------------------------------------------------------

# Utilizamos:
#
# objeto.atributo


print(fisico_einstein.nombre)


# Podemos leer:
#
# fisico_einstein.nombre
#
# como:
#
# "obtén el atributo nombre perteneciente
# al objeto fisico_einstein"


# ------------------------------------------------------------
# 15. MODIFICAR UN ATRIBUTO
# ------------------------------------------------------------

# Por ahora nuestros atributos son accesibles directamente.


fisico_einstein.area = (
    "Física teórica y relatividad"
)


print(fisico_einstein.area)


# El objeto conserva el nuevo valor.
#
# Más adelante veremos formas de controlar mejor cómo
# se accede o modifica cierta información.


# ------------------------------------------------------------
# 16. EJEMPLO CON NIKOLA TESLA
# ------------------------------------------------------------

class Inventor:

    def __init__(
        self,
        nombre,
        especialidad
    ):
        self.nombre = nombre
        self.especialidad = especialidad


inventor_tesla = Inventor(
    "Nikola Tesla",
    "Electricidad e ingeniería"
)


print(inventor_tesla.nombre)
print(inventor_tesla.especialidad)


# ------------------------------------------------------------
# 17. EJEMPLO CON ALAN TURING
# ------------------------------------------------------------

class PioneroComputacion:

    def __init__(
        self,
        nombre,
        contribucion
    ):
        self.nombre = nombre
        self.contribucion = contribucion


turing = PioneroComputacion(
    "Alan Turing",
    "Fundamentos de la computación"
)


print(turing.nombre)
print(turing.contribucion)


# ------------------------------------------------------------
# 18. EJEMPLO CON ADA LOVELACE
# ------------------------------------------------------------

lovelace = PioneroComputacion(
    "Ada Lovelace",
    "Algoritmos para la máquina analítica"
)


print(lovelace.nombre)
print(lovelace.contribucion)


# Una misma clase puede representar múltiples objetos
# relacionados conceptualmente.


# ------------------------------------------------------------
# 19. type()
# ------------------------------------------------------------

# Ya conocemos type().
#
# También podemos utilizarlo con objetos.


print(type(fisico_einstein))


# Veremos algo similar a:
#
# <class '__main__.Fisico'>
#
#
# Esto nos indica que el objeto pertenece a la clase:
#
# Fisico


# ------------------------------------------------------------
# 20. isinstance()
# ------------------------------------------------------------

# Python también incorpora:
#
# isinstance()
#
# que permite comprobar si un objeto pertenece a
# determinada clase.


es_fisico = isinstance(
    fisico_einstein,
    Fisico
)


print(es_fisico)


# Resultado:
#
# True


es_astronomo = isinstance(
    fisico_einstein,
    Astronomo
)


print(es_astronomo)


# Resultado:
#
# False


# ------------------------------------------------------------
# 21. EJEMPLO SIMPLE CON UN TICKET
# ------------------------------------------------------------

# POO no sirve solamente para representar personas.
#
# También podemos representar conceptos de un sistema.


class Ticket:

    def __init__(
        self,
        id_ticket,
        titulo,
        estado
    ):
        self.id_ticket = id_ticket
        self.titulo = titulo
        self.estado = estado


ticket_uno = Ticket(
    "WD-1001",
    "Usuario sin acceso",
    "Nuevo"
)


print(ticket_uno.id_ticket)
print(ticket_uno.titulo)
print(ticket_uno.estado)


# Podemos visualizar:
#
# Ticket
# → clase
#
# ticket_uno
# → objeto
#
# id_ticket
# titulo
# estado
# → atributos


# ------------------------------------------------------------
# 22. CREAR VARIOS TICKETS
# ------------------------------------------------------------

ticket_dos = Ticket(
    "WD-1002",
    "Impresora sin conexión",
    "En progreso"
)


ticket_tres = Ticket(
    "WD-1003",
    "Error de sincronización",
    "Resuelto"
)


print(ticket_dos.titulo)
print(ticket_tres.titulo)


# Todos pertenecen a:
#
# Ticket
#
# pero cada objeto conserva su propia información.


# ------------------------------------------------------------
# 23. OBJETOS DENTRO DE UNA LISTA
# ------------------------------------------------------------

# Podemos combinar POO con colecciones que ya conocemos.


tickets = [
    ticket_uno,
    ticket_dos,
    ticket_tres
]


for ticket_actual in tickets:

    print(
        ticket_actual.id_ticket,
        "-",
        ticket_actual.estado
    )


# Aquí combinamos:
#
# objetos
# listas
# for
# atributos


# ------------------------------------------------------------
# 24. UNA CLASE NO ES UN DICCIONARIO
# ------------------------------------------------------------

# Antes podríamos haber representado un ticket así:


ticket_diccionario = {
    "id": "WD-2001",
    "titulo": "Problema de conexión",
    "estado": "Nuevo"
}


# Ahora también sabemos que podemos representarlo mediante
# un objeto:


ticket_objeto = Ticket(
    "WD-2001",
    "Problema de conexión",
    "Nuevo"
)


# Ambas formas pueden ser válidas dependiendo del problema.
#
# POO no significa:
#
# "dejar de utilizar diccionarios".
#
#
# Significa que ahora tenemos otra herramienta para
# organizar información y comportamiento relacionados.


# ------------------------------------------------------------
# 25. DATOS + COMPORTAMIENTO
# ------------------------------------------------------------

# Hasta ahora estamos concentrados principalmente en los DATOS:
#
# nombre
# área
# estado
# título
#
#
# Pero los objetos también pueden tener comportamiento.
#
# Ese comportamiento se implementa mediante:
#
# MÉTODOS
#
#
# Por ejemplo, un Ticket podría posteriormente:
#
# cambiar_estado()
#
# mostrar_resumen()
#
#
# Eso lo estudiaremos en:
#
# 02_atributos_y_metodos.py


# ------------------------------------------------------------
# 26. RICK SANCHEZ COMO EJEMPLO FICTICIO
# ------------------------------------------------------------

# Rick Sanchez es un personaje ficticio de Rick and Morty.


cientifico_ficticio = Fisico(
    "Rick Sanchez",
    "Ciencia ficticia",
    1943
)


print(cientifico_ficticio.nombre)


# Lo utilizamos solamente como dato de ejemplo.


# ------------------------------------------------------------
# 27. ¿POR QUÉ UTILIZAR CLASES?
# ------------------------------------------------------------

# Las clases pueden ser útiles cuando tenemos conceptos con:
#
# - datos relacionados;
# - comportamiento relacionado;
# - múltiples instancias;
# - reglas asociadas al mismo concepto.
#
#
# Ejemplos:
#
# Usuario
# Ticket
# Producto
# Cuenta
# Vehiculo
# Cientifico
#
#
# Cada uno puede tener:
#
# atributos
# +
# comportamientos


# ------------------------------------------------------------
# 28. NO TODO NECESITA SER UNA CLASE
# ------------------------------------------------------------

# Este punto es importante.
#
# POO es una herramienta.
#
# No debemos convertir automáticamente todo nuestro código
# en clases.
#
#
# Una función simple puede seguir siendo perfectamente
# apropiada:


def calcular_total(
    cantidad,
    precio
):
    return cantidad * precio


print(
    calcular_total(
        3,
        15000
    )
)


# No necesitamos crear una clase solamente porque sabemos POO.
#
# Elegiremos la herramienta según el problema.


# ------------------------------------------------------------
# 29. CLASE Y OBJETO EN UNA FRASE
# ------------------------------------------------------------

# CLASE:
#
# define cómo serán determinados objetos.
#
#
# OBJETO:
#
# instancia concreta creada a partir de esa clase.


# ------------------------------------------------------------
# 30. QUÉ DEBEMOS RECORDAR DE __init__
# ------------------------------------------------------------

# Ejemplo:
#
# class Cientifico:
#
#     def __init__(self, nombre):
#         self.nombre = nombre
#
#
# Al ejecutar:
#
# cientifico = Cientifico("Galileo Galilei")
#
#
# Python utiliza __init__ para inicializar:
#
# self.nombre
#
# con:
#
# "Galileo Galilei"


# ------------------------------------------------------------
# 31. QUÉ DEBEMOS RECORDAR DE self
# ------------------------------------------------------------

# self representa la instancia actual.
#
#
# Si tenemos:
#
# einstein = Fisico(...)
# hawking = Fisico(...)
#
#
# cada objeto mantiene sus propios:
#
# self.nombre
# self.area
# self.anio_nacimiento
#
#
# Gracias a esto una misma clase puede producir muchos
# objetos independientes.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# PROGRAMACIÓN ORIENTADA A OBJETOS
#
# organiza programas alrededor de objetos que pueden
# representar datos y comportamiento.
#
#
# CLASE:
#
# class Cientifico:
#     ...
#
# → plantilla.
#
#
# OBJETO / INSTANCIA:
#
# cientifico = Cientifico(...)
#
# → elemento concreto creado desde la clase.
#
#
# __init__:
#
# def __init__(...):
#
# → inicializa los datos de una instancia.
#
#
# self:
#
# → representa el objeto actual.
#
#
# ATRIBUTO:
#
# self.nombre
#
# → dato perteneciente a un objeto.
#
#
# ACCEDER:
#
# objeto.atributo
#
#
# MODIFICAR:
#
# objeto.atributo = nuevo_valor
#
#
# COMPROBAR TIPO:
#
# isinstance(objeto, Clase)
#
#
# RELACIÓN:
#
# clase
# ↓
# crea objetos
#
# objeto
# ↓
# mantiene su propio estado
#
#
# Próximo paso:
#
# atributos
# +
# métodos
# +
# comportamiento