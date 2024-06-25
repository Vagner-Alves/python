'''
VARIAVEIS
    Em linguagens de programação podemos definir valores que podem sofrer alterações no decorrer
    da execução de um programa. Esses valores recebem o nome de variáveis , pois são criadas com 
    uma valor e não necessariamente deve permanecer o mesmo, ou seja, o valor é mutável.

CONSTANTES
    Assim como as variáveis, utilizamos constantes para armazenar valores, a diferença é que uma constante
    não irá sofrer alterações durante a execução do programa, ou seja, o valor é imutável.

    O PYTHON NÃO TEM CONSTANTES!!!!
    Não existe uma palavra reservada para informar ao interpretador que o valor é constante. Em algumas linguagens
    como Java e JavaScript utilizamos final e const respectivamente para declarar que o valor é constante.

    Em python usamos a convenção que diz ao programador que a variável é uma constante. Para fazer isso basta criar a variável
    com o nome escrito em letras maiúsculas.

'''

# exemplo de variável
nome, idade = ('vagner',18)
print(f'Meu nome é {nome} e tenho {idade} ano(s)')

# nome e idade podem ser mutáveis em um programa.
nome, idade = ('vagner alves',27)
print(f'Meu nome é {nome} e tenho {idade} ano(s)')

# exemplos válidos de constantes
CAMINHO_PASTA = '/home/documents/meucurso_python'
DEBUG = True
ESTADOS_DO_BRASIL = 'PE','SP','RJ'


