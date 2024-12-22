'''
HERANÇA SIMPLES
Quando uma classe filha herda apenas de uma classe pai , esse fenomeno é chamado de herança simples.
'''

class Veiculo:
    def __init__(self, placa, marca, cor):
        self.placa = placa
        self.marca = marca
        self.cor = cor
    
    pass

class Carro(Veiculo):
    pass

class Moticleta(Veiculo):
    pass

class Caminhao(Veiculo):
    pass

