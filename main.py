from Jogador import jogador

def main(): 
    selection = input("\n 1-Criar Partida\n 2-Entrar em uma partida ")
    
    match selection:
        case 1:
            createGame()
        case 2:
            enterGame()
    
# N = table -1 
def createGame():
    table = int(input("qual tamanho de jogo você quer ?"))
        
    
def enterGame():


if __name__ == '__main__':
    main()