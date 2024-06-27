'''
    FUNÇÃO INPUT
    essa função built in input é utilizada para ler dados da entrada padrão (teclado).
    Ela recebe (padrão) um argumento do tipo string. que é exibido para o usuário na
    saída padrão (tela do computador).
'''

teclado = input("Digite qualquer coisa: ")

# ler outros tipos de dados
numero_inteiro = int(input("Digite qualquer número  inteiro: "))
numero_racional = float(input("Digite qualquer número racional: "))

'''
    FUNÇÃO PRINT 

    essa função built in é utilizada quando queremos exibir dados na saída padrão (Tela do Computador).
    Ela recebe um argumento obrigátorio e 4 opcionais, tipo varargs de objetos e sep, end, file e flush
    respectivamente. Todos os Objetos são convertidos para String, separados por sep e terminados por end.
    A string final é exibida na tela para o usuário.
'''