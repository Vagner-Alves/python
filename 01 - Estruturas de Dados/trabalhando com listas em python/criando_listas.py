'''
LISTAS EM PYTHON
listas em python podem armarzenar de maneira sequencial qualquer tipo de objeto.
podemos criar listas utilizando o constructor list, a funçõa range ou colocando valores
separados por vírgula dentro de colchetes. Listas são objetos mutáveis, portanto podemos
alterar seus valores após a criação.

'''

letras            = list("curso de python")                     # vai criar uma lista com cada caractere da string.
numeros           = range(10)                                   # vai criar uma lista com números de 0 a 10.
lista_frutas      = ["maçã","banana","uva","pessego","manga"]   # vai criar uma lista com os elementos dentro dos colchetes.
carrinho_compras  = ['tenis branco',120, 'tenis preto',120]     # vai criar uma lista com diversos tipos de objeto ( string e integer).


print(letras)
print(numeros)
print(lista_frutas)
print(" ")

'''
ACESSO DIRETO

A lista é uma sequencia, portanto podemos acessar seus dados utilizando indices.
Contamos o indice de determinada sequencia apartir de zero.
'''

print(lista_frutas[0])