'''
PROPERTIES

PARA QUE SERVEM?
Com o property() do python, voce pode criar atributos gerenciados em suas classes.
Voce pode usar atributos gerenciados , também conhecidos como properties ( propriedades )
, quando precisar modificar sua implementação interna sem alterar a API pública da classe.
'''

class Foo:
    def __init__(self, x=None):
        self._x = x
    
    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        _x = self._x or 0
        _value = value or 0
        self._x = _x + _value
    
    @x.deleter
    def x(self):
        self._x = -1

foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x) 

