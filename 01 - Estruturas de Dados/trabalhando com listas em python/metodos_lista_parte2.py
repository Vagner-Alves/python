'''
a lista por padrão já vem organizada como uma PILHA
'''


# removendo elementos da lista

lista = ['uva','aveia', 'maçã', 'banana', 'pera']

# pop sempre irá remover apartir do último elemento 

print(lista.pop() )        # remove pera
print(lista.pop() )        # remove banana
print(lista.pop() )        # remove maçã
print(lista.pop(0))        # remove pelo índice ( uva )


# removendo elementos especificos da lista ( pelo nome )

linguagens_programacao = ["Python", "Java", "javaScript", "Ruby"]
linguagens_programacao.remove("Ruby")
print(linguagens_programacao)
