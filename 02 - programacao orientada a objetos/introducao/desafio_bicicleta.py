'''
DESAFIO

João tem uma loja de bicicletas e gostaria de registrar a venda de suas bicicletas.
Crie um programa onde joão informe: ano, modelo, cor e valor da bicicleta vendida.
Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos ( metódos )

'''

class Bicicleta():
    def __init__(self, ano, modelo, cor, valor):
        self.ano = ano
        self.modelo = modelo
        self.cor = cor
        self.valor = valor
    
    def buzinar(self):
        print(self.modelo , ": som genérico de bicicleta")
    
    def parar(self):
        print(self.modelo, ": parou")
    
    def correr(self):
        print(self.modelo, ": correu")


bicicleta = Bicicleta(ano=2024, modelo="monark", cor="azul", valor=2100)
bicicleta.buzinar()
    