'''
só devemos passar os parametros através das keywords nesse modelo de função
'''
def criar_carro(* modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Celta Preto", ano=2016, placa="ABC-123", marca="FIAT", motor="V12", combustivel="Gasolina") # correto

criar_carro("celta preto", 2016, "ABC-123", marca="FIAT", motor="V12", combustivel="gasolina" ) # incorreto