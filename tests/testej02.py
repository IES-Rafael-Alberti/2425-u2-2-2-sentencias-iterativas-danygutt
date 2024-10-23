import pytest
from src.ej02 import edadDeUnoAEdad  # Ajusta la ruta según tu estructura

def test_edadDeUnoAEdad():
    # Test con una edad positiva
    resultado = edadDeUnoAEdad(5)
    assert resultado == [1, 2, 3, 4, 5]

    # Test con la edad 1
    resultado = edadDeUnoAEdad(1)
    assert resultado == [1]