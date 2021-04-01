#Primeiro script de estudos em python
#Gustavo Costa - 29/03/2021 07:42

#OBJETIVO: Fazer um jogo onde deve-se adivinhar o número sorteado

#Pré requisitos: Número aleatório / Dificuldade / Quantidade de tentativas / Pontuação


import random

print("########## Adivinhe o número ##########")

dificuldade = 0
pontuacao = 1000

def gerar_num_random():

    #Criar um número aleatório entre 1 - 100

    random_number = random.randrange(1,101)

    return random_number

def define_dificuldade(dificuldade):

    #Definir a dificuldade e consequentemente as tentativas

    tentativas = 0

    if(dificuldade == 1):

        #Facil
        tentativas = 10

    elif(dificuldade == 2):

        #Medio
        tentativas = 5
    
    elif(dificuldade == 3):

        #Dificil
        tentativas = 3
    
    return tentativas

def valida_chute(chute):

    status = False
    print ("Seu chute é ",chute)
    if(chute > 0 and chute <= 100):

        status = True
    
    return status

def define_pontuacao(secret_number, chute):

    #Perda de ponta -> diferença entre o numero secreto e o chute

    status_ponto = abs(secret_number - chute)

    return status_ponto

print("INICIANDO JOGO\n")

dificuldade = int(input("Difina sua dificuldade:\n1-Fácil\n2-Médio\n3-Difícil\n"))
tentativas = define_dificuldade(dificuldade)

print("Sua quantidade de tentivas é {0}".format(tentativas))

print("Gerando numero aleatorio.....\n")
secret_number = gerar_num_random()
print("Numero secreto gerado!\n")

print (secret_number)

contador = 0
for contador in range(contador,tentativas):

    print("\n\nTentativa {0}".format(contador+1))

    chute = int(input("\nInforme o número escolhido\n"))

    if(not(valida_chute(chute))):

        print ("Informe um numero entre 1 - 100")
        break
    

    if(chute != secret_number):

        if(chute > secret_number):

            print("\n O numéro secreto é menor que {0} ".format(chute))

            pontuacao-= define_pontuacao(secret_number,chute)

        elif(chute < secret_number):

            print("\n O numéro secreto é maior que {0} ".format(chute))

            pontuacao-= define_pontuacao(secret_number,chute)


    if(chute == secret_number):

        print("\nPARABÉNS!!")
        print("Você acertou o número secreto!")
        break

print("\n\nSua pontuação foi {0}".format(pontuacao))




