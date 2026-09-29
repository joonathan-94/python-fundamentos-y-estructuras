# ============================================================
# ENCAPSULAMIENTO Y PROPIEDADES EN PYTHON
# ============================================================
#
# Hasta ahora nuestros objetos permiten acceder directamente
# a sus atributos.
#
# Ejemplo:
#
# cientifico.nombre
# ticket.estado
# cuenta.saldo
#
#
# Incluso podemos modificarlos directamente:
#
# cuenta.saldo = -500000
#
#
# Técnicamente Python permite hacerlo.
#
# Pero a veces queremos controlar cómo se modifica
# determinada información.
#
#
# Ahí aparece la idea de:
#
# ENCAPSULAMIENTO
#
#
# Conceptualmente:
#
# objeto
# ↓
# mantiene sus datos
# ↓
# controla cómo se utilizan o modifican
#
#
# En Python este concepto se maneja de forma más flexible
# que en lenguajes como Java.


# ------------------------------------------------------------
# 1. ATRIBUTO PÚBLICO
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


# Podemos modificar directamente:

cientifico_hawking.area = "Física teórica"

print(cientifico_hawking.area)


# Estos atributos son públicos.


# ------------------------------------------------------------
# 2. EL PROBLEMA DE MODIFICAR CUALQUIER VALOR
# ------------------------------------------------------------

class CuentaSimple:

    def __init__(self, saldo):
        self.saldo = saldo


cuenta = CuentaSimple(
    100000
)


# Python permite hacer:

cuenta.saldo = -999999


print(cuenta.saldo)


# Tal vez para nuestra aplicación esto no tenga sentido.
#
# El problema no es Python.
#
# El problema es que nuestra clase todavía no controla
# cómo se modifica ese dato.


# ------------------------------------------------------------
# 3. CONVENCIÓN _ATRIBUTO
# ------------------------------------------------------------

# En Python es común utilizar un guion bajo inicial:
#
# _saldo
#
# para indicar:
#
# "este atributo es para uso interno de la clase"
#
#
# IMPORTANTE:
#
# esto es una CONVENCIÓN.
#
# Python no impide completamente acceder al atributo.


class Cuenta:

    def __init__(self, saldo):
        self._saldo = saldo


cuenta_principal = Cuenta(
    150000
)


print(cuenta_principal._saldo)


# Esto técnicamente funciona.
#
# Pero al ver:
#
# _saldo
#
# entendemos:
#
# "no debería modificar este atributo directamente
# desde fuera de la clase".


# ------------------------------------------------------------
# 4. PÚBLICO VS USO INTERNO
# ------------------------------------------------------------

# Podemos pensar inicialmente:
#
# nombre
#
# → atributo público
#
#
# _saldo
#
# → atributo pensado para uso interno
#
#
# El "_" comunica una intención al programador.


# ------------------------------------------------------------
# 5. ¿CÓMO ACCEDEMOS ENTONCES AL DATO?
# ------------------------------------------------------------

# Podemos crear un método.


class CuentaConMetodo:

    def __init__(self, saldo):
        self._saldo = saldo

    def obtener_saldo(self):
        return self._saldo


cuenta_metodo = CuentaConMetodo(
    200000
)


print(
    cuenta_metodo.obtener_saldo()
)


# Esto funciona.
#
# Pero Python también ofrece una herramienta muy cómoda:
#
# @property


# ------------------------------------------------------------
# 6. @property
# ------------------------------------------------------------

class CuentaConPropiedad:

    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo


cuenta_propiedad = CuentaConPropiedad(
    250000
)


print(
    cuenta_propiedad.saldo
)


# Observa algo interesante.
#
# Definimos:
#
# def saldo(self):
#
# pero utilizamos:
#
# cuenta_propiedad.saldo
#
# y NO:
#
# cuenta_propiedad.saldo()
#
#
# @property permite utilizar un método como si fuera
# un atributo.


# ------------------------------------------------------------
# 7. ¿POR QUÉ USAR PROPERTY?
# ------------------------------------------------------------

# Desde fuera podemos escribir:
#
# cuenta.saldo
#
# de una forma sencilla.
#
#
# Pero internamente la clase continúa controlando
# cómo obtiene el valor.


class Astronomo:

    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre


astronomo_sagan = Astronomo(
    "Carl Sagan"
)


print(
    astronomo_sagan.nombre
)


# ------------------------------------------------------------
# 8. PROPERTY NO NECESITA MODIFICAR EL VALOR
# ------------------------------------------------------------

# Una propiedad puede simplemente devolver información.


class Fisico:

    def __init__(
        self,
        nombre,
        anio_nacimiento
    ):
        self._nombre = nombre
        self._anio_nacimiento = anio_nacimiento

    @property
    def nombre(self):
        return self._nombre

    @property
    def anio_nacimiento(self):
        return self._anio_nacimiento


fisico_einstein = Fisico(
    "Albert Einstein",
    1879
)


print(fisico_einstein.nombre)
print(fisico_einstein.anio_nacimiento)


# ------------------------------------------------------------
# 9. SETTER
# ------------------------------------------------------------

# Hasta ahora podemos consultar:
#
# cuenta.saldo
#
# pero todavía no definimos cómo modificarlo.
#
#
# Para eso podemos utilizar un setter.


class CuentaControlada:

    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        self._saldo = nuevo_saldo


cuenta_controlada = CuentaControlada(
    300000
)


print(cuenta_controlada.saldo)


cuenta_controlada.saldo = 350000


print(cuenta_controlada.saldo)


# Aunque parece:
#
# cuenta_controlada.saldo = 350000
#
# Python ejecuta internamente el setter:
#
# @saldo.setter


# ------------------------------------------------------------
# 10. CONTROLAR EL VALOR CON EL SETTER
# ------------------------------------------------------------

# Ahora aparece la principal utilidad.
#
# Podemos validar el dato antes de guardarlo.


class CuentaValidada:

    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):

        if nuevo_saldo < 0:
            raise ValueError(
                "El saldo no puede ser negativo."
            )

        self._saldo = nuevo_saldo


cuenta_validada = CuentaValidada(
    400000
)


cuenta_validada.saldo = 500000


print(
    cuenta_validada.saldo
)


# Si intentáramos:
#
# cuenta_validada.saldo = -500
#
# se produciría:
#
# ValueError


# ------------------------------------------------------------
# 11. PROPERTY + EXCEPCIONES
# ------------------------------------------------------------

# Podemos utilizar lo que ya estudiamos anteriormente.


try:
    cuenta_validada.saldo = -1000

except ValueError as error:
    print(error)


print(
    cuenta_validada.saldo
)


# El valor anterior se mantiene porque el setter rechazó
# el dato inválido.


# ------------------------------------------------------------
# 12. EJEMPLO CON UN CIENTÍFICO
# ------------------------------------------------------------

class CientificoRegistro:

    def __init__(
        self,
        nombre,
        anio_nacimiento
    ):
        self._nombre = nombre
        self._anio_nacimiento = anio_nacimiento

    @property
    def nombre(self):
        return self._nombre

    @property
    def anio_nacimiento(self):
        return self._anio_nacimiento


cientifico_tesla = CientificoRegistro(
    "Nikola Tesla",
    1856
)


print(cientifico_tesla.nombre)
print(cientifico_tesla.anio_nacimiento)


# ------------------------------------------------------------
# 13. AGREGAR VALIDACIÓN
# ------------------------------------------------------------

class CientificoValidado:

    def __init__(
        self,
        nombre,
        anio_nacimiento
    ):
        self._nombre = nombre
        self._anio_nacimiento = anio_nacimiento

    @property
    def nombre(self):
        return self._nombre

    @property
    def anio_nacimiento(self):
        return self._anio_nacimiento

    @anio_nacimiento.setter
    def anio_nacimiento(
        self,
        nuevo_anio
    ):

        if nuevo_anio <= 0:
            raise ValueError(
                "El año debe ser mayor que cero."
            )

        self._anio_nacimiento = nuevo_anio


cientifico_heisenberg = (
    CientificoValidado(
        "Werner Heisenberg",
        1901
    )
)


print(
    cientifico_heisenberg.anio_nacimiento
)


# ------------------------------------------------------------
# 14. GETTER Y SETTER
# ------------------------------------------------------------

# A veces escucharás los términos:
#
# getter
# setter
#
#
# GETTER:
#
# obtiene un valor.
#
#
# SETTER:
#
# modifica un valor.
#
#
# Con properties en Python:
#
#
# GETTER:

# @property
# def saldo(self):
#     return self._saldo


# SETTER:

# @saldo.setter
# def saldo(self, nuevo_saldo):
#     self._saldo = nuevo_saldo


# ------------------------------------------------------------
# 15. RELACIÓN CON JAVA
# ------------------------------------------------------------

# En otros lenguajes, como Java, es frecuente encontrar:
#
# getNombre()
# setNombre()
#
#
# Python puede utilizar métodos normales igualmente,
# pero @property permite una sintaxis más natural:
#
# cientifico.nombre
#
# en lugar de:
#
# cientifico.get_nombre()
#
#
# No significa que property deba utilizarse siempre.


# ------------------------------------------------------------
# 16. EJEMPLO CON TICKET
# ------------------------------------------------------------

class Ticket:

    def __init__(
        self,
        titulo,
        estado="Nuevo"
    ):
        self.titulo = titulo
        self._estado = estado

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado):

        estados_validos = [
            "Nuevo",
            "En progreso",
            "Resuelto"
        ]

        if nuevo_estado not in estados_validos:
            raise ValueError(
                "Estado de ticket inválido."
            )

        self._estado = nuevo_estado


ticket_servidor = Ticket(
    "Servidor sin conexión"
)


print(
    ticket_servidor.estado
)


# Modificación válida:

ticket_servidor.estado = "En progreso"


print(
    ticket_servidor.estado
)


# ------------------------------------------------------------
# 17. MODIFICACIÓN INVÁLIDA
# ------------------------------------------------------------

try:
    ticket_servidor.estado = "Desaparecido"

except ValueError as error:
    print(error)


print(
    ticket_servidor.estado
)


# El objeto conserva:
#
# En progreso
#
# porque el setter rechazó el nuevo valor.


# ------------------------------------------------------------
# 18. ENCAPSULAR UNA REGLA
# ------------------------------------------------------------

# Aquí aparece una idea importante.
#
# La regla:
#
# "el estado debe pertenecer a esta lista"
#
# está dentro de la propia clase Ticket.
#
#
# Otro código no necesita repetir:
#
# if estado in ...
#
# cada vez que quiera cambiarlo.
#
#
# El objeto controla su propio estado.


# ------------------------------------------------------------
# 19. EJEMPLO CON TEMPERATURA
# ------------------------------------------------------------

class MedicionTemperatura:

    def __init__(
        self,
        temperatura
    ):
        self._temperatura = temperatura

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(
        self,
        nuevo_valor
    ):

        if nuevo_valor < -273.15:
            raise ValueError(
                "Temperatura inferior "
                "al cero absoluto."
            )

        self._temperatura = nuevo_valor


medicion = MedicionTemperatura(
    25.0
)


print(
    medicion.temperatura
)


# ------------------------------------------------------------
# 20. ¿ES OBLIGATORIO USAR _ATRIBUTO?
# ------------------------------------------------------------

# No.
#
# Podemos seguir teniendo atributos públicos:
#
# self.nombre
#
#
# Utilizamos:
#
# self._nombre
#
# cuando queremos comunicar que ese dato forma parte
# del estado interno de la clase y preferimos acceder
# mediante métodos o propiedades.


# ------------------------------------------------------------
# 21. PYTHON NO FUNCIONA EXACTAMENTE COMO JAVA
# ------------------------------------------------------------

# En Java podemos utilizar modificadores como:
#
# public
# private
# protected
#
#
# Python utiliza principalmente convenciones y mecanismos
# diferentes.
#
#
# Por ahora basta con recordar:
#
# atributo
#
# nombre
# → público
#
#
# _nombre
# → uso interno por convención


# ------------------------------------------------------------
# 22. ¿EXISTE __ATRIBUTO?
# ------------------------------------------------------------

# También puedes encontrar atributos como:
#
# self.__nombre
#
#
# Python aplica un mecanismo llamado:
#
# name mangling
#
#
# No lo estudiaremos ahora.
#
# No necesitamos utilizarlo para comprender el
# encapsulamiento básico.
#
#
# Para este curso nos basta con:
#
# _atributo
# +
# @property


# ------------------------------------------------------------
# 23. NO CREAR PROPERTY PARA TODO
# ------------------------------------------------------------

# Este punto es importante.
#
# No necesitamos convertir automáticamente:
#
# self.nombre
#
# en:
#
# self._nombre
# +
# property
# +
# setter
#
# para todas las clases.
#
#
# Un atributo público simple puede ser perfectamente válido.


class Planeta:

    def __init__(
        self,
        nombre
    ):
        self.nombre = nombre


planeta_marte = Planeta(
    "Marte"
)


print(
    planeta_marte.nombre
)


# No existe ninguna razón especial para complicar
# este ejemplo.


# ------------------------------------------------------------
# 24. CUÁNDO PROPERTY TIENE MÁS SENTIDO
# ------------------------------------------------------------

# Puede resultar útil cuando:
#
# - necesitamos validar un valor;
# - queremos calcular algo al consultar;
# - queremos controlar modificaciones;
# - queremos mantener una interfaz sencilla;
# - necesitamos cambiar internamente cómo almacenamos
#   un dato sin cambiar cómo se utiliza desde fuera.


# ------------------------------------------------------------
# 25. PROPIEDAD CALCULADA
# ------------------------------------------------------------

# Una property no necesariamente tiene que devolver
# directamente un atributo.


class Rectangulo:

    def __init__(
        self,
        ancho,
        alto
    ):
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self):
        return (
            self.ancho
            * self.alto
        )


rectangulo = Rectangulo(
    10,
    5
)


print(
    rectangulo.area
)


# Observa:
#
# area
#
# no está almacenada como:
#
# self.area
#
# Se calcula cuando la consultamos.


# ------------------------------------------------------------
# 26. PROPIEDAD SOLO DE LECTURA
# ------------------------------------------------------------

# En el ejemplo anterior tenemos:
#
# @property
# def area(...)
#
# pero NO tenemos:
#
# @area.setter
#
#
# Por eso conceptualmente tratamos:
#
# area
#
# como una propiedad calculada de solo lectura.


# ------------------------------------------------------------
# 27. EJEMPLO CON AÑO Y EDAD HISTÓRICA
# ------------------------------------------------------------

class PersonaHistorica:

    def __init__(
        self,
        nombre,
        anio_nacimiento
    ):
        self.nombre = nombre
        self.anio_nacimiento = anio_nacimiento

    @property
    def anios_desde_nacimiento(self):
        return (
            2026
            - self.anio_nacimiento
        )


persona_galileo = PersonaHistorica(
    "Galileo Galilei",
    1564
)


print(
    persona_galileo.anios_desde_nacimiento
)


# Es una propiedad calculada.
#
# No está almacenada directamente.


# ------------------------------------------------------------
# 28. RICK SANCHEZ COMO DATO FICTICIO
# ------------------------------------------------------------

# Rick Sanchez es un personaje ficticio.


class CientificoFicticio:

    def __init__(
        self,
        nombre,
        inteligencia
    ):
        self.nombre = nombre
        self._inteligencia = inteligencia

    @property
    def inteligencia(self):
        return self._inteligencia

    @inteligencia.setter
    def inteligencia(
        self,
        valor
    ):

        if valor < 0:
            raise ValueError(
                "La inteligencia no puede ser negativa."
            )

        self._inteligencia = valor


rick = CientificoFicticio(
    "Rick Sanchez",
    100
)


print(
    rick.inteligencia
)


# ------------------------------------------------------------
# 29. ENCAPSULAMIENTO NO SIGNIFICA ESCONDER TODO
# ------------------------------------------------------------

# Este concepto puede confundirse al principio.
#
# Encapsular no significa:
#
# "hacer todos los atributos privados".
#
#
# La idea más útil es:
#
# un objeto controla los datos y reglas
# que pertenecen a su responsabilidad.


# ------------------------------------------------------------
# 30. EJEMPLO RESUMIDO
# ------------------------------------------------------------

class RegistroCientifico:

    def __init__(
        self,
        nombre,
        puntuacion
    ):
        self.nombre = nombre
        self._puntuacion = puntuacion

    @property
    def puntuacion(self):
        return self._puntuacion

    @puntuacion.setter
    def puntuacion(
        self,
        nueva_puntuacion
    ):

        if nueva_puntuacion < 0:
            raise ValueError(
                "La puntuación no puede ser negativa."
            )

        self._puntuacion = nueva_puntuacion


registro_turing = RegistroCientifico(
    "Alan Turing",
    95
)


print(
    registro_turing.puntuacion
)


registro_turing.puntuacion = 100


print(
    registro_turing.puntuacion
)


# Tenemos:
#
# nombre
# → atributo público
#
# _puntuacion
# → atributo interno por convención
#
# puntuacion
# → property
#
# @puntuacion.setter
# → controla modificaciones


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# ENCAPSULAMIENTO
#
# permite que un objeto controle mejor sus propios datos
# y las reglas asociadas a ellos.
#
#
# ATRIBUTO PÚBLICO:
#
# self.nombre
#
#
# ATRIBUTO DE USO INTERNO POR CONVENCIÓN:
#
# self._saldo
#
#
# PROPERTY:
#
# @property
# def saldo(self):
#     return self._saldo
#
#
# permite utilizar:
#
# objeto.saldo
#
#
# SETTER:
#
# @saldo.setter
# def saldo(self, nuevo_saldo):
#     ...
#
#
# permite controlar:
#
# objeto.saldo = nuevo_valor
#
#
# EJEMPLO DE VALIDACIÓN:
#
# if nuevo_saldo < 0:
#     raise ValueError(...)
#
#
# Una property también puede ser calculada:
#
# @property
# def area(self):
#     return self.ancho * self.alto
#
#
# REGLA IMPORTANTE:
#
# no necesitamos properties para absolutamente todos
# los atributos.
#
#
# Las utilizaremos cuando exista una razón concreta:
#
# validación
# control
# cálculo
# protección de reglas
#
#
# Próximo tema:
#
# herencia
# +
# polimorfismo