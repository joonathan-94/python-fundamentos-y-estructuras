# Python — Fundamentos y Estructuras de Datos

Repositorio personal de estudio, práctica y consulta de Python.

El objetivo de este repositorio es consolidar una base sólida del lenguaje mediante teoría breve, ejemplos, ejercicios y un proyecto integrador. El recorrido prioriza comprensión, práctica y organización del código por sobre la memorización de sintaxis.

También se utiliza Git y GitHub durante todo el proceso para practicar un flujo de trabajo real basado en ramas, commits, revisión de cambios y Pull Requests.

---

## Estado del recorrido

```text
Fundamentos de Python        ✅
Git y GitHub                 ✅
Testing básico               ✅
Proyecto integrador          ✅
```

El recorrido de fundamentos de este repositorio se considera completado.

---

## Objetivos alcanzados

- Comprender los tipos de datos y estructuras fundamentales de Python.
- Trabajar con operadores, condicionales, ciclos y entrada de usuario.
- Utilizar listas, tuplas, diccionarios y sets.
- Crear funciones reutilizables y organizar código en módulos y paquetes.
- Manejar excepciones y errores previsibles.
- Leer y escribir información en TXT, JSON y CSV.
- Aplicar programación orientada a objetos.
- Conocer herramientas intermedias frecuentes de Python.
- Comprender estructuras de datos y algoritmos fundamentales.
- Introducir análisis básico de complejidad con Big O.
- Crear y ejecutar tests con `assert` y `pytest`.
- Utilizar Git y GitHub durante el desarrollo.
- Integrar los conocimientos en un gestor de tickets por consola.

---

## Resumen de aprendizaje

| Tema | Conceptos principales |
|---|---|
| Fundamentos | Tipos de datos, variables, strings, conversiones y truthiness |
| Operadores | Aritméticos, comparación y operadores lógicos |
| Control de flujo | `if`, `elif`, `else`, `for`, `while`, `range`, `break` y `continue` |
| Colecciones | Listas, tuplas, diccionarios, sets y sus operaciones principales |
| Interacción con usuario | `input()`, limpieza y conversión de datos |
| Funciones | Parámetros, argumentos, `return`, valores por defecto, alcance, docstrings y type hints básicos |
| Módulos y paquetes | `import`, módulos propios, paquetes, `__init__.py` y `__name__` |
| Excepciones | `try`, `except`, `else`, `finally`, `raise` y excepciones comunes |
| Archivos y datos | TXT, JSON, CSV, `with` y codificación UTF-8 |
| POO | Clases, objetos, `self`, atributos, métodos, propiedades, encapsulamiento, herencia y polimorfismo |
| Python intermedio | Comprensiones, `enumerate`, `zip`, `any`, `all`, `sorted`, desempaquetado, `*args`, `**kwargs`, decoradores, generadores, context managers, `pathlib` y `datetime` |
| Estructuras de datos | Pilas, colas, colas de prioridad, listas enlazadas, árboles y grafos |
| Algoritmos | Pensamiento algorítmico, búsquedas, ordenamiento, recursión, BFS y DFS |
| Complejidad | Introducción a `O(1)`, `O(log n)`, `O(n)`, `O(n log n)` y `O(n²)` |
| Testing | `assert`, casos de prueba, casos límite, funciones `test_...` y `pytest` |
| Git y GitHub | Ramas, staging, commits, push, pull, Pull Requests, merge y limpieza de ramas |
| Proyecto final | Integración de POO, funciones, módulos, búsqueda, excepciones, JSON, `pathlib`, consola y pytest |

---

## Conceptos fundamentales

### Colecciones

| Colección | Característica principal | Uso habitual |
|---|---|---|
| `list` | Ordenada y mutable | Datos que cambian durante la ejecución |
| `tuple` | Ordenada e inmutable | Datos cuya estructura debe mantenerse estable |
| `dict` | Pares clave-valor | Registros y datos estructurados |
| `set` | Elementos únicos | Pertenencia, eliminación de duplicados y conjuntos |

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

### Funciones, módulos y paquetes

```text
función
→ encapsula una tarea

módulo
→ archivo .py con código relacionado

paquete
→ agrupa módulos relacionados
```

### Excepciones

```text
operación que puede fallar
↓
try
↓
except específico
↓
respuesta controlada
```

Se prioriza capturar excepciones concretas en lugar de utilizar `Exception` de forma innecesariamente amplia.

### Persistencia

```text
programa
↓
datos en memoria
↓
archivo
↓
datos disponibles en una ejecución posterior
```

Formatos estudiados:

```text
TXT  → texto
JSON → datos estructurados
CSV  → datos tabulares
```

### Programación orientada a objetos

```text
clase
→ define estructura y comportamiento

objeto
→ instancia de una clase

atributos
→ estado

métodos
→ comportamiento
```

### Estructuras de datos

| Estructura | Idea principal | Implementación estudiada |
|---|---|---|
| Pila | LIFO | `list` |
| Cola | FIFO | `collections.deque` |
| Cola de prioridad | Prioridad de procesamiento | `heapq` |
| Lista enlazada | Nodos conectados | Clase `Nodo` |
| Árbol | Jerarquías | Nodos con hijos |
| Grafo | Relaciones generales | `dict` + `set` |

### Algoritmos y complejidad

```text
O(1)       → trabajo aproximadamente constante
O(log n)   → el problema se reduce en cada paso
O(n)       → crecimiento proporcional a los datos
O(n log n) → común en ordenamientos eficientes
O(n²)      → crecimiento cuadrático
```

Algoritmos estudiados:

```text
búsqueda lineal
búsqueda binaria
ordenamiento
recursión
BFS
DFS
```

### Testing

```text
código
↓
test
↓
assert
↓
PASSED o FAILED
```

El objetivo del testing introductorio fue aprender a comprobar comportamiento esperado y detectar regresiones básicas.

---

## Proyecto integrador — Gestor de tickets

Como cierre se desarrolló un gestor de tickets por consola.

### Funcionalidades

```text
crear tickets
listar tickets
buscar tickets por ID
cambiar estado
guardar tickets en JSON
cargar tickets desde JSON
manejar IDs inválidos
ejecutar tests automatizados
```

Cada ticket contiene:

```text
ID
Título
Prioridad
Estado
```

Estados utilizados:

```text
Abierto
En progreso
Cerrado
```

Prioridades utilizadas:

```text
Alta
Media
Baja
```

### Conceptos integrados

```text
POO
listas
funciones
módulos
condicionales
ciclos
input
búsqueda lineal
excepciones
JSON
pathlib
pytest
```

El proyecto es deliberadamente pequeño. Su objetivo es integrar fundamentos antes de avanzar hacia aplicaciones web, bases de datos y arquitecturas de mayor tamaño.

---

## Ejecutar el proyecto

Desde la raíz del repositorio:

```bash
python 15_proyecto_gestor_tickets/main.py
```

Ejecutar sus tests:

```bash
python -m pytest 15_proyecto_gestor_tickets/test_gestor.py -q
```

---

## Roadmap completado

- [x] 00 - Entorno y herramientas
- [x] 01 - Fundamentos
- [x] 02 - Operadores
- [x] 03 - Control de flujo
- [x] 04 - Colecciones y métodos
- [x] 05 - Interacción con el usuario
- [x] 06 - Funciones
- [x] 07 - Módulos y paquetes
- [x] 08 - Manejo de excepciones
- [x] 09 - Archivos y datos
- [x] 10 - Programación orientada a objetos
- [x] 11 - Python intermedio
- [x] 12 - Estructuras de datos
- [x] 13 - Algoritmos y complejidad
- [x] 14 - Testing
- [x] 15 - Proyecto gestor de tickets

---

## Estructura general

```text
python-fundamentos-y-estructuras/
│
├── 00_entorno_y_herramientas/
│   ├── 01_git_y_github.md
│   └── 02_entorno_python_y_dependencias.md
│
├── 01_fundamentos/
├── 02_operadores/
├── 03_control_de_flujo/
├── 04_colecciones_y_metodos/
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
│
├── 15_proyecto_gestor_tickets/
│   ├── datos/
│   │   └── tickets.json
│   ├── gestor.py
│   ├── main.py
│   ├── persistencia.py
│   ├── README.md
│   ├── test_gestor.py
│   └── ticket.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Entorno y dependencias

El código del curso utiliza principalmente la biblioteca estándar de Python.

La dependencia externa utilizada para testing es:

```text
pytest
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Instalar dependencias:

```bash
python -m pip install -r requirements.txt
```

La explicación completa del entorno se encuentra en:

```text
00_entorno_y_herramientas/02_entorno_python_y_dependencias.md
```

---

## Metodología aplicada

```text
comprender
↓
probar
↓
resolver ejercicios
↓
revisar
↓
versionar
↓
integrar
```

Los ejercicios se mantuvieron intencionalmente breves durante los fundamentos. La complejidad aumentó progresivamente hasta llegar al proyecto integrador.

---

## Convenciones de código

Durante el recorrido se priorizaron:

- `snake_case` para variables y funciones.
- Nombres descriptivos.
- Código simple y legible.
- Funciones con responsabilidades claras.
- Comentarios que aporten contexto.
- Docstrings cuando agregan información útil.
- Separación progresiva en módulos.
- Excepciones específicas.
- UTF-8 para archivos de texto.
- Uso de `pathlib` para rutas cuando resulta apropiado.

---

## Git y GitHub

Git y GitHub se utilizaron durante todo el recorrido.

Flujo habitual:

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
git switch main
↓
git pull
↓
eliminar rama local
↓
git fetch --prune
```

Convenciones utilizadas:

```text
study/...    → estudio
docs/...     → documentación
refactor/... → refactorización
fix/...      → correcciones
feature/...  → funcionalidades
```

La guía completa se encuentra en:

```text
00_entorno_y_herramientas/01_git_y_github.md
```

---

## Próximo paso

Este repositorio cierra el recorrido de fundamentos.

Una progresión natural a partir de aquí es:

```text
Python
↓
Flask
↓
HTTP y aplicaciones web
↓
SQL
↓
PostgreSQL
↓
testing de aplicaciones
↓
proyectos backend completos
```

Los fundamentos adquiridos también pueden reutilizarse en:

```text
automatización
integraciones
APIs
procesamiento de archivos
procesamiento de datos
análisis de datos
```

---

## Fuentes de referencia

Se prioriza documentación oficial.

### Python

```text
https://docs.python.org/
https://docs.python.org/3/tutorial/
https://docs.python.org/3/library/
https://docs.python.org/3/library/venv.html
```

### pytest

```text
https://docs.pytest.org/
```

### pip

```text
https://pip.pypa.io/
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

## Cierre

El objetivo de este repositorio no es demostrar dominio absoluto de Python, sino documentar una base práctica sobre la cual continuar construyendo.

```text
leer código
↓
comprenderlo
↓
escribirlo
↓
probarlo
↓
depurarlo
↓
organizarlo
↓
versionarlo
↓
mantenerlo
↓
construir soluciones propias
```
