#modelo normalmente dado quando se cria conceitos de classe

class Filme:

    def __init__(self,nome,ano,duracao):

        #title aumenta letra de cada palavra
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    def dar_like(self):
        self.__likes +=1

    @property
    def likes(self):

        return self.__likes

    @property
    def nome(self):

        return self.__nome

    #para definir um set como propriedades

    @nome.setter

    def nome(self,novo_nome):

        self.__nome = novo_nome
class Serie:

    def __init__(self,nome,ano,temp):

        self.__nome = nome.title()
        self.ano = ano
        self.temp = temp
        self.__likes = 0

    def dar_like(self):
        self.likes +=1
    
    @property
    def likes(self):

        return self.__likes

    @property
    def nome(self):

        return self.__nome

    #para definir um set como propriedades

    @nome.setter

    def nome(self,novo_nome):

        self.__nome = novo_nome

filme = Filme("Vingadores",2018,120)
filme.dar_like()

#com as propriedade aqui conseguimos acessar o atributo de forma mais facil
print (f"Nome: {filme.nome} - Likes: {filme.likes}")

serie = Serie("Teste",2018,120)
print (f"Nome: {serie.nome} - Likes: {serie.likes}")