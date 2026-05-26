import random
import string
from Buffer import Buffer
from dotAndBox import Tabuleiro

class stebServer:
    
    def __init__(self, id):
       self.jogadoresID = {} 
       self.salas = {} ## vetor
       {
           "ABC123":{
               "jogadores":[],
               "tabuleiro":Tabuleiro,
               "buffer": Buffer
           }## setbServer contem salas a qual a estrutura é a de um código(a string ABC123) que contem um vetor de jogadores, um tabuleiro e o Buffer que relaciona os dois
       }
   
   # Envia a mensagem para o outro lado da comunicação
    def enviarMensagem(self, mensagem:str):
        self.buffer.inserirMensagem(self, mensagem)

    # Recebe uma mensagem enviada pelo outro lado da comunicação
    def receberMensagem(self) -> str:
        return self.buffer.removerMensagem(self)
    
    def createCodeRoom():
       return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) # definição de como é o código que será retornado
    
    def createGame(self,jogador,tamanho):
        
        codigo = self.createCodeRoom()
        
        self.salas[codigo] = {
            "jogadores" : [jogador],
            "tabuleiro" : Tabuleiro(tamanho),
            "buffer" : Buffer(self, codigo)
        }
        return codigo
    
    def enterGame(self,jogador,codigo):
        if codigo not in self.salas:
            return "Sala não encontrada"
        
        sala = self.salas[codigo]
        
        if len(sala["jogadores"]) >=2:  # mudar depois 
            return "Sala cheia"
        
        sala["jogadores"].append(jogador)
        return "ok"
    
    
