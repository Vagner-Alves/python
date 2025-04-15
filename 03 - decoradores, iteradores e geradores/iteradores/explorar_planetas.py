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
