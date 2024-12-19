'''
Método construtor
sempre é executado quando uma nova instancia da classe é criada. Nesse método, inicializamos
o estado do nosso objeto. Para declarar o método construtor da classe, criamos um método com o nome
__init__
'''

class Impressora():
    def __init__(self, modelo, marca, conectividade):
        self.modelo = modelo
        self.marca = marca
        self.conectividade = conectividade


# init é o método construtor da classe Impressora e nele são definidos os atributos da classe

impressora = Impressora("HP 581", "HP", "WIFI- USB")
print(impressora)