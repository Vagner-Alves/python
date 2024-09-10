'''
TUPLAS

são estruturas de dados muito parecidas com as listas, a principal diferença é que tuplas são imutáveis enquanto 
listas são mutáveis. Podemos criar tuplas através da classe tuple, ou colocando valores seperados por vírgula de parenteses.

'''

lista_frutas = ("morango", "maçã", "uva", "pessego", "banana", "jaca",)

print(lista_frutas)

paises = ("Brasil",) # sempre colocar uma virgula ao final para não confundir o compilador python.
continentes = tuple("america do sul",) # cria uma tupla com cada caractere 
print(continentes)