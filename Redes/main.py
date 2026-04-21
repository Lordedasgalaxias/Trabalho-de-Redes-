from Jogo import Jogo

def main(): 
    table = int(input("qual tamanho de jogo você quer ?"))
    jogo = Jogo(table - 1 )

    jogo.jogar()

if __name__ == '__main__':
    main()