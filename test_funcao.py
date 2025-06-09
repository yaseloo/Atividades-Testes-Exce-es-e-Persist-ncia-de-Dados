import pytest

# Função soma
def soma(a, b):
    return a + b

# Testes para soma
def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0

# Função dividir
def dividir(a, b):
    return a / b

# Testes para dividir
def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_zero():
    with pytest.raises(ZeroDivisionError):
        dividir(5, 0)
