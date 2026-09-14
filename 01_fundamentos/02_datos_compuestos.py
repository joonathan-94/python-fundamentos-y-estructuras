# ==============================================================================
# SCRIPT DE ESTUDIO COMPLETO: DATOS COMPUESTOS EN PYTHON
# ==============================================================================
# Este script está diseñado para principiantes. Demuestra el uso de los 4 tipos
# de datos compuestos principales: Listas, Tuplas, Diccionarios y Conjuntos (Sets).
#
# Cada sección tiene ejemplos reales explicados paso a paso, y al final del script
# encontrarás una batería de ejercicios prácticos para que apliques lo aprendido.
# ==============================================================================

# ==============================================================================
# PARTE 1: EXPLICACIÓN Y EJEMPLOS DE DATOS COMPUESTOS
# ==============================================================================

print("--- 1. LISTAS ---")
# ¿Qué son? Contenedores ORDENADOS y MODIFICABLES (mutables).
# Útiles para: Almacenar secuencias de elementos que pueden cambiar con el tiempo.
# Ejemplo real: Una lista de compras, nombres de alumnos en una clase, un inventario.

# Creando una lista (se usan corchetes [])
lista_compras = ["Manzanas", "Leche", "Pan", "Huevos"]
print("Lista inicial:", lista_compras)

# Accediendo a un elemento por su posición (índice). ¡Recuerda que empezamos a contar desde 0!
primer_producto = lista_compras[0]
print("Primer producto:", primer_producto)

# Modificando un elemento existente
lista_compras[2] = "Pan Integral"
print("Lista tras modificar el pan:", lista_compras)

# Agregando un elemento nuevo al final de la lista
lista_compras.append("Café")
print("Lista tras agregar café:", lista_compras)

# Eliminando un elemento específico por su valor
lista_compras.remove("Leche")
print("Lista tras quitar la leche:", lista_compras)

print("\n" + "="*50 + "\n")


print("--- 2. TUPLAS ---")
# ¿Qué son? Contenedores ORDENADOS e INMODIFICABLES (inmutables).
# Útiles para: Datos que NO deben cambiar bajo ninguna circunstancia.
# Ejemplo real: Coordenadas geográficas (latitud, longitud), los meses del año.

# Creando una tupla (se usan paréntesis ())
coordenadas_oficina = (-33.3663, -70.7302) # Coordenadas de ejemplo (Quilicura)
print("Coordenadas de la oficina:", coordenadas_oficina)

# Accediendo a los datos (igual que en las listas)
latitud = coordenadas_oficina[0]
longitud = coordenadas_oficina[1]
print("Latitud:", latitud)
print("Longitud:", longitud)

# ¡CUIDADO! Las tuplas no se pueden modificar.
# Si intentas hacer esto: coordenadas_oficina[0] = -33.40 
# Python te dará un error ("TypeError: 'tuple' object does not support item assignment")

print("\n" + "="*50 + "\n")


print("--- 3. DICCIONARIOS ---")
# ¿Qué son? Contenedores MODIFICABLES que guardan pares de CLAVE y VALOR.
# Útiles para: Estructurar información donde cada dato tiene una "etiqueta" (clave) descriptiva.
# Ejemplo real: El perfil de un usuario, la ficha de un libro, configuraciones.

# Creando un diccionario (se usan llaves {} y dos puntos : para separar clave:valor)
perfil_usuario = {
    "nombre_usuario": "dev_chile",
    "nivel_acceso": 2,
    "activo": True
}
print("Perfil del usuario:", perfil_usuario)

# Accediendo a un valor usando su clave en lugar de una posición numérica
nombre = perfil_usuario["nombre_usuario"]
print("El nombre de usuario es:", nombre)

# Modificando el valor de una clave existente
perfil_usuario["nivel_acceso"] = 3
print("Perfil tras aumentar nivel de acceso:", perfil_usuario)

# Agregando un nuevo par clave-valor
perfil_usuario["email"] = "dev@ejemplo.cl"
print("Perfil tras agregar email:", perfil_usuario)

print("\n" + "="*50 + "\n")


print("--- 4. CONJUNTOS (SETS) ---")
# ¿Qué son? Contenedores DESORDENADOS y de elementos ÚNICOS (sin duplicados).
# Útiles para: Eliminar duplicados rápidamente, saber si un elemento existe en un grupo.
# Ejemplo real: IDs de transacciones procesadas, etiquetas (tags) únicas de un artículo.

# Creando un conjunto (se usan llaves {} pero sin los dos puntos de los diccionarios)
# Nota cómo pongo "terror" dos veces intencionalmente
etiquetas_pelicula = {"accion", "terror", "suspenso", "terror"}

# Al imprimirlo, verás que el duplicado "terror" desapareció automáticamente y el orden puede variar
print("Etiquetas de la película:", etiquetas_pelicula)

# Agregando un nuevo elemento
etiquetas_pelicula.add("ciencia_ficcion")
print("Etiquetas tras agregar una nueva:", etiquetas_pelicula)

# Intentando agregar un elemento que ya existe (Python lo ignorará)
etiquetas_pelicula.add("accion")
print("Etiquetas tras intentar agregar 'accion' de nuevo:", etiquetas_pelicula)

print("\n" + "="*50 + "\n")




# ==============================================================================
# PARTE 2: EJERCICIOS PRÁCTICOS BÁSICOS
# ==============================================================================
# Instrucciones: Intenta resolver estos ejercicios creando tus propias variables
# debajo de cada instrucción. No uses bucles ni condicionales.

print("--- ZONA DE EJERCICIOS ---")
print("Abre el código de este script y resuelve los ejercicios propuestos.")

# ------------------------------------------------------------------------------
# SECCIÓN A: LISTAS
# ------------------------------------------------------------------------------
# 1. Crea una variable llamada 'mis_colores' que contenga una lista con tus 3 colores favoritos.
# Escribe tu código aquí abajo:

colores = ['Azul', 'Rojo', 'Verde']
print('Lista de colores: ', colores)

# 2. Reemplaza el segundo color de tu lista (índice 1) por el color "Negro".
# Escribe tu código aquí abajo:

colores[1] = 'Negro'
print('Lista de colores: ', colores)

# 3. Agrega un cuarto color al final de la lista usando el método correspondiente (.append).
# Escribe tu código aquí abajo:

colores.append('Calipso')
print('Lista de colores: ', colores)


# 4. Crea una nueva variable llamada 'color_favorito' y asígnale el valor del primer elemento de tu lista.
# Escribe tu código aquí abajo:

color_favorito = colores[0]
print('Color favorito: ', color_favorito)


# ------------------------------------------------------------------------------
# SECCIÓN B: TUPLAS
# ------------------------------------------------------------------------------
# 1. Crea una variable llamada 'datos_personales' que sea una tupla con tu nombre, tu edad y tu ciudad.
# Escribe tu código aquí abajo:

datos_personales = ('Jonathan Castro', 31, 'Quilicura')
print('Datos personales: ', datos_personales)


# 2. Crea una variable llamada 'mi_edad' y extráela accediendo a la posición correspondiente en tu tupla.
# Escribe tu código aquí abajo:

mi_edad = datos_personales[1]
print('Edad: ', mi_edad)


# 3. (Reflexión): Piensa qué pasaría si intentas cambiar tu ciudad haciendo datos_personales[2] = "Otra Ciudad". 
# (No lo escribas en código, solo recuerda por qué fallaría).



# ------------------------------------------------------------------------------
# SECCIÓN C: DICCIONARIOS
# ------------------------------------------------------------------------------
# 1. Crea un diccionario llamado 'mascota' que tenga las claves: "nombre", "especie", y "edad". Asígnale valores.
# Escribe tu código aquí abajo:

mascota = {
    'nombre': 'Camilo',
    'raza': 'Koker',
    'edad': 12
}

print('mascota: ', mascota)


# 2. Agrega una nueva clave al diccionario llamada "color" y asígnale un valor.
# Escribe tu código aquí abajo:

mascota["color"] = 'Blanco y cafe'

print('mascota con color: ', mascota)


# 3. Tu mascota cumplió años. Aumenta el valor de la clave "edad" reasignándole un nuevo número.
# Escribe tu código aquí abajo:

mascota["edad"] = 13
print('mascota: ', mascota)


# 4. Crea una variable llamada 'especie_mascota' y guarda ahí el valor de la clave "especie" del diccionario.
# Escribe tu código aquí abajo:

especie_mascota = mascota["raza"]
print('Especie de mascota: ', especie_mascota)



# ------------------------------------------------------------------------------
# SECCIÓN D: CONJUNTOS (SETS)
# ------------------------------------------------------------------------------
# 1. Crea una lista (con corchetes []) llamada 'numeros_repetidos' con: [1, 2, 2, 3, 4, 4, 4, 5]
# Escribe tu código aquí abajo:

numeros_repetidos = [1, 2, 2, 3, 4, 4, 4, 5]
print('Lista de numeros repetidos: ', numeros_repetidos)


# 2. Crea un conjunto (set) llamado 'numeros_unicos' utilizando la función set() sobre tu lista anterior.
# Escribe tu código aquí abajo:

numeros_unicos = set(numeros_repetidos)
print('Lista de numeros unicos: ', numeros_unicos)


# 3. Agrega el número 6 al conjunto 'numeros_unicos' usando .add()
# Escribe tu código aquí abajo:

numeros_unicos.add(6)
print('Lista de numeros unicos: ', numeros_unicos)


# ------------------------------------------------------------------------------
# SECCIÓN E: DESAFÍO FINAL (Mezclando conceptos)
# ------------------------------------------------------------------------------
# 1. Crea un diccionario llamado 'mi_curso'.
#    Debe tener las siguientes claves:
#    - "nombre_curso" (con un string)
#    - "unidades" (con un número entero)
#    - "temas" (con una lista de 3 temas en formato string)
# Escribe tu código aquí abajo:

mi_curso = {
    'nombre_curso': 'Python',
    'unidades' : 3,
    'temas': ['Variables','Tipos de datos', 'Datos compuestos']
}

print('Curso: ', mi_curso)



# 2. Accede a la clave "temas" de tu diccionario, y usando el índice [0], 
#    guarda el primer tema en una variable llamada 'primer_tema'.
# Escribe tu código aquí abajo:
primer_tema = mi_curso["temas"][0]
print('Primer tema: ', primer_tema)