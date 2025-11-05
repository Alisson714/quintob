# 🚀 CI/CD con GitHub Actions

## Objetivo de la clase

Comprender los conceptos fundamentales de Integración Continua (CI) y Despliegue Continuo (CD), y aplicar estos conocimientos mediante la configuración de un workflow automatizado en GitHub Actions que construye, prueba y publica una imagen Docker en el GitHub Container Registry (GHCR).

---

## 🧠 1. Introducción a CI/CD

### 🔹 ¿Qué es la Integración Continua (CI)?

La Integración Continua es una práctica de desarrollo de software donde los desarrolladores integran frecuentemente su código en un repositorio compartido.

Cada integración se verifica automáticamente mediante pruebas y análisis estáticos del código.

**Objetivo:** detectar errores lo antes posible y mantener el proyecto en un estado funcional.

### 🔹 ¿Qué es el Despliegue Continuo (CD)?

El Despliegue Continuo automatiza el proceso posterior: desde que el código pasa las pruebas, hasta que se despliega en un entorno de staging o producción.

**Objetivo:** entregar software de calidad más rápido, confiable y sin intervención manual.

---

## ⚙️ 2. Beneficios de la automatización

| Beneficio | Descripción |
|-----------|-------------|
| 🚀 **Velocidad** | Los cambios llegan más rápido a producción. |
| 🧩 **Calidad** | Se ejecutan pruebas y revisiones automáticas. |
| 🔁 **Consistencia** | Cada despliegue sigue el mismo proceso. |
| 🧱 **Confiabilidad** | Menos errores humanos en integración y despliegue. |
| 📈 **Escalabilidad** | Los pipelines crecen junto con el proyecto. |

---

## 🧰 3. GitHub Actions: herramienta de CI/CD

GitHub Actions permite automatizar tareas directamente desde un repositorio de GitHub.

Se define un archivo `.yml` en la carpeta `.github/workflows/` con los pasos del pipeline.

### 📘 Documentación oficial:

👉 [docs.github.com/en/actions](https://docs.github.com/en/actions)

---

## 🧪 4. Ejemplo práctico: Proyecto Python con Docker

### 🧩 Estructura del proyecto

```
my-python-app/
│
├── app.py
├── requirements.txt
├── Dockerfile
└── .github/
    └── workflows/
        └── ci.yml
```

---

## 🧱 5. Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
```

---

## 🧩 6. Workflow de CI/CD (.github/workflows/ci.yml)

Este pipeline ejecuta pruebas, verifica la calidad del código y publica la imagen Docker en el GitHub Container Registry.

```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: 🧾 Checkout repository
      uses: actions/checkout@v3

    - name: 🐍 Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: 📦 Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: 🧪 Run tests
      run: pytest

    - name: 🧹 Run lint
      run: flake8 .

    - name: 🔐 Login to GitHub Container Registry
      uses: docker/login-action@v3
      with:
        registry: ghcr.io
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}

    - name: 🏗️ Build and push Docker image
      uses: docker/build-push-action@v6
      with:
        push: true
        tags: ghcr.io/${{ github.repository }}:latest
```

---

## 📝 Próximos pasos

1. Crear un repositorio en GitHub
2. Configurar los secrets necesarios
3. Hacer push del código
4. Verificar que el workflow se ejecute correctamente
5. Acceder a la imagen publicada en GHCR

