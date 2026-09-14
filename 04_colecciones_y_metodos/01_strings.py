# ==============================================================================
# CLASE MAGISTRAL: MÉTODOS DE CADENAS (STRINGS) EN PYTHON
# Instructor: Tu 'Sensei' de Programación
# ==============================================================================
# UNIDAD 1: LA NATURALEZA INMUTABLE DE LOS STRINGS
# En Python, los strings son "inmutables". Esto significa que un método 
# NUNCA modifica la cadena original, sino que DEVUELVE UNA NUEVA CADENA 
# con los cambios aplicados. Siempre debes guardar ese resultado en una variable.
# ==============================================================================

print("--- INICIANDO CLASE DE STRINGS ---\n")

# ------------------------------------------------------------------------------
# 1. TRANSFORMACIÓN DE MAYÚSCULAS Y MINÚSCULAS
# Útil para normalizar datos, por ejemplo, cuando un usuario ingresa su correo.
# ------------------------------------------------------------------------------
mensaje = "hOla MUnDo deL deSArroLlo WeB"
print(f"Original: '{mensaje}'")

# .lower() -> Convierte todo a minúsculas
print(f".lower(): '{mensaje.lower()}'")

# .upper() -> Convierte todo a mayúsculas
print(f".upper(): '{mensaje.upper()}'")

# .capitalize() -> Solo la primera letra de toda la oración en mayúscula
print(f".capitalize(): '{mensaje.capitalize()}'")

# .title() -> La primera letra de CADA palabra en mayúscula (formato título)
print(f".title(): '{mensaje.title()}'")


# ------------------------------------------------------------------------------
# 2. LIMPIEZA DE ESPACIOS (STRIPPING)
# El pan de cada día en la validación de formularios. Los usuarios siempre
# dejan espacios en blanco por error.
# ------------------------------------------------------------------------------
correo_sucio = "    usuario@dominio.com    "
print(f"\nCorreo con basura: '{correo_sucio}'")

# .strip() -> Elimina espacios al principio y al final
print(f".strip(): '{correo_sucio.strip()}'")

# .lstrip() (Left strip) y .rstrip() (Right strip) eliminan solo de un lado
print(f".rstrip(): '{correo_sucio.rstrip()}'")


# ------------------------------------------------------------------------------
# 3. BÚSQUEDA Y CONTEO
# Ideal para saber si un texto contiene cierta información.
# ------------------------------------------------------------------------------
tecnologias = "python, html, css, javascript, python, git"

# .count() -> Cuenta cuántas veces aparece una subcadena
cantidad_python = tecnologias.count("python")
print(f"\nLa palabra 'python' aparece {cantidad_python} veces.")

# .find() -> Devuelve la posición (índice) donde empieza la palabra. 
# Si no la encuentra, devuelve -1. (Recuerda que en programación empezamos a contar desde 0).
posicion_css = tecnologias.find("css")
print(f"La palabra 'css' empieza en la posición: {posicion_css}")

# .startswith() / .endswith() -> Devuelven True o False si empieza/termina con algo
url = "https://mi-proyecto.com"
print(f"¿Es una web segura (https)?: {url.startswith('https')}")


# ------------------------------------------------------------------------------
# 4. REEMPLAZO Y FRAGMENTACIÓN (MAGIA NEGRA)
# Aquí es donde realmente empezamos a manipular los datos.
# ------------------------------------------------------------------------------
texto_error = "Tengo un error en Java"
# .replace(viejo, nuevo) -> Cambia una parte del texto por otra
texto_corregido = texto_error.replace("Java", "Python")
print(f"\nReemplazo: '{texto_corregido}'")

# .split(separador) -> ROMPE el string y lo convierte en una LISTA. 
# Si no le pasas separador, rompe por los espacios en blanco.
lista_tecnologias = tecnologias.split(", ")
print(f"Texto roto (Split): {lista_tecnologias}")

# .join(lista) -> El reverso de split. Toma una lista y la UNE usando el string inicial
lista_palabras = ["Aprender", "Python", "es", "el", "camino"]
frase_unida = " ".join(lista_palabras) # Usamos un espacio " " como pegamento
print(f"Lista unida (Join): '{frase_unida}'")

print("\n--- FIN DE LA TEORÍA ---\n")

# ==============================================================================
# EL DOJO DE PRÁCTICA (EJERCICIOS PARA TI)
# ==============================================================================
# Instrucciones del Sensei: 
# Comenta tu código anterior, y debajo de cada instrucción, intenta
# resolver el problema usando los métodos que vimos arriba.

# EJERCICIO 1: Limpieza Extrema
# Tienes la variable: nombre_usuario = "   pEdRo pErEz   "
# Tu misión: Mostrar en consola el nombre limpio de espacios y en formato Título 
# (debe quedar "Pedro Perez").

print('EJERCICIO 1')

nombre_usuario = "   pEdRo pErEz   "

nombre_usuario_limpio = nombre_usuario.strip().title()

print(f'Nombre de usuario limpio: {nombre_usuario_limpio}')



# EJERCICIO 2: Censura
# Tienes la variable: comentario = "Este sistema es una basura, me rindo"
# Tu misión: Reemplaza la palabra "basura" por "maravilla" y "me rindo" por "sigo adelante".

print('EJERCICIO 2')

comentario = "Este sistema es una basura, me rindo"
comentario_limpio = comentario.replace('basura','maravilla').replace('me rindo', 'sigo adelante')

print(f'Comentario corregido: {comentario_limpio}')

# EJERCICIO 3: El Extractor
# Tienes la variable: archivo = "mi_super_proyecto_final.py"
# Tu misión: Verifica si el archivo termina en ".py" usando el método correspondiente.
# Debería devolver True.

print('EJERCICIO 3')

archivo = "mi_super_proyecto_final.py"

contiene_py = archivo.endswith('.py')

print(f'Archivo contiene .py?: {contiene_py}')

# EJERCICIO 4: El Analista
# Tienes la variable: parrafo = "git es genial. aprender git salva vidas. usa git."
# Tu misión: Cuenta cuántas veces aparece la palabra "git" en el párrafo.

print('EJERCICIO 4')

parrafo = "git es genial. aprender git salva vidas. usa git."

contador_git = parrafo.count('git')

print(f'texto a evaluar: {parrafo}')

print(f'Cantidad apariciones palabra: Git, qty: {contador_git}')