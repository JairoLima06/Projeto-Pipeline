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
# Fluxo do Pipeline

<p align="center">
  <img src="https://github.com/JairoLima06/Projeto-Pipeline/blob/main/image/Fluxo%20do%20Pipeline.png" alt="Descrição da imagem">
</p>


# Extração dos Dados

Os dados utilizados no projeto foram importados a partir de um arquivo CSV contendo informações de vendas.

Exemplo de informações:
```bash
Produtos;
Vendedores;
Regiões;
Categorias;
Métodos de pagamento;
Canais de venda;
Valores de vendas.
```

# Processo ETL

O processo ETL foi desenvolvido em Python utilizando a biblioteca Pandas.

Etapas realizadas:
```bash
Leitura do CSV;
Remoção de valores nulos;
Remoção de duplicidades;
Organização dos dados;
Exportação da base tratada;
Envio dos dados para o MySQL.
```
# Tratamento de Dados

Durante o tratamento dos dados foram realizadas:
```bash
Limpeza de inconsistências;
Padronização;
Verificação de tipos de dados;
Validação da integridade da base.
```
# Banco de Dados

O banco de dados utilizado foi o MySQL.
```bash
Banco criado:
pipeline_vendas
Tabela principal:
vendas
```
# Dashboard Power BI

O dashboard desenvolvido no Power BI apresenta indicadores importantes para análise de negócio.
<p align="center">
  <img src="https://github.com/JairoLima06/Projeto-Pipeline/blob/main/image/Dash_Vendas.PNG" alt="Descrição da imagem">
</p>

# [Confira aqui o dashboard do projeto.](https://app.powerbi.com/groups/me/reports/3bfa1bfd-c0e8-48bd-871d-d0693a7d178a/19d8cd2eee92434de4eb?language=pt-BR&experience=power-bi)


KPIs criados:
```bash
Faturamento Total;
Ticket Médio;
Quantidade Vendida;
Total de Pedidos;
Média de Desconto.
Visualizações:
Vendas por Região;
Vendas por Categoria;
Top Vendedores;
Vendas por Canal;
Evolução Temporal das Vendas;
Métodos de Pagamento.
```

# Insights Obtidos

Alguns insights identificados:
```bah
Região North apresentou maior faturamento;
Categoria Clothing teve maior volume de vendas;
O vendedor David apresentou melhor desempenho;
O canal Online apresentou forte participação nas vendas.
```

# Objetivos do Projeto

Este projeto foi desenvolvido para:
```bash
Aprimorar conhecimentos em dados;
Praticar ETL;
Desenvolver habilidades em SQL e Python;
Criar um projeto real para portfólio;
Simular um fluxo profissional de dados.
```
# Melhorias Futuras

Possíveis evoluções do projeto:
```bah
Integração com APIs;
Automação do pipeline;
Deploy em Cloud;
Uso de Apache Airflow;
Criação de Machine Learning;
Integração com AWS;
Pipeline em tempo real com Kafka.
```

# Como Executar o Projeto
```bash
1. Clone o repositório
git clone LINK_DO_REPOSITORIO
2. Instale as dependências
pip install pandas sqlalchemy pymysql
3. Execute o script ETL
python scripts/etl.py
4. Execute consultas no MySQL
USE pipeline_vendas;

SELECT * FROM vendas;
```
# Aprendizados

Com este projeto foi possível desenvolver conhecimentos em:
```bash
ETL;
Python para Dados;
SQL;
MySQL;
Power BI;
Engenharia de Dados;
Visualização de Dados;
Integração entre ferramentas.
```
# Autor
Projeto desenvolvido por Jairo Lima como prática de Engenharia e Análise de Dados.
