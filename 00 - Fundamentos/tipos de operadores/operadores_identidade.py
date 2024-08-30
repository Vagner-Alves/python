'''
São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.
'''

curso = "Formação Python Developer"
nome_curso = curso
saldo_conta, limite_conta = 200,200

print( curso is nome_curso)

print(curso is not curso)

print(saldo_conta is limite_conta and saldo_conta is not limite_conta)