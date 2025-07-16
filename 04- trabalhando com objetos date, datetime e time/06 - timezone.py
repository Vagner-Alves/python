'''
quando trabalhamos com data e hora, lidar com fusos horários é uma necessidade comum. Python facilita isso através do módulo pytz.
'''
from datetime import datetime
import pytz

# America do Sul
south_america_recife = datetime.now(pytz.timezone("America/Recife"))
south_america_sao_paulo = datetime.now(pytz.timezone("America/Sao_paulo"))
south_america_noronha = datetime.now(pytz.timezone("America/Noronha"))
# Europa
fuso_horario_europa = datetime.now(pytz.timezone("Europe/Oslo"))

# America do Norte
north_america_vancouver = datetime.now(pytz.timezone("America/Vancouver"))
north_america_montreal = datetime.now(pytz.timezone("America/Montreal"))
north_america_new_york = datetime.now(pytz.timezone("America/New_York"))
# Africa

# Asia

# Oceania

# Antartica



print(fuso_horario_europa)
print(fuso_horario_sao_paulo)

