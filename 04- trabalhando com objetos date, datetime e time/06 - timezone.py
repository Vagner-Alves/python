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


print("America do Sul ")
print(f"Recife:  {south_america_recife}")
print(f"Noronha: {south_america_noronha}")
print(f"Maceio: {south_america_maceio}" )
print(f"Mexico: {south_america_mexico} ")
print(f"Santo Domingo: {south_america_santo_domingo} ")
print("\n")

print("Europa")
print(f"Athenas: {europe_athens}")
print(f"Lisboa: {europe_lisbon}")
print(f"Madrid: {europe_madrid}")
print(f"Paris: {europe_paris}")
print(f"Rome: {europe_rome}")
print("\n")

print("America do Norte")
print(f"Vancouver: {north_america_vancouver}")
print(f"Montreal: {north_america_montreal}")
print(f"Nova York: {north_america_new_york}")
print("\n")

print("Africa")
print(f"Abidjan: {africa_abidjan}")
print(f"Cairo: {africa_cairo}")
print(f"Dakar: {africa_dakar}")
print(f"Luanda: {africa_luanda}")
print("\n")

print("Asia")
print(f"Jakarta: {asia_jakarta}")
print(f"Tokyo: {asia_tokyo}")
print(f"Singapura: {asia_singapore}")
print("\n")

print("Oceania")
print(f"West: {oceania_west}")
print(f"Honolulu: {oceania_honolulu}")
print(f"Tahiti: {oceania_tahiti}")
print("\n")

print("Antartica")
print(f"Polo Sul: {antarctica_south_pole}")