# ============================================================
# EJERCICIOS - PROGRAMACIÓN ORIENTADA A OBJETOS
# ============================================================


# ------------------------------------------------------------
# POO-01 - CLASE, OBJETO, ATRIBUTOS Y MÉTODO
# ------------------------------------------------------------
#
# Crea una clase llamada Cientifico.
#
# Debe recibir:
#
# - nombre
# - area
#
# Guarda ambos valores como atributos.
#
# Crea un método llamado:
#
# obtener_resumen()
#
# que retorne un texto similar a:
#
# "Albert Einstein - Física"
#
#
# Luego:
#
# 1. Crea un objeto utilizando la clase.
# 2. Llama al método obtener_resumen().
# 3. Imprime el resultado.
#
#
# No utilices herencia ni properties en este ejercicio.


# ------------------------------------------------------------
# MI SOLUCIÓN INICIAL
# ------------------------------------------------------------

class CientificoInicial:
    def __init__(self, nombre, area):
        self._nombre = nombre
        self._area = area

    def obtener_resumen(self):
        print(
            f"{self._nombre} - {self._area}"
        )


cientifico_inicial = CientificoInicial(
    "Rick Sanchez",
    "Científico"
)

cientifico_inicial.obtener_resumen()


# Esta solución funciona para mostrar el resultado.
#
# Sin embargo, el ejercicio solicita que obtener_resumen()
# RETORNE el texto.
#
# print()
# → muestra información directamente.
#
# return
# → devuelve información para poder utilizarla posteriormente.
#
#
# Además, en este ejercicio no necesitamos marcar los
# atributos como internos mediante "_".
#
# Podemos utilizar simplemente:
#
# self.nombre
# self.area


# ------------------------------------------------------------
# VERSIÓN CORREGIDA
# ------------------------------------------------------------

class Cientifico:
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area

    def obtener_resumen(self):
        return (
            f"{self.nombre} - {self.area}"
        )


cientifico = Cientifico(
    "Rick Sanchez",
    "Científico"
)

print(
    cientifico.obtener_resumen()
)


# En esta versión:
#
# Cientifico
# → clase
#
# cientifico
# → objeto
#
# nombre / area
# → atributos
#
# obtener_resumen()
# → método
#
# return
# → entrega el resumen al código que llamó al método
#
# print()
# → muestra posteriormente ese resultado


# ============================================================
# POO-02 - HERENCIA Y POLIMORFISMO BÁSICO
# ============================================================
#
# Crea una clase llamada Usuario.
#
# Debe recibir:
#
# - nombre
#
# Debe tener un método:
#
# obtener_rol()
#
# que retorne:
#
# "Usuario"
#
#
# Después crea una clase:
#
# Tecnico
#
# que herede de Usuario.
#
#
# Sobrescribe obtener_rol() para que retorne:
#
# "Técnico"
#
#
# Finalmente:
#
# 1. Crea un objeto Tecnico.
# 2. Imprime su nombre.
# 3. Imprime el resultado de obtener_rol().
#
#
# No agregues atributos adicionales ni otras clases.


# ------------------------------------------------------------
# MI SOLUCIÓN INICIAL
# ------------------------------------------------------------

class UsuarioInicial:
    def __init__(self, nombre):
        self._nombre = nombre

    def obtener_rol(self):
        print("Usuario")


class TecnicoInicial(UsuarioInicial):
    def obtener_rol(self):
        print("Tecnico")


tecnico_inicial = TecnicoInicial(
    "Don Ramon"
)

print(tecnico_inicial._nombre)
print(tecnico_inicial.obtener_rol())


# Esta solución demuestra correctamente:
#
# - creación de la clase padre;
# - herencia;
# - creación de una clase hija;
# - sobrescritura de obtener_rol().
#
#
# El problema aparece nuevamente con print().
#
# obtener_rol() imprime:
#
# "Tecnico"
#
# pero no retorna ningún valor.
#
#
# Por eso al ejecutar:
#
# print(tecnico_inicial.obtener_rol())
#
# ocurre:
#
# obtener_rol()
# ↓
# imprime "Tecnico"
# ↓
# no encuentra return
# ↓
# Python devuelve None
# ↓
# print() imprime None
#
#
# Por eso la salida original terminaba mostrando:
#
# Tecnico
# None


# ------------------------------------------------------------
# VERSIÓN CORREGIDA
# ------------------------------------------------------------

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def obtener_rol(self):
        return "Usuario"


class Tecnico(Usuario):
    def obtener_rol(self):
        return "Técnico"


tecnico = Tecnico(
    "Don Ramón"
)

print(tecnico.nombre)
print(tecnico.obtener_rol())


# En esta versión:
#
# Usuario
# → clase padre
#
# Tecnico
# → clase hija
#
# Tecnico(Usuario)
# → herencia
#
# obtener_rol()
# → método heredado y posteriormente sobrescrito
#
#
# Usuario devuelve:
#
# "Usuario"
#
# Tecnico devuelve:
#
# "Técnico"
#
#
# El mismo método puede producir un comportamiento
# diferente dependiendo del tipo de objeto.
#
# Esta es la idea básica de polimorfismo.


# ============================================================
# APRENDIZAJE PRINCIPAL DE LOS EJERCICIOS
# ============================================================
#
# POO-01:
#
# clase
# ↓
# objeto
# ↓
# atributos
# ↓
# método
#
#
# POO-02:
#
# clase padre
# ↓
# herencia
# ↓
# clase hija
# ↓
# sobrescritura
# ↓
# polimorfismo
#
#
# IMPORTANTE:
#
# print()
# → muestra información.
#
# return
# → devuelve información.
#
#
# Un método que necesita utilizar datos del objeto
# normalmente recibe:
#
# self
#
#
# Ejemplo:
#
# def obtener_resumen(self):
#     return self.nombre
#
#
# Los atributos simples pueden mantenerse públicos:
#
# self.nombre
#
#
# El prefijo "_":
#
# self._nombre
#
# se reserva normalmente para indicar que un atributo
# está pensado para uso interno.