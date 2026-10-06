# ------------------------------------------------------------
# INT-01 - LIST COMPREHENSION
# ------------------------------------------------------------

numeros = [
    1,
    2,
    3,
    4,
    5,
    6
]


# OBJETIVO:
#
# crear una nueva lista solamente
# con los números pares.
#
#
# Recuerda:
#
# [
#     elemento
#     for elemento in coleccion
#     if condicion
# ]


numeros_pares = [
    numero
    for numero in numeros
    if numero % 2 == 0
]


print(
    numeros_pares
)



# ------------------------------------------------------------
# INT-02 - DESEMPAQUETADO CON **
# ------------------------------------------------------------

def crear_cientifico(
    nombre,
    area
):

    return {
        "nombre": nombre,
        "area": area
    }


datos = {
    "nombre": "Albert Einstein",
    "area": "Física"
}


# OBJETIVO:
#
# llamar crear_cientifico()
# utilizando:
#
# **datos


cientifico = crear_cientifico(
    **datos
)


print(
    cientifico
)