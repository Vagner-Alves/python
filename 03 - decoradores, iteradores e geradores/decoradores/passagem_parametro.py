def mensagem(nome):
    print('executando mensagem')
    return f'oi {nome}'

def mensagem_longa(nome):
    print('executando mensagem longa')
    return f'olá tudo bem com voce {nome}'

def executar(funcao):
    print('executando executar')
    return funcao('vagner alves')

print(executar(mensagem))