# Entorno Python y Dependencias

Esta guía documenta el entorno básico utilizado para trabajar con el repositorio.

---

## Comprobar Python

Ver la versión instalada:

```bash
python --version
```

Verificar `pip` usando el mismo intérprete:

```bash
python -m pip --version
```

Utilizar `python -m pip` ayuda a ejecutar `pip` con el mismo Python que estás utilizando.

---

## Ejecutar archivos Python

Ejemplo:

```bash
python 15_proyecto_gestor_tickets/main.py
```

La estructura:

```python
if __name__ == "__main__":
    main()
```

permite definir el punto de entrada cuando un archivo se ejecuta directamente.

---

## Entorno virtual

Un entorno virtual permite aislar las dependencias de un proyecto.

Crear:

```bash
python -m venv .venv
```

### Git Bash — Windows

```bash
source .venv/Scripts/activate
```

### PowerShell — Windows

```powershell
.venv\Scripts\Activate.ps1
```

### CMD — Windows

```cmd
.venv\Scripts\activate.bat
```

Salir del entorno:

```bash
deactivate
```

---

## Actualizar pip

Con el entorno virtual activo:

```bash
python -m pip install --upgrade pip
```

---

## Dependencias

El código principal del curso utiliza la biblioteca estándar de Python.

La dependencia externa utilizada para testing es:

```text
pytest
```

Instalar desde `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Instalar pytest directamente:

```bash
python -m pip install pytest
```

Comprobar instalación:

```bash
python -m pytest --version
```

---

## Ejecutar tests

Ejecutar todos los tests detectados:

```bash
python -m pytest
```

Ejecutar el test del proyecto final:

```bash
python -m pytest 15_proyecto_gestor_tickets/test_gestor.py -q
```

Convenciones básicas de pytest:

```text
test_*.py
*_test.py

def test_...():
    ...
```

---

## VS Code

Para trabajar con el entorno virtual en VS Code:

```text
Ctrl + Shift + P
↓
Python: Select Interpreter
↓
seleccionar el Python de .venv
```

---

## Rutas con pathlib

Para construir rutas asociadas al archivo actual:

```python
from pathlib import Path

ruta_base = Path(__file__).resolve().parent
ruta_archivo = ruta_base / "datos" / "tickets.json"
```

Esto evita depender del directorio desde donde se ejecutó el comando.

Crear una carpeta si no existe:

```python
ruta_archivo.parent.mkdir(
    parents=True,
    exist_ok=True
)
```

---

## Archivos generados

Python puede generar:

```text
__pycache__/
*.pyc
```

pytest puede generar:

```text
.pytest_cache/
```

Los entornos virtuales pueden estar en:

```text
.venv/
venv/
```

Estos archivos y carpetas no deberían versionarse.

---

## .gitignore recomendado

```gitignore
__pycache__/
*.py[cod]
.pytest_cache/
.venv/
venv/
```

---

## Flujo recomendado al clonar el repositorio

```text
clonar repositorio
↓
crear .venv
↓
activar .venv
↓
instalar requirements.txt
↓
ejecutar código
↓
ejecutar tests
```

Comandos principales:

```bash
python -m venv .venv
python -m pip install -r requirements.txt
python -m pytest
```

La activación del entorno depende de la terminal utilizada.

---

## Documentación oficial

### Python

```text
https://docs.python.org/
https://docs.python.org/3/library/venv.html
https://docs.python.org/3/library/pathlib.html
```

### pip

```text
https://pip.pypa.io/
```

### pytest

```text
https://docs.pytest.org/
```
