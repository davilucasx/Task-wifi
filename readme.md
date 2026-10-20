# 🌐 Monitoramento de Rede com Python

<p align="center">
  Script em Python para coleta periódica de métricas de rede em sistemas Linux.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Linux-orange?logo=linux&logoColor=white" alt="Linux">
  <img src="https://img.shields.io/badge/Storage-JSONL-green" alt="JSONL">
  <img src="https://img.shields.io/badge/Status-%20Concluído-green" alt="Status">
</p>

---

## 📌 Sobre o projeto

Este projeto consiste em um script de monitoramento de rede desenvolvido em Python, utilizando ferramentas do Linux para coletar informações sobre latência, rota e tráfego de dados.

As informações são organizadas e armazenadas localmente em um arquivo JSONL, permitindo consultar os registros posteriormente e utilizá-los em análises.

O projeto foi desenvolvido com o objetivo de praticar Python, comandos Linux, manipulação de arquivos e controle de versão com Git.

## ⚙️ Funcionalidades

- 📡 **Monitoramento de latência:** utiliza `ping` para obter a latência média até o gateway configurado.
- 🛣️ **Contagem de saltos:** utiliza `traceroute` para contabilizar os saltos encontrados até o destino.
- 📥 **Tráfego recebido:** calcula a diferença entre duas leituras dos bytes recebidos pela interface de rede.
- 📤 **Tráfego transmitido:** calcula a diferença entre duas leituras dos bytes transmitidos.
- 🕒 **Registro temporal:** registra a data e a hora de cada coleta.
- 🔢 **Identificação das coletas:** atribui um ID sequencial aos registros.
- 💾 **Armazenamento local:** salva os resultados em um arquivo JSONL.

## 🧰 Tecnologias utilizadas

- **Python 3** — implementação da lógica de coleta e armazenamento.
- **Linux** — acesso às ferramentas e estatísticas de rede do sistema.
- **Git e GitHub** — controle de versão e hospedagem do código.
- **JSON Lines (JSONL)** — formato de armazenamento dos dados.
- **ping e traceroute** — ferramentas de diagnóstico de rede.

## 📂 Estrutura do projeto

```text
monitoramento-rede/
├── main.py
├── atraso.py
├── traceroute.py
├── vazao.py
├── salvarJson.py
├── dados.jsonl
├── .gitignore
└── README.md
```

## 📋 Pré-requisitos

Antes de executar o projeto, verifique se você possui:

- Linux instalado.
- Python 3.
- Git.
- As ferramentas `ping` e `traceroute`.
- Uma interface de rede ativa.

Em distribuições baseadas em Ubuntu ou Debian, instale as ferramentas de rede com:

```bash
sudo apt update
sudo apt install iputils-ping traceroute
```

## 🚀 Instalação e execução

### 1. Clone o repositório

Substitua `URL_DO_REPOSITORIO` pelo endereço real do repositório no GitHub.

```bash
git clone URL_DO_REPOSITORIO
cd NOME_DO_PROJETO
```

### 2. Crie o ambiente virtual

```bash
python3 -m venv .venv
```

Ative o ambiente virtual:

```bash
source .venv/bin/activate
```

### 3. Crie o arquivo de dados

O arquivo `dados.jsonl` é utilizado para armazenar os registros das coletas e não precisa ser enviado ao GitHub.

Como o programa tenta abrir esse arquivo durante a inicialização, crie-o manualmente antes de executar o script:

```bash
touch dados.jsonl
```

O arquivo pode permanecer vazio. Durante a execução, os novos registros serão acrescentados a ele.

### 4. Execute o programa

```bash
python3 main.py
```

O script iniciará as coletas e exibirá os resultados no terminal. Para interromper a execução, pressione `Ctrl + C`.


## 📊 Dados coletados

Cada registro contém os seguintes campos:

| Campo | Descrição |
|---|---|
| `ID` | Identificador sequencial da coleta. |
| `Interface` | Interface de rede monitorada. |
| `Timestamp` | Data e hora da coleta. |
| `Latencia` | Latência média obtida pelo `ping`, em milissegundos. |
| `Traceroute` | Quantidade de saltos contabilizados pelo programa. |
| `Dados_recebidos` | Diferença de bytes recebidos durante a medição. |
| `Dados_transmitidos` | Diferença de bytes transmitidos durante a medição. |

### Exemplo de registro

```json
{"ID":1,"Interface":"wlp3s0","Timestamp":"2026-10-20T10:30:00","Latencia":1.25,"Traceroute":1,"Dados_recebidos":2048,"Dados_transmitidos":1024}
```

*Os valores são fictícios e servem apenas para demonstrar a estrutura de um registro.*

## 🔄 Como funciona

1. O programa verifica os registros anteriores para determinar o próximo ID.
2. Executa o `ping` para coletar a latência média.
3. Executa o `traceroute` para contabilizar os saltos encontrados.
4. Consulta as estatísticas de tráfego da interface de rede.
5. Organiza as informações em um objeto Python.
6. Registra os dados no arquivo `dados.jsonl`.
7. Aguarda 30 segundos antes de iniciar o próximo ciclo, além do tempo gasto nas operações.

## 🎯 Objetivos de aprendizagem

- Praticar funções, módulos e manipulação de arquivos em Python.
- Executar comandos do sistema operacional com `subprocess`.
- Consultar estatísticas de interfaces de rede no Linux.
- Trabalhar com dados estruturados em JSON.
- Utilizar Git e GitHub para versionar um projeto.

---

<p align="center">
  Desenvolvido como projeto de estudo de Python, Linux e git.
</p>
