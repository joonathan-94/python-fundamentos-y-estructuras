# =====================================================================
# EJERCICIOS DE PYTHON: VARIABLES Y TIPOS DE DATOS
# =====================================================================

# ---------------------------------------------------------------------
# NIVEL BÁSICO
# ---------------------------------------------------------------------

# Ejercicio 1: Perfil de Usuario
# Crea variables para almacenar el nombre (string), la edad (integer) 
# y el estado de conexión (boolean) de un usuario en una plataforma web.
# Imprime cada variable por consola usando la función print().
# Tu código aquí:

nombre = 'Jonathan'
edad = 31
estaActivo = True

print(nombre)
print(edad)
print(estaActivo)

# Ejercicio 2: Cálculo en Carrito de Compras
# Define una variable con el precio de un curso online (ej. 15.99) 
# y otra con la cantidad comprada (ej. 2). Ambas deben ser numéricas.
# Calcula el precio total, guárdalo en una nueva variable e imprímelo.
# Tu código aquí:

precio = 12990
qty = 3

total = precio * qty
print(total)

# Ejercicio 3: Mensaje de Bienvenida Dinámico
# Crea una variable con un nombre de usuario y otra con el nombre de tu aplicación.
# Utiliza f-strings (o concatenación) para formar el siguiente mensaje:
# "Bienvenido [usuario] a la plataforma [aplicacion]". Imprime el resultado.
# Tu código aquí:

userName = 'jcastro'
appName = 'TaskFlow'

msjeBienvenida = f'Bienvenido {userName} a la plataforma {appName}'
print(msjeBienvenida)

# ---------------------------------------------------------------------
# NIVEL INTERMEDIO
# ---------------------------------------------------------------------

# Ejercicio 4: Métodos HTTP (Listas)
# Crea una lista llamada 'metodos_permitidos' que contenga los strings: "GET", "POST", "PUT".
# Utiliza un método de lista para agregar "DELETE" al final.
# Luego, imprime la lista completa.
# Tu código aquí:



# Ejercicio 5: Configuración de Servidor (Diccionarios)
# Crea un diccionario llamado 'config_server' con las siguientes claves y valores:
# "host" (string: "127.0.0.1"), "puerto" (integer: 8000), y "debug" (boolean: True).
# Imprime únicamente el valor del puerto accediendo al diccionario.
# Tu código aquí:



# Ejercicio 6: Conversión de Tipos (Casting)
# Imagina que recibes el puerto desde un formulario web como texto:
# puerto_str = "8080"
# Conviértelo a un número entero (int) y guárdalo en la variable 'puerto_int'.
# Verifica que el tipo de dato ha cambiado usando la función type() e imprimiéndolo.
# Tu código aquí:



# Ejercicio 7: Credenciales de Base de Datos (Tuplas)
# Crea una tupla llamada 'credenciales' con tres valores: host, usuario y contraseña.
# Utiliza el "desempaquetado de tuplas" (tuple unpacking) para asignar estos 
# tres valores a tres variables distintas en una sola línea. Imprime las variables.
# Tu código aquí:



# ---------------------------------------------------------------------
# NIVEL AVANZADO
# ---------------------------------------------------------------------

# Ejercicio 8: Respuesta de una API (Estructuras Anidadas)
# Crea un diccionario llamado 'api_response' que simule una respuesta JSON.
# Debe tener una clave "status" con el número 200, y una clave "data" cuyo 
# valor sea una LISTA que contenga dos DICCIONARIOS. 
# Cada diccionario interno debe representar un usuario con "id" y "username".
# Imprime el 'username' del segundo usuario accediendo a la estructura.
# Tu código aquí:



# Ejercicio 9: Filtrado de Direcciones IP (Sets)
# Tienes el siguiente registro de visitas con IPs duplicadas:
# ips_visitantes = ["192.168.1.1", "10.0.0.5", "192.168.1.1", "172.16.0.1", "10.0.0.5"]
# Convierte esta lista en un Set para eliminar los duplicados.
# Luego, averigua cuántas IPs únicas hay en total usando la función len() e imprímelo.
# Tu código aquí:



# Ejercicio 10: Extracción y Mutación (Manipulación combinada)
# Tienes la siguiente estructura de un producto:
# producto = {
#     "id": 101, 
#     "nombre": "Curso de Desarrollo Web", 
#     "precio": 29.99, 
#     "tags": ["frontend", "javascript", "html"]
# }
# Escribe el código necesario para:
# 1. Extraer el segundo tag ("javascript") y guardarlo en una variable.
# 2. Modificar el "precio" en el diccionario a 24.99.
# 3. Añadir la clave "en_oferta" con el valor True al diccionario.
# Imprime el diccionario final actualizado.
# Tu código aquí: