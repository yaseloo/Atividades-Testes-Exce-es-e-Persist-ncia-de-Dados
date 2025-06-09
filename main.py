import pytest
import excecoes
import pontuacoes

def menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Testar funções matemáticas")
    print("2. Testar validação de entrada")
    print("3. Testar saque com exceção")
    print("4. Salvar pontuação")
    print("5. Ler pontuações do TXT")
    print("6. Ler pontuações do JSON")
    print("0. Sair")
    return input("Escolha uma opção: ")

def testar_funcoes():
    pytest.main(["-q", "test_funcoes.py"])

def testar_validacao():
    entrada = input("Digite uma idade: ")
    resultado = excecoes.converter_idade(entrada)
    if resultado is None:
        print("Entrada inválida! Retornou None.")
    else:
        print(f"Idade convertida: {resultado}")

def testar_saque():
    try:
        valor = float(input("Digite o valor para saque: "))
        resultado = excecoes.sacar(valor)
        print(f"Saque realizado: R$ {resultado}")
    except ValueError as e:
        print(f"Erro: {e}")

def salvar_pontuacao():
    nome = input("Digite seu nome: ")
    pontos = input("Digite a pontuação: ")
    pontuacoes.salvar_pontuacao(nome, pontos)
    pontuacoes.salvar_pontuacao_json(nome, pontos)
    print("Pontuação salva com sucesso!")

def ler_pontuacoes_txt():
    print("\nPontuações salvas (TXT):")
    for nome, pontos in pontuacoes.ler_pontuacoes():
        print(f"{nome}: {pontos}")

def ler_pontuacoes_json():
    print("\nPontuações salvas (JSON):")
    for item in pontuacoes.ler_pontuacoes_json():
        print(f"{item['nome']}: {item['pontos']}")

if __name__ == "__main__":
    while True:
        opcao = menu()
        if opcao == "1":
            testar_funcoes()
        elif opcao == "2":
            testar_validacao()
        elif opcao == "3":
            testar_saque()
        elif opcao == "4":
            salvar_pontuacao()
        elif opcao == "5":
            ler_pontuacoes_txt()
        elif opcao == "6":
            ler_pontuacoes_json()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")
