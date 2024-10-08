'''
METÓDOS UTEIS DA CLASSE STRING

A classe string do python é famosa por ser rica em metódos e possuir uma interface muito fácil de se trabalhar.

Em algumas linguagens manipular sequencias de caracteres não é um trabalho trivial, porém, em python esse trabalho é muito simples.
'''

NOME_CURSO = "python"
CURSO = "   python     "

print(' ')
print( 'Maiuscula, minuscula e Titulo' )

print(NOME_CURSO.upper())                # Transforma os caracteres em maiusculos

print(NOME_CURSO.lower())                # Transforma os caracteres em minusculos

print(NOME_CURSO.title())                # Transforma a string em um titulo ( apenas primeira letra maiuscula )


print(' ')
print( 'Eliminando espaços em branco' )
print(CURSO)
print(CURSO.lstrip())                # elimina os espaços em branco a esquerda
print(CURSO.rstrip())                # elimina os espaços em branco a direita
print(CURSO.strip())                 # elimina os espaços em ambos os lados

print(' ')
print( 'Junções e centralizações' )

print(CURSO.center(10, "#"))
print("+".join(CURSO))