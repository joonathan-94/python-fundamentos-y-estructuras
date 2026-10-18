# ============================================================
# TEST-01 - ASSERT
# ============================================================
#
# Crea calcular_total(precio, cantidad).
# Debe devolver precio * cantidad.
#
# Comprueba con assert:
#
# calcular_total(1000, 3) == 3000
# calcular_total(2500, 2) == 5000
# calcular_total(1000, 0) == 0

def calcular_total(precio, cantidad):
    return precio * cantidad

assert calcular_total(1000, 3) == 3000
assert calcular_total(2500, 2) == 5000
assert calcular_total(1000, 0) == 0