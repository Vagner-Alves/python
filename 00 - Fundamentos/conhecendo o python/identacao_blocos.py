'''
Identar código é uma forma de manter o código fonte mais legível e manutenível. Mas em python ela exerce um
segundo papel, através da identação o interpretador do python consegue determinar onde um bloco inicia e termina.
'''

def sacar( valor: float):
    saldo = 1800

    if (saldo >= valor):
        print(f" R${valor} sacado.")
        print(f" R${saldo - valor} disponível")

    print('Obrigado volte sempre')
#fim do bloco    

def depositar(valor:float):
    saldo = 1800
    saldo += valor


sacar(200)