'''
quando trabalhamos com data e hora, lidar com fusos horários é uma necessidade comum. Python facilita isso através do módulo pytz.
'''
from datetime import datetime
import pytz

# America do Sul
south_america_recife = datetime.now(pytz.timezone("America/Recife"))
south_america_noronha = datetime.now(pytz.timezone("America/Noronha"))
south_america_mexico = datetime.now(pytz.timezone("America/Mexico_City"))
south_america_maceio = datetime.now(pytz.timezone("America/Maceio"))
south_america_santo_domingo = datetime.now(pytz.timezone("America/Santo_Domingo"))

# Europa
europe_paris = datetime.now(pytz.timezone("Europe/Paris"))
europe_madrid = datetime.now(pytz.timezone("Europe/Madrid"))
europe_rome = datetime.now(pytz.timezone("Europe/Rome"))
europe_athens = datetime.now(pytz.timezone("Europe/Athens"))
europe_lisbon = datetime.now(pytz.timezone("Europe/Lisbon"))

# America do Norte
north_america_vancouver = datetime.now(pytz.timezone("America/Vancouver"))
north_america_montreal = datetime.now(pytz.timezone("America/Montreal"))
north_america_new_york = datetime.now(pytz.timezone("America/New_York"))

# Africa
africa_abidjan = datetime.now(pytz.timezone("Africa/Abidjan"))
africa_cairo =  datetime.now(pytz.timezone("Africa/Cairo"))
africa_dakar = datetime.now(pytz.timezone("Africa/Dakar"))
africa_luanda = datetime.now(pytz.timezone("Africa/Luanda"))

# Asia
asia_jakarta = datetime.now(pytz.timezone("Asia/Jakarta"))
asia_tokyo = datetime.now(pytz.timezone("Asia/Tokyo"))
asia_singapore = datetime.now(pytz.timezone("Asia/Singapore"))

# Oceania
oceania_west = datetime.now(pytz.timezone("Australia/West"))
oceania_honolulu = datetime.now(pytz.timezone("Pacific/Honolulu"))
oceania_tahiti = datetime.now(pytz.timezone("Pacific/Tahiti"))

# Antartica
antarctica_south_pole = datetime.now(pytz.timezone("Antarctica/South_Pole"))


print(fuso_horario_europa)
print(fuso_horario_sao_paulo)

