# ==============================================================================
# CLASE MAGISTRAL: MÉTODOS DE SETS (CONJUNTOS) EN PYTHON
# INSTRUCTOR: Tu Sensei de Programación
# ALUMNO: Futuro Desarrollador Web y Colega Ingeniero
# ==============================================================================

# Un 'set' (conjunto) en Python es una colección DESORDENADA de elementos ÚNICOS.
# A diferencia de las listas o tuplas, los sets no tienen índice (no puedes hacer mi_set[0])
# y NO permiten elementos duplicados. Son perfectos para limpiar datos.

print("--- INICIANDO LA LECCIÓN DE SETS ---\n")

# 1. CREACIÓN DE SETS
# ------------------------------------------------------------------------------
# Se crean usando llaves {} (como los diccionarios, pero sin los dos puntos ':')
# o usando la función set() si partimos desde una lista o tupla.

tecnologias_web = {"html", "css", "javascript", "python"}
print("Set original:", tecnologias_web)

# Si intentamos crear un set con duplicados, Python los elimina mágicamente:
etiquetas_duplicadas = ["frontend", "backend", "frontend", "api", "api"]
etiquetas_unicas = set(etiquetas_duplicadas)
print("Lista convertida a Set (adiós duplicados):", etiquetas_unicas)
print("-" * 50)


# ==============================================================================
# 2. MÉTODOS PARA AGREGAR Y ELIMINAR ELEMENTOS
# ==============================================================================

mi_perfil = {"html", "css"}

# add(elemento): Agrega un solo elemento al set.
mi_perfil.add("python")
print("Después de add('python'):", mi_perfil)

# update(iterable): Agrega múltiples elementos (puedes pasarle una lista, tupla u otro set)
mi_perfil.update(["git", "github", "sql"])
print("Después de update(['git', 'github', 'sql']):", mi_perfil)

# remove(elemento): Elimina un elemento específico. 
# ¡OJO! Si el elemento no existe, el programa arrojará un ERROR (KeyError).
mi_perfil.remove("css")
print("Después de remove('css'):", mi_perfil)

# discard(elemento): Elimina un elemento, pero a diferencia de remove(), 
# si el elemento NO existe, NO hace nada (no rompe tu programa). ¡Muy seguro!
mi_perfil.discard("java") # No está, pero no da error.
print("Después de discard('java'):", mi_perfil)

# pop(): Elimina y devuelve un elemento "aleatorio" (recuerda que no hay orden).
# Útil si solo necesitas vaciar el set elemento por elemento sin importar cuál.
elemento_eliminado = mi_perfil.pop()
print("Elemento eliminado con pop():", elemento_eliminado)
print("Set actual:", mi_perfil)

# clear(): Vacía el set por completo.
mi_perfil.clear()
print("Después de clear() (Set vacío):", mi_perfil)
print("-" * 50)


# ==============================================================================
# 3. MÉTODOS MATEMÁTICOS (LA MAGIA DE LAS BASES DE DATOS)
# ==============================================================================
# Colega, si sabes de bases de datos, esto es pan comido para ti.
# Piensa en los diagramas de Venn o en las sentencias JOIN de SQL.

backend_dev = {"python", "sql", "git", "linux"}
frontend_dev = {"html", "css", "javascript", "git"}

# union() o el operador | : Une ambos sets (equivalente a un FULL OUTER JOIN o UNION en SQL)
# Trae todo de ambos, sin repetir los que tienen en común.
full_stack = backend_dev.union(frontend_dev)
# También se puede escribir: full_stack = backend_dev | frontend_dev
print("UNION (Todos los conocimientos combinados):", full_stack)

# intersection() o el operador & : Encuentra los elementos que están en AMBOS sets.
# (Equivalente a un INNER JOIN en SQL).
herramientas_comunes = backend_dev.intersection(frontend_dev)
# También se puede escribir: herramientas_comunes = backend_dev & frontend_dev
print("INTERSECTION (Lo que ambos perfiles comparten):", herramientas_comunes)

# difference() o el operador - : Elementos que están en el primero pero NO en el segundo.
# (Equivalente a un LEFT JOIN donde B es NULL).
solo_backend = backend_dev.difference(frontend_dev)
# También se puede escribir: solo_backend = backend_dev - frontend_dev
print("DIFFERENCE (Solo de Backend, no de Frontend):", solo_backend)

# symmetric_difference() o el operador ^ : Elementos exclusivos de cada set.
# Es decir, la unión de ambos MENOS su intersección (lo opuesto a intersection).
exclusivos = backend_dev.symmetric_difference(frontend_dev)
# También se puede escribir: exclusivos = backend_dev ^ frontend_dev
print("SYMMETRIC DIFFERENCE (Habilidades que no comparten):", exclusivos)
print("-" * 50)


# ==============================================================================
# 4. MÉTODOS DE COMPROBACIÓN (Devuelven True o False / Operadores lógicos)
# ==============================================================================

habilidades_requeridas = {"python", "sql"}
candidato_actual = {"python", "sql", "git", "html"}

# issubset() o operador <= : ¿Están TODOS los elementos del set A dentro del set B?
cumple_requisitos = habilidades_requeridas.issubset(candidato_actual)
print("¿Las habilidades requeridas son un subconjunto del candidato? (¿Cumple?):", cumple_requisitos)

# issuperset() o operador >= : Al revés, ¿El set A contiene TODOS los elementos del set B?
candidato_es_superset = candidato_actual.issuperset(habilidades_requeridas)
print("¿El candidato es superset de los requisitos?:", candidato_es_superset)

# isdisjoint() : ¿Son conjuntos totalmente distintos? (True si NO comparten NINGÚN elemento)
disenador_grafico = {"photoshop", "illustrator"}
print("¿El candidato actual no tiene nada en común con el diseñador?:", candidato_actual.isdisjoint(disenador_grafico))
print("-" * 50)


# ==============================================================================
# 5. EJERCICIOS PROPUESTOS PARA EL ALUMNO (Nivel: Bases Sólidas)
# ==============================================================================
# INSTRUCCIONES: Resuelve esto en tu archivo sin usar if/else ni bucles (for/while), 
# ya que aún no llegamos ahí. Solo usa variables, tipos de datos, diccionarios, 
# listas, tuplas, y los métodos de sets que acabamos de ver.

print("--- ÁREA DE EJERCICIOS ---")
print("Imprime los resultados de tus ejercicios aquí abajo.\n")

# EJERCICIO 1: Limpieza de Base de Datos (Deduplicación)
# Imagina que extrajiste categorías de una base de datos antigua y vienen duplicadas en una lista.
# Tu misión: Convertir esta lista a un set para eliminar duplicados, y luego crear un 
# diccionario donde la clave sea "categorias_limpias" y el valor sea el set resultante.
# Imprime el diccionario.
datos_crudos = ["electronica", "hogar", "electronica", "jardineria", "hogar", "tecnologia"]
# TU CÓDIGO AQUÍ:



# EJERCICIO 2: Permisos de Usuarios en Aplicación Web
# Tienes los permisos de un usuario estándar y los permisos que requiere un panel de administración.
# Utiliza el método adecuado para imprimir un boolean (True/False) que indique si 
# los permisos_usuario NO TIENEN NINGÚN elemento en común con permisos_admin.
permisos_usuario = {"leer_posts", "comentar"}
permisos_admin = {"borrar_usuarios", "editar_roles", "configurar_sistema"}
# TU CÓDIGO AQUÍ:



# EJERCICIO 3: Análisis de carritos de compras (Intersección y Diferencia)
# Tienes dos clientes. Muestra en pantalla:
# a) Los productos que ambos compraron (intersección).
# b) Los productos que compró el cliente 1 pero NO el cliente 2 (diferencia).
cliente_1 = {"notebook", "mouse", "teclado_mecanico", "monitor"}
cliente_2 = {"monitor", "mouse", "audifonos", "escritorio"}
# TU CÓDIGO AQUÍ:



# EJERCICIO 4: Actualización de perfil
# Tienes un set vacío llamado 'mis_conocimientos'.
# Agrega "python" con el método para un solo elemento.
# Luego agrega "git", "github", "sql" con el método para múltiples elementos.
# Finalmente, intenta remover "java" usando el método seguro (el que no da error si no existe).
# Imprime el set final.
mis_conocimientos = set()
# TU CÓDIGO AQUÍ:


print("--- FIN DEL SCRIPT ---")