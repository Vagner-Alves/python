'''
O pop vai remover o valor de um dicionário, após remover o valor ele irá retornalo
'''

agenda_telefone = {"Vagner": {"telefone": 819889998, "email":"vagneralves@email.com"}, 
"priscila":{"telefone": 8888188, "email":"pri@email.com"}
}
print(agenda_telefone)

agenda_telefone.pop("Vagner")
print(agenda_telefone)

# definindo um valor de retorno padrão
resultado = agenda_telefone.pop("priscila", "chave nao encontrada")
print(resultado)