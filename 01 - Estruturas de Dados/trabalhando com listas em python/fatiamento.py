'''
FATIAMENTO
além de acessar elementos diretamente , podemos extrair um conjunto de valores de uma sequencia.
Para isso basta passar o indice inicial e /ou final para acessar o conjunto. Podemos ainda informar
quantas posições o cursos deve "pular" no processo.

'''

lista = list('python')

print(lista[2:])                # pega as últimas 3 letras
print(lista[:2])                # pega as duas primeiras letras
print(lista[1:3])               # pega a segunda e terceira letra
print(lista[0:3:2])             # 
print(lista[::])                # tira uma cópia da lista
print(lista[::-1])              # faz uma cópia espelhada da lista ( inversa )