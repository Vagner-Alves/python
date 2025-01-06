from abc import ABC, abstractmethod

class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractmethod
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
        print("ligada.")

    def desligar(self):
        print("Desligando a TV")
        print("desligada")
    
    @property
    def marca(self):
        return "controle LG"
    
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("ligando ar condicionado")
        print("ligado")
    
    def desligar(self):
        return super().desligar()
    
    @property
    def marca(self):
        return "ar condicionado LG"

    

televisao = ControleTV()
televisao.ligar()

ar_condicionado = ControleArCondicionado()
ar_condicionado.ligar()

print(ar_condicionado.marca)