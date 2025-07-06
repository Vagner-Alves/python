from datetime import date, datetime, time
data = date(2025,4,18)
print(data)
print(data.today())

data_hora = datetime(2018,6,22)
print(data_hora)
print(data_hora.today())

# hora atual usando a função datetime
hora = datetime.now()
print(hora)