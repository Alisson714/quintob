# Comandos para Verificar el Proyecto

## 🚀 Verificación Rápida (Recomendado)

```powershell
# Ejecutar el script de verificación completo
python verificar.py
```

Este script verifica automáticamente:
- Archivos principales
- Sintaxis de Python
- Workflows YAML (requiere `pip install pyyaml`)
- Dockerfile
- requirements.txt

## 1. Verificar estructura del proyecto

```powershell
# Verificar que existan los archivos principales
dir app.py, requirements.txt, Dockerfile, test_app.py

# Verificar workflows
dir .github\workflows\
```

## 2. Verificar sintaxis de Python

```powershell
# Verificar app.py
python -m py_compile app.py

# Verificar test_app.py
python -m py_compile test_app.py

# Verificar ambos a la vez
python -m py_compile app.py test_app.py
```

## 3. Verificar dependencias

```powershell
# Ver contenido de requirements.txt
type requirements.txt

# Instalar dependencias (opcional, para probar)
pip install -r requirements.txt
```

## 4. Verificar que la aplicación funciona

```powershell
# Ejecutar la aplicación Flask localmente
python app.py
```

Luego en otra terminal o navegador, verificar:
- Abrir: http://localhost:5000
- Debería mostrar: "¡Hola Mundo desde Flask con Traefik! 🚀"

## 5. Ejecutar tests

```powershell
# Instalar dependencias primero
pip install -r requirements.txt

# Ejecutar tests
pytest test_app.py -v

# O con más detalles
pytest test_app.py -v -s
```

## 6. Verificar Dockerfile

```powershell
# Verificar que el Dockerfile existe
type Dockerfile

# Construir la imagen Docker (opcional, requiere Docker Desktop)
docker build -t mi-app-flask:test .

# Verificar que la imagen se creó
docker images mi-app-flask:test

# Ejecutar el contenedor (opcional)
docker run -p 5000:5000 mi-app-flask:test
```

## 7. Verificar workflows de GitHub Actions

```powershell
# Verificar que los archivos YAML existen
type .github\workflows\crear_imagen.yml
type .github\workflows\ci.yml

# Instalar PyYAML para verificar sintaxis YAML
pip install pyyaml

# Verificar sintaxis YAML
python -c "import yaml; yaml.safe_load(open('.github/workflows/crear_imagen.yml')); print('OK')"
python -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml')); print('OK')"
```

## 8. Verificar linting (opcional)

```powershell
# Instalar flake8 si no está instalado
pip install flake8

# Ejecutar flake8
flake8 app.py test_app.py
```

## 9. Verificación completa (comandos manuales)

```powershell
# Verificar sintaxis de todos los archivos Python
python -m py_compile app.py test_app.py

# Verificar estructura
dir app.py, requirements.txt, Dockerfile, test_app.py
dir .github\workflows\

# Mostrar contenido de archivos clave
type Dockerfile
type requirements.txt
```

## 10. Probar el Dockerfile localmente (si tienes Docker)

```powershell
# Construir imagen
docker build -t test-flask-app .

# Ejecutar contenedor
docker run -d -p 5000:5000 --name test-container test-flask-app

# Verificar que funciona (en otra terminal)
curl http://localhost:5000
# O abrir en navegador: http://localhost:5000

# Detener y eliminar contenedor
docker stop test-container
docker rm test-container
```

## Resultado esperado

Si todo está bien, deberías ver:
- [OK] Todos los archivos existen
- [OK] Python compila sin errores
- [OK] Los tests pasan
- [OK] Flask se ejecuta correctamente
- [OK] El Dockerfile se construye sin errores
- [OK] Los workflows YAML tienen sintaxis válida

## Comando más rápido

```powershell
# Todo en uno: verificar todo el proyecto
python verificar.py
```

