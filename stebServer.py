from Buffer import Buffer


class stebServer:
    
    def __init__(self, id):
        """inicializa a classe stebServer com um id de parâmetro, o id deve ser o mesmo entre as entidades comunicadoras"""
        self.buffer = Buffer(self,id)
   # Envia a mensagem para o outro lado da comunicação
    def enviarMensagem(self, mensagem:str):
        self.buffer.inserirMensagem(self, mensagem)

    # Recebe uma mensagem enviada pelo outro lado da comunicação
    def receberMensagem(self) -> str:
        return self.buffer.removerMensagem(self)