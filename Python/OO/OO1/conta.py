class Conta:

    #definir metodo construtor

    def __init__(self, numero, titular, saldo, limite):

        #self -> referencia em memoria a propria clase, seria como se fosse o this

        print("Construiindo objeto....{}".format(self))

        #__ dois undrline é igaul a private
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__cod_banco = "001"


    def __valida_saque(self,valor):

        quantidade_disponivel = self.__saldo + self.__limite

        return valor <= quantidade_disponivel

    def extrato(self):

        saldo = self.__saldo

        print("O extrato é {}".format(saldo)) 
    
    def depositar(self,valor):

        self.__saldo+=valor
    
    def sacar(self,valor):

        validacao =  self.__valida_saque(valor)

        if(validacao):
            
            self.__saldo-=valor
        else:

            print("Limite ultrapassado")
    
    def transfere(self,valor,destino):

        self.sacar(valor)
        destino.depositar(valor)

    def getSaldo(self):

        return self.__saldo

    def getNumero(self):

        return self.__numero

    def getTitular(self):

        return self.__titular

    def getLimite(self):

        return self.__limite
 

    def setSaldo(self,saldo):

        self.__saldo = saldo


    #Em py é possivel fazer o seguinte:

    @property
    def setLimite(self,limite):

        self.__limite = limite

        #dessa forma na linha de execução podemos passar conta.setLimite = 0.0
        #o @ poderia ser tbm @limite.setter tbm, por exemplo

    #criando método estatico
    @staticmethod
    def cod_banco():

        return "001"

    @staticmethod
    def cod_bancos():

        #criando um dicionario
        bancos = {
            "BB":"001",
            "Caixa":"104",
            "Bradesco":"237"
        }

        return bancos

        