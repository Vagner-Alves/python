def mensagem(nome):
    print('executando mensagem')
    return f'oi {nome}'

def mensagem_longa(nome):
    print('executando mensagem longa')
    return f'olá tudo bem com voce {nome}'

def executar(funcao, nome):
    print('executando executar')
    return funcao(nome)

print(executar(mensagem, 'lavinia'))