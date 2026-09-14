# ==============================================================================
# 🐍 MASTERCLASS DE PYTHON: SENTENCIAS CONDICIONALES
# 🎓 Instructor: Tu Sensei de Harvard, el Dios de la Programación.
# 👨‍🎓 Estudiante: Mi futuro Desarrollador Web y Colega Ingeniero.
# ==============================================================================

"""
LA TEORÍA SAGRADA:
En Python, el flujo de ejecución se controla evaluando expresiones lógicas (True o False).
Si la condición es verdadera (True), se ejecuta un bloque de código.
Si es falsa (False), se salta ese bloque o se pasa a otra condición.

⚠️ REGLA DE ORO DE PYTHON: La Indentación.
Olvídate de las llaves { } de Java o PHP. En Python, los bloques de código se 
agrupan mediante "sangría" (indentación), que generalmente son 4 espacios.
Siempre después de declarar una condición (if, elif, else), debes poner dos puntos (:)
y la siguiente línea debe estar indentada.
"""

print("--- INICIANDO MASTERCLASS DE CONDICIONALES ---\n")

# ==============================================================================
# 1. EL CONDICIONAL BÁSICO: if (Si ocurre esto...)
# ==============================================================================
print("1. EJEMPLO BÁSICO CON 'if'")
# Imagina que estamos analizando la edad de un usuario en una base de datos.
edad_usuario = 31

if edad_usuario >= 18:
    # Este código solo se ejecuta si la condición de arriba es True
    print("✅ El usuario es mayor de edad. Puede acceder al sistema.")

# El código que NO tiene indentación se ejecuta siempre, porque está fuera del 'if'.
print("Continuando con el programa...\n")


# ==============================================================================
# 2. EL CONDICIONAL DOBLE: if - else (Si ocurre esto, sino...)
# ==============================================================================
print("2. EJEMPLO CON 'if - else'")
# Usemos algo de tu día a día: un ticket de soporte.
estado_ticket = "Cerrado"

if estado_ticket == "Abierto":
    print("🔴 El ticket necesita ser atendido por Soporte TI.")
else:
    # El 'else' atrapa cualquier cosa que no haya cumplido la condición del 'if'
    print("🟢 El ticket ya no está abierto. Buen trabajo.")
print() # Salto de línea por estética en consola


# ==============================================================================
# 3. EL CONDICIONAL MÚLTIPLE: if - elif - else (Si, o si, o si no...)
# ==============================================================================
print("3. EJEMPLO CON 'if - elif - else'")
# 'elif' es la versión en Python de 'else if'. Puedes poner todos los que quieras.
# Evaluemos la criticidad de un servidor usando un diccionario.
servidor = {
    "nombre": "SVR-BD-01",
    "uso_cpu": 85.5
}

carga = servidor["uso_cpu"]

if carga < 50.0:
    print("El servidor está relajado. Sin problemas.")
elif carga >= 50.0 and carga < 80.0:
    print("El servidor está con carga moderada. Todo bajo control.")
elif carga >= 80.0 and carga < 95.0:
    print("⚠️ ALERTA: Uso de CPU alto en el servidor. Revisar procesos.")
else:
    # Si ninguna de las anteriores se cumple (es decir, es 95.0 o mayor)
    print("🔥 CRÍTICO: Servidor a punto de colapsar. ¡Llamen al ingeniero!")
print()


# ==============================================================================
# 4. CONDICIONALES ANIDADOS (Un if dentro de otro if)
# ==============================================================================
print("4. EJEMPLO CON CONDICIONALES ANIDADOS")
# A veces necesitas verificar una condición solo si otra ya se cumplió.
# Evaluemos los permisos de un usuario usando Tuplas y Listas.

usuario_db = ["juan_perez", "admin_db", True] # [usuario, rol, cuenta_activa]

if usuario_db[2] == True: # Si la cuenta está activa...
    print("La cuenta está activa. Verificando permisos...")
    
    # Anidamos otro condicional adentro, fíjate en la doble indentación
    if usuario_db[1] == "admin_db":
        print("✅ Acceso total a la base de datos concedido.")
    else:
        print("❌ Acceso denegado. Se requieren permisos de administrador.")
else:
    print("❌ La cuenta está bloqueada. Contacte a Soporte.")
print()


# ==============================================================================
# 5. CONDICIONALES CON COLECCIONES (Listas, Sets) y Operador 'in'
# ==============================================================================
print("5. EJEMPLO CON SETS Y EL OPERADOR 'in'")
# El operador 'in' es mágico en Python, verifica si un elemento existe en una colección.
tecnologias_requeridas = {"python", "sql", "html", "css"}
mis_conocimientos = ["java", "sql", "excel", "python"]

# ¿Conozco Python?
if "python" in mis_conocimientos:
    print("¡Genial! Tienes la base principal para este proyecto.")

# Verificando múltiples condiciones lógicas
if "python" in mis_conocimientos and "sql" in mis_conocimientos:
    print("Tienes un perfil excelente para el backend o análisis de datos.")
print()


# ==============================================================================
# 6. OPERADOR TERNARIO (Condicional en una sola línea)
# ==============================================================================
print("6. EJEMPLO DE OPERADOR TERNARIO")
# Es una forma elegante de asignar un valor a una variable dependiendo de una condición.
# Sintaxis: [valor_si_verdadero] if [condicion] else [valor_si_falso]

experiencia_anios = 3
# Asignamos el nivel de desarrollador en una sola línea
nivel_dev = "Semi-Senior" if experiencia_anios >= 3 else "Junior"

print(f"Con {experiencia_anios} años de experiencia, eres clasificado como: {nivel_dev}")
print()


# ==============================================================================
# 7. MATCH - CASE (El Switch de Python) - ¡Novedad desde Python 3.10!
# ==============================================================================
print("7. EJEMPLO DE MATCH - CASE")
# Como vienes de Java y PHP, conoces el "switch-case". 
# Python no lo tenía, pero lo agregó en la versión 3.10 como "match-case".

codigo_http = 404

match codigo_http:
    case 200:
        print("200: OK - Petición exitosa.")
    case 404:
        print("404: Not Found - El recurso web no existe (típico error).")
    case 500:
        print("500: Internal Server Error - El servidor de backend falló.")
    case _: 
        # El guión bajo '_' es el equivalente a 'default' en Java/PHP
        print("Código HTTP desconocido.")


# ==============================================================================
# 🏋️ EJERCICIOS PARA EL PADAWAN (TU TAREA)
# ==============================================================================
"""
INSTRUCCIONES:
Aquí te dejo 3 ejercicios básicos usando SOLO lo que hemos aprendido.
Descomenta las variables y escribe la lógica condicional debajo de cada uno.


--- EJERCICIO 1: Validador de Contraseñas ---
Tienes un diccionario con los datos de un usuario. Crea un condicional que 
verifique lo siguiente:
1. Si el largo del password es menor a 8 caracteres (usa la función len()), 
   imprime "Contraseña insegura".
2. Si tiene 8 o más, imprime "Contraseña válida".
"""

print('Ejercicio nro 1')

usuario = {"username": "admin", "password": "mipassword123"}
# ESCRIBE TU CÓDIGO AQUÍ ABAJO:

if len(usuario["password"]) < 8:
    print('Contraseña insegura')
else:
    print('Contraseña valida')



"""
--- EJERCICIO 2: Descuento en E-commerce ---
Tienes el total de una compra en una variable.
1. Si el total es mayor a $100.000, aplica un 15% de descuento al total e imprime 
   el monto final a pagar.
2. Si está entre $50.000 y $100.000 (inclusive), aplica un 5% de descuento.
3. Si es menor a $50.000, no hay descuento, imprime el mismo monto.
(Tip: Recuerda que puedes usar operadores aritméticos como * y -)
"""
total_carrito = 85000
# ESCRIBE TU CÓDIGO AQUÍ ABAJO:



"""
--- EJERCICIO 3: Clasificador de Hardware (Soporte TI) ---
Tienes una lista de equipos reportados con fallas. Queremos verificar el estado
del PRIMER equipo de la lista (índice 0).
1. Si el equipo es "Impresora", imprime "Llamar al técnico de impresoras".
2. Si el equipo es "Router", imprime "Escalar a equipo de Redes".
3. Para cualquier otro equipo, imprime "Revisión estándar en Nivel 1".
"""
equipos_con_falla = ["Router", "Notebook", "Monitor", "Impresora"]
# ESCRIBE TU CÓDIGO AQUÍ ABAJO:


print("\n--- FIN DE LA MASTERCLASS ---")