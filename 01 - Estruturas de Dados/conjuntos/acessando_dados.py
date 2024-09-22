'''
Conjuntos em python não suportam indexação, nem fatiamento, caso queira acessar seus valores é necessário
converter o conjunto para uma lista.
'''

numeros = set([1,2,3,4,5,6,7,8,8,9,1,2,3,10,11,12])
print(numeros)

numeros = list(numeros)  # transformando em lista
print(numeros[1])

# percorrendo os itens do conjunto

carrinho_compra = {"maçã", "banana", "uva", "aveia", "manga"} # outra forma de definir um conjunto

for indice,items in enumerate(carrinho_compra):
    print(f"{indice} {items}")

