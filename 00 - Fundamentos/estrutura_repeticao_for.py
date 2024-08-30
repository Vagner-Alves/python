'''
laço for
Faz sentido usar o for quando sabemos o número exato de vezes que nosso bloco de código deve
ser executado, ou quando queremos percorrer um objeto iteravél.
'''

texto = str(input("Digite qualquer texto: "))
VOGAIS = 'AEIOU'

for letras in texto:
    if letras.upper() in VOGAIS:
        print(letras, end=" ")

else:
    print()


