'''
A palavra polimorfismo significa ter muitas formas. Na progrmação,
polimorfismo significa o mesmo nome da função, mas assinaturas diferentes
sendo usado para tipos diferentes.

MESMO MÉTODO COM COMPORTAMENTO DIFERENTE

na herança, a classe filha herda os métodos da classe pai. No entanto,
é possível modificar um método em uma classe filha herdada da
classe pai. Isso é particurlamente útil nos casos em que o método herdado
da classe pai não se encaixa perfeitamente na classe filha.
'''

class Passaro:
    def __init__(self):
        pass

    def voar(self):
        print("voando")

class Pardal(Passaro):
    def voar(self):
        return super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("avestruz não consegue voar...")

