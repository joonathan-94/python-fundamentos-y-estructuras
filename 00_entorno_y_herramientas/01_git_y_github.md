# Git y GitHub — Apuntes de estudio

Este documento registra los conceptos y comandos de Git y GitHub practicados durante el desarrollo del repositorio.

El objetivo es utilizarlo como referencia rápida y ampliar su contenido progresivamente a medida que se estudien nuevas herramientas.

---

# 1. Git y GitHub

Git y GitHub no son lo mismo.

## Git

Git es un sistema de control de versiones.

Permite registrar cambios realizados sobre archivos y mantener un historial del proyecto.

## GitHub

GitHub es una plataforma que permite alojar repositorios Git y trabajar con herramientas adicionales como:

- repositorios remotos;
- Pull Requests;
- Issues;
- revisión de código;
- Actions;
- releases.

---

# 2. Flujo utilizado en este repositorio

La metodología utilizada es:

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
actualizar main local
       ↓
eliminar rama terminada