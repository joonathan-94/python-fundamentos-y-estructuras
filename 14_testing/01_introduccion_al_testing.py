# ============================================================
# INTRODUCCIÓN AL TESTING
# ============================================================
#
# Testing consiste en comprobar que el código
# produce el comportamiento esperado.
#
#
# Idea principal:
#
# resultado obtenido
# ↓
# comparar
# ↓
# resultado esperado


# ============================================================
# 1. FUNCIÓN DE EJEMPLO
# ============================================================

def sumar(a, b):
    return a + b


resultado = sumar(
    2,
    3
)


print(
    resultado
)


# Resultado esperado:
#
# 5


# ============================================================
# 2. ASSERT
# ============================================================

# assert comprueba una condición.
#
#
# Si es True:
#
# el programa continúa.
#
#
# Si es False:
#
# Python genera:
#
# AssertionError


assert sumar(2, 3) == 5


# ============================================================
# 3. DIFERENTES CASOS
# ============================================================

assert sumar(10, 5) == 15

assert sumar(0, 0) == 0

assert sumar(-2, 2) == 0


# ============================================================
# 4. FUNCIÓN DE EJEMPLO REAL
# ============================================================

def es_mayor_de_edad(edad):
    return edad >= 18


assert es_mayor_de_edad(25) is True

assert es_mayor_de_edad(15) is False


# ============================================================
# 5. CASO LÍMITE
# ============================================================

# El valor 18 es importante
# porque está exactamente
# en el límite de la regla.


assert es_mayor_de_edad(18) is True


# ============================================================
# 6. EJEMPLO CON TICKETS
# ============================================================

def limpiar_titulo(titulo):
    return titulo.strip()


assert limpiar_titulo(
    "Error de acceso"
) == "Error de acceso"


assert limpiar_titulo(
    "  Error de acceso  "
) == "Error de acceso"


# ============================================================
# 7. RESULTADO ESPERADO
# ============================================================

# Si todos los assert son correctos,
# el programa termina normalmente.
#
#
# Si alguno falla:
#
# AssertionError


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# test
# ↓
# ejecutar código
# ↓
# obtener resultado
# ↓
# compararlo con lo esperado
#
#
# assert condición
#
# True
# → prueba correcta
#
# False
# → AssertionError