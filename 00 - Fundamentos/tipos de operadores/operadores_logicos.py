'''
OPERADORES LÓGICOS
são operadores usados utilizados em conjunto com os operadores de comparação, para montar
uma expressão lógica. Quando um operador de comparação é utilizado, o resultado retornado é um booleano, 
dessa forma podemos combinar operadores de comparação com os lógicos,
exemplo:
    comparação + lógico + comparação ... etc

AND, OR, NOT
'''

saldo_conta    = 1200
saque_conta    = 250
limite_saque   = 500
conta_especial = True

True  and True 
True  and False
False and False
True  or  True
True  or  False
False or  False

print( saque_conta >= limite_saque or saldo_conta < saque_conta)

print(saldo_conta > 0 and conta_especial == True)

print( (saldo_conta >= saque_conta and saque_conta > limite_saque) or (conta_especial > saque_conta) )

# evite usar blocos de expressões complidos, tente quebralos em variavéis.

primeira_expressao = ( saque_conta >= limite_saque ) # verificar se a conta tem saldo
segunda_expressao = ( conta_especial is True )       # verificar se a conta é especial

# combinando expressões
# conta é especial e tem saldo disponível
print( primeira_expressao and segunda_expressao) 
# a conta é especial ou tem saldo disponível
print( primeira_expressao or segunda_expressao)