# Pipeline de Dados - Rotatividade de Kits

## 📌 Descrição
Este projeto apresenta o desenvolvimento de um pipeline de dados completo (ETL) utilizando Python, com foco em automação, padronização e disponibilização de dados para análise em Power BI.

---

## 🎯 Objetivo
- Automatizar a extração de dados
- Eliminar processos manuais
- Garantir consistência e qualidade dos dados
- Disponibilizar base analítica para BI

---

## ▶️ Como executar o projeto

1. Navegue até a pasta `scripts`
2. Execute:

python main.py

O pipeline segue o fluxo:
Extract → Transform → Load

Executado via:
python main.py

---

## 🧠 Arquitetura do Pipeline

```
Oracle (OLTP)
   ↓
SQL Extraction
   ↓
RAW Layer
   ↓
Python Transformation
   ↓
SILVER Layer
   ↓
Business Rules
   ↓
GOLD Layer
   ↓
Power BI
```

---

## 🏗️ Estrutura do Projeto

```
rotatividade_kits/
│
├── scripts
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── sql
│   └── exemplo_query.sql
│
├── data_sample
│   └── exemplo.csv
```

---

## ⚙️ Tecnologias Utilizadas
- Python (pandas)
- SQL
- Oracle
- Power BI
- Windows Task Scheduler
- Gateway Power BI

---

## 🔄 Etapas do Pipeline

### 1. Extract
Responsável por:
- Leitura de query SQL
- Simulação de execução em banco relacional
- Geração de dados para processamento

Script: `extract_kits.py`

---

### 2. Transform
Responsável por:
- Padronização de colunas
- Tratamento de datas
- Conversão de tipos
- Padronização textual

Script: `transform_kits.py`

---

### 3. Load
Responsável por:
- Aplicação de regras de negócio
- Geração da camada GOLD
- Disponibilização para consumo analítico

Script: `load_kits.py`

---

## 📊 Regras de Negócio (Resumo)

### Etapa 1 - Pedidos
- Filtro de natureza fiscal conforme critérios definidos pelo negócio
- Filtro de data a partir de 01/06/2025
- Conversão de quantidade para inteiro

### Etapa 2 - Vale de Material
- Filtro por data de emissão
- Criação de coluna `descricao_kit`

### Etapa 3 - Cadastro de Kits
- Filtro de locais específicos
- Filtro de dono do kit

---

## ⚠️ Desafios Técnicos

### 1. Inconsistência de formatos de data
Solução:
- Implementação de parsing com suporte a múltiplos formatos

### 2. Duplicidade de registros
Solução:
- Revisão de chaves de relacionamento nos JOINs

### 3. Inconsistência na origem de dados
Solução:
- Ajuste da fonte para tabela mais confiável

---

## 🤖 Automação

O pipeline foi automatizado utilizando:
- Executável Python (.exe)
- Windows Task Scheduler
- Integração com Power BI via gateway para atualização automática dos dados

Fluxo:

```
Agendador Windows
   ↓
Execução do pipeline
   ↓
Atualização dos arquivos
   ↓
Power BI (Gateway)
   ↓
Atualização dos dashboards
```

---

## 📈 Resultado

- Pipeline automatizado
- Redução de processos manuais
- Base padronizada para análise
- Integração com Power BI

---

## 💡 Considerações

Este projeto demonstra a implementação de um pipeline de dados em ambiente próximo ao corporativo, com separação de camadas, aplicação de regras de negócio e automação do fluxo de dados.

---

## ⚠️ Observação

Este projeto é uma versão adaptada para portfólio.
Não contém dados reais ou informações sensíveis.

---

## 👩‍💻 Autora
Izabella
Cientista de Dados

