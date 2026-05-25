import socket

class ComunicadorCliente:

    def __init__(self, host="127.0.0.1", port=5000):

        self.client = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.client.connect((host, port))

    def enviar(self, mensagem):

        self.client.sendall(
            (mensagem + "\n").encode()
        )

    def receber(self):

        dados = self.client.recv(4096)

        if not dados:
            return None

        return dados.decode().strip()