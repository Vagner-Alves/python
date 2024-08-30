'''
IF Ternário
Permite escreve uma condição em uma única linha. Ele é composto por 3 partes, a primeira parte é o RETORNO, caso
a expressão retorne VERDADEIRO, a segunda parte é a EXPRESSÃO LÓGICA e a terceira parte é o RETORNO se a expressão for FALSA.

'''
saque_conta = 100
saldo_conta = 875

status = "Sucesso" if saque_conta <= saldo_conta  else "não há dinheiro o suficiente"

print(f"{status} ao realizar o saque na conta. ")
