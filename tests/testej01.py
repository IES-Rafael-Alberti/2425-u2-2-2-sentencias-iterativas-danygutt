import pytest
from src.ej01 import recibePalabraMultiplicaPorDiez


def test_recibePalabraMultiplicaPorDiez():
    # Test con una palabra normal
    resultado = recibePalabraMultiplicaPorDiez("hola")
    assert resultado == ["hola"] * 10
    # Test con un número como palabra
    resultado = recibePalabraMultiplicaPorDiez("123")
    assert resultado == ["123"] * 10
    # Test con una palabra con espacios
    resultado = recibePalabraMultiplicaPorDiez("Profe apruebame")
    assert resultado == ["Profe apruebame"] * 10