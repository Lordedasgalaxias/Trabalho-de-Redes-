from Servidor import Server
from Jogador import gamer


modo = input(
    "Digite s para servidor ou c para cliente: "
)
 
if modo == "s":

    N = int(input("Tamanho do jogo: "))

    s = Server(N)

    s.iniciar()

else:

    j = gamer()

    j.jogar()