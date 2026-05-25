import json
from ClientNet import ComunicadorCliente

class Tabuleiro:
    """Classe principal, faz o gestionamento do jogo"""
    def __init__(self, N):
        self.N = N
        self.size = 2 * N + 1  # tamanho real do grid interno
        self.movimentos = set()  # posições de linhas: (i, j)
        self.box = {}  # posições preenchidas: (i, j) -> jogador
        self.jogadas = 2 * N * (N + 1) #quantas jogadas possíveis há no jogo
    
    def printTabuleiro(self):
        print("Tabuleiro:")

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

class gamer:

    def __init__(self ):


        self.com = ComunicadorCliente()
        self.tabuleiro = None
        
        self.nome = input("Nome do jogador: ")

    def aplicarEstado(self, mensagem):

        dados = json.loads(mensagem)

        self.tabuleiro.movimentos = set(
            tuple(x)
            for x in dados["movimentos"]
        )

        

    def jogar(self):

        while True:

            mensagem = self.com.receber()

            if mensagem is None:

                print("Servidor desconectado")

                break

            if mensagem == "":

                continue

            # print("Recebido:", mensagem)

            dados = json.loads(mensagem)

            # ---------------- CONFIG ----------------

            if dados["tipo"] == "config":

                N = dados["N"]

                self.tabuleiro = Tabuleiro(N)

                print(f"\nTabuleiro {N}x{N} criado!\n")

            # ---------------- ESTADO ----------------

            elif dados["tipo"] == "estado":

                self.aplicarEstado(mensagem)



            elif dados["tipo"] == "sua_vez" or "erro":
                if (dados["tipo"] == "erro"):
                    print("jogada invalida")

                self.tabuleiro.printTabuleiro()

                print("\nSua vez!\n")

                i1, j1 = map(
                    int,
                    input("Origem (i j): ").split()
                )

                i2, j2 = map(
                    int,
                    input("Destino (i j): ").split()
                )
              
                msg = {

                    "tipo": "movimento",
                    "name": self.nome[0],
                    
                    "i1": i1,
                    "j1": j1,

                    "i2": i2,
                    "j2": j2
                }

                self.com.enviar(
                    json.dumps(msg)
                )