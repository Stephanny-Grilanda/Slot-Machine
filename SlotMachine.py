import random

MAX_LINHAS = 3
MAX_APOSTA = 100
MIN_APOSTA = 1
LINHAS = 3
COLUNAS = 3

qtde_simbolos = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

simbolo_valores = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def checar_vitoria(colunas, linhas, aposta, valores):
    vitorias = 0
    linhas_vitoria = []
    for linha in range(linhas):
        simbolo = colunas[0][linha]
        ganhou = True
        for coluna in colunas:
            if coluna[linha] != simbolo:
                ganhou = False
                break
        if ganhou:
            vitorias += valores[simbolo] * aposta
            linhas_vitoria.append(linha + 1)
    return vitorias, linhas_vitoria


def girar_roleta(linhas, colunas, simbolos):
    todos_simbolos = []
    for simbolo, qtde_simbolos in simbolos.items():
        for _ in range(qtde_simbolos):
            todos_simbolos.append(simbolo)

    cols = []
    for _ in range(colunas):
        col = []
        simbolos_atuais = todos_simbolos[:]
        for _ in range(linhas):
            valor = random.choice(simbolos_atuais)
            simbolos_atuais.remove(valor)
            col.append(valor)

        cols.append(col)

    return cols


def imprimir_roleta(colunas):
    for linha in range(len(colunas[0])):
        for i, coluna in enumerate(colunas):
            if i != len(colunas) - 1:
                print(coluna[linha], end=" | ")
            else:
                print(coluna[linha], end="")

        print()


def depositar():
    while True:
        valor = input("Quanto voce deseja depositar? R$ ")
        if valor.isdigit():  # verifica se o valor solicitado é um número
            valor = int(valor)
            if valor > 0:
                break
            else:
                print("Valor invalido, digite um valor acima de zero!")
        else:
            print("Por favor, digite um valor numerico!")

    return valor


def numero_linhas():
    while True:
        linhas = input("Quantas linhas deseja apostar? (1 - " + str(MAX_LINHAS) + ")  ")
        if linhas.isdigit():  # verifica se o valor solicitado é um número
            linhas = int(linhas)
            if 1 <= linhas <= MAX_LINHAS:
                break
            else:
                print("Insira um numero valido de linhas!")
        else:
            print("Por favor, digite um valor numerico!")
    return linhas


def definir_aposta():
    while True:
        valor = input("Quanto você deseja apostar em cada linha? R$ ")
        if valor.isdigit():  # verifica se o valor solicitado é um número
            valor = int(valor)
            if MIN_APOSTA <= valor <= MAX_APOSTA:
                break
            else:
                print(f"A aposta deve estar entre R${MIN_APOSTA} e R${MAX_APOSTA}")
        else:
            print("Por favor, digite um valor numerico!")

    return valor


def jogar(saldo):
    linhas = numero_linhas()
    while True:
        aposta = definir_aposta()
        total_aposta = aposta * linhas

        if total_aposta > saldo:
            print(f"Voce nao tem saldo suficiente para essa aposta! Saldo atual{saldo}")
        else:
            break
    print(f"Voce apostou R${aposta} em {linhas} linhas. O total da sua aposta foi {total_aposta}")

    campos = girar_roleta(LINHAS, COLUNAS, qtde_simbolos)
    imprimir_roleta(campos)
    vitorias, linhas_vitoria = checar_vitoria(campos, linhas, aposta, simbolo_valores)
    print(f"Voce ganhou R${vitorias}")
    print(f"Voce ganhou nas linhas: {linhas_vitoria}")
    return vitorias - total_aposta


def main():
    saldo = depositar()
    while True:
        print(f"Seu saldo atual é de R${saldo}")
        jogo = input("Aperte enter para jogar (s para sair) ")
        if jogo == "s":
            break
        saldo += jogar(saldo)

    print(f"Voce saiu com R${saldo}")


main()