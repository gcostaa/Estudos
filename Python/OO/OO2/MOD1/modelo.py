#modelo normalmente dado quando se cria conceitos de classe

class Filme:

    def __init__(self,nome,ano,duracao):

        self.nome = nome
        self.ano = ano
        self.duracao = duracao


class Serie:

    def __init__(self,nome,ano,temp):

        self.nome = nome
        self.ano = ano
        self.temp = temp

vingadores = Filme("Vingadores",2018,120)
print (f"Nome: {vingadores.nome}")