import subprocess # Permite que o python execute comandos do So como se estivesse no terminal
import re # expressoes regulares, procura padroes no texto

def atraso():
    # executa o comando ping do linux para pegar 10 valores
    res = subprocess.run(
    ["ping", "-c", "10", "192.168.20.1"], 
    capture_output=True,
    text=True
    )

    # Verifica se o comando foi executado, se for = 0 sucesso, diferente é erro
    if res.returncode != 0:
        return None

    # Vai procurar a saída do print, com infos de media,max e min...
    match = re.search(
        r'=\s*([\d.]+)/([\d.]+)/([\d.]+)/([\d.]+)',
        res.stdout
    )

    # Ele vai buscar o a segunda parte da saída que seria a média
    if match:
        return float(match.group(2))
    return None

