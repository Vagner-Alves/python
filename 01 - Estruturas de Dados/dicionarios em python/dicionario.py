'''
um dicionário é um conjunto não-ordenado de pares chave: valor,
onde as chaves são únicas em uma dada instancia do dicionário. Dicionários
são delimitados por chave: {} , e contém uma lista de pares chave: valor
separadas por vírgulas.

dicionários podem armazenar qualquer tipo de objeto python como valor, 
desde que a chave para esse objeto seja imutavel ( string e números)

'''

contatos = {
    "vagneralves997@gmail.com": {"nome":"vagner", "telefone":"(xx) xxxx-xxxx"},
    "alguem@email.com": {"nome":"alguém", "telefone":"33 3333-3333"},
    "ff@email.com": {"nome": "ff", "telefone": "44 4444-4444"},
    "yy@hotmail.com": {"nome": "xx", "telefone": "55 5555-5555"}
}

pesquisa = contatos["vagneralves997@gmail.com"]["nome"]
print(pesquisa)

# a forma mais comum de percorrer um dicionário é utilizando o comando for
for chave in contatos:
    print(contatos[chave])