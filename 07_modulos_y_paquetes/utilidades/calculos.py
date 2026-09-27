# ============================================================
# MÓDULO: calculos
# ============================================================
#
# Este archivo pertenece al paquete:
#
# utilidades
#
# Contiene funciones relacionadas con cálculos simples.
#
#
# Estructura:
#
# utilidades/
# └── calculos.py
#
#
# Podemos pensar:
#
# utilidades
# → paquete
#
# calculos
# → módulo
#
# calcular_promedio
# → función


# ------------------------------------------------------------
# 1. CALCULAR PROMEDIO
# ------------------------------------------------------------

def calcular_promedio(valor_a, valor_b):
    """Calcula y devuelve el promedio de dos valores."""

    return (valor_a + valor_b) / 2


# ------------------------------------------------------------
# 2. CALCULAR DIFERENCIA
# ------------------------------------------------------------

def calcular_diferencia(valor_inicial, valor_final):
    """Devuelve la diferencia entre dos valores."""

    return valor_final - valor_inicial