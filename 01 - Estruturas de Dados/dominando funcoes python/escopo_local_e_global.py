'''
python trabalha com escopo local e global, dentro do bloco da função o escopo é local.
Portanto alterações ali feitas em objetos imutáveis serão perdidas quando o método terminar
de ser executado. Para usar objetos globais utilizamos a palavra-chave global, que informa
ao interpretador que a variável que está sendo manipulada no escopo local é global.
essa NÃO É UMA BOA PRATICA E DEVE SER EVITADA.
'''

salario = 1880

def bonus_salario(valor, lista):
    global salario              # sem essa palavra-chave a funçõa não vai funcionar
    
    lista_auxiliar = lista.copy()
    lista_auxiliar.append(2)
    print(f"lista auxiliar = {lista_auxiliar}")
    salario += valor
    return salario

lista = [1]
salario_com_bonus = bonus_salario(100, lista)
print(salario_com_bonus)
print(lista)
