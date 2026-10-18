# ============================================================
# PYTEST BÁSICO
# ============================================================
#
# pytest es una herramienta externa para ejecutar tests.
#
# Permite:
#
# - descubrir tests automáticamente;
# - ejecutar varios tests;
# - mostrar cuáles pasan;
# - mostrar cuáles fallan;
# - entregar información útil cuando un assert falla.


# ============================================================
# 1. FUNCIÓN DE EJEMPLO
# ============================================================

def calcular_total(precio, cantidad):
    return precio * cantidad


# ============================================================
# 2. UNA FUNCIÓN DE TEST
# ============================================================

def test_calcular_total():

    assert calcular_total(
        1000,
        3
    ) == 3000


# ============================================================
# 3. ¿QUÉ TIENE DE ESPECIAL test_?
# ============================================================

# pytest busca funciones cuyo nombre
# comienza con:
#
# test_
#
#
# Por ejemplo:
#
# test_calcular_total()
# test_crear_usuario()
# test_buscar_ticket()
#
#
# Esto permite que pytest
# reconozca esas funciones
# como pruebas.


# ============================================================
# 4. VARIOS TESTS
# ============================================================

def test_calcular_total_cantidad_cero():

    assert calcular_total(
        1000,
        0
    ) == 0


def test_calcular_total_otro_valor():

    assert calcular_total(
        2500,
        2
    ) == 5000


# ============================================================
# 5. RESULTADO ESPERADO
# ============================================================

# Si ejecutamos estos tests con pytest
# y todos son correctos,
# veremos algo similar a:
#
# 3 passed
#
#
# Si uno falla:
#
# pytest mostrará:
#
# qué test falló
# +
# qué comparación fue incorrecta


# ============================================================
# 6. EJEMPLO DE TEST FALLIDO
# ============================================================

# Si escribimos:
#
# assert calcular_total(1000, 3) == 9999
#
# pytest detectará que:
#
# 3000 != 9999
#
# y marcará ese test como FAILED.


# ============================================================
# 7. NOMBRES DE ARCHIVOS
# ============================================================

# Por convención,
# pytest descubre automáticamente
# archivos como:
#
# test_calculos.py
#
# o:
#
# calculos_test.py
#
#
# y dentro de ellos busca funciones
# cuyo nombre comienza con:
#
# test_


# ============================================================
# 8. EJECUTAR PYTEST
# ============================================================

# Desde la terminal:
#
# pytest
#
#
# Para una salida más compacta:
#
# pytest -q
#
#
# También podemos ejecutar
# un archivo específico:
#
# pytest test_calculos.py


# ============================================================
# 9. ASSERT SIGUE SIENDO EL CENTRO
# ============================================================

# pytest no reemplaza:
#
# assert
#
#
# Lo utiliza para comprobar
# resultados esperados.


# ============================================================
# IDEA PRINCIPAL
# ============================================================
#
# función normal
# ↓
# función test_...
# ↓
# assert
# ↓
# pytest ejecuta
# ↓
# PASSED o FAILED