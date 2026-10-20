# 🌐 Monitoramento de Rede com Python

<p align="center">
  Um projeto de monitoramento de rede em Linux utilizando Python para coletar métricas de latência, rota e tráfego de dados.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/OS-Linux-orange?logo=linux&logoColor=white" alt="Linux">
  <img src="https://img.shields.io/badge/Data-JSONL-green" alt="JSONL">
  <img src="https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow" alt="Em desenvolvimento">
</p>

---

## 📌 Sobre o projeto

Este projeto tem como objetivo monitorar aspectos básicos de uma conexão de rede por meio de um script desenvolvido em Python.

A aplicação executa comandos do Linux, consulta estatísticas da interface de rede e registra os resultados em um arquivo JSONL, permitindo armazenar os dados para análises posteriores.

O projeto também serve como prática de programação em Python, utilização do terminal Linux e controle de versão com Git.

## ⚙️ Funcionalidades

| Funcionalidade | Descrição |
|:--|:--|
| 📡 Latência | Mede a latência média utilizando `ping`. |
| 🛣️ Traceroute | Contabiliza os saltos encontrados pelo comando `traceroute`. |
| 📥 Tráfego recebido | Mede a variação dos bytes recebidos pela interface. |
| 📤 Tráfego transmitido | Mede a variação dos bytes transmitidos pela interface. |
| 🕒 Registro temporal | Registra a data e a hora de cada coleta. |
| 💾 Armazenamento | Salva os resultados em formato JSONL. |
| 🔢 Identificação | Atribui um ID sequencial para cada registro. |

## 🧰 Tecnologias utilizadas

- **Python 3** — lógica de coleta, processamento e armazenamento dos dados.
- **Linux** — sistema operacional e fonte das estatísticas de rede.
- **Git e GitHub** — controle de versão e hospedagem do código.
- **JSON Lines (JSONL)** — armazenamento dos registros.
- **ping e traceroute** — ferramentas para diagnóstico de rede.

## 📂 Estrutura do projeto

```text
monitoramento-rede/
├── main.py
├── atraso.py
├── traceroute.py
├── vazao.py
├── salvarJson.py
├── dados.jsonl
└── README.md
```

> A estrutura acima representa a organização esperada com base nos módulos enviados. Ajuste os nomes caso estejam diferentes no seu repositório.

## 🚀 Como executar

### 1. Pré-requisitos

- Linux com Python 3 instalado.
- Ferramentas `ping` e `traceroute`.
- Interface de rede ativa e configurada.

Em sistemas Ubuntu ou Debian, instale as ferramentas necessárias:

```bash
sudo apt update
sudo apt install iputils-ping traceroute
```

### 2. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Acesse a pasta do projeto:

```bash
cd NOME_DO_PROJETO
```

### 3. Execute o programa

```bash
python3 main.py
```

O programa iniciará as coletas automaticamente e exibirá os resultados no terminal. Para interromper a execução, pressione `Ctrl + C`.

> **Importante:** o código atual espera encontrar o arquivo `dados.jsonl` ao iniciar. Caso ele ainda não exista, crie um arquivo vazio com `touch dados.jsonl` antes de executar o programa.

## 📊 Dados coletados

Cada coleta é armazenada como um objeto JSON independente, contendo informações como:

| Campo | Significado |
|:--|:--|
| `ID` | Identificador sequencial do registro. |
| `Interface` | Interface monitorada, atualmente `wlp3s0`. |
| `Timestamp` | Data e hora da coleta. |
| `Latencia` | Latência média em milissegundos. |
| `Traceroute` | Quantidade de saltos contabilizados. |
| `Dados_recebidos` | Diferença de bytes recebidos durante a medição. |
| `Dados_transmitidos` | Diferença de bytes transmitidos durante a medição. |

### Exemplo de registro JSONL

```json
{
  "ID": 1,
  "Interface": "wlp3s0",
  "Timestamp": "2026-10-20T10:30:00",
  "Latencia": 1.25,
  "Traceroute": 1,
  "Dados_recebidos": 2048,
  "Dados_transmitidos": 1024
}
```

*Os valores são ilustrativos. Cada registro real é salvo em uma única linha do arquivo.*

## 🔄 Funcionamento

1. O programa inicia a coleta de informações.
2. Executa o `ping` para obter a latência média até o destino configurado.
3. Executa o `traceroute` e contabiliza os saltos encontrados.
4. Consulta os contadores de tráfego da interface de rede.
5. Organiza os resultados em um objeto Python.
6. Salva os dados no arquivo `dados.jsonl`.
7. Aguarda aproximadamente 30 segundos antes de iniciar a próxima coleta, além do tempo gasto nas operações.

## 🎯 Objetivos de aprendizagem

- Praticar funções, módulos e manipulação de arquivos em Python.
- Executar comandos do sistema operacional utilizando `subprocess`.
- Consultar estatísticas de rede disponíveis no Linux.
- Trabalhar com dados estruturados em JSON.
- Utilizar Git para versionar o desenvolvimento do projeto.

## 🔮 Melhorias futuras

- [ ] Permitir configurar o endereço IP de destino.
- [ ] Permitir selecionar a interface de rede.
- [ ] Melhorar o tratamento de falhas e erros.
- [ ] Gerar gráficos de latência e tráfego.
- [ ] Criar relatórios a partir dos dados coletados.

---

<p align="center">
  Desenvolvido como projeto de estudo de Python, Linux e redes de computadores.
</p>