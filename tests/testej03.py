import pytest
from src.ej03 import generarNumerosImpares

def test_generarNumerosImpares():
    # Test con un número positivo
    resultado = generarNumerosImpares(10)
    assert resultado == "1, 3, 5, 7, 9"

    # Test con el número 1
    resultado = generarNumerosImpares(1)
    assert resultado == "1"