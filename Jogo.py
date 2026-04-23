from dotAndBox import DotBox

class Jogo():

    def __init__(self, N):
        self.jogo = DotBox(N)

        self.jogador_1 = {"nome": "", "id": ""}
        self.jogador_2 = {"nome": "", "id": ""}

        self.GetnameJ1()
        self.GetnameJ2()

        self.jogadorAtual = self.jogador_1

    def trocarJogador(self):
        if self.jogadorAtual == self.jogador_1:
            self.jogadorAtual = self.jogador_2
        else:
            self.jogadorAtual = self.jogador_1

    def GetnameJ1(self):
        self.jogador_1["nome"] = input("Qual o nome do jogador 1: ")
        self.jogador_1["id"] = input("Qual letra deseja usar: ")

    def GetnameJ2(self):
        self.jogador_2["nome"] = input("Qual o nome do jogador 2: ")
        
        while True:
            letra = input("Qual letra deseja usar: ")
            if letra != self.jogador_1["id"]:
                self.jogador_2["id"] = letra
                break
            else:
                print("Essa letra já foi escolhida!")

    def jogar(self):
        encerrado = False

        while not encerrado:

            print(f"\nVez do jogador {self.jogadorAtual['nome']}")
            self.jogo.printGame()

            again, jogadas = self.jogo.jogar(self.jogadorAtual["id"])

            if jogadas == 0:
                print("Fim de jogo!")
                self.jogo.printGame()
                encerrado = True
                break

            if again == 0:
                self.trocarJogador()