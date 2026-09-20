# ==============================================================================
# 🐍 CLASE MAGISTRAL: MÉTODOS Y MANEJO DE TUPLAS EN PYTHON
# ==============================================================================

print("--- INICIANDO CLASE DE TUPLAS ---\n")

# 1. EL CONCEPTO DE INMUTABILIDAD
# Las tuplas se crean usando paréntesis ()
puertos_servidor = (80, 443, 8080, 5432)

print("Tupla original de puertos:", puertos_servidor)

# Si intentaras hacer esto: puertos_servidor[0] = 81
# Python te arrojaría un error (TypeError), porque la tupla no se puede modificar.
# Esta es su mayor fortaleza: protegen los datos para que no cambien por accidente.


# ==============================================================================
# 2. LOS DOS MÉTODOS OFICIALES DE LAS TUPLAS
# Como no podemos modificar (append, remove, pop), solo podemos "consultar".
# ==============================================================================

# MÉTODO 1: .count(valor)
# Busca en la tupla el valor que le pases y cuenta cuántas veces aparece.
# Documentación: Devuelve el número de ocurrencias de un valor.

codigos_estado = (200, 404, 200, 500, 200, 403, 404)
cantidad_exitos = codigos_estado.count(200)
cantidad_no_encontrado = codigos_estado.count(404)

print("\n--- MÉTODO .count() ---")
print("El código 200 (OK) aparece:", cantidad_exitos, "veces.")
print("El código 404 (Not Found) aparece:", cantidad_no_encontrado, "veces.")


# MÉTODO 2: .index(valor)
# Busca de izquierda a derecha el valor que le pases y te dice en qué POSICIÓN (índice) está.
# Recuerda: En programación empezamos a contar desde el cero (0).
# Si el valor está repetido, solo te da la posición del primero que encuentra.

tecnologias_web = ("HTML", "CSS", "JavaScript", "Python", "SQL")
posicion_python = tecnologias_web.index("Python")

print("\n--- MÉTODO .index() ---")
print("La tupla es:", tecnologias_web)
print("Python se encuentra en el índice:", posicion_python)


# ==============================================================================
# 3. TRUCOS NINJA CON TUPLAS (Usando lo que ya sabes)
# ==============================================================================

# A. Desempaquetado (Unpacking): 
# Puedes asignar los elementos de una tupla directamente a variables individuales.
configuracion_bd = ("localhost", "root", "password123")
host, usuario, contraseña = configuracion_bd

print("\n--- DESEMPAQUETADO ---")
print("Host extraído:", host)
print("Usuario extraído:", usuario)

# B. Transformación (Tupla <-> Lista):
# Si en algún momento NECESITAS modificar una tupla, el truco es:
# 1. Convertirla a lista. 2. Modificarla. 3. Volverla a tupla.
tupla_original = ("Rojo", "Verde", "Azul")
lista_temporal = list(tupla_original)
lista_temporal.append("Amarillo")          # Modificamos la lista
tupla_modificada = tuple(lista_temporal)   # Regresamos a tupla

print("\n--- TRANSFORMACIÓN ---")
print("Tupla original:", tupla_original)
print("Tupla modificada:", tupla_modificada)


# ==============================================================================
# 🏋️‍♂️ ZONA DE ENTRENAMIENTO: EJERCICIOS PARA CONSOLIDAR
# ==============================================================================
print("\n--- INICIANDO EJERCICIOS (Descomenta el código para resolverlos) ---")

# EJERCICIO 1: Análisis de accesos
# Tienes una tupla con los roles que han accedido a un sistema hoy.
# Usando el método correspondiente, averigua cuántas veces accedió un "admin" 
# y cuántas veces accedió un "guest". Imprime los resultados.

accesos = ("guest", "user", "admin", "guest", "guest", "admin", "user")

# Escribe tu solución aquí:
total_admin = accesos.count('admin')
total_guest = accesos.count('guest')
print(total_admin)
print(total_guest)


# EJERCICIO 2: Buscando la configuración
# Tienes una tupla con las resoluciones de pantalla soportadas por tu futura app.
# Encuentra en qué índice exacto se encuentra la resolución "1920x1080".

resoluciones = ("800x600", "1280x720", "1920x1080", "2560x1440")

# Escribe tu solución aquí:
indice_fullhd = resoluciones.index("1920x1080")
print("El índice de 1920x1080 es:", indice_fullhd)


# EJERCICIO 3: Operaciones combinadas (Listas, Tuplas y Sets)
# Tienes una lista de permisos de usuario. 
# 1. Añade "escribir" a la lista.
# 2. Convierte esa lista en una tupla para que ya no se pueda modificar.
# 3. (Opcional usando Sets) Imagina que la lista original tuviera duplicados, 
#    pásala primero por un set para limpiarla, y luego conviértela a tupla.

permisos_lista = ["leer", "ejecutar", "leer"]

# Escribe tu solución aquí:
# ...

print("\n¡Excelente trabajo! Has dominado las tuplas.")