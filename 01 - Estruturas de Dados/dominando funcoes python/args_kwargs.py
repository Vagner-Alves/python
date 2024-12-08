'''
podemos combinar parametros obrigatórios com args e kwargs. Quando esses
são definidos ( *args, *kwargs) , o método recebe os valores como tupla e dicionário
respectivamente.
é bom observar o seguinte, os nomes args e kwargs pouco importam, na verdade voce pode
usar oque quiser , o python vai se atentar aos simbolos * e **
'''

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("o ano de 2024", "foi belo e cheio de conquistas", autor="Vagner Alves", ano=2024)