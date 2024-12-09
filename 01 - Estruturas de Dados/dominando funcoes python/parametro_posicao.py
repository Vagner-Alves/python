'''
por padrão, argumentos podem ser passados para uma função python
tanto por posição quanto expplicitamente pelo nome.
Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira
pelo qual argumentos possam ser passados, assim um desenvolvedor
precisa apenas olhar para a definição da função para determinar
se os itens são passados por posição, por posição e nome, ou por nome.
'''
# é util caso queira mudar o nome do parametro depois ( antes da barra)
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca,motor, combustivel)

criar_carro("Palio azul", 1997, "123-AB", marca="fiat", motor="V8", combustivel="alcool") # forma correta
