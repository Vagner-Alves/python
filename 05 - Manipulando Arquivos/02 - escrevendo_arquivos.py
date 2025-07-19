'''
Podemos usar write() e ou writeline() para escrever em um arquivo. Lembre-se, no entanto, de abrir
o arquivo no modo correto.
'''

file = open('escrita.txt', 'w')
file.write("escrevendo com python")
file.close()

# lendo o contéudo do arquivo
read_file = open('escrita.txt', 'r')
print(read_file.readlines())