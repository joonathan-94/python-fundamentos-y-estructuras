# ============================================================
# DICCIONARIOS EN PYTHON
# ============================================================
#
# Un diccionario (dict) es una estructura de datos que almacena
# información mediante pares:
#
# clave: valor
#
# Ejemplo:
#
# pokemon = {
#     "nombre": "Totodile",
#     "tipo": "Agua",
#     "generacion": 2
# }
#
# En este caso:
#
# "nombre"      -> clave
# "Totodile"    -> valor
#
# Los diccionarios son:
#
# - mutables;
# - accesibles mediante claves;
# - capaces de almacenar valores de distintos tipos;
# - estructuras que conservan el orden de inserción.
#
# Son especialmente útiles cuando queremos representar
# información con atributos identificables.
#
# Algunos usos reales:
#
# - datos de un ticket;
# - información de un usuario;
# - configuración de una aplicación;
# - respuestas de APIs;
# - datos JSON;
# - parámetros;
# - registros procesados desde archivos;
# - información proveniente de una base de datos.
#
# En desarrollo backend, los diccionarios aparecen
# constantemente.


# ------------------------------------------------------------
# 1. CREACIÓN DE UN DICCIONARIO
# ------------------------------------------------------------

pokemon_totodile = {
    "nombre": "Totodile",
    "tipo": "Agua",
    "generacion": 2
}

print(pokemon_totodile)
print(type(pokemon_totodile))


# También podemos crear un diccionario vacío.

ticket_nuevo = {}

print(ticket_nuevo)


# ------------------------------------------------------------
# 2. CLAVES Y VALORES
# ------------------------------------------------------------

# Cada elemento está formado por:
#
# clave: valor

auto_clasico = {
    "modelo": "Chevrolet Camaro",
    "anio": 1967,
    "motor": "V8",
    "disponible": True
}

print(auto_clasico)


# Las claves son únicas dentro de un mismo diccionario.
#
# Si asignamos nuevamente una clave existente,
# reemplazamos su valor.

auto_clasico["disponible"] = False

print(auto_clasico)


# ------------------------------------------------------------
# 3. QUÉ PUEDE SER UNA CLAVE
# ------------------------------------------------------------

# Las claves de un diccionario deben ser hashables.
#
# Para nuestros fundamentos podemos pensar principalmente
# en claves como:
#
# - strings;
# - números;
# - tuplas que contengan elementos hashables.
#
# Las claves más habituales en aplicaciones son strings.

faraon = {
    "nombre": "Tutankamón",
    "dinastia": 18,
    "titulo": "Faraón"
}

print(faraon)


# Una lista NO puede utilizarse como clave porque
# las listas son mutables.
#
# Esto produciría TypeError:
#
# ejemplo = {
#     ["nombre"]: "Tutankamón"
# }


# Los valores, en cambio, pueden ser de muchos tipos.

datos_servidor = {
    "nombre": "SRV-01",
    "activo": True,
    "puerto": 5432,
    "carga": 72.5
}

print(datos_servidor)


# ------------------------------------------------------------
# 4. ACCEDER A UN VALOR MEDIANTE SU CLAVE
# ------------------------------------------------------------

ticket_soporte = {
    "id": "WD-3001",
    "titulo": "Problema de conexión",
    "prioridad": "Alta",
    "estado": "Nuevo"
}

titulo_ticket = ticket_soporte["titulo"]
estado_ticket = ticket_soporte["estado"]

print("Título:", titulo_ticket)
print("Estado:", estado_ticket)


# A diferencia de una lista:
#
# lista[0]
#
# normalmente accedemos a un diccionario mediante una clave:
#
# diccionario["clave"]


# ------------------------------------------------------------
# 5. KeyError AL ACCEDER A UNA CLAVE INEXISTENTE
# ------------------------------------------------------------

# Si utilizamos [] con una clave que no existe:

# ticket_soporte["tecnico"]

# Python produce:
#
# KeyError


# Esto no significa que utilizar [] sea incorrecto.
#
# Es apropiado cuando esperamos que la clave exista.
#
# Si la ausencia de esa clave representa un error en nuestros
# datos, KeyError puede ayudarnos a detectar el problema.


# ------------------------------------------------------------
# 6. get()
# ------------------------------------------------------------

# get() resulta útil cuando una clave puede no existir.
#
# Si encuentra la clave, devuelve su valor.

prioridad_actual = ticket_soporte.get("prioridad")

print(prioridad_actual)


# Si la clave no existe, devuelve None por defecto.

tecnico_actual = ticket_soporte.get("tecnico")

print(tecnico_actual)


# También podemos proporcionar un valor predeterminado.

tecnico_mostrado = ticket_soporte.get(
    "tecnico",
    "Sin técnico asignado"
)

print(tecnico_mostrado)


# IMPORTANTE:
#
# [] y get() no son enemigos ni uno reemplaza siempre al otro.
#
# diccionario["clave"]
# → útil cuando la clave debería existir.
#
# diccionario.get("clave")
# → útil cuando la clave podría estar ausente.


# ------------------------------------------------------------
# 7. AGREGAR UNA NUEVA CLAVE
# ------------------------------------------------------------

# Podemos agregar información utilizando una nueva clave.

ticket_soporte["tecnico"] = "Brock"

print(ticket_soporte)


# Antes "tecnico" no existía.
# Después de la asignación pasa a formar parte del diccionario.


# ------------------------------------------------------------
# 8. MODIFICAR UN VALOR EXISTENTE
# ------------------------------------------------------------

ticket_soporte["estado"] = "En progreso"

print(ticket_soporte)


# Como la clave "estado" ya existía,
# su valor fue reemplazado.


# ------------------------------------------------------------
# 9. COMPROBAR SI UNA CLAVE EXISTE
# ------------------------------------------------------------

# El operador in comprueba las CLAVES del diccionario.

tiene_estado = "estado" in ticket_soporte
tiene_resolucion = "resolucion" in ticket_soporte

print("¿Tiene estado?:", tiene_estado)
print("¿Tiene resolución?:", tiene_resolucion)


# También podemos utilizar not in.

sin_resolucion = "resolucion" not in ticket_soporte

print(sin_resolucion)


# ------------------------------------------------------------
# 10. len()
# ------------------------------------------------------------

# len() devuelve la cantidad de pares clave-valor.

vehiculo_bel_air = {
    "marca": "Chevrolet",
    "modelo": "Bel Air",
    "anio": 1957
}

cantidad_campos = len(vehiculo_bel_air)

print("Cantidad de campos:", cantidad_campos)


# ------------------------------------------------------------
# 11. keys()
# ------------------------------------------------------------

# keys() devuelve una vista de las claves del diccionario.

claves_ticket = ticket_soporte.keys()

print(claves_ticket)


# No es necesario convertir siempre el resultado a lista.
#
# Podemos recorrer directamente esta vista:

for clave_ticket in ticket_soporte.keys():
    print(clave_ticket)


# También es posible recorrer directamente el diccionario:

for clave_ticket_actual in ticket_soporte:
    print(clave_ticket_actual)


# Por defecto, iterar un diccionario recorre sus claves.


# ------------------------------------------------------------
# 12. values()
# ------------------------------------------------------------

# values() devuelve una vista de los valores.

valores_ticket = ticket_soporte.values()

print(valores_ticket)


for valor_ticket in ticket_soporte.values():
    print(valor_ticket)


# ------------------------------------------------------------
# 13. items()
# ------------------------------------------------------------

# items() devuelve una vista de pares:
#
# (clave, valor)
#
# Esto es especialmente útil junto con for.

camaro_1967 = {
    "modelo": "Camaro",
    "anio": 1967,
    "motor": "V8"
}

for campo_auto, valor_auto in camaro_1967.items():
    print(campo_auto, ":", valor_auto)


# Esta estructura:
#
# for clave, valor in diccionario.items():
#
# aparecerá con mucha frecuencia en código Python.


# ------------------------------------------------------------
# 14. LAS VISTAS NO SON LISTAS
# ------------------------------------------------------------

# keys(), values() e items() devuelven objetos de vista.
#
# Si realmente necesitamos una lista, podemos convertirlos.

lista_claves_auto = list(camaro_1967.keys())

print(lista_claves_auto)
print(type(lista_claves_auto))


# No debemos realizar esta conversión automáticamente
# si no existe una razón para necesitar una lista.


# ------------------------------------------------------------
# 15. update()
# ------------------------------------------------------------

# update() permite agregar o actualizar varios pares
# clave-valor de una sola vez.

triceratops = {
    "nombre": "Triceratops",
    "periodo": "Cretácico"
}

datos_adicionales = {
    "alimentacion": "Herbívoro",
    "extinto": True
}

triceratops.update(datos_adicionales)

print(triceratops)


# Si update() recibe una clave existente,
# reemplaza su valor.

triceratops.update({
    "periodo": "Cretácico tardío"
})

print(triceratops)


# ------------------------------------------------------------
# 16. setdefault()
# ------------------------------------------------------------

# setdefault() busca una clave.
#
# Si existe:
# devuelve el valor existente.
#
# Si no existe:
# crea la clave utilizando el valor predeterminado indicado.

configuracion = {
    "idioma": "es"
}

tema_actual = configuracion.setdefault(
    "tema",
    "claro"
)

print(tema_actual)
print(configuracion)


# Si ejecutamos:

configuracion.setdefault("idioma", "en")


# "idioma" ya existe, por lo que NO se reemplaza.

print(configuracion)


# setdefault() es útil en determinados casos,
# pero para modificaciones normales suele ser más claro
# utilizar asignación directa o update().


# ------------------------------------------------------------
# 17. ELIMINAR CON pop()
# ------------------------------------------------------------

# pop(clave) elimina la clave y devuelve su valor.

usuario_temporal = {
    "nombre": "Saul Goodman",
    "rol": "Invitado",
    "token_temporal": "XYZ123"
}

token_eliminado = usuario_temporal.pop("token_temporal")

print("Token eliminado:", token_eliminado)
print(usuario_temporal)


# También podemos proporcionar un valor por defecto para evitar
# KeyError si la clave no existe.

resultado_eliminacion = usuario_temporal.pop(
    "telefono",
    None
)

print(resultado_eliminacion)


# ------------------------------------------------------------
# 18. ELIMINAR CON del
# ------------------------------------------------------------

# del permite eliminar directamente una clave.

configuracion_app = {
    "tema": "oscuro",
    "idioma": "es",
    "debug": True
}

del configuracion_app["debug"]

print(configuracion_app)


# Si la clave no existe, del produce KeyError.


# ------------------------------------------------------------
# 19. popitem()
# ------------------------------------------------------------

# popitem() elimina y devuelve el último par clave-valor
# insertado en el diccionario.

datos_temporales = {
    "nombre": "Velociraptor",
    "periodo": "Cretácico",
    "ubicacion": "Norteamérica"
}

ultimo_par = datos_temporales.popitem()

print("Eliminado:", ultimo_par)
print(datos_temporales)


# ------------------------------------------------------------
# 20. clear()
# ------------------------------------------------------------

# clear() elimina todos los elementos.

cache_temporal = {
    "dato_1": 100,
    "dato_2": 200
}

cache_temporal.clear()

print(cache_temporal)


# Resultado:
#
# {}


# ------------------------------------------------------------
# 21. DICCIONARIOS ANIDADOS
# ------------------------------------------------------------

# Un valor puede ser otro diccionario.
#
# Esto es habitual cuando representamos información
# estructurada.

ticket_detallado = {
    "id": "WD-4001",
    "titulo": "Error de impresión",
    "solicitante": {
        "nombre": "Tony Soprano",
        "area": "Administración"
    }
}

print(ticket_detallado)


# Para acceder al nombre:

nombre_solicitante = ticket_detallado["solicitante"]["nombre"]

print(nombre_solicitante)


# Este tipo de estructura aparece con frecuencia en datos JSON
# y respuestas de APIs.


# ------------------------------------------------------------
# 22. LISTAS DENTRO DE DICCIONARIOS
# ------------------------------------------------------------

# Como ya estudiamos listas, podemos utilizarlas como valores.

pokemon_entrenador = {
    "entrenador": "Ash",
    "equipo": [
        "Pikachu",
        "Charizard",
        "Squirtle"
    ]
}

print(pokemon_entrenador["equipo"])


# Podemos recorrer esa lista normalmente.

for nombre_pokemon in pokemon_entrenador["equipo"]:
    print(nombre_pokemon)


# ------------------------------------------------------------
# 23. LISTA DE DICCIONARIOS
# ------------------------------------------------------------

# Esta estructura es extremadamente común.
#
# Imaginemos varios tickets:

tickets_soporte = [
    {
        "id": "WD-5001",
        "prioridad": "Alta"
    },
    {
        "id": "WD-5002",
        "prioridad": "Media"
    },
    {
        "id": "WD-5003",
        "prioridad": "Crítica"
    }
]


for registro_ticket in tickets_soporte:
    print(
        registro_ticket["id"],
        registro_ticket["prioridad"]
    )


# Esta estructura puede aparecer cuando:
#
# - obtenemos varios registros de una API;
# - procesamos resultados;
# - trabajamos con JSON;
# - construimos datos temporales;
# - transformamos filas provenientes de una base de datos.
#
# Más adelante veremos estos contextos con mayor profundidad.


# ------------------------------------------------------------
# 24. copy()
# ------------------------------------------------------------

# copy() crea una COPIA SUPERFICIAL del diccionario.

datos_corvette = {
    "modelo": "Corvette Stingray",
    "anio": 1963
}

copia_corvette = datos_corvette.copy()

copia_corvette["anio"] = 1967

print("Original:", datos_corvette)
print("Copia:", copia_corvette)


# Modificar directamente un valor simple en la copia
# no cambia el mismo campo del diccionario original.


# ------------------------------------------------------------
# 25. CUIDADO CON LAS COPIAS SUPERFICIALES
# ------------------------------------------------------------

# Si existen objetos mutables dentro del diccionario,
# esos objetos internos pueden continuar compartidos.

registro_pokemon = {
    "entrenador": "Misty",
    "equipo": ["Staryu", "Starmie"]
}

copia_registro = registro_pokemon.copy()

copia_registro["equipo"].append("Psyduck")


print("Original:", registro_pokemon)
print("Copia:", copia_registro)


# Psyduck aparecerá en ambas estructuras porque copy()
# realizó una copia superficial.
#
# No profundizaremos todavía en deepcopy().
# Lo estudiaremos cuando realmente sea necesario.


# ------------------------------------------------------------
# 26. ASIGNACIÓN NO SIGNIFICA COPIA
# ------------------------------------------------------------

datos_originales = {
    "estado": "Nuevo"
}

misma_referencia = datos_originales

misma_referencia["estado"] = "En progreso"

print(datos_originales)
print(misma_referencia)


# Ambos nombres hacen referencia al mismo diccionario.


# ------------------------------------------------------------
# 27. EJEMPLO REALISTA: PROCESAR UN TICKET
# ------------------------------------------------------------

ticket_workdesk = {
    "id": "WD-6001",
    "titulo": "Usuario sin acceso al sistema",
    "prioridad": "Alta",
    "estado": "Nuevo",
    "tecnico": None
}


# Consultamos un campo obligatorio.

titulo_workdesk = ticket_workdesk["titulo"]


# Consultamos un campo que podría no existir.

ubicacion_workdesk = ticket_workdesk.get(
    "ubicacion",
    "Sin ubicación registrada"
)


# Asignamos un técnico.

ticket_workdesk["tecnico"] = "Elliot Alderson"


# Actualizamos el estado.

ticket_workdesk["estado"] = "Asignado"


# Comprobamos una clave.

tiene_prioridad = "prioridad" in ticket_workdesk


# Recorremos todos los datos.

for campo_workdesk, valor_workdesk in ticket_workdesk.items():
    print(f"{campo_workdesk}: {valor_workdesk}")


print("Título:", titulo_workdesk)
print("Ubicación:", ubicacion_workdesk)
print("¿Tiene prioridad?:", tiene_prioridad)


# Este ejemplo sigue siendo educativo.
#
# Un ticket real de WorkDesk terminará representándose mediante
# modelos y registros persistentes, no simplemente con un
# diccionario escrito manualmente.
#
# Sin embargo, comprender dict será fundamental para trabajar
# posteriormente con esos datos.


# ============================================================
# CUÁNDO UTILIZAR UN DICCIONARIO
# ============================================================
#
# Utiliza un diccionario cuando necesitas relacionar
# nombres o identificadores con valores.
#
# Por ejemplo:
#
# {
#     "nombre": "..."
#     "edad": ...
#     "activo": ...
# }
#
# suele ser más expresivo que:
#
# ["...", ..., ...]
#
# cuando cada posición representa un atributo diferente.
#
# Un diccionario es especialmente apropiado cuando queremos
# consultar información mediante nombres significativos.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# Un diccionario:
#
# - almacena pares clave-valor;
# - es mutable;
# - conserva el orden de inserción;
# - requiere claves hashables;
# - permite valores de diferentes tipos.
#
#
# OPERACIONES FUNDAMENTALES
#
# diccionario["clave"]
# → acceso directo.
#
# diccionario["clave"] = valor
# → agregar o modificar.
#
# diccionario.get("clave")
# → acceso cuando la clave puede no existir.
#
# "clave" in diccionario
# → comprobar existencia de una clave.
#
# diccionario.items()
# → recorrer claves y valores.
#
# diccionario.update(...)
# → actualizar múltiples pares.
#
# diccionario.pop(...)
# → eliminar y recuperar un valor.
#
#
# PATRÓN MUY FRECUENTE
#
# for clave, valor in diccionario.items():
#     ...
#
#
# Los diccionarios serán una estructura fundamental para
# backend, APIs, automatizaciones, integraciones y procesamiento
# de datos.