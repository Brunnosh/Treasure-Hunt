import random

MAPA = [] # MAPA do tesouro
PONTOS_EXPLORADOS = [] # Pontos já visitados
PONTOS_INCERTOS = []  # Pontos com mais de um caminho possivel

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

    print("PONTOS EXPLORADOS: ", PONTOS_EXPLORADOS)
    for movimento in proxpos:
        print("MOVIMENTO NO PROXPOS: ", movimento)
        if movimento in PONTOS_EXPLORADOS:
            proxpos.remove(movimento)

    if len(proxpos) > 1: # Adiciona a lista de pontos com mais de uma possibilidade de movimento
        PONTOS_INCERTOS.append(posatual)

    if len(proxpos) == 0: # Chegou num ponto onde não tem o que fazer a nao ser retornar
        return (["SEM SAIDA"])


    return proxpos

def mover(prox):
    escolha = random.randrange(len(prox))
    PONTOS_EXPLORADOS.append(prox[escolha])

    return prox[escolha]

def voltarUltimoAmbiguo():
    tam = len(PONTOS_INCERTOS)
    ultimoValor = PONTOS_INCERTOS[tam-1]
    PONTOS_INCERTOS.remove(ultimoValor)

    return ultimoValor


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
            print("TESOURO ENCONTRADO EM: ", prox[1])
            exit()
        if prox[0] == 'SEM SAIDA':
            posatual = voltarUltimoAmbiguo()
        else:
            posatual = mover(prox)
        

    
    

#Lógica

