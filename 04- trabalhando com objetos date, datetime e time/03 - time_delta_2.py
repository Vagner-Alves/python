import datetime

# criar data e hora
d = datetime.datetime(2025, 7, 19, 13, 45)
print(d)

# adicionando uma semana
d = d + datetime.timedelta(weeks=1)
print(d)