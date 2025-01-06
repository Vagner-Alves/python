from abc import ABC, abstractclassmethod, abstractproperty

class ControleRemoto(ABC):
    
    def ligar(self):
        pass
    def desligar(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        pass

    def desligar(self):
        return
    
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        pass
    
    def desligar(self):
        pass
    

