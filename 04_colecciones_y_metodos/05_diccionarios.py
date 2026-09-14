# ==============================================================================
# CLASE MAGISTRAL: MÉTODOS DE DICCIONARIOS (dict) EN PYTHON
# Instructor: Tu Sensei de Programación
# ==============================================================================

# Un diccionario es una estructura de datos mutable, desordenada (hasta Python 3.6) 
# y que almacena pares de "clave: valor". 
# REGLA DE ORO: Las claves deben ser inmutables (strings, números, tuplas), 
# pero los valores pueden ser cualquier cosa (listas, otros diccionarios, sets, etc).

print("--- 1. CREACIÓN DE DICCIONARIOS ---")
# Imaginemos un ticket de soporte de nivel 1 en una empresa de logística.
ticket_soporte = {
    "id_ticket": "TK-8475",
    "usuario": "bodega_central",
    "problema": "Falla conexión de red",
    "estado": "Abierto",
    "prioridad": 1
}
print("Ticket original:", ticket_soporte)


print("\n--- 2. MÉTODOS DE ACCESO Y CONSULTA ---")

# a) .get(clave, valor_por_defecto)
# Es la forma más segura de buscar algo. Si buscas una clave que no existe 
# directamente con corchetes (ej: ticket_soporte["tecnico"]), el programa explotará con un error. 
# .get() te protege devolviendo 'None' o un valor que tú elijas si no encuentra la clave.
tecnico_asignado = ticket_soporte.get("tecnico", "No asignado aún")
estado_actual = ticket_soporte.get("estado")

print("Técnico:", tecnico_asignado) # Imprime: No asignado aún
print("Estado:", estado_actual)     # Imprime: Abierto

# b) .keys()
# Devuelve una vista con todas las claves (como si vieras los nombres de las columnas en una BD).
# Lo convertimos a lista (que ya dominas) para verlo mejor.
claves_del_ticket = list(ticket_soporte.keys())
print("Claves disponibles:", claves_del_ticket)

# c) .values()
# Devuelve todos los valores del diccionario.
valores_del_ticket = list(ticket_soporte.values())
print("Valores del ticket:", valores_del_ticket)

# d) .items()
# Devuelve tuplas de (clave, valor). Excelente para cuando aprendamos bucles más adelante.
pares_ticket = list(ticket_soporte.items())
print("Pares Clave-Valor:", pares_ticket)


print("\n--- 3. MÉTODOS DE AGREGADO Y MODIFICACIÓN ---")

# a) .update(otro_diccionario)
# Actualiza el diccionario con nuevos pares clave/valor. 
# Si la clave ya existe, sobrescribe el valor. Si no existe, la crea.
actualizacion = {
    "tecnico": "ingeniero_master", # Nueva clave
    "estado": "En progreso",       # Clave existente (se sobrescribe)
    "tiempo_resolucion_hrs": 2.5   # Nueva clave
}
ticket_soporte.update(actualizacion)
print("Ticket actualizado con .update():\n", ticket_soporte)

# b) .setdefault(clave, valor_por_defecto)
# Busca una clave. Si existe, devuelve su valor y NO hace nada más.
# Si NO existe, la crea y le asigna el valor que le pases.
# Muy útil para inicializar datos sin pisar los que ya existen.
nota = ticket_soporte.setdefault("notas_cierre", "Sin observaciones")
prioridad = ticket_soporte.setdefault("prioridad", 5) # Ya existe como 1, NO la cambiará

print("Nota devuelta por setdefault:", nota)
print("Prioridad después de setdefault:", ticket_soporte["prioridad"]) # Sigue siendo 1


print("\n--- 4. MÉTODOS DE ELIMINACIÓN ---")

# a) .pop(clave, valor_por_defecto)
# Extrae y elimina un elemento basado en su clave. Si no existe y no das valor por defecto, da error.
tiempo = ticket_soporte.pop("tiempo_resolucion_hrs")
print("Se eliminó y guardó el tiempo:", tiempo)
print("Ticket sin el tiempo:", ticket_soporte)

# b) .popitem()
# Elimina y devuelve el ÚLTIMO par clave-valor que fue insertado en el diccionario (como una tupla).
ultimo_elemento_eliminado = ticket_soporte.popitem()
print("Se eliminó el último elemento:", ultimo_elemento_eliminado)

# c) .clear()
# Vacía el diccionario por completo, lo deja como {}. 
ticket_respaldo = {"id": 999, "data": "temporal"}
ticket_respaldo.clear()
print("Ticket respaldo tras .clear():", ticket_respaldo)


print("\n--- 5. MÉTODOS DE COPIA ---")

# a) .copy()
# Crea una copia superficial (shallow copy). Si igualas diccionarios con "=" (dict1 = dict2), 
# ambos apuntarán al mismo espacio en memoria y si modificas uno, se modifica el otro.
# .copy() crea un diccionario independiente.
ticket_clon = ticket_soporte.copy()

# Modificamos el clon para demostrar que son independientes
ticket_clon.update({"estado": "Cerrado"})

print("Estado ticket original:", ticket_soporte["estado"]) # Sigue En progreso
print("Estado ticket clon:", ticket_clon["estado"])        # Cambió a Cerrado


# ==============================================================================
# ÁREA DE ENTRENAMIENTO: EJERCICIOS PARA EL APRENDIZ
# ==============================================================================
# Instrucciones: Debajo de cada enunciado, escribe el código para resolverlo.
# Recuerda usar SOLAMENTE lo que hemos aprendido (nada de ifs, fors, ni defs).

print("\n--- RESOLUCIÓN DE EJERCICIOS ---")

# EJERCICIO 1: Creación y Acceso Seguro
# Crea un diccionario llamado 'perfil_usuario' con las claves: "nombre", "edad", "rol" (usa datos ficticios).
# Luego, intenta obtener la clave "telefono" usando el método seguro para que, 
# si no existe, devuelva el string "Teléfono no registrado". Imprime el resultado.

# [TU CÓDIGO AQUÍ]


# EJERCICIO 2: Actualización Masiva
# Tienes el siguiente registro de un servidor:
servidor_web = {"ip": "192.168.1.10", "os": "Linux", "estado": "offline"}
# Usando UN SOLO MÉTODO, cambia el "estado" a "online" y agrega una nueva clave 
# "ultima_revision" con el valor "hoy". Imprime el diccionario resultante.

# [TU CÓDIGO AQUÍ]


# EJERCICIO 3: Limpieza Quirúrgica
# Tienes la siguiente configuración de una app web:
config_app = {"tema": "oscuro", "idioma": "es", "notificaciones": True, "token_sesion": "abc123xyz"}
# Usando el método correspondiente, extrae (y elimina) el "token_sesion" guardándolo 
# en una variable llamada 'token_seguro'. Imprime el 'token_seguro' y luego imprime 
# 'config_app' para comprobar que ya no contiene esa clave.

# [TU CÓDIGO AQUÍ]


# EJERCICIO 4: Vistas y Tuplas
# Utilizando el diccionario 'config_app' resultante del ejercicio anterior:
# 1. Obtén una lista de solo sus claves e imprímela.
# 2. Obtén una lista de solo sus valores e imprímela.
# 3. Obtén la lista de tuplas (clave, valor) e imprímela.

# [TU CÓDIGO AQUÍ]