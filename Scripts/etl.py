import pandas as pd

# Serve para Ler o arquivo CSV
df = pd.read_csv("data/sales_data.csv")

# Serve para mostrar as primeiras linhas
print(df.head())

##########################################

# Remover linhas vazias
df.dropna(inplace=True)

# Remover duplicados
df.drop_duplicates(inplace=True)

print(df.info())

#Conexão com o MySQL

from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:Jairo.20@localhost/pipeline_vendas"
)

#Enviar dados para o banco

df.to_sql(
    "vendas",
    engine,
    if_exists="replace",
    index=False
)


#Exportar a tabela tratada
df.to_csv("vendas_tratadas.csv", index=False)