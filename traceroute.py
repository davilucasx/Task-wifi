import subprocess

def traceroute():

    quant = 0

    res = subprocess.run(
        ["traceroute", "ip"],
        capture_output=True,
        text=True
    )

    for linha in res.stdout.splitlines():

        linha = linha.strip()

        if linha and linha[0].isdigit():
            quant += 1

    return quant


