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
    
    def ligar(self):
        print(self.marca, 'ligando motor')

class Carro(Veiculo):
    pass

class Moticleta(Veiculo):
    pass

class Caminhao(Veiculo):
    pass


moto = Moticleta('XXXX','yamaha','amarela',2)
moto.ligar()

carro = Carro('YYYY','Fiat', 'branco', 4)
carro.ligar()

caminhao = Caminhao('ZZZZ', 'caminhão genérico', 'verde amarelo com óculos escuro', 17)