from ServerNet import ComunicadorServidor
from Jogador import gamer
from dotAndBox import Tabuleiro
import json

mensagem = {
    "tipo": "estado",
    "movimentos": [...],
    "box": [...],
    "vez": None
}

class Server:

    def __init__(self, N):

        self.tabuleiro = Tabuleiro(N)

        self.com = ComunicadorServidor()

    def iniciar(self):

        self.com.aceitarClientes()
        
        config = {
            "tipo": "config",
            "N": self.tabuleiro.N
        }
        self.com.broadcast(
            json.dumps(config)
        )
        
        vez = 0

        self.com.enviar(vez, json.dumps({
            "tipo": "sua_vez"
        }))

        while True:

            mensagem = self.com.receber(vez)

            dados = json.loads(mensagem)

            resultado = self.processarJogada(
                dados,
                vez
            )

            if not resultado:

                self.com.enviar(vez, json.dumps({
                    "tipo": "erro"
                }))

                continue

            estado = self.gerarEstado(vez)

            self.com.broadcast(
                json.dumps(estado)
            )

            vez = (vez + 1) % 2

            self.com.enviar(vez, json.dumps({
                "tipo": "sua_vez"
            }))

    def processarJogada(self, dados, jogador):

        nome = dados["name"]
        i1 = dados["i1"]
        j1 = dados["j1"]

        i2 = dados["i2"]
        j2 = dados["j2"]

        
        
        print(i1, j1, i2, j2)
        
        adjacente = (
            abs(i1 - i2) +
            abs(j1 - j2)
        ) == 1
        
        print("Adjacente:", adjacente)
        
        
        if not adjacente:
            return False

        return self.tabuleiro.gravarJogada(
            i1,
            j1,
            i2,
            j2,
            nome
        )

    def gerarEstado(self, vez):

        return {

            "tipo": "estado",

            "movimentos":
            [list(m)
             for m in self.tabuleiro.movimentos],

            "box":
            {f"{i},{j}": v
             for (i, j), v
             in self.tabuleiro.box.items()},

            "vez": vez
        }