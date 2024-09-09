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
print(lista2)


# contar quantas vezes um objeto aparece na lista

cores = ['vermelho','azul','verde','amarelo','rosa','roxo', 'azul']
azul = cores.count('azul')

print(azul)


# adicionar vários elementos de uma vez ( não exclui duplicadas )

linguagens = ['python','java','javascript','sql']

print(linguagens)

linguagens.extend(['react','c#','springBoot'])
print(linguagens)

# descobrir a primeira ocorrencia de um objeto

java = linguagens.index('java')
print(java)