import socket

class ComunicadorServidor:

    def __init__(self, host="0.0.0.0", port=5000):

        self.host = host
        self.port = port

        self.server = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.server.bind((self.host, self.port))

        self.server.listen(2)

        self.clientes = []

    def aceitarClientes(self):

        print("Esperando jogadores...")

        while len(self.clientes) < 2:

            conn, addr = self.server.accept()

            print(f"Cliente conectado: {addr}")

            self.clientes.append(conn)
    

    def enviar(self, jogador, mensagem):

        conn = self.clientes[jogador]

        conn.sendall((mensagem + "\n").encode())

    
        
        

    def receber(self, jogador):

        conn = self.clientes[jogador]

        dados = conn.recv(4096).decode()

        return dados.strip()

    def broadcast(self, mensagem):

        for conn in self.clientes:

            conn.sendall((mensagem + "\n").encode())