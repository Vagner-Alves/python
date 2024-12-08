'''
para retorna um valor, utilizamos a palavra reservada return.
Toda função python retorna None por padrão. Diferente de outras linguagens
de programação, em python uma função pode retornar mais de um valor.
'''

def calcular_total(numeros):
    return sum(numeros)

print(calcular_total([1,1,3,4]))

def retornar_antecessor_sucessor(numero):
    antecessor = numero -1
    sucessor = numero +1
    return antecessor, sucessor

print(retornar_antecessor_sucessor(8))
