import json

# Gravação e leitura de pontuação em TXT
def salvar_pontuacao(nome, pontos):
    with open("pontuacoes.txt", "a") as file:
        file.write(f"{nome},{pontos}\n")

def ler_pontuacoes():
    try:
        with open("pontuacoes.txt", "r") as file:
            return [tuple(line.strip().split(",")) for line in file]
    except FileNotFoundError:
        return []

# Gravação e leitura de pontuação em JSON
def salvar_pontuacao_json(nome, pontos):
    try:
        with open("pontuacoes.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append({"nome": nome, "pontos": pontos})

    with open("pontuacoes.json", "w") as file:
        json.dump(data, file, indent=4)

def ler_pontuacoes_json():
    try:
        with open("pontuacoes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
