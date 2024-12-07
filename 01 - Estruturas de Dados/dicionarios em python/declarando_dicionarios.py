'''
como declarar dicionários em python
'''

carrinho_compras = {"nome": "banana", "valor": 0.15}

print(carrinho_compras)

pessoa = dict(nome= "vagner alves", idade=27)
print(pessoa)

# criando novas chaves
pessoa["telefone"] = "xx xxxx-xxxx"
print(pessoa)

# alterando o valor de uma chave ( diminuir o preço da banana)
carrinho_compras["valor"] = 0.05  
print(carrinho_compras)