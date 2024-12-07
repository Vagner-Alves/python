'''
o metódo copy serve para tirar uma cópia de um dicionário. 
muito util quando querendo manipular um dicionário ao mesmo tempo que desejamos
manter a estrutura original sem modificações
'''

contatos = {
    "vagneralves997@gmail.com": {"nome":"vagner", "telefone":"(xx) xxxx-xxxx"},
    "alguem@email.com": {"nome":"alguém", "telefone":"33 3333-3333"},
    "ff@email.com": {"nome": "ff", "telefone": "44 4444-4444"},
    "yy@hotmail.com": {"nome": "xx", "telefone": "55 5555-5555"}
}

copia_contatos = contatos.copy()
copia_contatos["alguem@email.com"] = {"nome": "vanessa", "telefone":"44 3333-3333"}

print(copia_contatos["alguem@email.com"])
print(contatos["alguem@email.com"])