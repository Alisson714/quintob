#!/bin/bash

echo "=== Verificando estructura del proyecto ==="
echo ""
echo "1. Verificando archivos principales..."
ls -la app.py requirements.txt Dockerfile

echo ""
echo "2. Verificando workflows..."
ls -la .github/workflows/

echo ""
echo "=== Verificando sintaxis de Python ==="
echo ""
echo "3. Verificando sintaxis de app.py..."
python -m py_compile app.py && echo "✓ app.py OK" || echo "✗ Error en app.py"

echo ""
echo "4. Verificando sintaxis de test_app.py..."
python -m py_compile test_app.py && echo "✓ test_app.py OK" || echo "✗ Error en test_app.py"

echo ""
echo "=== Verificando dependencias ==="
echo ""
echo "5. Verificando que requirements.txt existe y tiene contenido..."
if [ -f requirements.txt ] && [ -s requirements.txt ]; then
    echo "✓ requirements.txt OK"
    cat requirements.txt
else
    echo "✗ requirements.txt no existe o está vacío"
fi

echo ""
echo "=== Verificando Dockerfile ==="
echo ""
echo "6. Verificando sintaxis del Dockerfile..."
if docker build --dry-run -f Dockerfile . 2>&1 | grep -q "error"; then
    echo "✗ Error en Dockerfile"
else
    echo "✓ Dockerfile parece correcto"
fi

echo ""
echo "=== Verificando workflows de GitHub Actions ==="
echo ""
echo "7. Verificando sintaxis de crear_imagen.yml..."
python -c "import yaml; yaml.safe_load(open('.github/workflows/crear_imagen.yml'))" && echo "✓ crear_imagen.yml OK" || echo "✗ Error en crear_imagen.yml"

echo ""
echo "8. Verificando sintaxis de ci.yml..."
python -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml'))" && echo "✓ ci.yml OK" || echo "✗ Error en ci.yml"

echo ""
echo "=== Verificación completa ==="

