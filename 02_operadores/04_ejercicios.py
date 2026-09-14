# =====================================================================
# EJERCICIOS DE PRÁCTICA: VARIABLES, TIPOS DE DATOS Y OPERADORES
# =====================================================================
# Instrucciones: Escribe tu código debajo de cada bloque de comentarios.
# Al ejecutar el archivo, deberías usar print() para ver tus resultados.
# Solo se requiere el uso de variables, tipos de datos simples y 
# compuestos, y operadores aritméticos y de comparación.
# =====================================================================

print('Ejercicios parte 1: Operadores aritmeticos')

# ---------------------------------------------------------------------
# PARTE 1: OPERADORES ARITMÉTICOS (+, -, *, /, //, %, **)
# ---------------------------------------------------------------------

# Ejercicio 1: Suma y Resta básica
# Imagina que estás auditando un inventario.
# Crea una variable 'equipos_totales' con el valor 150.
# Crea una variable 'equipos_descartados' con el valor 12.
# Calcula cuántos equipos quedan operativos y asigna el resultado a una 
# nueva variable. Imprime el resultado final.

equipos_totales = 150
equipos_descartados = 12

qty_equipos = equipos_totales - equipos_descartados

print('Cantidad equipos: ', qty_equipos)



# Ejercicio 2: Multiplicación, División y Tipos Compuestos (Diccionarios)
# Tienes un diccionario con los costos mensuales de distintos servicios web:
# servicios = {"hosting": 15.50, "dominio": 2.00}
# Calcula el costo de pagar 12 meses de "hosting" y 12 meses de "dominio".
# Suma ambos valores en una sola variable 'costo_anual' e imprímela.

servicios = {"hosting": 15.50, "dominio": 2.00}
costo_hosting = servicios['hosting'] * 12
print('Costo anual hosting: ', costo_hosting)
costo_dominio = servicios['dominio'] * 12
print('Costo anual dominio: ', costo_dominio)

costo_anual = costo_hosting + costo_dominio
print('Costo anual total: ',costo_anual)


# Ejercicio 3: División Entera (//) y Módulo (%)
# Tienes una lista con 85 tickets de soporte técnico acumulados.
# Tienes 4 técnicos disponibles en el turno.
# Usando la división entera, calcula cuántos tickets le tocan a cada 
# técnico equitativamente.
# Usando el módulo, calcula cuántos tickets sobrarán sin asignar.
# Imprime ambos resultados.


# Ejercicio 4: Exponenciación (**)
# Crea una variable 'base' con el valor 2.
# Crea una variable 'exponente' con el valor 8.
# Calcula el resultado de elevar la base al exponente (útil para 
# calcular combinaciones de bits, por ejemplo) e imprímelo.


# ---------------------------------------------------------------------
# PARTE 2: OPERADORES DE COMPARACIÓN (==, !=, >, <, >=, <=)
# ---------------------------------------------------------------------
# Nota: Recuerda que estos operadores devuelven un valor booleano 
# (True o False).

# Ejercicio 5: Mayor y Menor que
# Crea dos variables de tipo float: 'tiempo_carga_actual' = 1.4 y 
# 'tiempo_carga_maximo' = 2.0.
# Evalúa si el tiempo de carga actual es menor que el tiempo máximo.
# Imprime el resultado (debe mostrar True o False).


# Ejercicio 6: Igualdad y Desigualdad
# Tienes las siguientes dos variables de tipo string:
# rol_asignado = "administrador"
# rol_intentado = "usuario_basico"
# Verifica si ambos roles son exactamente iguales usando '=='.
# Luego, verifica si son diferentes usando '!='.
# Imprime ambos resultados booleanos.


# Ejercicio 7: Comparación de números negativos
# Crea una variable 'temperatura_servidor' con el valor 75.
# Crea una variable 'umbral_alerta' con el valor 75.
# Evalúa si la temperatura del servidor es mayor o igual (>=) al umbral.
# Imprime el resultado.


# ---------------------------------------------------------------------
# PARTE 3: COMBINACIÓN DE CONCEPTOS
# ---------------------------------------------------------------------

# Ejercicio 8: Tipos compuestos y operadores
# Tienes la siguiente tupla con los tiempos de respuesta (en milisegundos)
# de tres servidores diferentes:
# tiempos_respuesta = (120, 95, 110)
# Suma los tres valores accediendo a cada uno por su índice 
# (ejemplo: tiempos_respuesta[0]).
# Divide el total entre 3 para obtener el promedio (usa división normal).
# Finalmente, evalúa si ese promedio es estrictamente mayor que 100.
# Imprime el booleano resultante.


# Ejercicio 9: Conjuntos (Sets) y variables booleanas
# Crea un conjunto (set) llamado 'puertos_abiertos' con los valores: 80, 443, 22.
# Crea una variable booleana 'es_seguro' con el valor False.
# (No uses condicionales if, solo crea las variables e imprímelas para 
# repasar su sintaxis y cómo se ven al usar print).
# Imprime el tipo de dato de ambas variables usando la función type().
# Ejemplo: print(type(puertos_abiertos))