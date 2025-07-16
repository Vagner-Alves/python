from datetime import datetime, timedelta

tipo_carro = "M"

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60

data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(days = tempo_pequeno)
    print(f"O carro chegou em: {data_atual} e ficara pronto em {data_estimada}")

elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(days=tempo_medio)
    print(f"O carro chegou em: {data_atual} e ficara pronto em {data_estimada}")
else:
    data_estimada = data_atual + timedelta(days=tempo_grande)
    print(f"O carro chegou em: {data_atual} e ficara pronto em {data_estimada}")