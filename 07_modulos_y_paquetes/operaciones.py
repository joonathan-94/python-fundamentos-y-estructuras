# ============================================================
# MÓDULO PROPIO: operaciones
# ============================================================
#
# Este archivo contiene funciones que pueden ser utilizadas
# desde otros archivos Python.
#
# El archivo:
#
# operaciones.py
#
# puede ser importado como:
#
# import operaciones
#
#
# IDEA:
#
# operaciones.py
#     ↓
# contiene lógica reutilizable
#
# otros archivos
#     ↓
# importan y utilizan esa lógica


# ------------------------------------------------------------
# 1. SUMAR DOS VALORES
# ------------------------------------------------------------

def sumar(valor_a, valor_b):
    """Devuelve la suma de dos valores."""

    return valor_a + valor_b


# ------------------------------------------------------------
# 2. CALCULAR UN TOTAL
# ------------------------------------------------------------

def calcular_total(cantidad, precio_unitario):
    """Calcula el total según cantidad y precio unitario."""

    return cantidad * precio_unitario


# ------------------------------------------------------------
# 3. NORMALIZAR UN CÓDIGO
# ------------------------------------------------------------

def normalizar_codigo(codigo):
    """Limpia espacios y convierte un código a mayúsculas."""

    return codigo.strip().upper()


# ------------------------------------------------------------
# 4. CREAR UN RESUMEN DE TICKET
# ------------------------------------------------------------

def crear_resumen_ticket(
    id_ticket,
    titulo_ticket,
    estado_ticket="Nuevo"
):
    """Construye un diccionario con información básica."""

    return {
        "id": id_ticket,
        "titulo": titulo_ticket,
        "estado": estado_ticket
    }


# ------------------------------------------------------------
# 5. CÓDIGO DE PRUEBA DEL MÓDULO
# ------------------------------------------------------------

# Python asigna automáticamente un valor especial a:
#
# __name__
#
# Si este archivo se ejecuta directamente:
#
# __name__ == "__main__"
#
# Si este archivo es importado desde otro:
#
# __name__ == "operaciones"
#
#
# Esto permite escribir pruebas simples que solamente
# se ejecutan cuando abrimos operaciones.py directamente.


if __name__ == "__main__":

    print("Ejecutando operaciones.py directamente")

    resultado_prueba = sumar(10, 5)

    print(resultado_prueba)