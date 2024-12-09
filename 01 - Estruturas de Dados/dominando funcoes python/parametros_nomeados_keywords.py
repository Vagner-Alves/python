'''
Aqui devemos usar tanto os nomes quanto as keywords ao usar essa função, por isso a presenca dos simbolos / e *
'''

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("celta preto", 2016, "ABC-123", marca="FIAT", motor="V12", combustivel="gasolina" ) # correto
criar_carro(modelo="Celta Preto", ano=2016, placa="ABC-123", marca="FIAT", motor="V12", combustivel="Gasolina") # incorreto