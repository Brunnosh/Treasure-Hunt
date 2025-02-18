import random
from matplotlib import pyplot as plt

MAPA = [] # MAPA do tesouro
PONTOS_EXPLORADOS = [] # Pontos já visitados
PONTOS_INCERTOS = []  # Pontos com mais de um caminho possivel
CAMINHO_CORRETO = [] # A cada vez que o codigo volta num ponto incerto, remove todos os pontos após aquele ponto no array


def lerMAPA ():
    with open('MAPA.txt','r') as file:
        for line in file:
            linha = line.strip()
            temp = []
            for char in linha:
                temp.append(char)                
            MAPA.append(temp)

def achar_pos_inicial():
    
    numlinha =0
    numcoluna =0
    for linha in MAPA:
        numcoluna = 0
        for coluna in linha:
            if coluna == 'S':
                posinicial = [numlinha,numcoluna]
                PONTOS_EXPLORADOS.append(posinicial)
                CAMINHO_CORRETO.append(posinicial)
                return posinicial
            numcoluna = numcoluna +1
        numlinha = numlinha + 1
    


def ler_pos_proximas(posatual):
    #   #
    #  #S#
    #   #
    proxpos = []
    
    cima = [posatual[0]-1,posatual[1]]
    baixo = [posatual[0]+1,posatual[1]]
    esq = [posatual[0],posatual[1]-1]
    dir = [posatual[0],posatual[1]+1]

    if MAPA[cima[0]][cima[1]] == 'T': return ('TESOURO',cima)
    if MAPA[baixo[0]][baixo[1]] == 'T': return ('TESOURO',baixo)
    if MAPA[esq[0]][esq[1]] == 'T': return ('TESOURO',esq)
    if MAPA[dir[0]][dir[1]] == 'T': return ('TESOURO',dir)

    if MAPA[cima[0]][cima[1]] == '.': proxpos.append(cima)
    if MAPA[baixo[0]][baixo[1]] == '.': proxpos.append(baixo)
    if MAPA[esq[0]][esq[1]] == '.': proxpos.append(esq)
    if MAPA[dir[0]][dir[1]] == '.': proxpos.append(dir)

    #Remover do vetor movimentos possiveis pontos onde ja foi explorado

    movRepetidos = []

    proxpos = [mov for mov in proxpos if mov not in PONTOS_EXPLORADOS]
        
    

    if len(proxpos) > 1: # Adiciona a lista de pontos com mais de uma possibilidade de movimento
        PONTOS_INCERTOS.append(posatual)

    if len(proxpos) == 0: # Chegou num ponto onde não tem o que fazer a nao ser retornar
        return (["SEM SAIDA"])


    return proxpos

def mover(prox):
    escolha = random.randrange(len(prox))
    PONTOS_EXPLORADOS.append(prox[escolha])
    CAMINHO_CORRETO.append(prox[escolha])

    return prox[escolha]

def voltarUltimoAmbiguo():
    global CAMINHO_CORRETO

    tam = len(PONTOS_INCERTOS)
    ultimoValor = PONTOS_INCERTOS[tam-1]
    PONTOS_INCERTOS.remove(ultimoValor)

    if ultimoValor in CAMINHO_CORRETO:
        indice = CAMINHO_CORRETO.index(ultimoValor)
        CAMINHO_CORRETO = CAMINHO_CORRETO[:indice+1]

    return ultimoValor

def plotar_mapa():
    fig, ax = plt.subplots(figsize=(10, 6))



    # Plotando o mapa
    for i in range(len(MAPA)):
        for j in range(len(MAPA[i])):
            if MAPA[i][j] == '#':
                ax.plot(j, i, marker='s', color='black', markersize=10)  # Parede
            elif MAPA[i][j] == '.':
                ax.plot(j, i, marker='s', color='white', markersize=10)  # Caminho livre
            elif MAPA[i][j] == 'S':
                ax.plot(j, i, marker='o', color='blue', markersize=12)  # Início
            elif MAPA[i][j] == 'T':
                ax.plot(j, i, marker='o', color='yellow', markersize=12)  # Tesouro

    # Plotando o caminho explorado (linha vermelha)
    for ponto in PONTOS_EXPLORADOS:
        ax.plot(ponto[1], ponto[0], marker='o', color='red', markersize=6)

    # Plotando o caminho correto (linha verde)
    for ponto in CAMINHO_CORRETO:
        ax.plot(ponto[1], ponto[0], marker='o', color='green', markersize=6)

    # Ajustar o gráfico
    ax.set_aspect('equal')
    plt.gca().invert_yaxis()  # Para o gráfico ficar mais como um mapa tradicional

    ax.text(1, -len(MAPA) - 1.5, f"Passos Totais: {len(PONTOS_EXPLORADOS)}", fontsize=12, color="red")
    ax.text(1, -len(MAPA) - 3, f"Menor Caminho: {len(CAMINHO_CORRETO)}", fontsize=12, color="green")

    plt.show()


if __name__ == "__main__":
    lerMAPA()
    posinicial = achar_pos_inicial() # Posição inicial do aventureiro
    posatual = posinicial # Posição atual do aventureiro (inicia na inicial e muda conforme o programa)
    

    while True:
        print("PONTOS EXPLORADOS", PONTOS_EXPLORADOS)
        prox = []
        prox = ler_pos_proximas(posatual)
        print(prox)
        if prox[0] == 'TESOURO':
            print("CAMINHO FINAL: ", CAMINHO_CORRETO)
            print("PASSOS NO TOTAL: ", len(PONTOS_EXPLORADOS))
            print("TAMANHO DO MENOR CAMINHO: ", len(CAMINHO_CORRETO))
            print("TESOURO ENCONTRADO EM: ", prox[1])
            plotar_mapa()
            exit()
        if prox[0] == 'SEM SAIDA':
            posatual = voltarUltimoAmbiguo()

        else:
            posatual = mover(prox)
        

    


