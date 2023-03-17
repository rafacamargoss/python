
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    #enquanto não enforcou e não acertou
    while(not enforcou and not acertou):
        chute = input("Qual letra?")
        chute = chute.strip()

        index = 0 #posicao
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
                #print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        print(letras_acertadas)

    print("Fim do jogo")

##This allows the code to determine
##if it's being executed as the main program or being imported as a module into another program.
if(__name__ == "__main__"):
    jogar()