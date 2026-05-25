
class Tabuleiro:
    """Classe principal, faz o gestionamento do jogo"""
    def __init__(self, N):
        self.N = N
        self.size = 2 * N + 1  # tamanho real do grid interno
        self.movimentos = set()  # posições de linhas: (i, j)
        self.box = {}  # posições preenchidas: (i, j) -> jogador
        self.jogadas = 2 * N * (N + 1) #quantas jogadas possíveis há no jogo
        

    def adicionarMovimento(self, i, j):
        self.movimentos.add((i, j))

    def adicionarBox(self, i, j, jogador):
        self.box[(i, j)] = jogador

    def verificarBox(self, i, j, jogador):
        def existe(x, y):
            return (x, y) in self.movimentos

        fez = 0

        simbolo = jogador 
        
        # Linhas horizontais
        if i % 2 == 0 and j % 2 != 0:
            # Box acima
            if i - 1 > 0:
                if existe(i-2, j) and existe(i-1, j-1) and existe(i-1, j+1):
                    self.box[(i-1, j)] = simbolo
                    fez += 1

            # Box abaixo
            if i + 1 < self.size:
                if existe(i+2, j) and existe(i+1, j-1) and existe(i+1, j+1):
                    self.box[(i+1, j)] = simbolo
                    fez += 1

        # Linhas verticais
        elif i % 2 != 0 and j % 2 == 0:
            # Box à esquerda
            if j - 1 > 0:
                if existe(i, j-2) and existe(i-1, j-1) and existe(i+1, j-1):
                    self.box[(i, j-1)] = simbolo
                    fez += 1

            # Box à direita
            if j + 1 < self.size:
                if existe(i, j+2) and existe(i-1, j+1) and existe(i+1, j+1):
                    self.box[(i, j+1)] = simbolo
                    fez += 1

        return fez
    
    def validaPos(self, linha, coluna):
        if not (1 <= linha <= self.N + 1 and 1 <= coluna <= self.N + 1):
            return False
        return True

    def gravarJogada(self, i1, j1, i2, j2, jogador):

        i1_grid = (i1 - 1) * 2
        j1_grid = (j1 - 1) * 2

        i2_grid = (i2 - 1) * 2
        j2_grid = (j2 - 1) * 2

        i_mov = (i1_grid + i2_grid) // 2
        j_mov = (j1_grid + j2_grid) // 2

        if (i_mov, j_mov) in self.movimentos:

            print("Já foi jogado!")

            return False

        self.adicionarMovimento(i_mov, j_mov)

        self.verificarBox(
            i_mov,
            j_mov,
            jogador
        )

        self.jogadas -= 1

        return True