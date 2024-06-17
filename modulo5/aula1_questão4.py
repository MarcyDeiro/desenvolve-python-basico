from datetime import datetime

data_hora_atual = datetime.now()

data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")

print("Data e hora atuais:", data_hora_formatada)