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


# ============================================================
# TEST-02 - PYTEST
# ============================================================
#
# Crea es_ticket_valido(titulo).
#
# Debe devolver True si titulo no está vacío.
# Debe devolver False si titulo está vacío.
#
# Crea dos funciones de test:
#
# test_ticket_con_titulo()
# test_ticket_sin_titulo()
#
# Usa assert en ambas.


def es_ticket_valido(titulo):

    if titulo == "":
        return False

    return True


def test_ticket_con_titulo():

    assert es_ticket_valido(
        "Error de acceso"
    ) is True


def test_ticket_sin_titulo():

    assert es_ticket_valido(
        ""
    ) is False
    
