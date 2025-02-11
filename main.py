import random

PONTOS_EXPLORADOS = []

def lermapa (mapa):
    with open('mapa.txt','r') as file:
        for line in file:
            linha = line.strip()
            temp = []
            for char in linha:
                temp.append(char)                
            mapa.append(temp)

def achar_pos_inicial():
    
    numlinha =0
    numcoluna =0
    for linha in mapa:
        numcoluna = 0
        for coluna in linha:
            if coluna == 'S':
                posinicial = [numlinha,numcoluna]
                PONTOS_EXPLORADOS.append(posinicial)
                return posinicial
            numcoluna = numcoluna +1
        numlinha = numlinha + 1
    


def ler_pos_proximas(posinicial,mapa):
    #   #
    #  #S#
    #   #
    proxpos = []
    
    cima = [posinicial[0]-1,posinicial[1]]
    baixo = [posinicial[0]+1,posinicial[1]]
    esq = [posinicial[0],posinicial[1]-1]
    dir = [posinicial[0],posinicial[1]+1]

    if mapa[cima[0]][cima[1]] == '.': proxpos.append(cima)
    if mapa[baixo[0]][baixo[1]] == '.': proxpos.append(baixo)
    if mapa[esq[0]][esq[1]] == '.': proxpos.append(esq)
    if mapa[dir[0]][dir[1]] == '.': proxpos.append(dir)

    #Remover do vetor movimentos possiveis pontos onde ja foi explorado

    for movimento in proxpos:
        if movimento in PONTOS_EXPLORADOS:
            proxpos.remove(movimento)


    return proxpos

#def mover(mapa):

if __name__ == "__main__":
    mapa = []
    lermapa(mapa)
    posinicial = achar_pos_inicial() # Posição inicial do aventureiro
    posatual = posinicial # Posição atual do aventureiro (inicia na inicial e muda conforme o programa)
    pontos_incertos = [] # Pontos com mais de um caminho possivel

    #while True:
    prox = ler_pos_proximas(posinicial,mapa)
    print(prox)

    
    

#Lógica

