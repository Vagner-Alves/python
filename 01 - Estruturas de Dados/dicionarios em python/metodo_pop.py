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

# o metodo popitem é tem a mesma função, porém remove os dados em sequencia 

carrinho_compras = {"banana": {"preco":0.15, "quantidade":8},"aveia": {"preco": 1.12, "quantidade": 1}}

carrinho_compras.popitem()
print(carrinho_compras)
carrinho_compras.popitem()
print(carrinho_compras)