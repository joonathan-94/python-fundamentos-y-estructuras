# ============================================================
# PENSAMIENTO ALGORÍTMICO Y BIG O
# ============================================================
#
# Un algoritmo es una secuencia ordenada y finita
# de pasos utilizada para resolver un problema.
#
#
# En programación normalmente tenemos:
#
# entrada
# ↓
# procesamiento
# ↓
# salida
#
#
# Ejemplo:
#
# problema:
#
# encontrar si existe un ticket concreto.
#
#
# entrada:
#
# colección de tickets
# +
# código buscado
#
#
# procesamiento:
#
# revisar los tickets
#
#
# salida:
#
# encontrado / no encontrado
#
#
# En este archivo estudiaremos:
#
# - pensamiento algorítmico;
# - descomposición de problemas;
# - entrada, proceso y salida;
# - qué significa eficiencia;
# - introducción a Big O;
# - O(1);
# - O(log n);
# - O(n);
# - O(n log n);
# - O(n²);
# - cómo reconocer patrones frecuentes.
#
#
# El objetivo NO es realizar demostraciones matemáticas.
#
# El objetivo es aprender a mirar código
# y razonar cómo crecerá el trabajo realizado
# cuando aumenta la cantidad de datos.


# ============================================================
# 1. QUÉ ES UN ALGORITMO
# ============================================================

# Un algoritmo puede entenderse como:
#
# problema
# ↓
# pasos para resolverlo
# ↓
# resultado
#
#
# No necesita ser algo extremadamente complejo.
#
#
# Por ejemplo:
#
# calcular promedio de tres números.
#
#
# PASOS:
#
# 1. recibir tres números;
# 2. sumarlos;
# 3. dividir la suma entre 3;
# 4. devolver el resultado.


def calcular_promedio(
    numero_uno,
    numero_dos,
    numero_tres
):

    suma = (
        numero_uno
        + numero_dos
        + numero_tres
    )

    promedio = suma / 3

    return promedio


resultado_promedio = calcular_promedio(
    10,
    20,
    30
)


print(
    "Promedio:",
    resultado_promedio
)


# ============================================================
# 2. PENSAMIENTO ALGORÍTMICO
# ============================================================

# Pensar algorítmicamente significa:
#
# tomar un problema
#
# y dividirlo en pasos pequeños,
# claros y ejecutables.
#
#
# Ejemplo:
#
# "Necesito buscar un usuario activo
# dentro de una colección."
#
#
# Podemos pensar:
#
# 1. recibir la colección;
# 2. recorrer los usuarios;
# 3. comprobar si coincide el nombre;
# 4. comprobar si está activo;
# 5. devolver el usuario si corresponde;
# 6. devolver None si no aparece.


usuarios = [
    {
        "nombre": "Albert Einstein",
        "activo": False
    },
    {
        "nombre": "Alan Turing",
        "activo": True
    },
    {
        "nombre": "Grace Hopper",
        "activo": True
    }
]


def buscar_usuario_activo(
    usuarios,
    nombre_buscado
):

    for usuario in usuarios:

        if (
            usuario["nombre"]
            == nombre_buscado
            and usuario["activo"]
        ):

            return usuario

    return None


usuario_encontrado = buscar_usuario_activo(
    usuarios,
    "Alan Turing"
)


print(
    usuario_encontrado
)


# ============================================================
# 3. ENTRADA, PROCESO Y SALIDA
# ============================================================

# Muchos problemas pueden analizarse mediante:
#
# ENTRADA
# ↓
# PROCESO
# ↓
# SALIDA


# ------------------------------------------------------------
# EJEMPLO
# ------------------------------------------------------------

# Problema:
#
# contar cuántos tickets están abiertos.
#
#
# ENTRADA:
#
# colección de tickets.
#
#
# PROCESO:
#
# recorrer los tickets
# y comprobar su estado.
#
#
# SALIDA:
#
# cantidad de tickets abiertos.


tickets = [
    {
        "id": "TK-001",
        "estado": "Abierto"
    },
    {
        "id": "TK-002",
        "estado": "Cerrado"
    },
    {
        "id": "TK-003",
        "estado": "Abierto"
    }
]


cantidad_abiertos = 0


for ticket in tickets:

    if ticket["estado"] == "Abierto":

        cantidad_abiertos += 1


print(
    "Tickets abiertos:",
    cantidad_abiertos
)


# ============================================================
# 4. NO EXISTE UNA ÚNICA SOLUCIÓN
# ============================================================

# Un mismo problema puede resolverse
# de varias maneras.
#
#
# Por ejemplo:
#
# comprobar si existe:
#
# "Alan Turing"
#
# dentro de una colección.


cientificos = [
    "Albert Einstein",
    "Nikola Tesla",
    "Alan Turing",
    "Grace Hopper"
]


# SOLUCIÓN 1:
#
# recorrer manualmente.


encontrado = False


for cientifico in cientificos:

    if cientifico == "Alan Turing":

        encontrado = True

        break


print(
    encontrado
)


# SOLUCIÓN 2:
#
# utilizar una operación incorporada.


print(
    "Alan Turing"
    in cientificos
)


# Ambas pueden resolver el problema.
#
# Una parte importante de programar
# consiste en elegir soluciones:
#
# correctas
# legibles
# suficientemente eficientes


# ============================================================
# 5. QUÉ SIGNIFICA EFICIENCIA
# ============================================================

# Podemos pensar principalmente en:
#
# tiempo
# y
# memoria.
#
#
# TIEMPO:
#
# cuánto trabajo aproximadamente
# debe realizar el programa.
#
#
# MEMORIA:
#
# cuánto espacio necesita.
#
#
# En este bloque nos concentraremos
# principalmente en:
#
# tiempo de ejecución
#
# desde un punto de vista conceptual.


# ============================================================
# 6. ¿POR QUÉ NO MEDIMOS SOLAMENTE SEGUNDOS?
# ============================================================

# Supongamos que un programa tarda:
#
# 0.002 segundos.
#
#
# Ese valor puede cambiar según:
#
# procesador
# memoria
# sistema operativo
# otros programas ejecutándose
# versión de Python
#
#
# Por eso para analizar algoritmos
# suele ser más útil observar:
#
# cómo crece el trabajo
#
# cuando aumenta el tamaño de la entrada.


# ============================================================
# 7. QUÉ REPRESENTA n
# ============================================================

# En análisis de algoritmos suele utilizarse:
#
# n
#
# para representar:
#
# cantidad de datos.
#
#
# Ejemplo:
#
# si tenemos:
#
# 10 usuarios
#
# n = 10
#
#
# si tenemos:
#
# 1_000 usuarios
#
# n = 1_000


# ============================================================
# 8. BIG O
# ============================================================

# Big O es una notación utilizada para describir
# cómo crece aproximadamente el trabajo
# de un algoritmo al aumentar n.
#
#
# Para nuestro estudio:
#
# NO intentaremos calcular tiempos exactos.
#
#
# Nos interesa responder:
#
# "¿qué sucede si los datos crecen mucho?"


# ============================================================
# 9. O(1) - TIEMPO CONSTANTE
# ============================================================

# O(1)
#
# significa:
#
# la cantidad de trabajo principal
# no depende significativamente
# de cuántos elementos existan.
#
#
# Ejemplo:
#
# acceder a una posición concreta
# de una lista.


numeros = [
    10,
    20,
    30,
    40,
    50
]


print(
    numeros[2]
)


# Aunque la lista tenga:
#
# 5 elementos
#
# o:
#
# 5 millones,
#
# acceder directamente a:
#
# numeros[2]
#
# no requiere recorrer todos
# los elementos anteriores.
#
#
# Conceptualmente:
#
# acceso directo
# → O(1)


# ============================================================
# 10. OTRO EJEMPLO O(1)
# ============================================================

usuario = {
    "nombre": "Alan Turing",
    "area": "Computación"
}


print(
    usuario["nombre"]
)


# El acceso a claves de un diccionario
# suele considerarse O(1) en promedio.
#
#
# IMPORTANTE:
#
# "en promedio"
#
# porque internamente existen detalles
# relacionados con tablas hash.
#
#
# Para nuestro nivel:
#
# dict[key]
# → normalmente pensar O(1)


# ============================================================
# 11. O(n) - TIEMPO LINEAL
# ============================================================

# O(n)
#
# significa que el trabajo crece
# aproximadamente en proporción
# a la cantidad de elementos.
#
#
# Si tenemos:
#
# 10 elementos
#
# podríamos revisar hasta:
#
# 10.
#
#
# Si tenemos:
#
# 1_000 elementos
#
# podríamos revisar hasta:
#
# 1_000.


cientificos_lineal = [
    "Einstein",
    "Tesla",
    "Turing",
    "Hopper",
    "Sagan"
]


for cientifico in cientificos_lineal:

    print(
        cientifico
    )


# Estamos recorriendo:
#
# todos los elementos.
#
#
# Conceptualmente:
#
# O(n)


# ============================================================
# 12. BÚSQUEDA LINEAL
# ============================================================

def buscar_cientifico(
    nombres,
    objetivo
):

    for nombre in nombres:

        if nombre == objetivo:

            return True

    return False


print(
    buscar_cientifico(
        cientificos_lineal,
        "Turing"
    )
)


# En el peor caso:
#
# podríamos tener que revisar
# todos los elementos.
#
#
# Por eso:
#
# O(n)
#
#
# Estudiaremos formalmente
# búsqueda lineal en el siguiente archivo.


# ============================================================
# 13. O(n²) - TIEMPO CUADRÁTICO
# ============================================================

# O(n²)
#
# aparece frecuentemente cuando:
#
# por cada elemento
#
# recorremos nuevamente
# muchos elementos.
#
#
# El ejemplo más evidente:
#
# bucles anidados.


nombres = [
    "Einstein",
    "Tesla",
    "Turing"
]


for nombre_uno in nombres:

    for nombre_dos in nombres:

        print(
            nombre_uno,
            nombre_dos
        )


# Tenemos:
#
# 3 nombres.
#
#
# combinaciones procesadas:
#
# aproximadamente:
#
# 3 * 3
#
# =
#
# 9.
#
#
# Si tuviéramos:
#
# 100 elementos
#
# podríamos realizar:
#
# aproximadamente:
#
# 100 * 100
#
# =
#
# 10_000 operaciones.
#
#
# Por eso:
#
# O(n²)


# ============================================================
# 14. VISUALIZAR O(n²)
# ============================================================

# n = 10
#
# n² = 100
#
#
# n = 100
#
# n² = 10_000
#
#
# n = 1_000
#
# n² = 1_000_000
#
#
# Aquí podemos observar cómo
# el trabajo crece mucho más rápidamente
# que en O(n).


# ============================================================
# 15. NO TODO BUCLE ANIDADO ES AUTOMÁTICAMENTE O(n²)
# ============================================================

# Esta es una precisión importante.
#
#
# Ver:
#
# for ...
#     for ...
#
# puede ser una señal.
#
#
# Pero la complejidad real depende
# de cuánto recorre cada ciclo.
#
#
# Por ahora utilizaremos la regla mental:
#
# dos recorridos completos anidados
# sobre conjuntos de tamaño similar
#
# → probablemente O(n²)
#
#
# Más adelante podrás analizar
# casos más específicos.


# ============================================================
# 16. O(log n) - CRECIMIENTO LOGARÍTMICO
# ============================================================

# O(log n)
#
# aparece cuando en cada paso
# podemos descartar una parte importante
# del problema.
#
#
# Un ejemplo clásico:
#
# búsqueda binaria.
#
#
# Supongamos números ordenados:
#
# 1 2 3 4 5 6 7 8
#
#
# queremos buscar:
#
# 7.
#
#
# Podemos mirar aproximadamente
# la mitad:
#
# 4
#
#
# Como:
#
# 7 > 4
#
# descartamos:
#
# 1 2 3 4
#
#
# Ahora quedan:
#
# 5 6 7 8
#
#
# volvemos a dividir.
#
#
# Cada paso reduce significativamente
# el espacio de búsqueda.


# ============================================================
# 17. VISUALIZAR O(log n)
# ============================================================

# Supongamos:
#
# 1_024 elementos.
#
#
# Si aproximadamente dividimos
# el problema por la mitad:
#
# 1024
# ↓
# 512
# ↓
# 256
# ↓
# 128
# ↓
# 64
# ↓
# 32
# ↓
# 16
# ↓
# 8
# ↓
# 4
# ↓
# 2
# ↓
# 1
#
#
# En aproximadamente 10 reducciones
# pasamos de:
#
# 1_024 elementos
#
# a:
#
# 1.
#
#
# Esa es la intuición
# que quiero que recuerdes.


# ============================================================
# 18. O(n log n)
# ============================================================

# O(n log n)
#
# aparece frecuentemente en algoritmos
# eficientes de ordenamiento.
#
#
# Algunos algoritmos de ordenamiento
# trabajan aproximadamente de esta forma.
#
#
# Python utiliza algoritmos altamente
# optimizados para:
#
# sorted()
#
# y:
#
# list.sort()
#
#
# No necesitamos estudiar su implementación
# interna en este momento.
#
#
# Lo importante:
#
# O(n log n)
#
# suele escalar mucho mejor
# que:
#
# O(n²)
#
# para colecciones grandes.


# ============================================================
# 19. COMPARACIÓN CONCEPTUAL
# ============================================================

# De mejor crecimiento
# hacia peor crecimiento:
#
#
# O(1)
#
# ↓
#
# O(log n)
#
# ↓
#
# O(n)
#
# ↓
#
# O(n log n)
#
# ↓
#
# O(n²)
#
#
# IMPORTANTE:
#
# Esto NO significa automáticamente
# que una función O(1) siempre sea
# más rápida en cualquier situación real.
#
#
# Big O describe principalmente
# cómo escala el trabajo.


# ============================================================
# 20. EJEMPLO: ENCONTRAR UN TICKET
# ============================================================

tickets_busqueda = [
    {
        "id": "TK-001",
        "titulo": "Crear usuario"
    },
    {
        "id": "TK-002",
        "titulo": "Servidor caído"
    },
    {
        "id": "TK-003",
        "titulo": "Actualizar software"
    }
]


def buscar_ticket(
    tickets,
    id_buscado
):

    for ticket in tickets:

        if ticket["id"] == id_buscado:

            return ticket

    return None


ticket_encontrado = buscar_ticket(
    tickets_busqueda,
    "TK-003"
)


print(
    ticket_encontrado
)


# En el peor caso:
#
# debemos recorrer todos los tickets.
#
#
# Si existen:
#
# n tickets
#
# entonces:
#
# O(n)


# ============================================================
# 21. CAMBIAR LA ESTRUCTURA PUEDE CAMBIAR EL PROBLEMA
# ============================================================

# Ahora imaginemos que organizamos
# los tickets en un diccionario
# utilizando el ID como clave.


tickets_por_id = {
    "TK-001": {
        "titulo": "Crear usuario"
    },

    "TK-002": {
        "titulo": "Servidor caído"
    },

    "TK-003": {
        "titulo": "Actualizar software"
    }
}


ticket_directo = (
    tickets_por_id["TK-003"]
)


print(
    ticket_directo
)


# Aquí ya no necesitamos recorrer:
#
# TK-001
# TK-002
# TK-003
#
#
# Podemos consultar directamente
# mediante la clave.
#
#
# Promedio conceptual:
#
# O(1)


# ============================================================
# 22. ESTRUCTURA DE DATOS + ALGORITMO
# ============================================================

# Este ejemplo conecta el bloque anterior
# con el actual.
#
#
# Con:
#
# list
#
# buscar un ID puede requerir:
#
# O(n)
#
#
# Con:
#
# dict
#
# consultar una clave suele ser:
#
# O(1) en promedio.
#
#
# Por eso elegir estructuras de datos
# correctamente puede mejorar:
#
# claridad
# diseño
# eficiencia


# ============================================================
# 23. NO OPTIMIZAR TODO PREMATURAMENTE
# ============================================================

# Esto también es importante.
#
#
# No debemos convertir cada programa
# pequeño en una obsesión por Big O.
#
#
# Si tenemos:
#
# 5 elementos
#
# una solución sencilla O(n)
# puede ser perfectamente apropiada.
#
#
# Antes de optimizar debemos pensar:
#
# ¿la solución es correcta?
#
# ¿es legible?
#
# ¿el volumen de datos justifica mejorarla?
#
#
# Una solución ligeramente más eficiente
# pero muchísimo más difícil de mantener
# no siempre es mejor.


# ============================================================
# 24. BIG O IGNORA MUCHOS DETALLES PEQUEÑOS
# ============================================================

# Supongamos:
#
# recorremos una lista dos veces.
#
#
# Podríamos pensar:
#
# n + n
#
# =
#
# 2n
#
#
# En Big O:
#
# normalmente simplificamos:
#
# O(2n)
#
# a:
#
# O(n)
#
#
# Porque nos interesa principalmente:
#
# cómo crece el trabajo.
#
#
# No necesitamos profundizar
# matemáticamente en esto ahora.


# ============================================================
# 25. EJEMPLO DE DOS RECORRIDOS
# ============================================================

numeros_ejemplo = [
    10,
    20,
    30
]


for numero in numeros_ejemplo:

    print(
        "Primer recorrido:",
        numero
    )


for numero in numeros_ejemplo:

    print(
        "Segundo recorrido:",
        numero
    )


# Dos recorridos separados:
#
# n + n
#
# siguen creciendo linealmente.
#
#
# Conceptualmente:
#
# O(n)


# ============================================================
# 26. DOS RECORRIDOS ANIDADOS
# ============================================================

for numero_uno in numeros_ejemplo:

    for numero_dos in numeros_ejemplo:

        print(
            numero_uno,
            numero_dos
        )


# Aquí:
#
# n * n
#
# →
#
# O(n²)


# ============================================================
# 27. REGLA MENTAL PARA IDENTIFICAR COMPLEJIDAD
# ============================================================

# ACCESO DIRECTO:
#
# colección[posición]
# diccionario[clave]
#
# → pensar O(1)
#
#
# ------------------------------------------------------------
#
# RECORRER TODOS:
#
# for elemento in elementos
#
# → pensar O(n)
#
#
# ------------------------------------------------------------
#
# RECORRER TODOS POR CADA ELEMENTO:
#
# for elemento in elementos:
#
#     for otro in elementos:
#
# → pensar O(n²)
#
#
# ------------------------------------------------------------
#
# DIVIDIR EL PROBLEMA REPETIDAMENTE:
#
# mitad
# mitad
# mitad
#
# → pensar O(log n)
#
#
# ------------------------------------------------------------
#
# ORDENAMIENTO EFICIENTE GENERAL:
#
# → suele aparecer O(n log n)


# ============================================================
# 28. EJEMPLO DE RAZONAMIENTO
# ============================================================

# Problema:
#
# comprobar si existe un código
# dentro de una lista.
#
#
# Opción:
#
# recorrer uno por uno.
#
#
# Pregunta:
#
# ¿cuántos elementos podría revisar?
#
#
# En el peor caso:
#
# todos.
#
#
# Entonces:
#
# O(n)
#
#
# Ese tipo de razonamiento
# es más importante ahora
# que memorizar fórmulas.


# ============================================================
# 29. PENSAR ANTES DE PROGRAMAR
# ============================================================

# Antes de escribir código,
# podemos hacernos preguntas:
#
# ¿qué recibo?
#
# ¿qué necesito obtener?
#
# ¿qué pasos transforman
# la entrada en la salida?
#
# ¿qué estructura de datos
# representa mejor el problema?
#
# ¿necesito recorrer todos
# los elementos?
#
# ¿estoy repitiendo trabajo
# innecesariamente?
#
#
# Estas preguntas forman parte
# del pensamiento algorítmico.


# ============================================================
# 30. EJEMPLO COMPLETO DE DESCOMPOSICIÓN
# ============================================================

# Problema:
#
# encontrar el primer ticket crítico.
#
#
# ENTRADA:
#
# lista de tickets.
#
#
# PROCESO:
#
# recorrer los tickets;
# revisar la prioridad;
# detenerse al encontrar
# el primer ticket crítico.
#
#
# SALIDA:
#
# ticket encontrado
#
# o:
#
# None.


tickets_prioridad = [
    {
        "id": "TK-1001",
        "prioridad": "Media"
    },
    {
        "id": "TK-1002",
        "prioridad": "Crítica"
    },
    {
        "id": "TK-1003",
        "prioridad": "Baja"
    }
]


def encontrar_critico(
    tickets
):

    for ticket in tickets:

        if (
            ticket["prioridad"]
            == "Crítica"
        ):

            return ticket

    return None


print(
    encontrar_critico(
        tickets_prioridad
    )
)


# En el mejor caso:
#
# el primer ticket ya es crítico.
#
#
# En el peor caso:
#
# revisamos todos.
#
#
# Cuando analizamos Big O
# normalmente nos interesa
# especialmente cómo crece
# el peor caso.


# ============================================================
# 31. MEJOR CASO Y PEOR CASO
# ============================================================

# Una búsqueda lineal:
#
# objetivo:
#
# ["A", "B", "C", "D"]
#
#
# buscar:
#
# "A"
#
# → encontramos inmediatamente.
#
#
# buscar:
#
# "D"
#
# → recorremos prácticamente todo.
#
#
# buscar:
#
# "Z"
#
# → recorremos todo.
#
#
# Para nuestro estudio:
#
# consideraremos principalmente
# el comportamiento del peor caso.


# ============================================================
# 32. BIG O NO REEMPLAZA EL SENTIDO COMÚN
# ============================================================

# Imaginemos dos soluciones:
#
# solución A:
#
# sencilla
# legible
# O(n)
#
#
# solución B:
#
# extremadamente compleja
# O(log n)
#
#
# pero trabajamos únicamente
# con 10 elementos.
#
#
# La solución A puede ser
# completamente razonable.
#
#
# Programar bien implica equilibrar:
#
# corrección
# legibilidad
# mantenibilidad
# eficiencia


# ============================================================
# 33. LO QUE DEBES SABER DE MEMORIA
# ============================================================

# O(1)
#
# trabajo aproximadamente constante.
#
#
# O(log n)
#
# reducimos significativamente
# el problema en cada paso.
#
#
# O(n)
#
# el trabajo crece aproximadamente
# con la cantidad de elementos.
#
#
# O(n log n)
#
# común en algoritmos eficientes
# de ordenamiento.
#
#
# O(n²)
#
# el trabajo puede crecer
# aproximadamente como n * n.


# ============================================================
# 34. LO QUE NO NECESITAS TODAVÍA
# ============================================================

# No necesitas:
#
# demostrar matemáticamente Big O;
#
# calcular límites;
#
# estudiar notación Omega;
#
# estudiar notación Theta;
#
# analizar recurrencias;
#
# demostrar formalmente algoritmos.
#
#
# Eso puede estudiarse posteriormente
# si alguna necesidad académica
# o profesional lo requiere.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# ALGORITMO:
#
# secuencia de pasos para resolver
# un problema.
#
#
# ------------------------------------------------------------
#
# PENSAMIENTO ALGORÍTMICO:
#
# problema
# ↓
# entrada
# ↓
# pasos pequeños
# ↓
# salida
#
#
# ------------------------------------------------------------
#
# BIG O:
#
# herramienta para razonar
# cómo crece el trabajo
# cuando aumentan los datos.
#
#
# ------------------------------------------------------------
#
# O(1)
#
# acceso aproximadamente constante.
#
#
# ------------------------------------------------------------
#
# O(log n)
#
# reducir el problema repetidamente.
#
#
# ------------------------------------------------------------
#
# O(n)
#
# recorrer los elementos.
#
#
# ------------------------------------------------------------
#
# O(n log n)
#
# frecuente en ordenamientos eficientes.
#
#
# ------------------------------------------------------------
#
# O(n²)
#
# recorridos anidados completos.
#
#
# ------------------------------------------------------------
#
# REGLA MÁS IMPORTANTE:
#
# no memorizar solamente símbolos.
#
# Preguntarse:
#
# "¿cuánto trabajo realiza
# mi solución cuando crecen los datos?"
#
#
# ------------------------------------------------------------
#
# SIGUIENTE TEMA:
#
# BÚSQUEDAS
#
# donde compararemos:
#
# búsqueda lineal
#
# y:
#
# búsqueda binaria.