'''
Métodos de classe

métodos de classe estão ligados a classe e não ao objeto.
Eles tem acesso ao estado da classe, pois recebem um parametro
que aponta para a classe e não para a instancia do objeto.

Método estáticos

um método estático não recebe um primeiro argumento explícito, Ele também é um método
vinculado a classe e não ao objeto da classe. Este método não pode acessar ou modificar o estado
da classe. Ele está presente em uma classe porque faz sentido que o método esteja presente nela.

qual a diferença?

um método de classe recebe um primeiro parametro que aponta para a classe,
enquanto um método estático não.

um método de classe pode acessar ou modificar o estado da classe enquanto um método estático não pode
acessá-lo ou modificá-lo

quando utilizar cada um deles ?

geralmente usamos o método de classe para criar métodos de fábrica.
geralmente usamos métodos estáticos para criar funções utilitárias.
'''

class Pessoa:
    def __init__(self,nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_apartir_data_nascimento(cls,ano, mes, dia, nome):
        # cls é uma referencia para  a classe
        idade = 2025 - ano
        return cls(nome, idade)

    @staticmethod
    def maior_idade(idade):
        return idade >= 18

#pessoa = Pessoa("Vagner Alves", 28)
#print(pessoa.nome, pessoa.idade)

pessoa2 = Pessoa.criar_apartir_data_nascimento(1997, 1, 5, "vagner Alves")
print(pessoa2.nome, pessoa2.idade)

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(17))
