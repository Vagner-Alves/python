'''
Existem diferentes modos de abrir um arquivo, como somente leitura (r), gravação (w) e anexar (a).
O modo de abertura deve ser escolhido de acordo com a operação que iremos realizar no mesmo.
'''

arquivo_texto = open("texto.txt")

for texto in arquivo_texto.readlines():
    print(texto)
arquivo_texto.close() # importante fechar para economizar recursos