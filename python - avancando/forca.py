
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    palavra_secreta = "maçã".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    #enquanto não enforcou e não acertou
    while(not enforcou and not acertou):
        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0 #posicao
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                    #print("Encontrei a letra {} na posição {}".format(letra, index))
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")

##This allows the code to determine
##if it's being executed as the main program or being imported as a module into another program.
if(__name__ == "__main__"):
    jogar()