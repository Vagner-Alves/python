'''
para evitar numerosas linhas de código, laços de repetição para verificar a existencia de chaves
usamos o operador associação IN
'''


contatos = {
    "vagneralves997@gmail.com": {"nome":"vagner", "telefone":"(xx) xxxx-xxxx"},
    "alguem@email.com": {"nome":"alguém", "telefone":"33 3333-3333"},
    "ff@email.com": {"nome": "ff", "telefone": "44 4444-4444"},
    "yy@hotmail.com": {"nome": "xx", "telefone": "55 5555-5555"}
}

# forma bem simples de verificar chaves em uma sequencia
resultado = "vagneralves997@gmail.com" in contatos
print(resultado)

resultado_valor = "telefone" in contatos["yy@hotmail.com"]
print(resultado_valor)
