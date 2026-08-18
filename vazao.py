import time

# Wlp3s0 é a interface de rede wifi

# Essa função abre o arquivo onde o linux guarda as estatisticas das interfaces de rede
def lerDados(interface = "wlp3s0"):
    with open("/proc/net/dev", "r") as arquivo:
        for linha in arquivo: # percore o arquivo ate achar a interface 'wlp3s0'
            if interface in linha: # se ele achar segue o if
                dados = linha.split() # Faz com que cada informação tenha uma posição
                recebidos = int(dados[1]) # bytes recebidos rx são dados recebidos
                transmitidos = int(dados[9]) # bytes transmitidos tx sao dados transmitidos
    return recebidos, transmitidos

def medirVazao(interface="wlp3s0"):

    # Primeira leitura dos bytes
    dadosRecebidos1, dadosTransmitidos1 = lerDados(interface)

    # Espera 1 segundo
    time.sleep(1)

    # Segunda leitura dos bytes
    dadosRecebidos2, dadosTransmitidos2 = lerDados(interface)

    # Calcula quantos bytes foram recebidos durante o intervalo
    recebidos = dadosRecebidos2 - dadosRecebidos1

    # Calcula quantos bytes foram transmitidos durante o intervalo
    transmitidos = dadosTransmitidos2 - dadosTransmitidos1

    return recebidos, transmitidos


