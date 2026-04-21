class Tabuleiro:
    def __init__(self, N):
        self.N = N
        self.size = 2 * N + 1  # tamanho real do grid interno
        self.movimentos = set()  # posições de linhas: (i, j)
        self.box = {}  # posições preenchidas: (i, j) -> jogador

    def adicionarMovimento(self, i, j):
        self.movimentos.add((i, j))

    def adicionarBox(self, i, j, jogador):
        self.box[(i, j)] = jogador

    def verificarBox(self, i, j, jogador):
        def existe(x, y):
            return (x, y) in self.movimentos

        fez = 0

        # Linhas horizontais
        if i % 2 == 0 and j % 2 != 0:
            # Box acima
            if i - 1 > 0:
                if existe(i-2, j) and existe(i-1, j-1) and existe(i-1, j+1):
                    self.box[(i-1, j)] = jogador
                    fez += 1
            # Box abaixo
            if i + 1 < self.size:
                if existe(i+2, j) and existe(i+1, j-1) and existe(i+1, j+1):
                    self.box[(i+1, j)] = jogador
                    fez += 1

        # Linhas verticais
        elif i % 2 != 0 and j % 2 == 0:
            # Box à esquerda
            if j - 1 > 0:
                if existe(i, j-2) and existe(i-1, j-1) and existe(i+1, j-1):
                    self.box[(i, j-1)] = jogador
                    fez += 1
            # Box à direita
            if j + 1 < self.size:
                if existe(i, j+2) and existe(i-1, j+1) and existe(i+1, j+1):
                    self.box[(i, j+1)] = jogador
                    fez += 1

        return fez

    def printTabuleiro(self):
        # Criar grid vazio
        grid = [[" " for _ in range(self.size)] for _ in range(self.size)]

        # Pontos
        for i in range(0, self.size, 2):
            for j in range(0, self.size, 2):
                grid[i][j] = "+"

        # Movimentos (linhas)
        for (i, j) in self.movimentos:
            if i % 2 == 0:
                grid[i][j] = "-"
            else:
                grid[i][j] = "|"

        # Boxes preenchidas
        for (i, j), jogador in self.box.items():
            grid[i][j] = jogador

        # Print cabeçalho
        print("   ", end="")
        for col in range(1, self.N + 2):
            print(f"{col}  ", end=" ")
        print()

        # Print linhas
        linha_num = 1
        for i in range(self.size):
            if i % 2 == 0:
                print(f"{linha_num:2} ", end="")
                linha_num += 1
            else:
                print("   ", end="")

            for j in range(self.size):
                print(grid[i][j], end=" ")
            print()


class DotBox:
    def __init__(self, N):
        self.tabuleiro = Tabuleiro(N)
        self.jogadas = 2 * N * (N + 1)

    def printGame(self):
        print("Tabuleiro:")
        self.tabuleiro.printTabuleiro()

    def validaPos(self, linha, coluna):
        if not (1 <= linha <= self.tabuleiro.N + 1 and 1 <= coluna <= self.tabuleiro.N + 1):
            return False
        return True

    def gravarJogada(self, i1, j1, i2, j2, jogador):
        # Converter coordenadas do usuário para grid interno
        i1_grid = (i1 - 1) * 2
        j1_grid = (j1 - 1) * 2
        i2_grid = (i2 - 1) * 2
        j2_grid = (j2 - 1) * 2

        i_mov = (i1_grid + i2_grid) // 2
        j_mov = (j1_grid + j2_grid) // 2

        if (i_mov, j_mov) in self.tabuleiro.movimentos:
            print("Já foi jogado!")
            return 0, self.jogadas

        self.tabuleiro.adicionarMovimento(i_mov, j_mov)
        fez = self.tabuleiro.verificarBox(i_mov, j_mov, jogador)
        self.jogadas -= 1

        if fez > 0:
            return 1, self.jogadas
        return 0, self.jogadas

    def jogar(self, jogador):
        while True:
            try:
                i1, j1 = map(int, input("Digite a origem (linha coluna): ").split())
                i2, j2 = map(int, input("Digite o destino (linha coluna): ").split())
            except:
                print("Entrada inválida! Use dois números separados por espaço.")
                continue

            if (self.validaPos(i1, j1) and self.validaPos(i2, j2) and
                ((i1 == i2 and abs(j1 - j2) == 1) or (j1 == j2 and abs(i1 - i2) == 1))):
                return self.gravarJogada(i1, j1, i2, j2, jogador)
            else:
                print("Jogada inválida! Tente novamente.")
