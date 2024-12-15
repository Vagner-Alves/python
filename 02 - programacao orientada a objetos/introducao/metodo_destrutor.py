'''
Método Destrutor
o método destrutor sempre é executado quando uma instancia
 (objeto) é destruída. Destrutores em python não são tão necessários quanto em C++
 porque o python tem um coletor de lixo que lida com o gerenciamento de memória automaticamente.
 Para declarar o método destrutor da classe, criamos um método com o nome __del__
'''

class Impressora():
    def __init__(self, modelo, marca, conectividade):
        self.modelo = modelo
        self.marca = marca
        self.conectividade = conectividade
    
    def __del__(self):
        print("instancia", self.__class__.__name__, "deletada")

impressora = Impressora("HP 581", "HP", "WIFI- USB")
impressora.__del__()
        