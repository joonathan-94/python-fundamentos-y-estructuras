# ============================================================
# MÓDULO: texto
# ============================================================
#
# Este módulo contiene funciones relacionadas con
# transformación y normalización de texto.
#
#
# Estructura:
#
# utilidades/
# └── texto.py


# ------------------------------------------------------------
# 1. NORMALIZAR CÓDIGO
# ------------------------------------------------------------

def normalizar_codigo(codigo):
    """Elimina espacios externos y convierte a mayúsculas."""

    return codigo.strip().upper()


# ------------------------------------------------------------
# 2. NORMALIZAR NOMBRE
# ------------------------------------------------------------

def normalizar_nombre(nombre):
    """Limpia un nombre y aplica formato de título."""

    return nombre.strip().title()