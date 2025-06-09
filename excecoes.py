# Validação de entrada
def converter_idade(texto):
    try:
        return int(texto)
    except ValueError:
        return None

# Exceção personalizada
def sacar(valor):
    if valor < 0:
        raise ValueError("Valor negativo não é permitido")
    return valor
