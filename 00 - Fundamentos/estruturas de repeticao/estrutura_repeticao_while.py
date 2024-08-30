'''
WHILE

O comando while é usado para repetir um bloco de código várias vezes.
Faz sentido usar essa estrutura de repetição quando não sabemos o número exato de vezes
que nosso bloco de código deve ser executado.
'''

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print('Saque realizado com sucesso: ')
    
    elif opcao == 2:
        print('Imprimindo Extrato da conta: ')
else:
    print("Obrigado por usar nosso sistema.") 
