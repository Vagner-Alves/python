'''
o metódo get serve para "puxa" um valor do dicionário
'''

contatos = {
    "vagneralves997@gmail.com": {"nome":"vagner", "telefone":"(xx) xxxx-xxxx"},
    "alguem@email.com": {"nome":"alguém", "telefone":"33 3333-3333"},
    "ff@email.com": {"nome": "ff", "telefone": "44 4444-4444"},
    "yy@hotmail.com": {"nome": "xx", "telefone": "55 5555-5555"}
}

print(contatos.get("vagneralves997@gmail.com")) # usamos uma chave como valor, caso não exista retorna None