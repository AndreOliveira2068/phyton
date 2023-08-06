# jogo de tabuleiro #

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(posicao == jogador for posicao in linha):
            return True

    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True

    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ["X", "O"]
    jogador_atual = 0
    rodada = 1

    while rodada <= 9:
        exibir_tabuleiro(tabuleiro)

        jogador = jogadores[jogador_atual]
        print(f"Rodada {rodada}: Vez do jogador {jogador}")

        linha = int(input("Digite o número da linha (0, 1 ou 2): "))
        coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador
            if verificar_vitoria(tabuleiro, jogador):
                exibir_tabuleiro(tabuleiro)
                print(f"O jogador {jogador} venceu!")
                return
            jogador_atual = 1 - jogador_atual
            rodada += 1
        else:
            print("Posição já ocupada. Tente novamente.")

    exibir_tabuleiro(tabuleiro)
    print("O jogo terminou em empate!")

if __name__ == "__main__":
    jogar()