# ============================================================
# EJERCICIOS - MANEJO DE EXCEPCIONES
# ============================================================
#
# Objetivo:
#
# - utilizar try;
# - utilizar except;
# - reconocer ValueError;
# - reconocer ZeroDivisionError.
#
# No es necesario complicarlos.


# ------------------------------------------------------------
# EXC-01 - CONVERTIR EDAD
# ------------------------------------------------------------
#
# Solicita al usuario su edad utilizando input().
#
# Intenta convertir el valor a int().
#
# Si la conversión funciona:
#
# imprime:
#
# Edad registrada: <edad>
#
#
# Si ocurre ValueError:
#
# imprime:
#
# Debes ingresar un número entero.
#
#
# Ejemplo válido:
#
# 31
#
# Resultado:
#
# Edad registrada: 31
#
#
# Ejemplo inválido:
#
# treinta
#
# Resultado:
#
# Debes ingresar un número entero.
#
#
# Tu código aquí:
try:
    edad = int(input("Ingrese su edad: "))
    print(f"Edad registrada: {edad}")
except ValueError:
    print("Debes ingresar un número entero")


# ------------------------------------------------------------
# EXC-02 - DIVISIÓN SEGURA
# ------------------------------------------------------------
#
# Solicita al usuario:
#
# - dividendo
# - divisor
#
# Convierte ambos valores a int().
#
# Luego calcula:
#
# dividendo / divisor
#
#
# Debes controlar:
#
# ValueError
# → si el usuario no ingresa números enteros.
#
# ZeroDivisionError
# → si intenta dividir por cero.
#
#
# Si todo funciona correctamente:
#
# imprime el resultado.
#
#
# Ejemplo:
#
# dividendo = 100
# divisor = 4
#
# Resultado:
#
# Resultado: 25.0
#
#
# Si divisor = 0:
#
# Resultado:
#
# No puedes dividir por cero.
#
#
# Si el usuario escribe texto:
#
# Resultado:
#
# Debes ingresar números enteros.
#
#
# Tu código aquí:

try:
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))
    resultado = dividendo / divisor
    print(f"Resultado: {resultado}")
except ValueError:
    print("Debes ingresar números enteros.")
except ZeroDivisionError:
    print("No puedes dividir por cero.")