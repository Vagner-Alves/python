'''
OQUE SÃO ESTRUTURAS DE REPETIÇÃO ?

são estruturas utilizadas para repetir um trecho de código, um determinado número de vezes. Esse número pode ser conhecido
previamente ou determinado através de uma expressão lógica.
'''

'''
laço for
Faz sentido usar o for quando sabemos o número exato de vezes que nosso bloco de código deve
ser executado, ou quando queremos percorrer um objeto iteravél.
'''

VOGAIS = "AEIOU"
texto = str(input("Digite qualquer palavra ou texto: "))

for letras in texto:
    if letras.upper() in VOGAIS:
        print(letras, end=" ")

else:
    print()
    print("Executa no Final do Laço")


