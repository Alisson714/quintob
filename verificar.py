#!/usr/bin/env python3
"""
Script para verificar que todo el proyecto esté correcto.
"""

import os
import sys

def verificar_archivos():
    """Verifica que existan los archivos principales."""
    print("=== Verificando archivos principales ===")
    archivos = ['app.py', 'requirements.txt', 'Dockerfile', 'test_app.py']
    todos_ok = True
    
    for archivo in archivos:
        if os.path.exists(archivo):
            print(f"[OK] {archivo} existe")
        else:
            print(f"[ERROR] {archivo} NO existe")
            todos_ok = False
    
    return todos_ok

def verificar_sintaxis_python():
    """Verifica la sintaxis de los archivos Python."""
    print("\n=== Verificando sintaxis Python ===")
    archivos = ['app.py', 'test_app.py']
    todos_ok = True
    
    for archivo in archivos:
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                compile(f.read(), archivo, 'exec')
            print(f"[OK] {archivo} - Sintaxis correcta")
        except SyntaxError as e:
            print(f"[ERROR] {archivo} - Error de sintaxis: {e}")
            todos_ok = False
        except Exception as e:
            print(f"[ERROR] {archivo} - Error: {e}")
            todos_ok = False
    
    return todos_ok

def verificar_workflows():
    """Verifica la sintaxis YAML de los workflows."""
    print("\n=== Verificando workflows ===")
    workflows = ['.github/workflows/crear_imagen.yml', '.github/workflows/ci.yml']
    todos_ok = True
    
    try:
        import yaml
    except ImportError:
        print("[WARN] PyYAML no esta instalado. Instala con: pip install pyyaml")
        return False
    
    for workflow in workflows:
        if not os.path.exists(workflow):
            print(f"[ERROR] {workflow} NO existe")
            todos_ok = False
            continue
            
        try:
            with open(workflow, 'r', encoding='utf-8') as f:
                yaml.safe_load(f)
            print(f"[OK] {workflow} - Sintaxis YAML correcta")
        except yaml.YAMLError as e:
            print(f"[ERROR] {workflow} - Error YAML: {e}")
            todos_ok = False
        except Exception as e:
            print(f"[ERROR] {workflow} - Error: {e}")
            todos_ok = False
    
    return todos_ok

def verificar_dockerfile():
    """Verifica que el Dockerfile exista y tenga contenido."""
    print("\n=== Verificando Dockerfile ===")
    if not os.path.exists('Dockerfile'):
        print("[ERROR] Dockerfile NO existe")
        return False
    
    with open('Dockerfile', 'r', encoding='utf-8') as f:
        contenido = f.read()
        if len(contenido.strip()) == 0:
            print("[ERROR] Dockerfile esta vacio")
            return False
        if 'FROM' in contenido and 'CMD' in contenido:
            print("[OK] Dockerfile parece correcto")
            return True
        else:
            print("[WARN] Dockerfile existe pero podria estar incompleto")
            return True

def verificar_requirements():
    """Verifica que requirements.txt tenga contenido."""
    print("\n=== Verificando requirements.txt ===")
    if not os.path.exists('requirements.txt'):
        print("[ERROR] requirements.txt NO existe")
        return False
    
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        contenido = f.read().strip()
        if len(contenido) == 0:
            print("[ERROR] requirements.txt esta vacio")
            return False
        print(f"[OK] requirements.txt contiene:\n{contenido}")
        return True

def main():
    """Ejecuta todas las verificaciones."""
    print("Verificacion del Proyecto CI/CD\n")
    
    resultados = {
        'Archivos': verificar_archivos(),
        'Sintaxis Python': verificar_sintaxis_python(),
        'Workflows': verificar_workflows(),
        'Dockerfile': verificar_dockerfile(),
        'Requirements': verificar_requirements(),
    }
    
    print("\n" + "="*50)
    print("=== RESUMEN ===")
    print("="*50)
    
    todos_ok = True
    for nombre, resultado in resultados.items():
        estado = "[OK]" if resultado else "[ERROR]"
        print(f"{nombre}: {estado}")
        if not resultado:
            todos_ok = False
    
    print("="*50)
    if todos_ok:
        print("[OK] Todo esta correcto!")
        return 0
    else:
        print("[ERROR] Hay errores que corregir")
        return 1

if __name__ == '__main__':
    sys.exit(main())

