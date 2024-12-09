'''
OBJETOS DE PRIMEIRA CLASSE
Em python tudo é objeto, dessa forma funções também são objetos
o que as tornam objetos de primeira classe. Com isso podemos atribuir
funções a variáveis, passá-las como parametro para funções, usá-las como valores
em estruturas de dados (listas, tuplas, dicionários e etc) e usar como valor
de retorno para uma função ( closures ).
'''

def somar(numero1, numero2):
    return numero1 + numero2

def subtrair(numero1, numero2):
    return numero1 - numero2

def exibir_resultado(numero1, numero2, funcao):
    resultado = funcao(numero1, numero2)
    print(f"resultado da operação: {resultado}")

exibir_resultado(2,2, somar)
exibir_resultado(5,2, subtrair)
guardar_funcao = subtrair

print(guardar_funcao(10,8))