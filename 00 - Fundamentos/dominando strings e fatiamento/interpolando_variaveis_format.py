NOME = "Vagner Alves"
IDADE = 27
PROFISSAO = "DevOps"
CURSO = "analise e desenvolvimento de sistemas"
DADOS = {"nome":"Vagner alves", "idade":27, "profissao":"DevOps","curso":"ciencia da computação"}

MENSAGEM    =  "Olá, meu nome é {} , tenho {} anos , minha profissão é {} e estou cursando {}"
MENSAGEM_2  =  "Olá, meu nome é {0} , tenho {1} anos , minha profissão é {2} e estou cursando {3}"
MENSAGEM_3  =  "Olá, meu nome é {valor1} , tenho {valor2} anos , minha profissão é {valor3} e estou cursando {valor4}"
MENSAGEM_4  =  "Olá, meu nome é {nome} , tenho {idade} anos , minha profissão é {profissao} e estou cursando {curso}"

print(MENSAGEM.format(NOME, IDADE, PROFISSAO, CURSO))

print(" ")

print(MENSAGEM_2.format(NOME, IDADE, PROFISSAO, CURSO))

print(" ")

print(MENSAGEM_3.format(valor1 = NOME, valor2=IDADE, valor3=PROFISSAO, valor4=CURSO))

print(" ")

print(MENSAGEM_4.format(**DADOS))