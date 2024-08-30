'''
BREAK E CONTINUE
Break é utilizado para "quebrar" ou parar a execução de um laço de repetição ( for / while ).
Continue é uma variação da palavra reservada acima, e é utilizado para "pular" uma condição dentro de um laço de repetição.

'''

opcao = -1

while opcao != 0:

    opcao = int(input("[ 1 ] Sacar \n[ 2 ] Extrato \n[ 0 ] Sair."))

    if opcao == 0:
        print("Obrigado por usar o sistema")
        break
        

    elif opcao == 1:
        print("Saque realizado com sucesso. ")
    
    elif opcao == 2:
        print("Tire o extrato na boca do caixa.")


for numero in range(50):
    if numero == 40:
        break
    
    #print(numero, end=" ")


# executar números de 1 a 30, excluindo (pulando) o número 12.

for numeros in range(30):

    if numeros == 12:
        continue

    print(numeros, end=" ")