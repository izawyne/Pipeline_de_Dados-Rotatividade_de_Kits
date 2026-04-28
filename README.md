# Pipeline de Dados - Rotatividade de Kits

## 📌 Descrição
Este projeto consiste na construção de um pipeline de dados completo para extração, transformação e disponibilização de dados para análise de rotatividade de kits.

O pipeline foi estruturado com foco em automação, padronização e rastreabilidade dos dados, permitindo o consumo confiável via Power BI.

---

## 🎯 Objetivo
- Automatizar a extração de dados
- Eliminar processos manuais
- Garantir consistência e qualidade dos dados
- Disponibilizar base analítica para BI

---

## 🧠 Arquitetura do Pipeline

```
Oracle (OLTP)
   ↓
Extração via SQL
   ↓
RAW Layer
   ↓
Transformação (Python)
   ↓
SILVER Layer
   ↓
Regras de Negócio
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
├── 01_sql
│   └── raw/
│
├── 02_scripts_python
│   ├── extract_kits.py
│   ├── transform_kits.py
│   ├── load_kits.py
│   └── main.py
│
├── 03_dados
│   ├── raw
│   ├── staging
│   └── gold
│
├── 04_logs
│
└── 05_powerbi
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
- Conectar ao banco Oracle
- Executar queries SQL
- Gerar arquivos na camada RAW (CSV e Parquet)

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

## ⚠️ Observação

Este projeto é uma versão adaptada para portfólio.
Não contém dados reais ou informações sensíveis.

---

## 👩‍💻 Autora
Izabella
Cientista de Dados

