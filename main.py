import json
from atraso import atraso
from traceroute import traceroute
from vazao import medirVazao
from salvarJson import salvar 
from datetime import datetime
import time

id_coleta = 1

with open("dados.jsonl", "r") as arquivo:
    for line in arquivo:
        data = json.loads(line)
        id_coleta = max(id_coleta, data["ID"] + 1)

while True:
    latencia = atraso()
    hops = traceroute()
    dadosrecebidos, dadosTransmitidos = medirVazao()

    dados = {
        "ID": id_coleta,
        "Interface": "wlp3s0",
        "Timestamp": datetime.now().isoformat(),
        "Latencia": latencia,
        "Traceroute": hops,
        "Dados_recebidos": dadosrecebidos,
        "Dados_transmitidos": dadosTransmitidos 
    }

    salvar(dados)
    id_coleta += 1

    print("\n--- Coleta dos dados ---")
    print("Latência:", latencia, "ms")
    print("Quantidade de hops:", hops)
    print("Recebidos:", dadosrecebidos, "bytes/s")
    print("Transmitidos:", dadosTransmitidos, "bytes/s")
    
    time.sleep(30)