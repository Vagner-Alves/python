'''
RANGE
é uma função built-in ( embutida) do python, ela é usada para produzir uma sequencia de números inteiros
a partir de um inico ( inclusivo ) para um fim ( exclusivo ) 

essa função recebe 3 argumentos: start (opcional), stop (obrigatório) e step (opcional).
'''

for numero in range(0,11):
    print(numero, end=' ')

print( )

print('# exibindo uma tabuada de 5')

for tabuada in range(0,51,5):
    print(tabuada, end=" ")