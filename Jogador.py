from dotAndBox import DotBox


class jogador:
    
    def __init__(self):
        self.jogador = {"nome": "", "id": ""}
        self.jogo 

    def getName(self):
        self.jogador["nome"] = input("Qual Seu Nome? ")
        id = self.jogador["nome"[0]]
        # função para validar o ID 
        
    def startGame(self,N):
        self.jogo = DotBox(N)

    