'''
METODOS

a classe lista traz vários metódos embutidos.
'''

# adicionar elementos na lista

lista = []

lista.append('curso python')
lista.append(19.90)
lista.append(['curso java',19.90])

print(lista)

# limpar a lista

lista.clear()
print(lista)

# criar uma copia da lista

nova_lista = ['maçã','uva','aveia','banana']
lista2 = nova_lista.copy()