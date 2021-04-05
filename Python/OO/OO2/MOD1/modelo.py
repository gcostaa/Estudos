#modelo normalmente dado quando se cria conceitos de classe

class Filme:

    def __init__(self,nome,ano,duracao):

        #title aumenta letra de cada palavra
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_like(self):
        self.likes +=1

class Serie:

    def __init__(self,nome,ano,temp):

        self.nome = nome.title()
        self.ano = ano
        self.temp = temp
        self.likes = 0

    def dar_like(self):
        self.likes +=1

filme = Filme("Vingadores",2018,120)
filme.dar_like()
print (f"Nome: {filme.nome} - Likes: {filme.likes}")

serie = Serie("Teste",2018,120)
print (f"Nome: {serie.nome} - Likes: {serie.likes}")