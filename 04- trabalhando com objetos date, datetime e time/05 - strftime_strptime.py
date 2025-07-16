'''
O python também permite converter e formatar datas e horas.
STRFTIME - String format time
STRPTIME - String parse time
'''
import datetime

# capturar o momento ( data ) presente
data_hora_atual = datetime.datetime.now()
print(data_hora_atual)
'''
por padrão as datas são exibidas no formato americano: ano , mes e dia (%Y/%m/%d).
é necessário formatar para usar o padrão brasileiro, ai que utilizamos a função strftime!
'''
mascara_ptbr = "%d/%m/%Y"
print(data_hora_atual.strftime(mascara_ptbr))

# objeto do tipo string ( data )
data_hora_formatada = "2025-10-20 8:18"
mascara_eng = "%Y-%m-%d %H:%M"

'''para evitar o erro
AttributeError: module 'datetime' has no attribute 'strptime

'''
from datetime import datetime
data_convertida = datetime.strptime(data_hora_formatada, mascara_eng)
print(data_convertida)