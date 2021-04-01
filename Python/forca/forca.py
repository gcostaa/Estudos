import random

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def gerar_tentativas(secret_word):

    open_word = []

    #FUNCIONA TBM!:
    
    open_word = ["_" for word in secret_word]


    #for cont in range(0,len(secret_word)):

        #open_word.append("_")

    
    
    return open_word

def ler_arquivo():

    words = []
    caminho = "C:\\Users\\Administrador\\Desktop\\dados.txt"

    #abrindo no modo leitura
    arquivo = open(caminho,"r")

    for linha in arquivo:

        words.append(linha.strip())
        #print(linha,end="\n")

    arquivo.close()

    return words

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    words = ler_arquivo()
    sort = random.randrange(0,len(words))
    secret_word = words[sort].upper()
    gameover = False
    win = False
    errors = 0
    print(secret_word)
    open_word = gerar_tentativas(secret_word)

    print("\n",open_word)   
    
    while ((not gameover) and (not win)):

        word = input("\nQual a letra escolhida?....")
        #Tirando espaço
        word = word.strip().upper()

        if (word in secret_word):
            #Se a letra escolhida existe na palavra

            index = 0
            for syllable in secret_word:
            
                if(word == syllable):
                    #Se a letra escolhida esta na posicao index da palavra
                    print("Letra {0} encontrada na posição {1}".format(word,index))
                    open_word[index] = word
                
                index += 1
        elif (word not in secret_word):

            #Letra não existe na palavra
            errors+=1
            desenha_forca(errors)
            #print("Errou ",errors)
        
        else:

            print("Comando inválido")
        
        #Altera variavel para true caso erre 6 vezes
        gameover = errors == 6
        #Verifica se acertou todas as letras
        win = "_" not in open_word
            
        print("\nStatus da forca:\n",open_word)

        
    
    if(gameover):

        print("Tu perdeu")

    elif(win):

        print("Tu Ganhou")
    
    else:

        print("Impossivel ler um resultado")

if(__name__ == "__main__"):
    jogar()
