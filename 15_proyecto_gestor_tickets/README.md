# Gestor de Tickets por Consola

Proyecto integrador del recorrido de fundamentos de Python.

Su objetivo es reunir en una aplicación pequeña varios de los conceptos estudiados durante el curso.

---

## Funcionalidades

```text
1. Crear ticket
2. Listar tickets
3. Buscar ticket por ID
4. Cambiar estado
5. Guardar tickets
6. Salir
```

Cada ticket contiene:

```text
ID
Título
Prioridad
Estado
```

Prioridades utilizadas:

```text
Alta
Media
Baja
```

Estados utilizados:

```text
Abierto
En progreso
Cerrado
```

---

## Estructura

```text
15_proyecto_gestor_tickets/
├── datos/
│   └── tickets.json
├── gestor.py
├── main.py
├── persistencia.py
├── test_gestor.py
└── ticket.py
```

### `ticket.py`

Contiene la clase `Ticket`.

### `gestor.py`

Contiene las operaciones principales:

```text
crear_ticket()
listar_tickets()
buscar_ticket()
cambiar_estado()
```

### `persistencia.py`

Convierte los objetos `Ticket` a datos compatibles con JSON y los reconstruye al cargar el archivo.

### `main.py`

Contiene el menú por consola y coordina las funciones del programa.

### `test_gestor.py`

Contiene tests básicos con pytest para comprobar operaciones principales.

---

## Ejecutar

Desde la raíz del repositorio:

```bash
python 15_proyecto_gestor_tickets/main.py
```

---

## Ejecutar tests

```bash
python -m pytest 15_proyecto_gestor_tickets/test_gestor.py -q
```

Resultado esperado:

```text
2 passed
```

---

## Persistencia

Los tickets se almacenan en:

```text
15_proyecto_gestor_tickets/datos/tickets.json
```

La ruta se construye con `pathlib` a partir de la ubicación de `main.py`, evitando depender del directorio actual de la terminal.

---

## Conceptos integrados

```text
variables
listas
condicionales
ciclos
funciones
módulos
POO
búsqueda lineal
excepciones
JSON
archivos
pathlib
pytest
```

---

## Alcance

Este proyecto es una aplicación educativa por consola.

No incluye:

```text
autenticación
usuarios y roles
base de datos
API
Flask
HTML/CSS
SLA
adjuntos
reportes
```

Esas funcionalidades corresponden a una etapa posterior de desarrollo.
