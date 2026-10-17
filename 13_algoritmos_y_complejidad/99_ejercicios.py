# ============================================================
# ALGO-01 - PENSAMIENTO ALGORÍTMICO Y BIG O
# ============================================================
#
# Observa los siguientes tres fragmentos.
#
# Debes indicar mediante comentarios:
#
# - qué complejidad aproximada representa cada uno;
# - por qué.
#
#
# Utiliza solamente:
#
# O(1)
# O(n)
# O(n²)
#
#
# ------------------------------------------------------------
# CASO A
# ------------------------------------------------------------

cientificos = [
    "Albert Einstein",
    "Nikola Tesla",
    "Alan Turing"
]


primer_cientifico = cientificos[0]


# RESPUESTA:
#
# Complejidad:
#
# O(1) 
#
# Explicación:
#
# porque accede directamente al elemento que se requiere.


# ------------------------------------------------------------
# CASO B
# ------------------------------------------------------------

for cientifico in cientificos:

    print(
        cientifico
    )


# RESPUESTA:
#
# Complejidad:
#
# O(n)
#
# Explicación:
#
# Porque recorre todos los elementos de la lista


# ------------------------------------------------------------
# CASO C
# ------------------------------------------------------------

for cientifico_uno in cientificos:

    for cientifico_dos in cientificos:

        print(
            cientifico_uno,
            cientifico_dos
        )


# RESPUESTA:
#
# Complejidad:
#
# O(n²)
#
# Explicación:
#
# Porque estamos anidando el proceso de  recorrido


# ------------------------------------------------------------
# PREGUNTA FINAL
# ------------------------------------------------------------
#
# Si la colección pasara de:
#
# 10 elementos
#
# a:
#
# 1.000 elementos,
#
# ¿cuál de los tres casos crecería
# más rápidamente en cantidad de trabajo?
#
#
# RESPUESTA:
#
# El O(n²) Porque por cada elemento se vuelven a recorrer todos
# los elementos de la colección.


# ============================================================
# ALGO-02 - BÚSQUEDAS
# ============================================================
#
# En este ejercicio practicarás:
#
# - búsqueda lineal;
# - búsqueda binaria;
# - índices;
# - enumerate();
# - while;
# - división entera //;
# - return;
# - None.
#
#
# ============================================================
# PARTE A - BÚSQUEDA LINEAL
# ============================================================
#
# Tienes la siguiente colección:

cientificos_busqueda = [
    "Albert Einstein",
    "Nikola Tesla",
    "Alan Turing",
    "Grace Hopper",
    "Carl Sagan"
]


# Crea una función:
#
# buscar_cientifico()
#
#
# Debe recibir:
#
# lista
# científico_buscado
#
#
# Debe recorrer la colección
# mediante enumerate().
#
#
# Si encuentra el científico:
#
# debe devolver su índice.
#
#
# Si NO lo encuentra:
#
# debe devolver:
#
# None
#
#
# Después prueba buscando:
#
# "Alan Turing"
#
#
# Resultado esperado:
#
# 2

def buscar_cientifico(lista_cientificos, cientifico_buscado):
    
    for indice, valor in enumerate(lista_cientificos):
        if valor == cientifico_buscado:
            return indice

    return None

resultado_busqueda = buscar_cientifico(cientificos_busqueda, "Alan Turing")

print(f"Resultado busqueda de cientifico: {resultado_busqueda}") 


# ============================================================
# PARTE B - BÚSQUEDA BINARIA
# ============================================================
#
# Utiliza esta colección YA ORDENADA:

numeros_busqueda = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90
]


# Crea una función:
#
# buscar_numero()
#
#
# Debe recibir:
#
# lista
# objetivo
#
#
# Debes utilizar:
#
# inicio
# fin
# medio
#
#
# y:
#
# while inicio <= fin
#
#
# Calcula medio mediante:
#
# (inicio + fin) // 2
#
#
# Si:
#
# valor_medio == objetivo
#
# devuelve:
#
# medio
#
#
# Si:
#
# valor_medio < objetivo
#
# mueve inicio hacia la derecha.
#
#
# Si:
#
# valor_medio > objetivo
#
# mueve fin hacia la izquierda.
#
#
# Si termina el while
# sin encontrar el número:
#
# devuelve:
#
# None
#
#
# Prueba buscando:
#
# 70
#
#
# Resultado esperado:
#
# 6

def buscar_numero(lista, objetivo):

    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:

        medio = (inicio + fin) // 2

        valor_medio = lista[medio]

        if valor_medio == objetivo:
            return medio

        if valor_medio < objetivo:
            inicio = medio +1

        else:
            fin = medio -1

    return None

indice_buscado = buscar_numero(numeros_busqueda, 70)

print(f"Indice encontrado: {indice_buscado}")

# ============================================================
# ALGO-03 - ORDENAMIENTO
# ============================================================
#
# Tienes los siguientes autos clásicos:

autos_clasicos = [
    {
        "modelo": "Chevrolet Camaro",
        "anio": 1967
    },
    {
        "modelo": "Chevrolet Bel Air",
        "anio": 1957
    },
    {
        "modelo": "Chevrolet Corvette",
        "anio": 1963
    }
]


# ------------------------------------------------------------
# OBJETIVO
# ------------------------------------------------------------
#
# Ordena los autos desde el más antiguo
# hasta el más nuevo.
#
#
# Debes:
#
# 1. Crear una función:
# obtener_anio(auto)
#
# que devuelva:
# auto["anio"]
#
# 2. Utilizar:
# sorted()
#
# 3. Utilizar:
# key=obtener_anio
#
# 4. Guardar el resultado en:
# autos_ordenados
#
#
# 5. Recorrer autos_ordenados
# mediante un for.
#
#
# 6. Imprimir:
#
# modelo
# año
#
#
# Resultado esperado:
#
# Chevrolet Bel Air - 1957
# Chevrolet Corvette - 1963
# Chevrolet Camaro - 1967

def obtener_anio(auto):
    return auto["anio"]

autos_ordenados = sorted(autos_clasicos, key=obtener_anio)

for auto in autos_ordenados:
    print(f"{auto['modelo']} - {auto['anio']}")