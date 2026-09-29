# ============================================================
# HERENCIA Y POLIMORFISMO
# ============================================================
#
# Hasta ahora hemos visto:
#
# clase
# objeto
# atributos
# métodos
# encapsulamiento
# properties
#
#
# Ahora estudiaremos:
#
# HERENCIA
# POLIMORFISMO
#
#
# HERENCIA:
#
# permite crear una clase nueva utilizando como base
# otra clase existente.
#
#
# POLIMORFISMO:
#
# permite que distintos objetos respondan al mismo método
# de maneras diferentes.


# ------------------------------------------------------------
# 1. PROBLEMA: CLASES MUY PARECIDAS
# ------------------------------------------------------------

# Supongamos que queremos representar diferentes tipos
# de personas dentro de un sistema.


class Tecnico:

    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo


class Supervisor:

    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo


# Ambas clases contienen:
#
# nombre
# correo
#
# Estamos repitiendo código.
#
# Una posible solución es identificar lo que tienen
# en común.


# ------------------------------------------------------------
# 2. CLASE PADRE
# ------------------------------------------------------------

class Usuario:

    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo


# Usuario representa la información común.
#
#
# Podemos llamarla:
#
# clase padre
# clase base
# superclase


# ------------------------------------------------------------
# 3. CLASE HIJA
# ------------------------------------------------------------

class TecnicoSoporte(Usuario):
    pass


# Esta sintaxis:
#
# class TecnicoSoporte(Usuario):
#
# significa:
#
# TecnicoSoporte
# hereda de
# Usuario
#
#
# Podemos llamarla:
#
# clase hija
# clase derivada
# subclase


# ------------------------------------------------------------
# 4. HEREDAR ATRIBUTOS Y COMPORTAMIENTO
# ------------------------------------------------------------

tecnico = TecnicoSoporte(
    "Alan Turing",
    "turing@example.com"
)


print(tecnico.nombre)
print(tecnico.correo)


# Aunque TecnicoSoporte no tiene su propio __init__,
# puede utilizar el __init__ heredado desde Usuario.


# ------------------------------------------------------------
# 5. RELACIÓN ENTRE CLASES
# ------------------------------------------------------------

# Podemos visualizar:
#
# Usuario
#    ↓
# TecnicoSoporte
#
#
# TecnicoSoporte es un tipo más específico de Usuario.


# ------------------------------------------------------------
# 6. HEREDAR MÉTODOS
# ------------------------------------------------------------

class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        return f"Soy {self.nombre}."


class Cientifico(Persona):
    pass


cientifico = Cientifico(
    "Albert Einstein"
)


print(
    cientifico.presentarse()
)


# Cientifico heredó:
#
# nombre
# presentarse()
#
# desde Persona.


# ------------------------------------------------------------
# 7. AGREGAR COMPORTAMIENTO A LA CLASE HIJA
# ------------------------------------------------------------

class Astronomo(Persona):

    def observar_cielo(self):
        return (
            f"{self.nombre} está realizando "
            "una observación astronómica."
        )


astronomo = Astronomo(
    "José Maza"
)


print(
    astronomo.presentarse()
)

print(
    astronomo.observar_cielo()
)


# Astronomo tiene:
#
# comportamiento heredado:
# presentarse()
#
# comportamiento propio:
# observar_cielo()


# ------------------------------------------------------------
# 8. CUANDO LA CLASE HIJA NECESITA MÁS ATRIBUTOS
# ------------------------------------------------------------

# Imaginemos:
#
# Usuario:
# nombre
# correo
#
#
# Técnico:
# nombre
# correo
# especialidad
#
#
# Queremos reutilizar nombre y correo sin repetir
# toda la inicialización.


# ------------------------------------------------------------
# 9. super()
# ------------------------------------------------------------

class UsuarioSistema:

    def __init__(
        self,
        nombre,
        correo
    ):
        self.nombre = nombre
        self.correo = correo


class TecnicoSistema(UsuarioSistema):

    def __init__(
        self,
        nombre,
        correo,
        especialidad
    ):
        super().__init__(
            nombre,
            correo
        )

        self.especialidad = especialidad


tecnico_redes = TecnicoSistema(
    "Grace Hopper",
    "hopper@example.com",
    "Redes"
)


print(tecnico_redes.nombre)
print(tecnico_redes.correo)
print(tecnico_redes.especialidad)


# ------------------------------------------------------------
# 10. ¿QUÉ HACE super()?
# ------------------------------------------------------------

# En este ejemplo:
#
# super().__init__(
#     nombre,
#     correo
# )
#
# permite ejecutar el __init__ de la clase padre.
#
#
# Podemos visualizar:
#
# TecnicoSistema(...)
#        ↓
# __init__ de TecnicoSistema
#        ↓
# super().__init__(...)
#        ↓
# __init__ de UsuarioSistema
#        ↓
# guarda nombre y correo
#        ↓
# TecnicoSistema agrega especialidad


# ------------------------------------------------------------
# 11. ¿POR QUÉ USAR super()?
# ------------------------------------------------------------

# Sin super() podríamos repetir:
#
# self.nombre = nombre
# self.correo = correo
#
# dentro de cada clase hija.
#
#
# Eso generaría duplicación.
#
#
# Con super():
#
# reutilizamos la lógica de la clase padre.


# ------------------------------------------------------------
# 12. SOBRESCRITURA DE MÉTODOS
# ------------------------------------------------------------

# Una clase hija puede reemplazar el comportamiento
# de un método heredado.


class CientificoBase:

    def presentarse(self):
        return "Soy un científico."


class Fisico(CientificoBase):

    def presentarse(self):
        return "Soy un físico."


class AstronomoCientifico(CientificoBase):

    def presentarse(self):
        return "Soy un astrónomo."


fisico = Fisico()
astronomo_cientifico = AstronomoCientifico()


print(
    fisico.presentarse()
)

print(
    astronomo_cientifico.presentarse()
)


# Ambos heredaron de CientificoBase.
#
# Pero cada clase redefinió:
#
# presentarse()


# ------------------------------------------------------------
# 13. POLIMORFISMO
# ------------------------------------------------------------

# Ahora aparece la idea principal.
#
#
# Tenemos diferentes objetos:
#
# Fisico
# AstronomoCientifico
#
#
# Ambos pueden responder a:
#
# presentarse()
#
#
# pero el resultado depende del tipo de objeto.


cientificos = [
    Fisico(),
    AstronomoCientifico()
]


for cientifico_actual in cientificos:

    print(
        cientifico_actual.presentarse()
    )


# El mismo código:
#
# cientifico_actual.presentarse()
#
# funciona con distintos objetos.
#
#
# Cada objeto decide qué implementación ejecutar.
#
#
# Esa es una forma sencilla de entender:
#
# POLIMORFISMO


# ------------------------------------------------------------
# 14. EJEMPLO MÁS REALISTA CON USUARIOS
# ------------------------------------------------------------

class UsuarioAplicacion:

    def __init__(
        self,
        nombre
    ):
        self.nombre = nombre

    def obtener_rol(self):
        return "Usuario"


class Solicitante(UsuarioAplicacion):

    def obtener_rol(self):
        return "Solicitante"


class TecnicoAplicacion(UsuarioAplicacion):

    def obtener_rol(self):
        return "Técnico"


class SupervisorAplicacion(UsuarioAplicacion):

    def obtener_rol(self):
        return "Supervisor"


usuarios = [
    Solicitante("Carl Sagan"),
    TecnicoAplicacion("Alan Turing"),
    SupervisorAplicacion("Grace Hopper")
]


for usuario in usuarios:

    print(
        usuario.nombre,
        "-",
        usuario.obtener_rol()
    )


# Resultado conceptual:
#
# Carl Sagan - Solicitante
# Alan Turing - Técnico
# Grace Hopper - Supervisor
#
#
# Todos responden a:
#
# obtener_rol()
#
# pero cada tipo de usuario responde de forma diferente.


# ------------------------------------------------------------
# 15. EJEMPLO CON TICKETS
# ------------------------------------------------------------

class Ticket:

    def __init__(
        self,
        titulo
    ):
        self.titulo = titulo

    def obtener_prioridad(self):
        return "Normal"


class TicketCritico(Ticket):

    def obtener_prioridad(self):
        return "Crítica"


class TicketBajo(Ticket):

    def obtener_prioridad(self):
        return "Baja"


tickets = [
    Ticket(
        "Solicitud de instalación"
    ),
    TicketCritico(
        "Servidor principal sin conexión"
    ),
    TicketBajo(
        "Cambio de fondo de pantalla"
    )
]


for ticket in tickets:

    print(
        ticket.titulo,
        "-",
        ticket.obtener_prioridad()
    )


# Nuevamente:
#
# mismo método:
#
# obtener_prioridad()
#
#
# diferentes comportamientos según el objeto.


# ------------------------------------------------------------
# 16. isinstance() CON HERENCIA
# ------------------------------------------------------------

tecnico_ejemplo = TecnicoSistema(
    "Nikola Tesla",
    "tesla@example.com",
    "Electricidad"
)


print(
    isinstance(
        tecnico_ejemplo,
        TecnicoSistema
    )
)


print(
    isinstance(
        tecnico_ejemplo,
        UsuarioSistema
    )
)


# Ambos resultados son:
#
# True
#
#
# Porque:
#
# TecnicoSistema
# hereda de
# UsuarioSistema
#
#
# Por lo tanto, un TecnicoSistema también puede
# considerarse un UsuarioSistema.


# ------------------------------------------------------------
# 17. HERENCIA REPRESENTA UNA RELACIÓN "ES UN"
# ------------------------------------------------------------

# Una buena pregunta antes de usar herencia:
#
# ¿La clase hija ES UN tipo de clase padre?
#
#
# Ejemplo:
#
# Técnico
# ES UN
# Usuario
#
# → puede tener sentido.
#
#
# Astrónomo
# ES UNA
# Persona
#
# → puede tener sentido.


# ------------------------------------------------------------
# 18. EJEMPLO DE HERENCIA QUE NO TENDRÍA SENTIDO
# ------------------------------------------------------------

# Supongamos:
#
# Ticket
# Computador
#
#
# ¿Un Ticket ES UN Computador?
#
# No.
#
#
# Entonces probablemente:
#
# class Ticket(Computador):
#
# no representaría una relación correcta.
#
#
# No debemos utilizar herencia solamente para
# reutilizar código.


# ------------------------------------------------------------
# 19. HERENCIA SIMPLE
# ------------------------------------------------------------

# En este bloque solamente utilizaremos:
#
# HERENCIA SIMPLE
#
#
# Una clase hija:
#
# ↓
#
# una clase padre
#
#
# Ejemplo:
#
# Usuario
#    ↓
# Tecnico
#
#
# Python también permite herencia múltiple,
# pero no la estudiaremos ahora.


# ------------------------------------------------------------
# 20. super() TAMBIÉN PUEDE USARSE CON MÉTODOS
# ------------------------------------------------------------

class PersonaBase:

    def presentarse(self):
        return "Soy una persona."


class FisicoEspecializado(PersonaBase):

    def presentarse(self):

        presentacion_base = (
            super().presentarse()
        )

        return (
            f"{presentacion_base} "
            "También soy físico."
        )


fisico_especializado = (
    FisicoEspecializado()
)


print(
    fisico_especializado.presentarse()
)


# Aquí:
#
# super().presentarse()
#
# ejecuta el método de la clase padre.


# ------------------------------------------------------------
# 21. POLIMORFISMO NO SIGNIFICA HERENCIA SIEMPRE
# ------------------------------------------------------------

# Este punto es útil conocerlo aunque no profundizaremos.
#
#
# En Python, dos objetos no necesariamente tienen
# que compartir una clase padre para utilizar el
# mismo nombre de método.
#
#
# Ejemplo:


class Radio:

    def encender(self):
        return "Radio encendida."


class Computador:

    def encender(self):
        return "Computador encendido."


dispositivos = [
    Radio(),
    Computador()
]


for dispositivo in dispositivos:

    print(
        dispositivo.encender()
    )


# Ambos responden a:
#
# encender()
#
#
# Python puede trabajar con ellos sin exigir que
# tengan exactamente la misma clase padre.
#
#
# No necesitamos profundizar más por ahora.


# ------------------------------------------------------------
# 22. EJEMPLO COMPLETO
# ------------------------------------------------------------

class UsuarioBase:

    def __init__(
        self,
        nombre,
        correo
    ):
        self.nombre = nombre
        self.correo = correo

    def obtener_descripcion(self):
        return (
            f"{self.nombre} "
            f"({self.correo})"
        )


class TecnicoUsuario(UsuarioBase):

    def __init__(
        self,
        nombre,
        correo,
        especialidad
    ):
        super().__init__(
            nombre,
            correo
        )

        self.especialidad = especialidad

    def obtener_descripcion(self):
        return (
            f"{self.nombre} "
            f"({self.correo}) - "
            f"Técnico de {self.especialidad}"
        )


class SolicitanteUsuario(UsuarioBase):

    def obtener_descripcion(self):
        return (
            f"{self.nombre} "
            f"({self.correo}) - "
            "Solicitante"
        )


usuarios_sistema = [
    TecnicoUsuario(
        "Alan Turing",
        "turing@example.com",
        "Software"
    ),
    SolicitanteUsuario(
        "Carl Sagan",
        "sagan@example.com"
    )
]


for usuario in usuarios_sistema:

    print(
        usuario.obtener_descripcion()
    )


# Aquí tenemos:
#
# UsuarioBase
# → clase padre
#
#
# TecnicoUsuario
# SolicitanteUsuario
# → clases hijas
#
#
# super().__init__()
# → reutiliza inicialización del padre
#
#
# obtener_descripcion()
# → método sobrescrito
#
#
# usuario.obtener_descripcion()
# → ejemplo de polimorfismo


# ------------------------------------------------------------
# 23. CUÁNDO PUEDE SER ÚTIL LA HERENCIA
# ------------------------------------------------------------

# Puede ser útil cuando:
#
# - existen clases realmente relacionadas;
# - comparten datos o comportamiento;
# - una clase representa una versión más específica
#   de otra;
# - existe una relación clara de tipo "es un".


# ------------------------------------------------------------
# 24. CUÁNDO NO UTILIZARLA
# ------------------------------------------------------------

# No debemos crear jerarquías innecesariamente.
#
#
# Si dos clases solamente comparten unas pocas líneas,
# eso no significa automáticamente que deban utilizar
# herencia.
#
#
# Herencia es una herramienta.
#
# No una obligación.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# HERENCIA:
#
# permite crear una clase basada en otra.
#
#
# EJEMPLO:
#
# class Usuario:
#     ...
#
#
# class Tecnico(Usuario):
#     ...
#
#
# Usuario
# → clase padre
#
# Tecnico
# → clase hija
#
#
# ------------------------------------------------------------
#
# super():
#
# permite acceder a comportamiento de la clase padre.
#
#
# EJEMPLO:
#
# super().__init__(
#     nombre,
#     correo
# )
#
#
# ------------------------------------------------------------
#
# SOBRESCRITURA:
#
# una clase hija puede redefinir un método heredado.
#
#
# ------------------------------------------------------------
#
# POLIMORFISMO:
#
# diferentes objetos pueden responder al mismo método
# de maneras diferentes.
#
#
# Ejemplo:
#
# usuario.obtener_rol()
#
# puede producir:
#
# "Solicitante"
# "Técnico"
# "Supervisor"
#
# dependiendo del objeto.
#
#
# ------------------------------------------------------------
#
# REGLA PRÁCTICA PARA HERENCIA:
#
# preguntarnos:
#
# ¿X ES UN tipo de Y?
#
#
# Técnico ES UN Usuario
# → posible herencia
#
#
# Ticket ES UN Computador
# → no tiene sentido
#
#
# ------------------------------------------------------------
#
# Con esto completamos la teoría fundamental de POO.
#
# Próximo paso:
#
# 99_ejercicios.py