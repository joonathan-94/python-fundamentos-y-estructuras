# Python — Fundamentos y Estructuras de Datos

Repositorio personal de estudio, práctica y consulta de Python.

El objetivo es construir una base sólida del lenguaje, mejorar progresivamente la lógica de programación y comprender los conceptos fundamentales necesarios para desarrollar aplicaciones reales.

El aprendizaje está orientado principalmente a desarrollo backend, pero busca mantener una base general de Python que pueda aplicarse posteriormente en áreas como automatización, integraciones entre sistemas, procesamiento de datos y análisis de datos.

Este repositorio también funciona como registro del aprendizaje práctico de Git y GitHub utilizado durante todo el proceso.

---

## Objetivos

- Consolidar los fundamentos esenciales de Python.
- Comprender cómo funciona el lenguaje y no limitar el aprendizaje a memorizar sintaxis.
- Mejorar progresivamente la lógica de programación.
- Aprender a seleccionar estructuras de datos según el problema que se desea resolver.
- Estudiar las principales colecciones y estructuras de datos de Python.
- Aprender funciones, módulos, paquetes, excepciones y manejo de archivos.
- Estudiar programación orientada a objetos.
- Introducir testing y buenas prácticas de desarrollo.
- Estudiar estructuras de datos y algoritmos fundamentales.
- Desarrollar un gestor de tickets por consola como proyecto integrador.
- Preparar una base técnica para continuar con Flask y PostgreSQL.
- Construir conocimientos reutilizables en backend, automatizaciones, integraciones y procesamiento de datos.
- Practicar Git y GitHub mediante ramas, commits, Pull Requests y revisión de cambios.

---

## Enfoque de estudio

El repositorio sigue una metodología progresiva orientada a comprender primero los conceptos que tienen mayor utilidad práctica.

El objetivo no es memorizar todas las características disponibles en Python, sino dominar primero los fundamentos que permiten resolver la mayoría de los problemas habituales.

Flujo general de estudio:

```text
comprender el concepto
↓
revisar ejemplos
↓
escribir código
↓
resolver ejercicios breves
↓
revisar resultados
↓
versionar con Git
↓
continuar al siguiente tema
```

Los ejercicios iniciales se mantienen deliberadamente simples y enfocados.

La complejidad aumentará progresivamente al combinar conocimientos en módulos posteriores y, especialmente, en el proyecto integrador.

---

## Estado actual

### Bloques completados

- [x] 01 - Fundamentos
- [x] 02 - Operadores
- [x] 03 - Control de flujo
- [x] 04 - Colecciones y métodos

### Próximo bloque

- [ ] 05 - Interacción con el usuario

---

## Colecciones estudiadas

Hasta ahora se han estudiado las principales colecciones incorporadas de Python:

| Colección | Característica principal | Uso habitual |
|---|---|---|
| `list` | Secuencia mutable y ordenada | Datos que pueden cambiar, agregarse, eliminarse o recorrerse en orden |
| `tuple` | Secuencia inmutable y ordenada | Datos cuya estructura debería permanecer estable |
| `dict` | Pares clave-valor | Registros, configuraciones, datos estructurados, APIs y JSON |
| `set` | Elementos únicos sin posiciones | Eliminar duplicados, comprobar pertenencia y comparar conjuntos |

Regla rápida:

```text
¿Necesito una secuencia modificable?
→ list

¿Necesito una secuencia estable?
→ tuple

¿Necesito relacionar claves con valores?
→ dict

¿Necesito elementos únicos o comparar grupos?
→ set
```

---

## Roadmap

- [ ] 00 - Entorno y herramientas
- [x] 01 - Fundamentos
- [x] 02 - Operadores
- [x] 03 - Control de flujo
- [x] 04 - Colecciones y métodos
- [ ] 05 - Interacción con el usuario
- [ ] 06 - Funciones
- [ ] 07 - Módulos y paquetes
- [ ] 08 - Manejo de excepciones
- [ ] 09 - Archivos y datos
- [ ] 10 - Programación orientada a objetos
- [ ] 11 - Python intermedio
- [ ] 12 - Estructuras de datos
- [ ] 13 - Algoritmos y complejidad
- [ ] 14 - Testing
- [ ] 15 - Proyecto gestor de tickets

> El bloque `00_entorno_y_herramientas` se trabaja en paralelo al estudio de Python e incluye principalmente Git, GitHub y otras herramientas utilizadas durante el desarrollo.

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
├── 06_funciones/
├── 07_modulos_y_paquetes/
├── 08_manejo_excepciones/
├── 09_archivos_y_datos/
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

> Git no almacena carpetas vacías de forma independiente. Por esta razón, algunos directorios planificados pueden no aparecer todavía en GitHub hasta que contengan archivos versionados.

---

## Organización de los ejercicios

Los ejercicios de cada módulo se concentran principalmente en:

```text
99_ejercicios.py
```

Se utilizan identificadores según el tema estudiado.

Ejemplos:

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
```

La cantidad de ejercicios se mantiene reducida durante los fundamentos.

La prioridad es comprobar comprensión y continuar avanzando.

Los ejercicios de mayor complejidad aparecerán posteriormente al integrar diferentes conceptos.

---

## Convenciones de código

Se prioriza:

```text
snake_case
nombres descriptivos
código legible
comentarios útiles
simplicidad
consistencia
```

Los nombres de archivos y carpetas se mantienen principalmente en español para facilitar la organización del material de estudio.

Los ejemplos buscan representar situaciones cercanas a aplicaciones reales siempre que sea posible.

---

## Git y GitHub

Git y GitHub se estudian en paralelo con Python.

Flujo utilizado actualmente:

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
revisión
↓
merge
↓
sincronizar main
↓
eliminar rama terminada
```

Convenciones utilizadas:

```text
study/...      → bloques de estudio
docs/...       → documentación
refactor/...   → reorganización o mejora interna
fix/...        → correcciones
feature/...    → funcionalidades
```

Los mensajes de commit se escriben en inglés y deben describir claramente la intención del cambio.

Ejemplo:

```text
Expand Python collections study and exercises
```

La documentación específica de Git y GitHub se encuentra en:

```text
00_entorno_y_herramientas/01_git_y_github.md
```

---

## Proyecto integrador

Después de completar los módulos principales se desarrollará un gestor de tickets por consola.

El proyecto permitirá integrar progresivamente conceptos como:

```text
variables
operadores
colecciones
condicionales
ciclos
funciones
módulos
excepciones
archivos
POO
testing
```

La intención no será únicamente lograr que el programa funcione, sino aprender a estructurar código que pueda comprenderse, mantenerse y evolucionar.

---

## Camino posterior

El recorrido previsto es:

```text
Python sólido
↓
gestor de tickets por consola
↓
Flask
↓
aplicación web
↓
PostgreSQL
↓
proyectos reales
```

Los fundamentos adquiridos también podrán utilizarse posteriormente en:

```text
backend
automatizaciones
integraciones
APIs
procesamiento de archivos
procesamiento y análisis de datos
```

---

## Proyectos futuros

Los conocimientos desarrollados en este repositorio servirán como base para proyectos personales de mayor escala.

```text
WorkDesk
→ sistema de gestión de tickets y trabajo

MoneyDesk
→ aplicación de finanzas personales
```

---

## Fuentes de referencia

Se prioriza documentación oficial como fuente técnica.

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

## Filosofía del repositorio

```text
entender
+
practicar
+
documentar
+
versionar
+
construir
```

El objetivo no es convertirse inmediatamente en experto en cada característica de Python.

El objetivo es desarrollar fundamentos suficientemente sólidos para escribir código, comprender código existente, detectar errores, aprender nuevas herramientas y comenzar a construir proyectos reales con criterio técnico.