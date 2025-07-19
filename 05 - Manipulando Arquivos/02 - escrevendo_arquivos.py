'''
Podemos usar write() e ou writeline() para escrever em um arquivo. Lembre-se, no entanto, de abrir
o arquivo no modo correto.
'''

file = open('escrita.txt', 'w')
file.write("escrevendo com python") # é possível passar uma string
file.close()

file_2 = open('escrita.txt','w')
file_2.writelines(["escrevendo ", "textos ", " com python!"]) # é possível usar um iteravél ( lista ou tuplas )
file_2.close()
# lendo o contéudo do arquivo
read_file = open('escrita.txt', 'r')
print(read_file.readlines())