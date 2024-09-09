'''
COMPREENSÃO DE LISTAS

A compreensão de listas oferece uma sintaxe mais curta quando voce deseja: criar
uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista
aplicando alguma modificação nos elementos de uma lista existente.
'''

numeros = [1,18,8,2,9,56,13]

numeros_pares = [numero for numero in numeros if numero % 2 == 0]
numeros_aoquadrado = [numero ** 2 for numero in numeros]

print(numeros_pares)
print(numeros_aoquadrado)