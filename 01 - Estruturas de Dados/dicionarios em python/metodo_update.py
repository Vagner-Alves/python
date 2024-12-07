'''
o update nos permite atualizar um dicionário com outro
'''

contatos = {"caralegal@gmail.com": {"nome":"pessoa aleatoria", "telefone":"819767583"}
}
# uma nova chave com esses dados é criada
contatos.update({"carachato@gmail.com": {"nome":"pessoa especifica", "telefone":"87839392"}})
print(contatos)

# quando a chave já existe, os dados serão atualizados
contatos.update({"caralegal@gmail.com": {"nome":"jao", "telefone": "8178992829"}})
print(contatos)