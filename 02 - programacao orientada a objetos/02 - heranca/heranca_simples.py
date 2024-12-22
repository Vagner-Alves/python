'''
HERANÇA SIMPLES
Quando uma classe filha herda apenas de uma classe pai , esse fenomeno é chamado de herança simples.
'''

class Veiculo:
    def __init__(self, placa, marca, cor, numero_rodas):
        self.placa = placa
        self.marca = marca
        self.cor = cor
        self.numero_rodas = numero_rodas
    
    pass

class Carro(Veiculo):
    pass

class Moticleta(Veiculo):
    pass

class Caminhao(Veiculo):
    pass


moto = Moticleta('XXXX','yamaha','amarela',2)
print(moto)