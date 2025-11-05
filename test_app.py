"""
Tests para la aplicación de ejemplo.
"""

import pytest
from app import app


def test_hello_route():
    """Test para la ruta principal."""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert "¡Hola Mundo desde Flask con Traefik! 🚀" in response.data.decode('utf-8')


def test_hello_content():
    """Test para verificar el contenido de la respuesta."""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert isinstance(response.data, bytes)

