# ============================================================
# ATRIBUTOS Y MÉTODOS EN PROGRAMACIÓN ORIENTADA A OBJETOS
# ============================================================
#
# Ya sabemos que una clase puede utilizarse para crear objetos.
#
# Cada objeto puede almacenar información mediante:
#
# ATRIBUTOS
#
#
# Ahora agregaremos:
#
# MÉTODOS
#
#
# Un método es una función definida dentro de una clase
# que representa comportamiento relacionado con sus objetos.
#
#
# IDEA PRINCIPAL:
#
# objeto
# =
# datos
# +
# comportamiento
#
#
# Ejemplo:
#
# Ticket
#
# datos:
# - id
# - titulo
# - estado
#
# comportamiento:
# - cambiar_estado()
# - obtener_resumen()


# ------------------------------------------------------------
# 1. RECORDATORIO: ATRIBUTOS
# ------------------------------------------------------------

class Cientifico:

    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area


cientifico_hawking = Cientifico(
    "Stephen Hawking",
    "Cosmología"
)


print(cientifico_hawking.nombre)
print(cientifico_hawking.area)


# En este objeto:
#
# nombre
# area
#
# son atributos.


# ------------------------------------------------------------
# 2. QUÉ ES UN MÉTODO
# ------------------------------------------------------------

# Un método es una función definida dentro de una clase.
#
# Normalmente recibe:
#
# self
#
# como primer parámetro.


class Astronomo:

    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        print(f"Soy {self.nombre}.")


astronomo_sagan = Astronomo(
    "Carl Sagan"
)


astronomo_sagan.presentarse()


# Aquí:
#
# presentarse()
#
# es un método.


# ------------------------------------------------------------
# 3. FUNCIÓN VS MÉTODO
# ------------------------------------------------------------

# FUNCIÓN:
#
# def calcular_total():
#     ...
#
# existe de manera independiente.
#
#
# MÉTODO:
#
# class Cientifico:
#
#     def presentarse(self):
#         ...
#
# pertenece conceptualmente a una clase.


# Ejemplo de función:

def mostrar_mensaje():
    print("Mensaje general.")


mostrar_mensaje()


# Ejemplo de método:

class Fisico:

    def mostrar_area(self):
        print("Física")


fisico = Fisico()

fisico.mostrar_area()


# ------------------------------------------------------------
# 4. LLAMAR UN MÉTODO
# ------------------------------------------------------------

# Utilizamos:
#
# objeto.metodo()


class Matematico:

    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(self.nombre)


matematico_turing = Matematico(
    "Alan Turing"
)


matematico_turing.mostrar_nombre()


# ------------------------------------------------------------
# 5. self DENTRO DE UN MÉTODO
# ------------------------------------------------------------

# self permite acceder a los datos del objeto actual.


class Investigador:

    def __init__(self, nombre, campo):
        self.nombre = nombre
        self.campo = campo

    def presentarse(self):
        print(
            f"{self.nombre} trabaja en {self.campo}."
        )


investigador_tesla = Investigador(
    "Nikola Tesla",
    "Electricidad"
)


investigador_tesla.presentarse()


# Cuando ejecutamos:
#
# investigador_tesla.presentarse()
#
# self representa:
#
# investigador_tesla


# ------------------------------------------------------------
# 6. DIFERENTES OBJETOS, MISMO MÉTODO
# ------------------------------------------------------------

investigador_einstein = Investigador(
    "Albert Einstein",
    "Física"
)


investigador_curie = Investigador(
    "Marie Curie",
    "Física y química"
)


investigador_einstein.presentarse()
investigador_curie.presentarse()


# El método es el mismo:
#
# presentarse()
#
# pero self representa un objeto diferente en cada llamada.


# ------------------------------------------------------------
# 7. MÉTODOS QUE DEVUELVEN VALORES
# ------------------------------------------------------------

# Igual que una función, un método puede utilizar return.


class CientificoDatos:

    def __init__(
        self,
        nombre,
        anio_nacimiento
    ):
        self.nombre = nombre
        self.anio_nacimiento = anio_nacimiento

    def calcular_anios_desde_nacimiento(
        self,
        anio_actual
    ):
        return (
            anio_actual
            - self.anio_nacimiento
        )


cientifico_galileo = CientificoDatos(
    "Galileo Galilei",
    1564
)


anios_transcurridos = (
    cientifico_galileo.calcular_anios_desde_nacimiento(
        2026
    )
)


print(anios_transcurridos)


# Observa:
#
# self.anio_nacimiento
#
# viene del objeto.
#
#
# anio_actual
#
# es un argumento entregado al método.


# ------------------------------------------------------------
# 8. MÉTODOS QUE RECIBEN ARGUMENTOS
# ------------------------------------------------------------

class Calculadora:

    def multiplicar(self, valor_a, valor_b):
        return valor_a * valor_b


calculadora = Calculadora()


resultado = calculadora.multiplicar(
    4,
    5
)


print(resultado)


# self NO representa uno de los números.
#
# self representa:
#
# calculadora
#
#
# valor_a y valor_b son parámetros normales del método.


# ------------------------------------------------------------
# 9. MODIFICAR ATRIBUTOS DESDE UN MÉTODO
# ------------------------------------------------------------

# Los métodos pueden modificar el estado de un objeto.


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

    def cambiar_estado(
        self,
        nuevo_estado
    ):
        self.estado = nuevo_estado


ticket_acceso = Ticket(
    "WD-1001",
    "Usuario sin acceso",
    "Nuevo"
)


print(ticket_acceso.estado)


ticket_acceso.cambiar_estado(
    "En progreso"
)


print(ticket_acceso.estado)


# Resultado:
#
# Nuevo
# En progreso


# ------------------------------------------------------------
# 10. ESTADO DEL OBJETO
# ------------------------------------------------------------

# Cuando hablamos del:
#
# estado de un objeto
#
# normalmente nos referimos a los valores que contienen
# sus atributos en un determinado momento.
#
#
# Antes:
#
# estado = "Nuevo"
#
#
# Después:
#
# estado = "En progreso"
#
#
# El mismo objeto cambió internamente.


# ------------------------------------------------------------
# 11. MÉTODOS PARA MOSTRAR INFORMACIÓN
# ------------------------------------------------------------

class AstronomoDatos:

    def __init__(
        self,
        nombre,
        especialidad
    ):
        self.nombre = nombre
        self.especialidad = especialidad

    def mostrar_resumen(self):
        print(
            f"{self.nombre} - "
            f"{self.especialidad}"
        )


astronomo_maza = AstronomoDatos(
    "José Maza",
    "Astronomía"
)


astronomo_maza.mostrar_resumen()


# ------------------------------------------------------------
# 12. MÉTODOS QUE RETORNAN INFORMACIÓN
# ------------------------------------------------------------

# Generalmente resulta más reutilizable retornar información
# en lugar de imprimirla directamente.


class AstronomoResumen:

    def __init__(
        self,
        nombre,
        especialidad
    ):
        self.nombre = nombre
        self.especialidad = especialidad

    def obtener_resumen(self):
        return (
            f"{self.nombre} - "
            f"{self.especialidad}"
        )


astronomo_kepler = AstronomoResumen(
    "Johannes Kepler",
    "Astronomía"
)


resumen_kepler = (
    astronomo_kepler.obtener_resumen()
)


print(resumen_kepler)


# Aquí aplicamos nuevamente una idea ya estudiada:
#
# print()
# → muestra información
#
# return
# → devuelve información para reutilizarla


# ------------------------------------------------------------
# 13. EJEMPLO MÁS COMPLETO CON TICKET
# ------------------------------------------------------------

class TicketSoporte:

    def __init__(
        self,
        id_ticket,
        titulo,
        prioridad,
        estado="Nuevo"
    ):
        self.id_ticket = id_ticket
        self.titulo = titulo
        self.prioridad = prioridad
        self.estado = estado

    def cambiar_estado(
        self,
        nuevo_estado
    ):
        self.estado = nuevo_estado

    def obtener_resumen(self):
        return (
            f"{self.id_ticket} | "
            f"{self.titulo} | "
            f"{self.prioridad} | "
            f"{self.estado}"
        )


ticket_servidor = TicketSoporte(
    id_ticket="WD-2001",
    titulo="Servidor sin conexión",
    prioridad="Alta"
)


print(
    ticket_servidor.obtener_resumen()
)


ticket_servidor.cambiar_estado(
    "En progreso"
)


print(
    ticket_servidor.obtener_resumen()
)


# Aquí el mismo objeto contiene:
#
# DATOS:
#
# id_ticket
# titulo
# prioridad
# estado
#
#
# COMPORTAMIENTO:
#
# cambiar_estado()
# obtener_resumen()


# ------------------------------------------------------------
# 14. EL OBJETO AGRUPA DATOS Y COMPORTAMIENTO
# ------------------------------------------------------------

# Sin POO podríamos tener:
#
# ticket = {
#     "id": "WD-2001",
#     "estado": "Nuevo"
# }
#
#
# y una función separada:
#
# def cambiar_estado(ticket, estado):
#     ...
#
#
# Con una clase podemos representar:
#
# ticket.cambiar_estado(...)
#
#
# Los datos y operaciones relacionadas quedan agrupados
# conceptualmente en el mismo objeto.


# ------------------------------------------------------------
# 15. MÉTODO QUE UTILIZA VARIOS ATRIBUTOS
# ------------------------------------------------------------

class VehiculoClasico:

    def __init__(
        self,
        modelo,
        anio,
        fabricante
    ):
        self.modelo = modelo
        self.anio = anio
        self.fabricante = fabricante

    def obtener_descripcion(self):
        return (
            f"{self.fabricante} "
            f"{self.modelo} "
            f"({self.anio})"
        )


camaro = VehiculoClasico(
    "Camaro",
    1967,
    "Chevrolet"
)


print(
    camaro.obtener_descripcion()
)


# El método utiliza varios atributos del mismo objeto.


# ------------------------------------------------------------
# 16. MÉTODO CON LÓGICA CONDICIONAL
# ------------------------------------------------------------

# Un método puede contener los mismos conceptos que una
# función normal:
#
# if
# for
# listas
# diccionarios
# excepciones
# etc.


class CientificoPremiado:

    def __init__(
        self,
        nombre,
        cantidad_premios
    ):
        self.nombre = nombre
        self.cantidad_premios = cantidad_premios

    def tiene_premios(self):

        if self.cantidad_premios > 0:
            return True

        return False


cientifico_premiado = CientificoPremiado(
    "Albert Einstein",
    1
)


print(
    cientifico_premiado.tiene_premios()
)


# ------------------------------------------------------------
# 17. MÉTODO UTILIZANDO UNA LISTA
# ------------------------------------------------------------

class InvestigadorAportes:

    def __init__(
        self,
        nombre,
        aportes
    ):
        self.nombre = nombre
        self.aportes = aportes

    def cantidad_aportes(self):
        return len(self.aportes)


investigador_hopper = InvestigadorAportes(
    "Grace Hopper",
    [
        "Compiladores",
        "COBOL",
        "Computación"
    ]
)


print(
    investigador_hopper.cantidad_aportes()
)


# Estamos combinando:
#
# POO
# listas
# len()
# return


# ------------------------------------------------------------
# 18. MÉTODO QUE MODIFICA UNA LISTA DEL OBJETO
# ------------------------------------------------------------

class InvestigadorContribuciones:

    def __init__(
        self,
        nombre
    ):
        self.nombre = nombre
        self.contribuciones = []

    def agregar_contribucion(
        self,
        contribucion
    ):
        self.contribuciones.append(
            contribucion
        )


investigador_turing = (
    InvestigadorContribuciones(
        "Alan Turing"
    )
)


investigador_turing.agregar_contribucion(
    "Máquina de Turing"
)

investigador_turing.agregar_contribucion(
    "Criptoanálisis"
)


print(
    investigador_turing.contribuciones
)


# Cada objeto puede mantener sus propias colecciones.


# ------------------------------------------------------------
# 19. DOS OBJETOS CON LISTAS INDEPENDIENTES
# ------------------------------------------------------------

investigador_lovelace = (
    InvestigadorContribuciones(
        "Ada Lovelace"
    )
)


investigador_lovelace.agregar_contribucion(
    "Algoritmo para la máquina analítica"
)


print(
    investigador_turing.contribuciones
)

print(
    investigador_lovelace.contribuciones
)


# Las listas pertenecen a objetos diferentes.


# ------------------------------------------------------------
# 20. ATRIBUTOS DE INSTANCIA
# ------------------------------------------------------------

# Los atributos que hemos creado mediante:
#
# self.nombre
# self.estado
# self.area
#
# son atributos de instancia.
#
#
# Cada objeto puede tener su propio valor.


class FisicoInstancia:

    def __init__(
        self,
        nombre
    ):
        self.nombre = nombre


fisico_newton = FisicoInstancia(
    "Isaac Newton"
)

fisico_feynman = FisicoInstancia(
    "Richard Feynman"
)


print(fisico_newton.nombre)
print(fisico_feynman.nombre)


# ------------------------------------------------------------
# 21. ATRIBUTOS DE CLASE
# ------------------------------------------------------------

# También podemos definir un atributo directamente
# dentro de la clase.


class CientificoRegistro:

    categoria = "Científico"

    def __init__(
        self,
        nombre
    ):
        self.nombre = nombre


registro_curie = CientificoRegistro(
    "Marie Curie"
)

registro_heisenberg = CientificoRegistro(
    "Werner Heisenberg"
)


print(registro_curie.categoria)
print(registro_heisenberg.categoria)


# categoria fue definida en la clase:
#
# categoria = "Científico"
#
#
# Por eso es compartida conceptualmente por las instancias.


# ------------------------------------------------------------
# 22. INSTANCIA VS CLASE
# ------------------------------------------------------------

# En este ejemplo:
#
# self.nombre
# → atributo de instancia
#
#
# categoria
# → atributo de clase


print(
    CientificoRegistro.categoria
)


# También podemos acceder directamente desde la clase.


# ------------------------------------------------------------
# 23. CUÁNDO UTILIZAR UN ATRIBUTO DE CLASE
# ------------------------------------------------------------

# Puede tener sentido cuando existe un valor que representa
# algo común para todas las instancias.
#
#
# Ejemplo sencillo:


class Planeta:

    tipo_objeto = "Planeta"

    def __init__(
        self,
        nombre
    ):
        self.nombre = nombre


planeta_tierra = Planeta(
    "Tierra"
)

planeta_marte = Planeta(
    "Marte"
)


print(planeta_tierra.tipo_objeto)
print(planeta_marte.tipo_objeto)


# No profundizaremos más en atributos de clase por ahora.


# ------------------------------------------------------------
# 24. LLAMAR UN MÉTODO DESDE OTRO MÉTODO
# ------------------------------------------------------------

# Un método puede utilizar otro método del mismo objeto.


class Registro:

    def __init__(
        self,
        codigo
    ):
        self.codigo = codigo

    def obtener_codigo_normalizado(self):
        return self.codigo.strip().upper()

    def obtener_resumen(self):
        codigo_normalizado = (
            self.obtener_codigo_normalizado()
        )

        return (
            f"Registro: {codigo_normalizado}"
        )


registro = Registro(
    "   abc-1001   "
)


print(
    registro.obtener_resumen()
)


# Observa:
#
# self.obtener_codigo_normalizado()
#
# llama otro método del mismo objeto.


# ------------------------------------------------------------
# 25. MÉTODOS PUEDEN UTILIZAR EXCEPCIONES
# ------------------------------------------------------------

# También podemos combinar lo aprendido anteriormente.


class Cuenta:

    def __init__(
        self,
        saldo
    ):
        self.saldo = saldo

    def retirar(
        self,
        cantidad
    ):

        if cantidad > self.saldo:
            raise ValueError(
                "Saldo insuficiente."
            )

        self.saldo -= cantidad


cuenta_ejemplo = Cuenta(
    100000
)


try:
    cuenta_ejemplo.retirar(
        30000
    )

except ValueError as error:
    print(error)


print(cuenta_ejemplo.saldo)


# Aquí combinamos:
#
# clase
# objeto
# método
# atributo
# if
# raise
# try
# except


# ------------------------------------------------------------
# 26. MÉTODO QUE DEVUELVE UN DICCIONARIO
# ------------------------------------------------------------

class CientificoFicha:

    def __init__(
        self,
        nombre,
        area
    ):
        self.nombre = nombre
        self.area = area

    def obtener_datos(self):

        return {
            "nombre": self.nombre,
            "area": self.area
        }


cientifico_noether = CientificoFicha(
    "Emmy Noether",
    "Matemáticas"
)


datos_noether = (
    cientifico_noether.obtener_datos()
)


print(datos_noether)


# Un método puede devolver:
#
# str
# int
# float
# bool
# list
# dict
# tuple
# None
#
# exactamente igual que una función.


# ------------------------------------------------------------
# 27. RICK SANCHEZ COMO EJEMPLO FICTICIO
# ------------------------------------------------------------

# Rick Sanchez es un personaje ficticio.


class CientificoFicticio:

    def __init__(
        self,
        nombre,
        universo
    ):
        self.nombre = nombre
        self.universo = universo

    def obtener_descripcion(self):
        return (
            f"{self.nombre} pertenece a "
            f"{self.universo}."
        )


rick = CientificoFicticio(
    "Rick Sanchez",
    "Rick and Morty"
)


print(
    rick.obtener_descripcion()
)


# ------------------------------------------------------------
# 28. MÉTODO VS FUNCIÓN: IDEA PRÁCTICA
# ------------------------------------------------------------

# FUNCIÓN:
#
# calcular_total(...)
#
# recibe todos los datos que necesita.
#
#
# MÉTODO:
#
# ticket.cambiar_estado(...)
#
# puede utilizar información que ya pertenece al objeto.
#
#
# Ejemplo:
#
# self.estado
#
# ya existe dentro del ticket.


# ------------------------------------------------------------
# 29. NO TODO COMPORTAMIENTO DEBE SER UN MÉTODO
# ------------------------------------------------------------

# Igual que no todo necesita ser una clase,
# tampoco toda función debe transformarse en método.
#
#
# Pregunta útil:
#
# ¿Este comportamiento pertenece naturalmente
# al objeto?
#
#
# Si hablamos de:
#
# cambiar_estado()
#
# tiene sentido como comportamiento de Ticket.
#
#
# Pero una operación completamente independiente podría
# continuar siendo una función normal.


# ------------------------------------------------------------
# 30. EJEMPLO RESUMIDO
# ------------------------------------------------------------

class CientificoResumen:

    categoria = "Científico"

    def __init__(
        self,
        nombre,
        area
    ):
        self.nombre = nombre
        self.area = area

    def cambiar_area(
        self,
        nueva_area
    ):
        self.area = nueva_area

    def obtener_resumen(self):
        return (
            f"{self.nombre} - "
            f"{self.area}"
        )


cientifico_resumen = CientificoResumen(
    "Stephen Hawking",
    "Física"
)


print(
    cientifico_resumen.obtener_resumen()
)


cientifico_resumen.cambiar_area(
    "Cosmología"
)


print(
    cientifico_resumen.obtener_resumen()
)


# Aquí tenemos:
#
# CientificoResumen
# → clase
#
# cientifico_resumen
# → objeto
#
# nombre / area
# → atributos de instancia
#
# categoria
# → atributo de clase
#
# cambiar_area()
# → método que modifica el objeto
#
# obtener_resumen()
# → método que devuelve información


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# OBJETO
#
# puede contener:
#
# DATOS
# +
# COMPORTAMIENTO
#
#
# ATRIBUTOS:
#
# self.nombre
# self.estado
# self.area
#
# representan información de una instancia.
#
#
# MÉTODOS:
#
# def cambiar_estado(self, nuevo_estado):
#     ...
#
# representan comportamiento relacionado con el objeto.
#
#
# LLAMAR MÉTODO:
#
# objeto.metodo()
#
#
# MÉTODO CON ARGUMENTOS:
#
# objeto.metodo(valor)
#
#
# MÉTODO CON RETURN:
#
# def obtener_resumen(self):
#     return ...
#
#
# MODIFICAR ESTADO:
#
# def cambiar_estado(self, nuevo_estado):
#     self.estado = nuevo_estado
#
#
# ATRIBUTO DE INSTANCIA:
#
# self.nombre
#
# cada objeto puede tener un valor diferente.
#
#
# ATRIBUTO DE CLASE:
#
# categoria = "Científico"
#
# representa información común definida en la clase.
#
#
# CONCEPTO FUNDAMENTAL:
#
# clase
# ↓
# crea objetos
#
# objeto
# ↓
# mantiene atributos
# +
# ejecuta métodos
#
#
# Próximo tema:
#
# encapsulamiento
# propiedades
# control del acceso y modificación de atributos