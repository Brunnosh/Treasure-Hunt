import random

def gerar_mapa(largura, altura):
    # Criar um mapa cheio de paredes
    mapa = [["#" for _ in range(largura)] for _ in range(altura)]

    # Posição inicial (canto superior esquerdo)
    inicio = (1, 1)
    mapa[inicio[0]][inicio[1]] = "S"

    # Lista de direções (cima, baixo, esquerda, direita)
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def criar_caminho(x, y):
        random.shuffle(direcoes)  # Aleatoriza a ordem de exploração
        for dx, dy in direcoes:
            nx, ny = x + dx * 2, y + dy * 2  # Pular uma célula para evitar paredes unidas
            if 1 <= nx < altura - 1 and 1 <= ny < largura - 1 and mapa[nx][ny] == "#":
                # Criar passagem
                mapa[x + dx][y + dy] = "."  # Remover a parede no meio
                mapa[nx][ny] = "."  # Criar caminho na nova posição
                criar_caminho(nx, ny)  # Continuar cavando o caminho

    # Iniciar a geração a partir do início
    criar_caminho(inicio[0], inicio[1])

    # Adicionar alguns caminhos extras aleatórios
    for _ in range((largura * altura) // 10):  # Pequena chance de remover algumas paredes
        x, y = random.randint(1, altura - 2), random.randint(1, largura - 2)
        if mapa[x][y] == "#":
            mapa[x][y] = "."

    # Encontrar um ponto acessível para o tesouro
    pontos_livres = [(x, y) for x in range(1, altura - 1) for y in range(1, largura - 1) if mapa[x][y] == "."]
    if pontos_livres:
        tesouro = random.choice(pontos_livres)
        mapa[tesouro[0]][tesouro[1]] = "T"

    return mapa

# Salvar o mapa em um arquivo
def salvar_mapa(mapa, nome_arquivo="mapa.txt"):
    with open(nome_arquivo, "w") as file:
        for linha in mapa:
            file.write("".join(linha) + "\n")

# Gerar e salvar o mapa
largura, altura = 32, 12  # Tamanho do mapa
mapa_gerado = gerar_mapa(largura, altura)
salvar_mapa(mapa_gerado)

print(f"Mapa salvo como '{'mapa.txt'}'.")
