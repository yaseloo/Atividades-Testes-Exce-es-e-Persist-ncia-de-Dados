import pytest
from excecoes import converter_idade, sacar

# Testes para converter_idade
def test_converter_idade():
    assert converter_idade("20") == 20
    assert converter_idade("abc") is None

# Testes para sacar
def test_sacar():
    assert sacar(100) == 100

def test_sacar_negativo():
    with pytest.raises(ValueError, match="Valor negativo não é permitido"):
        sacar(-50)
