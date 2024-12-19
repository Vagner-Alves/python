'''
DESAFIO

João tem uma loja de bicicletas e gostaria de registrar a venda de suas bicicletas.
Crie um programa onde joão informe: ano, modelo, cor e valor da bicicleta vendida.
Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos ( metódos )

'''
class Bicicleta():
    def __init__(self, ano, modelo, cor, valor, numero_marchas):
        self.ano = ano
        self.modelo = modelo
        self.cor = cor
        self.valor = valor
        self.numero_marchas = numero_marchas

    def __str__(self):
        print("atributos da classe", self.__class__.__name__)
        return f'\n'.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])

    def buzinar(self):
        print(self.modelo , ": som genérico de bicicleta")
    
    def parar(self):
        print(self.modelo, ": parou")
    
    def correr(self):
        print(self.modelo, ": correu")
    
    def trocar_marcha(self, marcha):  # observe que o interpretador python não se importa com o nome self ele é apenas uma convenção
        
        def _trocar_marcha():
            if marcha > self.numero_marchas:
                print("marcha trocada")
            else:
                print("Não foi possível trocar de marcha")

bicicleta = Bicicleta(ano=2024, modelo="monark", cor="azul", valor=2100, numero_marchas=3)
bicicleta.buzinar()
#print(bicicleta.__str__())
bicicleta.trocar_marcha(4)
    