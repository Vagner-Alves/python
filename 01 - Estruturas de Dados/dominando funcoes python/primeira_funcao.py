'''
função é um bloco de código identificado por um nome e pode receber uma lista de parametros,
esses parametros podem ou não ter valores padrões. Usar funções torna o código mais légivel e possibilita
o reaproveitamento do código. Programar baseado em funções , é o mesmo que dizer que estamos programando de 
maneira estruturada.
'''

def exibir_mensagem():
    print("Olá Mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}")

def exibir_mensagem_3(nome="usuario não identificado"):
    print(f"seja bem vindo {nome}")

exibir_mensagem()
exibir_mensagem_2("Vagner Alves")
exibir_mensagem_3()