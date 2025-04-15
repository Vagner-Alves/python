class Galaxia:
    def __init__(self, planetas):
        self.planetas = planetas
        self.indice = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.indice < len(self.planetas):
            planeta = self.planetas[self.indice]
            self.indice += 1
            return planeta
        else:
            raise StopIteration

planetas = ["Mercurio","Venus","Terra","Marte","Júpiter","Saturno","Netuno","Urano"]

galaxia = Galaxia(planetas)

for planeta in galaxia:
    print(f"Visitando o planeta {planeta}...")