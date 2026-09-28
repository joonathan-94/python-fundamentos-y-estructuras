# Python — Fundamentos y Estructuras de Datos

Repositorio personal de estudio y práctica de Python.

El objetivo es construir fundamentos sólidos del lenguaje mediante un aprendizaje progresivo, combinando teoría, ejemplos, ejercicios breves y aplicación práctica.

El recorrido está orientado a desarrollar una base reutilizable para programación general, desarrollo backend, automatización, integraciones, procesamiento de archivos y análisis de datos.

Git y GitHub se estudian y utilizan en paralelo para aplicar desde el inicio un flujo de trabajo basado en ramas, commits, Pull Requests y revisión de cambios.

---

## Estado actual

### Progreso en Python

- [x] Fundamentos
- [x] Operadores
- [x] Control de flujo
- [x] Colecciones y métodos
- [x] Interacción con el usuario
- [x] Funciones
- [x] Módulos y paquetes
- [x] Manejo de excepciones
- [x] Archivos y datos
- [ ] Programación orientada a objetos

### Próximo tema

```text
Programación orientada a objetos (POO)
```

El bloque de entorno, Git y GitHub se trabaja en paralelo durante todo el proceso.

---

## Resumen de aprendizaje

| Tema | Conceptos principales |
|---|---|
| Fundamentos | Tipos de datos, variables, strings y conversión de tipos |
| Operadores | Operadores aritméticos, de comparación y lógicos |
| Control de flujo | `if`, `elif`, `else`, ciclos `for` y `while`, `break` y `continue` |
| Colecciones | Listas, tuplas, diccionarios y sets |
| Interacción con el usuario | `input()`, recepción de datos y conversión de valores |
| Funciones | `def`, parámetros, argumentos, `return`, alcance, docstrings y type hints básicos |
| Módulos y paquetes | `import`, módulos propios, paquetes, `__init__.py` y reutilización entre archivos |
| Manejo de excepciones | `try`, `except`, `else`, `finally`, `raise` y excepciones comunes |
| Archivos y datos | Lectura y escritura de TXT, JSON y CSV |

El objetivo no es memorizar cada característica del lenguaje, sino comprender los conceptos esenciales y aprender a combinarlos progresivamente.

---

## Conceptos fundamentales

### Colecciones

| Colección | Característica | Uso habitual |
|---|---|---|
| `list` | Secuencia mutable y ordenada | Datos que pueden cambiar durante la ejecución |
| `tuple` | Secuencia inmutable y ordenada | Datos cuya estructura debería mantenerse estable |
| `dict` | Pares clave-valor | Registros y datos estructurados |
| `set` | Elementos únicos | Eliminar duplicados y realizar operaciones entre conjuntos |

Regla práctica:

```text
Secuencia modificable
→ list

Secuencia estable
→ tuple

Relación clave-valor
→ dict

Elementos únicos
→ set
```

### Organización del código

```text
función
↓
encapsula una tarea reutilizable

módulo
↓
archivo .py que organiza código relacionado

paquete
↓
agrupa módulos relacionados
```

### Manejo de errores

```text
operación que puede fallar
↓
try

excepción conocida
↓
except

respuesta controlada
```

También se estudiaron:

```text
else
finally
raise
```

como herramientas complementarias para controlar el comportamiento ante errores.

### Persistencia básica

Antes:

```text
programa
↓
variables
↓
los datos desaparecen al finalizar
```

Ahora:

```text
programa
↓
archivo
↓
los datos pueden conservarse
```

Formatos trabajados:

```text
TXT
→ texto simple

JSON
→ información estructurada

CSV
→ información tabular
```

---

## Roadmap

- [ ] 00 - Entorno y herramientas — estudio paralelo
- [x] 01 - Fundamentos
- [x] 02 - Operadores
- [x] 03 - Control de flujo
- [x] 04 - Colecciones y métodos
- [x] 05 - Interacción con el usuario
- [x] 06 - Funciones
- [x] 07 - Módulos y paquetes
- [x] 08 - Manejo de excepciones
- [x] 09 - Archivos y datos
- [ ] 10 - Programación orientada a objetos
- [ ] 11 - Python intermedio
- [ ] 12 - Estructuras de datos
- [ ] 13 - Algoritmos y complejidad
- [ ] 14 - Testing
- [ ] 15 - Proyecto gestor de tickets

---

## Estructura del repositorio

```text
python-fundamentos-y-estructuras/
│
├── 00_entorno_y_herramientas/
│   └── 01_git_y_github.md
│
├── 01_fundamentos/
│   ├── 01_tipos_datos.py
│   ├── 02_variables.py
│   ├── 03_strings.py
│   ├── 04_conversion_tipos.py
│   └── 99_ejercicios.py
│
├── 02_operadores/
│   ├── 01_aritmeticos.py
│   ├── 02_comparacion.py
│   ├── 03_logicos.py
│   └── 99_ejercicios.py
│
├── 03_control_de_flujo/
│   ├── 01_sentencias_condicionales.py
│   ├── 02_ciclos.py
│   └── 99_ejercicios.py
│
├── 04_colecciones_y_metodos/
│   ├── 01_listas.py
│   ├── 02_tuplas.py
│   ├── 03_diccionarios.py
│   ├── 04_sets.py
│   └── 99_ejercicios.py
│
├── 05_interaccion_usuario/
│   ├── 01_inputs.py
│   └── 99_ejercicios.py
│
├── 06_funciones/
│   ├── 01_funciones_basicas.py
│   ├── 02_parametros_y_retorno.py
│   ├── 03_alcance_y_buenas_practicas.py
│   └── 99_ejercicios.py
│
├── 07_modulos_y_paquetes/
│   ├── 01_modulos_e_importaciones.py
│   ├── 02_modulos_propios.py
│   ├── 03_paquetes.py
│   ├── operaciones.py
│   ├── utilidades/
│   │   ├── __init__.py
│   │   ├── calculos.py
│   │   └── texto.py
│   └── 99_ejercicios.py
│
├── 08_manejo_excepciones/
│   ├── 01_excepciones_y_try_except.py
│   ├── 02_else_finally_raise_y_buenas_practicas.py
│   └── 99_ejercicios.py
│
├── 09_archivos_y_datos/
│   ├── 01_archivos_texto.py
│   ├── 02_json.py
│   ├── 03_csv.py
│   ├── datos/
│   └── 99_ejercicios.py
│
├── 10_POO/
├── 11_python_intermedio/
├── 12_estructuras_de_datos/
├── 13_algoritmos_y_complejidad/
├── 14_testing/
├── 15_proyecto_gestor_tickets/
│
├── .gitignore
└── README.md
```

> Git no almacena carpetas vacías de forma independiente. Algunos directorios planificados pueden no aparecer todavía en GitHub hasta contener archivos versionados.

---

## Metodología de estudio

El aprendizaje se desarrolla de forma incremental:

```text
comprender el concepto
↓
revisar ejemplos
↓
escribir y ejecutar código
↓
resolver ejercicios breves
↓
revisar resultados
↓
versionar con Git
↓
continuar al siguiente tema
```

La cantidad de ejercicios se mantiene deliberadamente reducida durante los fundamentos.

El objetivo es comprobar la comprensión y mantener un avance constante.

La complejidad aumentará progresivamente al combinar conocimientos y desarrollar programas más completos.

---

## Organización de los ejercicios

Cada bloque concentra principalmente sus ejercicios en:

```text
99_ejercicios.py
```

Se utilizan identificadores según el tema:

```text
VAR-01
STR-01
CONV-01
OP-01
CF-01
LIST-01
TUP-01
DICT-01
SET-01
INPUT-01
FUNC-01
MOD-01
EXC-01
ARCH-01
```

Esto permite identificar rápidamente qué concepto practica cada ejercicio.

---

## Convenciones de código

Durante el estudio se priorizan:

- `snake_case` para funciones y variables.
- Nombres descriptivos.
- Código simple y legible.
- Comentarios que aporten contexto.
- Funciones con responsabilidades claras.
- Docstrings cuando agregan información útil.
- Separación progresiva del código en módulos.
- Manejo explícito de errores previsibles.
- UTF-8 para archivos de texto.
- Consistencia de estilo.

Los nombres de archivos y carpetas se mantienen principalmente en español para facilitar la organización y consulta del material.

---

## Git y GitHub

Git y GitHub forman parte del aprendizaje y se utilizan para versionar cada bloque de estudio.

Flujo de trabajo aplicado:

```text
main actualizado
↓
crear rama
↓
realizar cambios
↓
git status
↓
git diff
↓
git add
↓
git diff --staged
↓
git commit
↓
git push
↓
Pull Request
↓
revisión de cambios
↓
merge
↓
sincronizar main
↓
eliminar rama terminada
```

### Convención de ramas

```text
study/...
→ bloques de estudio

docs/...
→ documentación

refactor/...
→ reorganización interna

fix/...
→ correcciones

feature/...
→ funcionalidades
```

### Commits

Los mensajes de commit se escriben en inglés y buscan describir claramente la intención del cambio.

Ejemplos:

```text
Expand Python functions study and exercises

Expand Python modules and packages study and exercises

Expand Python exception handling study and exercises

Expand Python files and data study and exercises
```

La documentación específica de Git y GitHub se mantiene en:

```text
00_entorno_y_herramientas/01_git_y_github.md
```

---

## Proyecto integrador

El último bloque del recorrido será un gestor de tickets por consola desarrollado dentro de este mismo repositorio.

Su propósito será integrar progresivamente los conocimientos adquiridos:

```text
fundamentos
+
operadores
+
control de flujo
+
colecciones
+
interacción con el usuario
+
funciones
+
módulos y paquetes
+
manejo de excepciones
+
archivos y datos
+
programación orientada a objetos
+
testing
```

El objetivo no será solamente conseguir que el programa funcione, sino practicar organización, reutilización, mantenibilidad y evolución del código.

---

## Aplicación de los conocimientos

Los fundamentos estudiados buscan servir como base para continuar aprendiendo y desarrollar posteriormente soluciones relacionadas con:

```text
desarrollo backend
automatización
APIs
integraciones entre sistemas
procesamiento de archivos
procesamiento de datos
análisis de datos
```

El repositorio representa una base de aprendizaje, no una especialización cerrada en una única área.

---

## Fuentes de referencia

Durante el estudio se prioriza documentación oficial.

### Python

```text
https://docs.python.org/
https://docs.python.org/3/tutorial/
https://docs.python.org/3/library/
```

### Git

```text
https://git-scm.com/docs
```

### GitHub

```text
https://docs.github.com/
```

---

## Objetivo del repositorio

Este repositorio busca registrar una evolución progresiva desde los fundamentos de Python hasta la capacidad de construir programas propios con una estructura cada vez más organizada.

El objetivo es desarrollar una base suficiente para:

```text
leer código
↓
comprenderlo
↓
escribirlo
↓
depurarlo
↓
organizarlo
↓
reutilizarlo
↓
mantenerlo
↓
construir soluciones propias
```

No se busca memorizar cada característica del lenguaje, sino adquirir fundamentos que permitan continuar aprendiendo y resolver problemas progresivamente más complejos.