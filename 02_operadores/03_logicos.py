"""
=========================================================
APUNTES DE PYTHON: OPERADORES LÓGICOS
=========================================================
Los operadores lógicos se utilizan para combinar sentencias
condicionales (evaluar si algo es Verdadero o Falso). 
Son fundamentales para tomar decisiones en el código de tu 
futura aplicación, como validar accesos, comprobar datos 
de formularios, etc.

Los 3 operadores principales son:
1. and (Y lógico)
2. or  (O lógico)
3. not (Negación lógica)
=========================================================
"""

# ==========================================
# 1. Operador 'and'
# ==========================================
# Devuelve True SOLO si TODAS las condiciones son verdaderas.
# Si tan solo una es False, el resultado completo es False.

print("--- 1. Operador 'and' ---")
usuario_autenticado = True
es_administrador = True
es_usuario_estandar = False

# Ejemplo 1: El usuario cumple ambos requisitos (True y True)
puede_entrar_panel = usuario_autenticado and es_administrador
print(f"¿Puede entrar al panel de admin?: {puede_entrar_panel}") # Resultado: True

# Ejemplo 2: Falta un requisito (True y False)
puede_editar_config = es_usuario_estandar and es_administrador
print(f"¿Puede editar la configuración?: {puede_editar_config}") # Resultado: False


# ==========================================
# 2. Operador 'or'
# ==========================================
# Devuelve True si AL MENOS UNA de las condiciones es verdadera.
# Solo será False si TODAS las condiciones son falsas.

print("\n--- 2. Operador 'or' ---")
correo_verificado = False
telefono_verificado = True

# Ejemplo 1: Tiene al menos un método de contacto verificado (False o True)
cuenta_activa = correo_verificado or telefono_verificado
print(f"¿La cuenta está activa?: {cuenta_activa}") # Resultado: True

# Ejemplo 2: Ambos son falsos
pago_con_tarjeta = False
pago_con_paypal = False
compra_realizada = pago_con_tarjeta or pago_con_paypal
print(f"¿Se realizó la compra?: {compra_realizada}") # Resultado: False


# ==========================================
# 3. Operador 'not'
# ==========================================
# Invierte el valor de verdad. Si es True, lo hace False y viceversa.

print("\n--- 3. Operador 'not' ---")
cuenta_bloqueada = False

# Ejemplo 1: Si la cuenta NO está bloqueada, permitir el acceso
permitir_acceso = not cuenta_bloqueada
print(f"¿Permitir acceso al sistema?: {permitir_acceso}") # Resultado: True (porque invierte el False)

# Ejemplo 2: Funciona muy bien para "interruptores" (toggles) en aplicaciones
modo_oscuro_activado = True
nuevo_estado_modo_oscuro = not modo_oscuro_activado
print(f"¿Modo oscuro tras presionar el botón?: {nuevo_estado_modo_oscuro}") # Resultado: False


# ==========================================
# 4. COMBINANDO OPERADORES
# ==========================================
# Puedes usar paréntesis para agrupar condiciones y darles 
# prioridad, igual que en matemáticas.

print("\n--- Combinando operadores ---")
edad_usuario = 31
tiene_suscripcion_activa = False
dias_prueba_restantes = 3

# Lógica: Puede ver el contenido si es mayor de 18 Y (tiene suscripción O le quedan días de prueba)
puede_ver_contenido = (edad_usuario >= 18) and (tiene_suscripcion_activa or dias_prueba_restantes > 0)
print(f"¿Puede ver el contenido premium?: {puede_ver_contenido}")


"""
=========================================================
EJERCICIOS BÁSICOS PARA CONSOLIDAR CONOCIMIENTOS
=========================================================
Instrucciones: Borra el símbolo '#' de las variables en cada 
ejercicio, escribe tu lógica usando and, or, not según 
corresponda en la línea indicada, y ejecuta el script.

# --- Ejercicio 1: Validación de formulario de registro ---
# Un usuario intenta registrarse. El registro es válido si
# el correo no está vacío (tiene_correo es True) Y la contraseña 
# es segura (password_seguro es True).

# tiene_correo = True
# password_seguro = False
# registro_valido = # TU CÓDIGO AQUÍ (Usa: and)
# print("Ejercicio 1 - ¿Registro válido?:", registro_valido)


# --- Ejercicio 2: Sistema de envíos en e-commerce ---
# Un cliente obtiene envío gratis si su total de compra es 
# mayor a 50000 (compra_mayor_50k es True) O si tiene un 
# cupón (tiene_cupon es True).

# compra_mayor_50k = False
# tiene_cupon = True
# envio_gratis = # TU CÓDIGO AQUÍ (Usa: or)
# print("Ejercicio 2 - ¿Envío gratis?:", envio_gratis)


# --- Ejercicio 3: Acceso a base de datos ---
# Un desarrollador puede conectarse a la base de datos si
# NO está en mantenimiento (en_mantenimiento es False) Y
# su conexión de red es estable (red_estable es True).

# en_mantenimiento = False
# red_estable = True
# puede_conectar = # TU CÓDIGO AQUÍ (Combina: not y and)
# print("Ejercicio 3 - ¿Puede conectar a DB?:", puede_conectar)
=========================================================
"""