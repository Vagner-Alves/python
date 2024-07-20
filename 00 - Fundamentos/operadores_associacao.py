'''
São operadores utilizados para verificar se um objeto está presente em uma sequencia.
'''

items_lista = [

    "maça", "uva", "banana","granola","mamão",
]

saques_conta = [49.9, 100.00]

print("maça" in items_lista)
print("banana" not in items_lista)

print(81 in saques_conta)
print(49.9 not in saques_conta)