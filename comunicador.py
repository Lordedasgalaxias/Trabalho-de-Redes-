from Buffer import Buffer

class Comunicador:

    def __init__(self, id):
        self.buffer = Buffer(self,id)

    # Envia a mensagem para o outro lado da comunicação
    def enviarMensagem(self, mensagem:str):
        self.buffer.inserirMensagem(self, mensagem)

    # Recebe uma mensagem enviada pelo outro lado da comunicação
    def receberMensagem(self) -> str:
        return self.buffer.removerMensagem(self)