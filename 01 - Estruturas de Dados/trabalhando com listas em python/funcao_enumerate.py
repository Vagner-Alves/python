'''
ENUMERATE

as vezes é necessário saber qual é o índice do objeto dentro do laço for.
Para isso podemos usar a funçõa enumerate. 
'''

carros = ["GOl","CELTA", "KWID ( carro descartável )"]

for indice, carro in enumerate(carros):
    print(f"{indice} -  {carro}")