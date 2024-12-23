'''
Em linguagens como java e C++, existem palavras reservadas para definir
o nível de acesso aos atributos e métodos da classe. Em python não
temos palavras reservadas, porém usamos convenções no nome do recurso, para
definir se a variável é pública ou privada.

Público: Pode ser acessado de fora da classe.
Privado: Só pode ser acessado pela classe.

todos os recursos são públicos, a menos que o nome inicie com underline.
Ou seja, o interpretador python não irá garantir a proteção do recurso, mas por ser uma convenção
amplamente adotada na comunidade, quando encontramos uma variável e/ou método com nome iniciado por underline
, sabemos que não deveríamos manipular o seu valor diretamente, ou invocar método fora do escopo da classe.
'''

class Conta:
    def __init__(self, numero_agencia, saldo=0):
        self._saldo = saldo
        self.numero_agencia = numero_agencia
    
    def depositar(self, valor):
        # faz de conta que está implementado

        self._saldo += valor
    
    def sacar(self, valor):
        # mesma coisa

        self._saldo -= valor
    
    def mostrar_saldo(self):
        return self._saldo

conta = Conta("1234", 100)
conta.depositar(20)
print(conta.mostrar_saldo())



