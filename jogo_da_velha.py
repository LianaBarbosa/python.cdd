import os
import random
from colorama  import Fore, Back , Style

jogarNovamente = "s"
jogadas = 0
quemJoga = 2
maxJogadas = 9
vit = "n"

velha = [
    [ " "," "," "]
    [" ", " ", " "]
    [" ", " ", " "]
]

def tela():
    global velha
    os.system('cls')
    print("  0 1 2 ")
    print("0: " + velha[0][0] + " " + velha[0][1] + " " + velha[0][2])
    print (" -----------")
    print("1: " + velha[1][0] + " " + velha[1][1] + " " + velha[1][2])
    print(" -----------")
    print("2: " + velha[2][0] + " " + velha[2][1] + " " + velha[2][2])
    print(" -----------")
    print("jogadas: " + Fore.GREEN str(jogadas) + Fore.RESET)


def jogadorJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas
    if quemJoga == 2 and jogadas<maxJogadas:
        l=int(input("Linha..."))
        c=int(input("Coluna..."))

        while velha[l][c]!=" ":
            l=int(input("Linha..."))
            c=int(input("Coluna..."))

        try:
            velha[l][c]="x"
            quemJoga = 1
            jogadas += 1
        except:
            print("linha e ou coluna invalida")
                os.system("pause")

def cpuJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas
    if quemJoga == 1 and jogadas<maxJogadas:
        l=random.randrange(0,3)
        c=random.randrange(0,3)
        while velha[l][c]!=" ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
            velha[l][c] = "O"
            jogadas += 1
            quemJoga = 2

def verificarVitoria():
    global velha
    vitoria = "n"
    simbolos=["x","O"]
    for s in simbolos:
        vitoria="n"
        il=ic=0
        while ic<3:
            soma=0
            il=0
            while ic<3:
                if (velha[il][ic]==s):
                    soma +=1
                il+=1
            if(soma == 3):
                vitoria = s
                break
            ic+=1
        if(vitoria!= "n"):
                    break

            soma=0
        idiagl=0
        idiagc=0
        while idiagc<3:
            if (velha[idiagl][idiagc]==s):
                soma +=1
                idiagl+=1
                idiagc-=1
            if soma == 3:
                vitoria = s
                break
        return vitoria

def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    jogadas = 0
    quemJoga = 2
    maxJogadas = 9
    vit = "n"

    velha = [
        [" ", " ", " "]
        [" ", " ", " "]
        [" ", " ", " "]
    ]


    while(jogarNovamente=="s" or jogarNovamente=="S"):
    while True:
        tela()
        jogadorJoga()
        cpuJoga()
        tela()
        vit=verificarVitoria()
        if (vit == "n") or (jogadas >= maxJogadas):
            break

        print(Fore.RED + "FIM DE JOGO" + Fore.YELLOW)
        if (vit == "x" or vit == "O"):
            print("resultado: jogador" + vit + "venceu")
        else:
            print("Resultado: Empate")
          jogarNovamente=input(Fore.BLUE + "jogar novamente? (s/n)" + Fore.RESET)
        redefinir()

