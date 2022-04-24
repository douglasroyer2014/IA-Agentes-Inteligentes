import matplotlib.pyplot as plt
import random


# Escolhe proxima ação de movimento do agente
def escolhe_proximo_passo():
    global matrix
    global posAPAx
    global posAPAy
    global acoesDisponiveis
    global ponto

    # Variaveis temporaria da posição atual
    posXTemp = posAPAx
    posYTemp = posAPAy
    while True:
        acaoMovimento = random.randint(1, 4)
        if (acaoMovimento == 1):
            posAPAx += 1
        elif (acaoMovimento == 2):
            posAPAx -= 1
        elif acaoMovimento == 3:
            posAPAy += 1
        elif acaoMovimento == 4:
            posAPAy -= 1

        # Valida se a proxima ação é valida
        if matrix[posAPAx][posAPAy] == 1:
            posAPAx = posXTemp
            posAPAy = posYTemp
        else:
            print("Estado da percepção: 0 Ação escolhida:", acoesDisponiveis[acaoMovimento - 1])
            ponto += 1
            break


# Verifica se na posição atual o agente precisa limpar
def verifica_precisa_Limpar():
    global matrix
    global posAPAx
    global posAPAy
    global sujeiraTotal
    global ponto
    global acoesDisponiveis

    matrix[posAPAx][posAPAy] = 0
    sujeiraTotal -= 1
    ponto += 1
    print("Estado da percepção: 1 Ação escolhida:", acoesDisponiveis[4])


# Agente escolhe uma ação pra fazer
def acao():
    global posAPAx
    global posAPAy
    global ponto
    global acoesDisponiveis

    # Posição atual estiver suja ele limpa
    if (matrix[posAPAx][posAPAy] == 2):
        verifica_precisa_Limpar()

    # Escolhe o próximo passo.
    else:
        escolhe_proximo_passo()


# Loop onde o agente faz uma ação e exibi a ação
def loop():
    global sujeiraTotal

    while (sujeiraTotal != 0):
        exibir()
        acao()


# Conta as sujeiras pro agente saber quantas vezes ele vai precisar aspirar antes de finalizar
def contar_sujeira():
    global matrix
    global sujeiraTotal
    global ponto

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 2:
                sujeiraTotal += 1

    loop()

    # Mostra a quantidade de ações que o agente vez
    print("Ponto: ->", ponto)

    # Deixa o programa em loop pra mostra o ambiente limpo
    while True:
        exibir()


# Criar o ambiente e colocara sujeira no ambiente
def cria_ambiente_sujeira():
    global matrix

    matrix = [[1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 1, 1, 1, 1, 1]]

    # Gera a sujeira no ambiente
    qntSujeira = random.randint(4, 12)
    for i in range(qntSujeira):
        x = random.randint(1, 4)
        y = random.randint(1, 4)
        matrix[x][y] = 2

    contar_sujeira()


# Função que exibe o ambiente na tela
def exibir():
    global posAPAx
    global posAPAy

    # Altera o esquema de cores do ambiente
    plt.imshow(matrix, 'gray')
    plt.nipy_spectral()

    # Coloca o agente no ambiente
    plt.plot([posAPAy], [posAPAx], marker='o', color='r', ls='')
    plt.show(block=False)

    # Pausa a execução do código por 0.5 segundos para facilitar a visualização
    plt.pause(1)
    plt.clf()


# Parâmetros de inicialização
posAPAx = 1
posAPAy = 1
matrix = []
sujeiraTotal = 0
ponto = 0
acoesDisponiveis = ["abaixo", "acima", "direita", "esquerda", "aspirar"]

if __name__ == '__main__':
    cria_ambiente_sujeira()
