# ============================================================
# DECORADORES EN PYTHON
# ============================================================
#
# Un decorador permite agregar o modificar comportamiento
# alrededor de una función sin cambiar directamente
# el código interno de esa función.
#
#
# IDEA GENERAL:
#
# función original
# ↓
# decorador
# ↓
# función con comportamiento adicional
#
#
# Más adelante encontraremos decoradores en frameworks
# como Flask:
#
# @app.route("/tickets")
#
# Por eso es importante comprender primero
# cómo funcionan conceptualmente.


# ------------------------------------------------------------
# 1. LAS FUNCIONES TAMBIÉN SON OBJETOS
# ------------------------------------------------------------

# En Python podemos guardar una función en una variable.


def saludar():
    return "Hola"


otra_funcion = saludar


print(
    otra_funcion()
)


# No escribimos:
#
# otra_funcion = saludar()
#
# porque eso ejecutaría la función.
#
#
# En cambio:
#
# otra_funcion = saludar
#
# guarda una referencia a la función.


# ------------------------------------------------------------
# 2. PASAR UNA FUNCIÓN COMO ARGUMENTO
# ------------------------------------------------------------

def mostrar_resultado(funcion):

    resultado = funcion()

    print(resultado)


def obtener_mensaje():
    return "Sistema funcionando correctamente."


mostrar_resultado(
    obtener_mensaje
)


# Aquí:
#
# obtener_mensaje
#
# fue enviada como argumento a otra función.


# ------------------------------------------------------------
# 3. UNA FUNCIÓN PUEDE CREAR OTRA FUNCIÓN
# ------------------------------------------------------------

def crear_saludo():

    def saludo():
        return "Hola desde una función interna."

    return saludo


saludo_generado = crear_saludo()


print(
    saludo_generado()
)


# Esto demuestra que una función puede:
#
# - contener otra función;
# - devolver otra función.
#
#
# Esta idea será importante para los decoradores.


# ------------------------------------------------------------
# 4. PRIMER DECORADOR
# ------------------------------------------------------------

def registrar_ejecucion(funcion):

    def envoltura():

        print(
            "Antes de ejecutar la función."
        )

        funcion()

        print(
            "Después de ejecutar la función."
        )

    return envoltura


def crear_ticket():

    print(
        "Ticket creado."
    )


crear_ticket_decorado = registrar_ejecucion(
    crear_ticket
)


crear_ticket_decorado()


# Flujo:
#
# crear_ticket
# ↓
# registrar_ejecucion(crear_ticket)
# ↓
# devuelve envoltura
# ↓
# envoltura ejecuta comportamiento adicional


# ------------------------------------------------------------
# 5. SINTAXIS @DECORADOR
# ------------------------------------------------------------

# Python permite escribir lo anterior de forma
# mucho más sencilla.


def registrar_operacion(funcion):

    def envoltura():

        print(
            "Iniciando operación..."
        )

        funcion()

        print(
            "Operación finalizada."
        )

    return envoltura


@registrar_operacion
def procesar_ticket():

    print(
        "Procesando ticket."
    )


procesar_ticket()


# Esta sintaxis:
#
# @registrar_operacion
# def procesar_ticket():
#
# es conceptualmente equivalente a:
#
# procesar_ticket = registrar_operacion(
#     procesar_ticket
# )


# ------------------------------------------------------------
# 6. EL DECORADOR NO CAMBIA LA RESPONSABILIDAD PRINCIPAL
# ------------------------------------------------------------

# procesar_ticket()
#
# sigue ocupándose de:
#
# procesar el ticket.
#
#
# registrar_operacion()
#
# se ocupa de:
#
# registrar qué ocurre alrededor de la ejecución.
#
#
# Esto permite separar responsabilidades.


# ------------------------------------------------------------
# 7. DECORADOR CON RETURN
# ------------------------------------------------------------

# Una función decorada puede devolver valores.


def registrar_consulta(funcion):

    def envoltura():

        print(
            "Ejecutando consulta..."
        )

        resultado = funcion()

        return resultado

    return envoltura


@registrar_consulta
def obtener_estado():

    return "En progreso"


estado = obtener_estado()


print(estado)


# Es importante devolver:
#
# resultado
#
# porque de lo contrario perderíamos el valor
# retornado por la función original.


# ------------------------------------------------------------
# 8. PROBLEMA: FUNCIONES CON ARGUMENTOS
# ------------------------------------------------------------

# Supongamos que queremos decorar:


def cambiar_estado(
    estado
):
    return f"Nuevo estado: {estado}"


# Nuestro decorador también debe poder recibir
# esos argumentos.
#
# Aquí se vuelve útil algo que acabamos de estudiar:
#
# *args
# **kwargs


# ------------------------------------------------------------
# 9. DECORADOR CON *args Y **kwargs
# ------------------------------------------------------------

def registrar_llamada(funcion):

    def envoltura(
        *args,
        **kwargs
    ):

        print(
            f"Ejecutando {funcion.__name__}"
        )

        resultado = funcion(
            *args,
            **kwargs
        )

        return resultado

    return envoltura


@registrar_llamada
def actualizar_ticket(
    id_ticket,
    estado
):

    return (
        f"{id_ticket} actualizado "
        f"a {estado}"
    )


resultado_actualizacion = actualizar_ticket(
    "TK-1001",
    "Resuelto"
)


print(
    resultado_actualizacion
)


# Aquí:
#
# *args
# **kwargs
#
# permiten que el decorador sea reutilizable
# con funciones que reciben diferentes argumentos.


# ------------------------------------------------------------
# 10. EJEMPLO REAL: LOGGING BÁSICO
# ------------------------------------------------------------

# Una aplicación puede querer registrar qué funciones
# importantes están siendo ejecutadas.


def registrar_log(funcion):

    def envoltura(
        *args,
        **kwargs
    ):

        print(
            f"[LOG] Ejecutando: "
            f"{funcion.__name__}"
        )

        resultado = funcion(
            *args,
            **kwargs
        )

        print(
            f"[LOG] Finalizado: "
            f"{funcion.__name__}"
        )

        return resultado

    return envoltura


@registrar_log
def cerrar_ticket(
    id_ticket
):

    return (
        f"Ticket {id_ticket} cerrado."
    )


print(
    cerrar_ticket(
        "TK-2001"
    )
)


# Un caso real podría enviar estos registros
# a un archivo o sistema de logging.
#
# Por ahora solamente utilizamos print()
# para comprender el concepto.


# ------------------------------------------------------------
# 11. EJEMPLO REAL: CONTROL DE PERMISOS
# ------------------------------------------------------------

def requiere_admin(funcion):

    def envoltura(
        usuario,
        *args,
        **kwargs
    ):

        if usuario["rol"] != "Administrador":

            return (
                "Acceso denegado."
            )

        return funcion(
            usuario,
            *args,
            **kwargs
        )

    return envoltura


@requiere_admin
def eliminar_ticket(
    usuario,
    id_ticket
):

    return (
        f"Ticket {id_ticket} eliminado "
        f"por {usuario['nombre']}."
    )


usuario_admin = {
    "nombre": "Alan Turing",
    "rol": "Administrador"
}


usuario_tecnico = {
    "nombre": "Grace Hopper",
    "rol": "Técnico"
}


print(
    eliminar_ticket(
        usuario_admin,
        "TK-3001"
    )
)


print(
    eliminar_ticket(
        usuario_tecnico,
        "TK-3001"
    )
)


# El método principal:
#
# eliminar_ticket()
#
# no necesita implementar directamente
# la comprobación del rol.
#
#
# El decorador se encarga de esa responsabilidad.


# ------------------------------------------------------------
# 12. functools.wraps
# ------------------------------------------------------------

# Existe un pequeño problema con nuestros decoradores.
#
# La función original puede perder información
# como su nombre y documentación.
#
#
# Python incluye:
#
# functools.wraps
#
# para conservar esa información.


from functools import wraps


def registrar_accion(funcion):

    @wraps(funcion)
    def envoltura(
        *args,
        **kwargs
    ):

        print(
            f"Ejecutando {funcion.__name__}"
        )

        return funcion(
            *args,
            **kwargs
        )

    return envoltura


@registrar_accion
def crear_usuario(
    nombre
):

    """Crea un usuario."""

    return (
        f"Usuario {nombre} creado."
    )


print(
    crear_usuario(
        "Ada Lovelace"
    )
)


print(
    crear_usuario.__name__
)


# Gracias a:
#
# @wraps(funcion)
#
# Python conserva mejor la identidad
# de la función decorada.
#
#
# Es una buena práctica al crear
# decoradores propios.


# ------------------------------------------------------------
# 13. DECORADOR CON PARÁMETROS
# ------------------------------------------------------------

# Hasta ahora usamos:
#
# @registrar_log
#
#
# Pero también encontraremos:
#
# @algo("valor")
#
#
# Por ejemplo Flask utiliza una sintaxis como:
#
# @app.route("/tickets")
#
#
# Para comprender esa forma necesitamos
# un decorador que reciba parámetros.


def requiere_rol(
    rol_requerido
):

    def decorador(
        funcion
    ):

        @wraps(funcion)
        def envoltura(
            usuario,
            *args,
            **kwargs
        ):

            if (
                usuario["rol"]
                != rol_requerido
            ):

                return (
                    "Acceso denegado."
                )

            return funcion(
                usuario,
                *args,
                **kwargs
            )

        return envoltura

    return decorador


@requiere_rol(
    "Administrador"
)
def configurar_sistema(
    usuario
):

    return (
        f"{usuario['nombre']} "
        "puede configurar el sistema."
    )


print(
    configurar_sistema(
        usuario_admin
    )
)


# Tenemos ahora tres niveles:
#
# requiere_rol("Administrador")
# ↓
# recibe configuración
#
# decorador(funcion)
# ↓
# recibe la función
#
# envoltura(...)
# ↓
# ejecuta lógica alrededor de la función


# ------------------------------------------------------------
# 14. ¿POR QUÉ FLASK UTILIZA DECORADORES?
# ------------------------------------------------------------

# Más adelante veremos código parecido a:
#
#
# @app.route("/tickets")
# def listar_tickets():
#     ...
#
#
# Conceptualmente podemos leer:
#
# "registra listar_tickets como la función
# asociada a la ruta /tickets"
#
#
# NO estamos estudiando Flask todavía.
#
# Lo importante ahora es que la sintaxis:
#
# @app.route(...)
#
# ya no debería parecer algo misterioso.


# ------------------------------------------------------------
# 15. OTROS USOS REALES
# ------------------------------------------------------------

# Los decoradores pueden utilizarse para:
#
# - rutas web;
# - autenticación;
# - autorización;
# - logging;
# - medición de tiempo;
# - caché;
# - validaciones;
# - transacciones;
# - testing;
#
#
# Muchas librerías y frameworks utilizan
# decoradores porque permiten agregar
# comportamiento sin modificar directamente
# la lógica principal.


# ------------------------------------------------------------
# 16. NO TODO NECESITA UN DECORADOR
# ------------------------------------------------------------

# Igual que con POO:
#
# decoradores son una herramienta.
#
#
# Si algo puede resolverse claramente con:
#
# una función
# un if
# un método
#
# no necesitamos crear un decorador.
#
#
# Se vuelven especialmente útiles cuando
# el mismo comportamiento debe aplicarse
# a varias funciones.


# ------------------------------------------------------------
# 17. EJEMPLO CON VARIAS FUNCIONES
# ------------------------------------------------------------

@registrar_accion
def crear_ticket_simple(
    titulo
):

    return (
        f"Ticket creado: {titulo}"
    )


@registrar_accion
def cerrar_ticket_simple(
    id_ticket
):

    return (
        f"Ticket cerrado: {id_ticket}"
    )


print(
    crear_ticket_simple(
        "Problema de red"
    )
)


print(
    cerrar_ticket_simple(
        "TK-4001"
    )
)


# Ambas funciones reutilizan exactamente
# el mismo comportamiento adicional:
#
# registrar_accion


# ------------------------------------------------------------
# 18. RESUMEN MENTAL
# ------------------------------------------------------------

# SIN DECORADOR:
#
# funcion()
#
#
# CON DECORADOR:
#
# @decorador
# def funcion():
#     ...
#
#
# Conceptualmente:
#
# funcion
# ↓
# decorador(funcion)
# ↓
# nueva función


# ------------------------------------------------------------
# 19. DECORADOR CON PARÁMETROS
# ------------------------------------------------------------

# Cuando vemos:
#
# @decorador("valor")
#
#
# existe una etapa adicional:
#
# decorador("valor")
# ↓
# devuelve un decorador
# ↓
# recibe la función
# ↓
# devuelve la función envuelta


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# DECORADOR:
#
# función que recibe otra función
# y devuelve una función con comportamiento
# adicional o modificado.
#
#
# ------------------------------------------------------------
#
# SINTAXIS:
#
# @decorador
# def funcion():
#     ...
#
#
# equivale conceptualmente a:
#
# funcion = decorador(funcion)
#
#
# ------------------------------------------------------------
#
# wrapper / envoltura:
#
# es la función interna que normalmente
# ejecuta comportamiento:
#
# antes
# ↓
# función original
# ↓
# después
#
#
# ------------------------------------------------------------
#
# *args y **kwargs:
#
# permiten crear decoradores reutilizables
# para funciones con distintos argumentos.
#
#
# ------------------------------------------------------------
#
# @wraps(funcion):
#
# conserva información de la función original.
#
#
# ------------------------------------------------------------
#
# DECORADOR CON PARÁMETROS:
#
# @requiere_rol("Administrador")
#
# agrega una etapa para configurar
# el decorador.
#
#
# ------------------------------------------------------------
#
# USOS REALES:
#
# Flask
# autenticación
# permisos
# logging
# validación
# caché
# testing
#
#
# ------------------------------------------------------------
#
# REGLA PRÁCTICA:
#
# utilizar un decorador cuando existe
# comportamiento reutilizable que debe
# aplicarse alrededor de varias funciones.