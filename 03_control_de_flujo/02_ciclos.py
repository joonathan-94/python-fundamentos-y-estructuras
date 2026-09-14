"""
=============================================================================
|                 ENTRENAMIENTO PYTHON: CICLOS (LOOPS)                      |
| Instructor: Tu Sensei de Programación (Ingeniero Informático - Harvard)   |
| Módulo actual: for, while, break, continue y simulación de do-while       |
=============================================================================

Bienvenido a tu clase de ciclos. Un ciclo nos permite repetir bloques de 
código sin tener que escribirlos una y otra vez. 

En lenguajes como Java, C# o PHP que viste en tus años de estudio, 
probablemente recuerdes tres ciclos: for, while y do-while.
En Python, la filosofía es "Simple es mejor que complejo", por lo que 
SOLO tenemos dos ciclos nativos: 'while' y 'for'. El 'do-while' no existe, 
pero te enseñaré el truco maestro para simularlo.

Prepárate. Ejecuta este script y lee los comentarios paso a paso.
"""

print("--- INICIANDO CLASE DE CICLOS ---\n")

# =============================================================================
# 1. EL CICLO 'WHILE' (MIENTRAS)
# =============================================================================
# El ciclo 'while' repite un bloque de código MIENTRAS una condición sea 
# evaluada como Verdadera (True). Es ideal cuando no sabemos cuántas veces 
# se va a repetir algo (por ejemplo, esperar a que el usuario ingrese un dato correcto).

print("1. CICLO WHILE:")
contador = 1

while contador <= 3:
    # Este bloque se repetirá mientras contador sea menor o igual a 3.
    print(f"El contador actual es: {contador}")
    # ¡CRÍTICO!: Siempre debemos modificar la variable de control.
    # Si no sumamos 1, el ciclo será infinito.
    contador += 1  # Esto es lo mismo que contador = contador + 1

print("Fin del ciclo while.\n")


# =============================================================================
# 2. EL CICLO 'FOR' (PARA CADA ELEMENTO)
# =============================================================================
# Aquí es donde Python brilla. En Python, el 'for' no usa contadores como en Java.
# En su lugar, el 'for' de Python itera (recorre) directamente sobre COLECCIONES
# (listas, tuplas, diccionarios, sets o strings).

print("2. CICLO FOR CON LISTAS:")
# Imagina que extraes una lista de servidores de tu área de soporte TI:
servidores_ti = ["Servidor_Logistica", "Servidor_Correos", "Servidor_BD"]

# Se lee: "Para cada 'servidor' dentro de 'servidores_ti', haz lo siguiente:"
for servidor in servidores_ti:
    print(f"Revisando estado de: {servidor}")

print("Revisión completada.\n")


print("2.1 CICLO FOR CON RANGOS (range):")
# Si necesitas un ciclo que simplemente cuente números (como el viejo for de C#),
# usamos la función nativa range().
# range(5) genera los números del 0 al 4. (Siempre empieza en 0 y llega hasta n-1).
for numero in range(5):
    print(f"Número del rango: {numero}")
print("\n")


print("2.2 CICLO FOR CON DICCIONARIOS:")
# Como trabajas con BD y Excel, los diccionarios te serán muy familiares, 
# son como registros JSON o filas de una tabla.
usuario_db = {
    "nombre": "Goku",
    "raza": "Saiyajin",
    "nivel_poder": 9000
}

# Por defecto, iterar un diccionario solo te da las claves (keys):
print("Iterando solo claves:")
for clave in usuario_db:
    print(clave)

# Si queremos la clave Y el valor, usamos el método .items() que aprendiste antes:
print("\nIterando claves y valores simultáneamente:")
for clave, valor in usuario_db.items():
    print(f"{clave.capitalize()}: {valor}")
print("\n")


# =============================================================================
# 3. CONTROL DE FLUJO: BREAK Y CONTINUE
# =============================================================================
# A veces necesitamos alterar el comportamiento normal de un ciclo en tiempo
# de ejecución utilizando sentencias condicionales (if).

print("3. USO DE 'BREAK' Y 'CONTINUE':")

# CONTINUE: Salta a la siguiente iteración del ciclo, ignorando el código de abajo.
# BREAK: Rompe y destruye el ciclo por completo, saliendo de él.

equipos_red = ["Router", "Switch", "PC_Mala", "Firewall", "AccessPoint"]

for equipo in equipos_red:
    if equipo == "PC_Mala":
        print(">> Se detectó una PC Mala. Ignorando y pasando al siguiente...")
        continue  # El ciclo no ejecuta la línea de abajo, salta directo a 'Firewall'
    
    if equipo == "Firewall":
        print(f"Configurando {equipo}...")
        print(">> Firewall configurado. Deteniendo todo el proceso de red por seguridad.")
        break  # Destruye el ciclo. 'AccessPoint' nunca será procesado.
        
    print(f"Configurando {equipo}...")
print("\n")


# =============================================================================
# 4. ¿QUÉ PASA CON 'DO-WHILE'? (EL TRUCO DE PYTHON)
# =============================================================================
# En PHP o Java usabas do-while para asegurar que el código se ejecutara 
# AL MENOS UNA VEZ antes de evaluar la condición.
# En Python, lo simulamos creando un 'while True' (ciclo infinito intencional)
# y ponemos la condición de salida dentro de un 'if' con un 'break'.

print("4. SIMULANDO DO-WHILE:")
# Comenta y descomenta las siguientes líneas si quieres probar el input.
# Lo dejaré comentado para que el script corra del tirón la primera vez, 
# pero puedes quitar las comillas triples para probarlo.

"""
while True:
    comando = input("Ingresa 'salir' para terminar el ciclo do-while: ")
    print(f"Procesando tu comando: {comando}")
    
    if comando.lower() == 'salir':
        print("Comando de salida recibido. Rompiendo el ciclo.")
        break  # Aquí está nuestra condición de escape
"""
print("Simulación de do-while mostrada en código (comentada).\n")


# =============================================================================
# =============================================================================
# 5. TU MISIÓN: EJERCICIOS DE CONSOLIDACIÓN
# =============================================================================
# =============================================================================
"""
Aquí tienes tus ejercicios, mi estimado futuro desarrollador web.
Utiliza únicamente lo que hemos visto: variables, tipos de datos, operadores, 
métodos de cadenas, listas/diccionarios, if/elif/else, inputs y ahora ciclos.

Escribe tu código debajo de las instrucciones de cada ejercicio.
"""

# -----------------------------------------------------------------------------
# EJERCICIO 1: El Sistema de Soporte TI (While y Condicionales)
# -----------------------------------------------------------------------------
# Crea un sistema que simule un inicio de sesión.
# 1. Define una contraseña correcta en una variable (ej: "Admin123").
# 2. Inicia un contador de intentos fallidos en 0.
# 3. Usa un ciclo 'while' que permita un MÁXIMO de 3 intentos.
# 4. Dentro del ciclo, pide al usuario (con input) que ingrese la contraseña.
# 5. Si la contraseña es correcta, imprime "Acceso concedido" y usa 'break' para salir.
# 6. Si es incorrecta, suma 1 al contador y advierte de los intentos restantes.
# 7. Si llega a 3 intentos, el ciclo debe terminar e imprimir "Cuenta bloqueada por seguridad".

print("--- INICIANDO EJERCICIO 1 ---")
# Escribe tu código del Ejercicio 1 aquí abajo:





# -----------------------------------------------------------------------------
# EJERCICIO 2: Auditoría de Inventario Logístico (For, Listas e If/Else)
# -----------------------------------------------------------------------------
# Tienes la siguiente lista con los pesos en kilogramos de cajas en la bodega:
pesos_cajas = [12.5, 4.0, 35.2, 8.5, 50.1, 18.0, 2.5]

# Se requiere automatizar una clasificación:
# 1. Usa un ciclo 'for' para recorrer la lista 'pesos_cajas'.
# 2. Si la caja pesa menos de 10 kg, imprime: "Caja de {peso}kg: Clasificación LIGERA".
# 3. Si pesa entre 10 kg y 25 kg (inclusive), imprime: "Caja de {peso}kg: Clasificación MEDIA".
# 4. Si pesa más de 25 kg, imprime: "Caja de {peso}kg: Clasificación PESADA - Requiere grúa".

print("\n--- INICIANDO EJERCICIO 2 ---")
# Escribe tu código del Ejercicio 2 aquí abajo:





# -----------------------------------------------------------------------------
# EJERCICIO 3: El Menú de Estrategia (Simulación de Do-While)
# -----------------------------------------------------------------------------
# Vamos a usar la lógica de un menú de videojuego clásico de estrategia.
# 1. Crea un ciclo infinito (`while True:`).
# 2. Dentro, muestra un menú usando 'print':
#    - "1. Crear Aldeano"
#    - "2. Enviar a recolectar madera"
#    - "3. Avanzar a la Edad Feudal (Salir)"
# 3. Pide al usuario que elija una opción mediante `input()`.
# 4. Si elige "1", imprime "Aldeano creado. Población +1".
# 5. Si elige "2", imprime "Aldeano talando madera...".
# 6. Si elige "3", imprime "Avanzando de edad..." y rompe el ciclo con `break`.
# 7. Si elige cualquier otra cosa, imprime "Opción inválida. Elige 1, 2 o 3."

print("\n--- INICIANDO EJERCICIO 3 ---")
# Escribe tu código del Ejercicio 3 aquí abajo:





# -----------------------------------------------------------------------------
# EJERCICIO 4: Extracción de Base de Datos (For y Diccionarios)
# -----------------------------------------------------------------------------
# Simulemos que hiciste una consulta SQL a tu BD de RRHH y la transformaste 
# en una lista de diccionarios en Python (algo súper común en desarrollo backend).

empleados = [
    {"nombre": "Carlos", "cargo": "Soporte TI", "salario": 800},
    {"nombre": "Maria", "cargo": "Desarrolladora Web", "salario": 1500},
    {"nombre": "Luis", "cargo": "Analista de Datos", "salario": 1200}
]

# 1. Usa un ciclo 'for' para recorrer la lista 'empleados'.
# 2. En cada iteración, el elemento será un diccionario.
# 3. Imprime una cadena formateada que diga: 
#    "El empleado {nombre} trabaja como {cargo} y gana ${salario}."

print("\n--- INICIANDO EJERCICIO 4 ---")
# Escribe tu código del Ejercicio 4 aquí abajo:





print("\n--- FIN DEL ENTRENAMIENTO DE HOY ---")
"""
¡Excelente trabajo! 
Copia este archivo completo. Ábrelo en tu editor de código. Lee los ejemplos, 
analiza la salida de los 'print' que ya están armados, y luego ensucia tus manos 
con el código en las secciones de ejercicios. 

La sintaxis muscular y la memoria lógica se desarrollan escribiendo. Si cometes 
errores de indentación (espacios), Python te avisará: en Python, lo que va DENTRO 
del ciclo debe tener 4 espacios hacia la derecha.

Quedo atento a tus resultados, futuro maestro de Python. ¡Éxito en el código!
"""