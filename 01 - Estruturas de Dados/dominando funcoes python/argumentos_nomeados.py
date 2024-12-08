'''
Funções também podem ser chamadas usando argumentos nomeados da forma chave=valor
'''

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# há 3 formas de passar os parametros para uma função
salvar_carro("aston martin", "DB12", 2023, "placa XX-XXX-XX")
salvar_carro(marca="aston martin", modelo="DB12", ano=2024, placa="placa XX-XXX-XX")
salvar_carro(**{"marca": "aston martin", "modelo":"DB12", "ano":2024, "placa":"placa XX-XXX-XX"})

'''
porém há nuances na forma como passamos os parametros

na primeira opção, o usuário pode não passar os parametros no ordem correta
isso irá alterar a ordem dos valores, exemplo o modelo pode receber o valor da placa e etc.

na segunda opção não temos esse problema, porém com a desvantagem de escrever mais código.

na última opção temos um dicionário como argumento, onde as chaves serão os nomes dos argumentos e os valores , valores!
'''