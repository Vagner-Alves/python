'''
um uso mais interessante das properties em python.
'''

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual  - self._ano_nascimento
    

pessoa = Pessoa("Vagner alves", 1997)
print(f"Nome: {pessoa.__delattr__nome} \tIdade: {pessoa.idade}")
    

    