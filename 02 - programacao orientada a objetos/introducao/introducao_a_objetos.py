'''
Uma classe define as características e comportamentos de um objeto, porém não conseguimos usá-las diretamente.
Já os objetos podemos usá-los e eles possume as características e comportamento que foram definidos nas classes.
'''

# exemplo de classe em python
class Cachorro():
    def __init__(self, nome, raca, cor_pelo, acordado=True):
        self.nome = nome
        self.raca = raca
        self.cor_pelo = cor_pelo
        self.acordado = acordado
    
    def __self__(self):
        print(self.nome, self.raca, self.cor_pelo, self.acordado)
    
    def latir(self):
        print(f"{self.nome}: AuAu")
    
    def dormir(self):

        if self.acordado==True:
            self.acordado = False
        else:
            self.acordado = False

        print("ZzzZzz")

# objetos da classe cachorro

primeiro_cachorro = Cachorro(nome="paçoca", raca="pastor alemão", cor_pelo="marrom com listas pretas",acordado=False)

primeiro_cachorro.latir()
primeiro_cachorro.dormir()
print(primeiro_cachorro.acordado) 
primeiro_cachorro.__self__()

# é possível criar vários objetos usando a mesma classe, aproveitando os atributos e metódos ( características e comportamentos)
segundo_cachorro = Cachorro(nome="Bella", raca="labrador retriever", cor_pelo="branco com manchas pretas", acordado=True)