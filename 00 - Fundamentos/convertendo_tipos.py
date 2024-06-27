'''
Em alguns momentos será necessário converter o tipo de uma variável para que possamos usar esse dado de forma coerente.
exemplo:
Podemos pedir ao usuário sua data de nascimento (string) ex 05/02/2002 , para saber a sua idade é necessário
dividir essa string e transformar o ano (2002) em um objeto do tipo inteiro, oque nos permite realizar operações matemáticas.
'''

# Convertendo tipos

PRECO = "8.00"
IDADE = "27"

print(PRECO) # o interpretador do python vai identificar automáticamente.

# convertendo manualmente
print(float(PRECO))
print(int(IDADE))

