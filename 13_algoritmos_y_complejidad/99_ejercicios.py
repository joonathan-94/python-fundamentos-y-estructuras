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
