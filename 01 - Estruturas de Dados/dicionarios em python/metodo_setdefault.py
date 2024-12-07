'''
set default verifica se uma chave existe no dicionário e alterar o valor, caso a chave não exista ela
será criada.
'''

contato = {"nome": "vagner", "telefone": 81998327840}

contato.setdefault("idade", 27)
print(contato)