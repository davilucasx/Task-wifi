import json
from datetime import datetime

def salvar(dados):
    with open("dados.jsonl", "a+") as arquivo:
        json.dump(dados, arquivo)
        arquivo.write("\n")