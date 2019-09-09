

import random

#-----------------------------------------------------
def main():
    nomePlayer = []
    nrPlayer = int(input("Insira o numero de jogadores[maximo 4 jogadores]: "))

    for i in range(nrPlayer):
        nomePlayer.append(str(input('Informe o Nome do {}° Player'.format(i+1))))
        print('O jogador: {} foi add com sucesso!'.format(nomePlayer))         



def rolarDados(quantidade, valorMaximo, numeroJogadas):
    print ("Funcao rolar rolar dados")



#-----------------------------------------------------
if __name__ == '__main__':
    main()
    