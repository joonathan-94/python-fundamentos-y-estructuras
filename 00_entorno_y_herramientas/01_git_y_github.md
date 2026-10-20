# Git y GitHub — Guía de estudio

Esta guía resume el flujo de Git y GitHub utilizado durante el estudio de Python.

---

## Git y GitHub

```text
Git
→ sistema de control de versiones local

GitHub
→ plataforma remota para almacenar repositorios y colaborar
```

Git permite registrar cambios en el código. GitHub permite publicar el repositorio, trabajar con ramas y utilizar Pull Requests.

---

## Estados principales

```text
Working tree
→ archivos que estás modificando

Staging area
→ cambios preparados para el próximo commit

Repository
→ historial de commits
```

Flujo:

```text
modificar
↓
git diff
↓
git add
↓
git diff --staged
↓
git commit
```

---

## Revisar cambios

Ver estado:

```bash
git status
```

Ver cambios todavía no preparados:

```bash
git diff
```

Ver cambios preparados:

```bash
git diff --staged
```

Ver historial resumido:

```bash
git log --oneline --graph --decorate
```

---

## Preparar y registrar cambios

Agregar un archivo:

```bash
git add ruta/archivo.py
```

Agregar varios archivos:

```bash
git add archivo1.py archivo2.py
```

Agregar todos los cambios de una carpeta:

```bash
git add -A carpeta/
```

Crear commit:

```bash
git commit -m "Describe the change"
```

Los mensajes de commit de este repositorio se escriben en inglés y describen la intención del cambio.

Ejemplos:

```text
Add Python testing fundamentals and assert exercise
Add ticket search and status update
Add ticket persistence and console menu
Add tests for ticket manager
```

---

## Ramas

Ver ramas:

```bash
git branch
```

Cambiar de rama:

```bash
git switch main
```

Crear una rama y cambiar a ella:

```bash
git switch -c study/testing
```

Convenciones utilizadas:

```text
study/...    → bloques de estudio
docs/...     → documentación
feature/...  → funcionalidades
fix/...      → correcciones
refactor/... → reorganización interna
```

---

## Sincronizar main

Antes de comenzar un bloque nuevo:

```bash
git switch main
git pull
```

---

## Push y upstream

Primer push de una rama:

```bash
git push -u origin nombre-rama
```

`-u` establece la relación entre la rama local y la rama remota.

Después normalmente basta con:

```bash
git push
```

---

## Pull Request

Flujo utilizado:

```text
crear rama
↓
trabajar
↓
commits
↓
push
↓
abrir Pull Request
↓
revisar Files changed
↓
merge
```

Convención de títulos:

```text
Study: ...
Docs: ...
Feature: ...
Fix: ...
Refactor: ...
```

Plantilla breve:

```md
## Summary

Resumen del cambio.

## Changes

- Cambio 1.
- Cambio 2.

## Purpose

Motivo del cambio.
```

---

## Después del merge

Actualizar `main`:

```bash
git switch main
git pull
```

Eliminar la rama local integrada:

```bash
git branch -d nombre-rama
```

Limpiar referencias a ramas remotas eliminadas:

```bash
git fetch --prune
```

---

## Remote origin

```text
origin
→ repositorio remoto principal
```

Ver remotos:

```bash
git remote -v
```

---

## .gitignore

`.gitignore` evita versionar archivos generados o locales.

Configuración recomendada para este repositorio:

```gitignore
__pycache__/
*.py[cod]
.pytest_cache/
.venv/
venv/
```

---

## Flujo completo aplicado

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
git branch -d ...
↓
git fetch --prune
```

---

## Buenas prácticas aplicadas

- Crear ramas para cambios coherentes.
- Revisar `git diff` antes de preparar cambios.
- Revisar `git diff --staged` antes del commit.
- Evitar mezclar cambios no relacionados en un mismo commit.
- Utilizar mensajes de commit descriptivos.
- Revisar `Files changed` antes del merge.
- Actualizar `main` después de integrar una rama.
- Eliminar ramas locales terminadas.
- Ignorar archivos generados mediante `.gitignore`.

---

## Referencia rápida

```text
git status
→ estado actual

git diff
→ cambios no staged

git add
→ preparar cambios

git diff --staged
→ revisar staged

git commit
→ registrar cambios

git switch
→ cambiar de rama

git branch
→ listar o eliminar ramas

git pull
→ traer e integrar cambios

git push
→ subir commits

git fetch --prune
→ actualizar referencias y limpiar ramas remotas eliminadas

git log --oneline --graph --decorate
→ revisar historial
```

---

## Documentación oficial

```text
https://git-scm.com/docs
https://docs.github.com/
```
