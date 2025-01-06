from abc import ABC, abstractmethod, property

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    def desligar(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")

    def desligar(self):
        print("Desligando a TV")
    
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        pass

    def desligar(self):
        pass
    

