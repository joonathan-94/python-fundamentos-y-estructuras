# ==============================================================================
# PERGAMINO DE SABIDURÍA: MÉTODOS DE LISTAS EN PYTHON
# Instruido por: Tu Sensei de Programación (Ing. Harvard / Maestro del Código)
# ==============================================================================
# 
# Aprendiz, ejecuta este script en tu consola. Lee el código y observa 
# lo que imprime. He diseñado esta clase maestra especialmente para ti.
# Las listas en Python son colecciones ordenadas, mutables (se pueden cambiar) 
# y permiten elementos duplicados.
# ==============================================================================

print("\n" + "="*50)
print("INICIANDO EL ENTRENAMIENTO DE LISTAS")
print("="*50 + "\n")

# Nuestra lista base de entrenamiento
lenguajes = ["HTML", "CSS", "JavaScript"]
print(f"1. Empezamos con tu base actual de conocimientos: {lenguajes}")

# ------------------------------------------------------------------------------
# CAPÍTULO 1: AGREGAR ELEMENTOS (Creciendo tu arsenal)
# ------------------------------------------------------------------------------
print("\n--- CAPÍTULO 1: AGREGANDO ELEMENTOS ---")

# 1. append(elemento)
# Agrega un elemento AL FINAL de la lista. 
lenguajes.append("Python")
print(f"-> Después de append('Python'): {lenguajes}")
# Sensei dice: Usa append cuando solo necesites meter un dato rápido al final.

# 2. insert(índice, elemento)
# Inserta un elemento en una POSICIÓN ESPECÍFICA (recuerda, empezamos a contar desde 0).
lenguajes.insert(0, "SQL") # Lo ponemos de primerito
print(f"-> Después de insert(0, 'SQL'): {lenguajes}")
# Sensei dice: Muy útil cuando el orden de los datos es crítico para tu lógica.

# 3. extend(iterable)
# Toma otra lista (o cualquier iterable) y une sus elementos al final de la tuya.
tecnologias_extra = ["Git", "GitHub"]
lenguajes.extend(tecnologias_extra)
print(f"-> Después de extend(['Git', 'GitHub']): {lenguajes}")
# Sensei dice: Ojo, no es lo mismo que append. Si haces append de una lista, 
# metes una lista DENTRO de la lista. Extend saca los elementos y los une.


# ------------------------------------------------------------------------------
# CAPÍTULO 2: ELIMINAR ELEMENTOS (Limpiando el código)
# ------------------------------------------------------------------------------
print("\n--- CAPÍTULO 2: ELIMINANDO ELEMENTOS ---")

# 4. remove(elemento)
# Busca el PRIMER elemento que coincida con el valor y lo elimina.
lenguajes.remove("CSS") 
print(f"-> Después de remove('CSS'): {lenguajes}")
# Sensei dice: Cuidado, si el elemento no existe, Python te lanzará un error (ValueError).

# 5. pop(índice)
# Elimina y TE DEVUELVE el elemento en la posición dada. 
# Si no le pasas número, elimina el ÚLTIMO.
ultimo_aprendido = lenguajes.pop()
print(f"-> Hicimos pop(). El elemento sacado fue: '{ultimo_aprendido}'")
print(f"-> La lista quedó así: {lenguajes}")
# Sensei dice: pop() es oro puro cuando necesitas procesar un dato y sacarlo 
# de la fila al mismo tiempo.

# 6. clear()
# Vacía la lista por completo. Queda viva, pero sin nada por dentro.
lista_temporal = ["Bug 1", "Bug 2", "Error fatal"]
print(f"\nLista de bugs antes de clear: {lista_temporal}")
lista_temporal.clear()
print(f"Lista de bugs después de clear: {lista_temporal} (¡Código limpio!)")


# ------------------------------------------------------------------------------
# CAPÍTULO 3: BÚSQUEDA Y ANÁLISIS (Conociendo tus datos)
# ------------------------------------------------------------------------------
print("\n--- CAPÍTULO 3: BÚSQUEDA Y ANÁLISIS ---")

# Vamos a crear una nueva lista para esto
notas_curso = [85, 90, 100, 90, 75, 90, 100]
print(f"Nuevos datos de notas: {notas_curso}")

# 7. index(elemento)
# Te dice en qué POSICIÓN (índice) se encuentra la primera aparición del elemento.
posicion_cien = notas_curso.index(100)
print(f"-> El primer 100 está en el índice: {posicion_cien}")

# 8. count(elemento)
# Cuenta CUÁNTAS VECES aparece un elemento en la lista.
veces_noventa = notas_curso.count(90)
print(f"-> La nota 90 aparece {veces_noventa} veces.")


# ------------------------------------------------------------------------------
# CAPÍTULO 4: ORDEN Y ESTRUCTURA (El arte de la elegancia)
# ------------------------------------------------------------------------------
print("\n--- CAPÍTULO 4: ORDEN Y ESTRUCTURA ---")

puntos = [45, 12, 89, 5, 100, 23]
print(f"Puntos desordenados: {puntos}")

# 9. sort()
# Ordena la lista de forma ASCENDENTE por defecto. Modifica la lista original.
puntos.sort()
print(f"-> Después de sort() (Menor a mayor): {puntos}")

# Puedes pasarle reverse=True para ordenar de mayor a menor
puntos.sort(reverse=True)
print(f"-> Después de sort(reverse=True) (Mayor a menor): {puntos}")

# 10. reverse()
# Simplemente le da LA VUELTA a la lista actual, sin importar si estaba ordenada o no.
palabras = ["camino", "el", "es", "Este"]
palabras.reverse()
print(f"-> Después de reverse() a ['camino', 'el', 'es', 'Este']: {palabras}")

# 11. copy()
# Crea una copia superficial de la lista. Fundamental para no dañar la original.
# Si haces lista_B = lista_A, ambas apuntan a lo mismo y si cambias B, cambias A.
puntos_respaldo = puntos.copy()
print(f"-> Copia de seguridad creada: {puntos_respaldo}")


# ==============================================================================
# EL DOJO DE PRÁCTICA: EJERCICIOS PARA EL APRENDIZ
# ==============================================================================
print("\n" + "="*50)
print("EL DOJO: TU TURNO DE ESCRIBIR CÓDIGO")
print("="*50)
print("""
A continuación, tienes 4 ejercicios básicos. 
Descomenta las líneas debajo de cada instrucción y escribe tu lógica.
¡Demuéstrame de qué estás hecho!
""")

# --- EJERCICIO 1: El Inventario ---
# Tienes esta lista:
inventario = ["Teclado", "Ratón", "Monitor"]
# Tu misión: 
# 1. Agrega "Auriculares" al final.
# 2. Inserta "Alfombrilla" en la primera posición (índice 0).
# 3. Imprime la lista final.

# ESCRIBE TU CÓDIGO AQUÍ:
# 
# 
# print(inventario)


# --- EJERCICIO 2: Limpieza de Base de Datos ---
# Tienes esta lista de usuarios:
usuarios = ["admin", "invitado", "hacker", "usuario_comun"]
# Tu misión:
# 1. Elimina al "hacker" usando su nombre.
# 2. Saca al último usuario de la lista usando pop() y guárdalo en una variable.
# 3. Imprime la lista resultante y el usuario que sacaste.

# ESCRIBE TU CÓDIGO AQUÍ:
# 
# 
# print(usuarios)


# --- EJERCICIO 3: Estadísticas del Servidor ---
tiempos_respuesta_ms = [120, 45, 300, 45, 80, 45, 90]
# Tu misión:
# 1. Cuenta cuántas veces se repite el tiempo '45' y muéstralo en un print.
# 2. Encuentra en qué índice ocurre el tiempo '300' y muéstralo en un print.

# ESCRIBE TU CÓDIGO AQUÍ:
# 
# 
# 


# --- EJERCICIO 4: Ordenando Prioridades ---
tareas = ["Desplegar app", "Revisar logs", "Arreglar bug", "Tomar café"]
# Tu misión:
# 1. Ordena la lista alfabéticamente de la A a la Z.
# 2. Imprime la lista ordenada.
# 3. Dale la vuelta a la lista (reverse) y vuélvela a imprimir.

# ESCRIBE TU CÓDIGO AQUÍ:
# 
# 
# 

print("\n¡Que el código te acompañe! Guarda este script y consúltalo siempre que lo necesites.")