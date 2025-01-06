'''
VARIAVEIS DE OBJETO

Todos os objetos nascem com o mesmo número de atributos de classe
e de instancia. Atributos de instancia são diferentes para cada objeto
( cada objeto tem uma cópia), já os atributos de classe
são compartilhados entre os objetos.
'''

class Estudante:
    escola = "IFPE"

    def __init__(self, nome, numero):
        self.nome =  nome
        self.numero = numero
    
    def __str__():
        return f"nome: {self.nome}  numero: {self.numero}"

vagner = Estudante("Vagner", "20222ADS-PM0202")