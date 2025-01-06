'''
VARIAVEIS DE OBJETO

Todos os objetos nascem com o mesmo número de atributos de classe
e de instancia. Atributos de instancia são diferentes para cada objeto
( cada objeto tem uma cópia), já os atributos de classe
são compartilhados entre os objetos.
'''

class Estudante:
    escola = "IFPE"

    def __init__(self, nome, numero_matricula):
        self.nome =  nome
        self.numero_matricula = numero_matricula
    
    def __str__(self):
        return f"nome: {self.nome}  numero: {self.numero_matricula} - {self.escola}"


def mostrar_objetos(*objetos):
    for objs in objetos:
        print(objs)

aluno = Estudante("Vagner", "20222ADS-PM0202")
aluno2 = Estudante("larissa", "20222ADS-PM0303")

mostrar_objetos(aluno, aluno2)

Estudante.escola = "Instituto  Federal de Pernambuco"

aluno3 = Estudante("Outro aluno", "20222ADS-PM0404")
mostrar_objetos(aluno, aluno2, aluno3)