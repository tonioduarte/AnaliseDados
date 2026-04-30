import pandas as pd

base = pd.read_csv('train.csv')
# print(base.head(3))
# print(base.shape)
# print(base.info)

# Verificando a quantidade de valores nulos
# print(base.isnull().sum())


# Mostrando os 20 campos com mais valores nulos
# print(base.isnull().sum().sort_values(ascending=False).head(20))

# Mostrando os 20 campos com mais valores nulos em porcentagem
# print((base.isnull().sum()/base.shape[0]).sort_values(ascending=False).head(19))

eliminar = base.columns[(base.isnull().sum()/base.shape[0]) > 0.1]
base = base.drop(eliminar, axis=1)

# print(base.dtypes)
# Selecionando as colunas numéricas
colunas = base.columns[base.dtypes != 'object']

# Criar uma base nova com esses valores

base2 = base.loc[:, colunas]

# Verificando os valores nulos
# print(base2.isnull().sum().sort_values(ascending=False).head(20))

# Substituindo os valores nulos por -1
base2 = base2.fillna(-1)