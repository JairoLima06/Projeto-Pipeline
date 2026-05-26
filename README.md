# Pipeline de Dados de Vendas

## Sobre o Projeto

Este projeto tem como objetivo desenvolver um pipeline de dados completo utilizando ferramentas amplamente utilizadas no mercado de tecnologia e análise de dados.

O pipeline realiza:
- Extração de dados;
- Tratamento e limpeza;
- Armazenamento em banco de dados;
- Análise de dados;
- Visualização de informações estratégicas.

O projeto foi desenvolvido como prática de:
- Engenharia de Dados;
- ETL;
- SQL;
- Python;
- Power BI;
- Análise de Dados.

---

# Tecnologias Utilizadas

## Linguagens
- Python
- SQL

## Bibliotecas Python
- Pandas
- SQLAlchemy
- PyMySQL

## Ferramentas
- VS Code
- MySQL
- MySQL Workbench
- Power BI
- Git/GitHub

---

# Estrutura do Projeto

```bash
pipeline-vendas/
│
├── data/
│   ├── vendas.csv
│   └── vendas_tratadas.csv
│
├── scripts/
│   └── etl.py
│
├── sql/
│
├── dashboard/
│
├── README.md
│
└── requirements.txt
```

```bash
# Fluxo do Pipeline

Fonte de Dados (CSV)
        ↓
Extração com Python
        ↓
Limpeza e Tratamento dos Dados
        ↓
Armazenamento no MySQL
        ↓
Análise e Dashboard no Power BI
