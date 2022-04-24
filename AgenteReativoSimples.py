import matplotlib.pyplot as plt
import random


# Agente escolhe uma ação pra fazer
def acao():
    global posAPAx
    global posAPAy

    # Posição atual estiver suja ele limpa
    if (matrix[posAPAx][posAPAy] == 2):
        matrix[posAPAx][posAPAy] = 0
    # Escolhe o próximo passo.
    else:
        acaoMovimento = mapeamentoCaminho[posAPAx - 1][posAPAy - 1]
        if (acaoMovimento == 1):
            posAPAx += 1
        elif (acaoMovimento == 2):
            posAPAx -= 1
        elif acaoMovimento == 3:
            posAPAy += 1
        elif acaoMovimento == 4:
            posAPAy -= 1


# Loop onde o agente faz uma ação e exibi a ação
def loop():
    while (True):
        exibir()
        acao()


# Criar o ambiente e colocara sujeira no ambiente
def cria_ambiente_sujeira():
    global matrix
    global mapeamentoCaminho

    matrix = [[1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 1, 1, 1, 1, 1]]

    mapeamentoCaminho = [[1, 4, 4, 4],
                         [1, 3, 3, 2],
                         [1, 2, 4, 4],
                         [3, 3, 3, 2]]

    # Gera a sujeira no ambiente
    qntSujeira = random.randint(4, 12)
    for i in range(qntSujeira):
        x = random.randint(1, 4)
        y = random.randint(1, 4)
        matrix[x][y] = 2

    loop()


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
mapeamentoCaminho = []

if __name__ == '__main__':
    cria_ambiente_sujeira()
