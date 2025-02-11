
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
                return [numlinha,numcoluna]
            numcoluna = numcoluna +1
        numlinha = numlinha + 1
    
    


if __name__ == "__main__":
    mapa = []
    lermapa(mapa)
    posinicial = achar_pos_inicial()
    print (posinicial)

    #Lógica

