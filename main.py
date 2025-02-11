import random

MAPA = [] # Mapa do tesouro
PONTOS_EXPLORADOS = [] # Pontos já visitados
PONTOS_INCERTOS = []  # Pontos com mais de um caminho possivel

def lermapa ():
    with open('mapa.txt','r') as file:
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
    


def ler_pos_proximas(posatual,mapa):
    #   #
    #  #S#
    #   #
    proxpos = []
    
    cima = [posatual[0]-1,posatual[1]]
    baixo = [posatual[0]+1,posatual[1]]
    esq = [posatual[0],posatual[1]-1]
    dir = [posatual[0],posatual[1]+1]

    if mapa[cima[0]][cima[1]] == 'T': return (["TESOURO"],cima)
    if mapa[baixo[0]][baixo[1]] == 'T': return (["TESOURO"],baixo)
    if mapa[esq[0]][esq[1]] == 'T': return (["TESOURO"],esq)
    if mapa[dir[0]][dir[1]] == 'T': return (["TESOURO"],dir)

    if mapa[cima[0]][cima[1]] == '.': proxpos.append(cima)
    if mapa[baixo[0]][baixo[1]] == '.': proxpos.append(baixo)
    if mapa[esq[0]][esq[1]] == '.': proxpos.append(esq)
    if mapa[dir[0]][dir[1]] == '.': proxpos.append(dir)

    #Remover do vetor movimentos possiveis pontos onde ja foi explorado

    for movimento in proxpos:
        if movimento in PONTOS_EXPLORADOS:
            proxpos.remove(movimento)

    if len(proxpos) > 1:
        PONTOS_INCERTOS.append(posatual)


    return proxpos

def mover(mapa,prox):
    escolha = random.randrange(len(prox))
    PONTOS_EXPLORADOS.append(prox[escolha])

    return prox[escolha]


if __name__ == "__main__":
    lermapa()
    posinicial = achar_pos_inicial() # Posição inicial do aventureiro
    posatual = posinicial # Posição atual do aventureiro (inicia na inicial e muda conforme o programa)
    

    while True:
        prox = []
        prox = ler_pos_proximas(posatual,MAPA)
        if prox[0] == "TESOURO":
            print("TESOURO ENCONTRADO EM: ", prox[1])
            exit()
        posatual = mover(MAPA,prox)
        print("POSICAO ATUAL",  posatual)
        print("PONTOS EXPLORADOS:",  PONTOS_EXPLORADOS)
        print("PONTOS INCERTOS" , PONTOS_INCERTOS)

    
    

#Lógica

