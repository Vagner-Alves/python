'''
NA MATEMÁTICA

a seguinte ordem de operações é a correta:
* Parentesis
* Expoentes
* Multiplicação e Divisão ( da esquerda para a direita)
* Soma e Subtração (da esquerda para  a direita)

O python obedece a ordem de operações

'''

numero_1 = 8
numero_2 = 20

print(numero_1  +  numero_2) # adição
print(numero_1  -  numero_2) # subtração
print(numero_1  *  numero_2) # multiplicação
print(numero_1  /  numero_2) # divisão
print(numero_1  // numero_2) # divisão inteira
print(numero_1  %  numero_2) # Módulo
print(numero_1  ** numero_2) # exponenciação


# qual o valor de X , 10 ou 0 ?

X = 10 - 5 * 2
print(X) # zero

# utilizando a ordem de operação podemos mudar o resultado da equação
X = ( 10 - 5 ) * 2
print(X) # dez
