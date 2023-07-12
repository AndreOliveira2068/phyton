

# Cria um tabuleiro  Damas 8x8 com espaços vazios

tabuleiro = [[' ' for _ in range(8)] for _ in range(8)]

# Adiciona as peças de damas
for i in range(8):
    for j in range(8):
        # Peças pretas no topo
        if i < 3 and (i+j)%2 == 0:
            tabuleiro[i][j] = '\033[30mP\033[m' # P para peças pretas
        # Peças brancas na parte inferior
        if i > 4 and (i+j)%2 == 0:
            tabuleiro[i][j] = '\033[37mB\033[m' # B para peças brancas

# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    print("  a b c d e f g h")
    for i in range(8):
        print(i+1, end=' ')
        for j in range(8):
            print(tabuleiro[i][j], end=' ')
        print()

# Imprime o tabuleiro inicial
imprimir_tabuleiro(tabuleiro)