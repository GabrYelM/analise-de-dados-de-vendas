import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
dados = pd.read_csv('Superstore.csv', encoding='latin1')


# Verificar estrutura dos dados
print(dados.head())
print(dados.info())

# Tratar dados faltantes (se houver)
dados.dropna(inplace=True)

# Converter coluna de data para formato adequado
dados['Order Date'] = pd.to_datetime(dados['Order Date'])


# Gráfico de Vendas por categoria
vendas_por_cat = dados.groupby('Category')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
vendas_por_cat.plot(kind='bar', color='skyblue')
plt.title('Vendas por Categoria de Produto')
plt.xlabel('Categoria')
plt.ylabel('Vendas (US$)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
plt.show()


# Gráfico de Lucro por subcategoria
lucro_por_subcat = dados.groupby('Sub-Category')['Profit'].sum().sort_values()

plt.figure(figsize=(12, 8))
lucro_por_subcat.plot(kind='barh', color='#4CAF50')
plt.title('Lucro por Subcategoria')
plt.xlabel('Lucro (US$)')
plt.ylabel('Subcategoria')
plt.grid(axis='x', linestyle='--')
plt.show()


# Gráfico de Vendas mensais
vendas_mensais = dados.resample('M', on='Order Date')['Sales'].sum()

plt.figure(figsize=(12, 6))
vendas_mensais.plot(kind='line', marker='o', color='purple')
plt.title('Vendas Mensais (2015-2018)')
plt.xlabel('Data')
plt.ylabel('Vendas (US$)')
plt.grid(True)
plt.show()


#Gráfico de Vendas por estado
vendas_por_estado = dados.groupby('State')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(14, 8))
vendas_por_estado.plot(kind='bar', color='orange')
plt.title('Vendas por Estado')
plt.xlabel('Estado')
plt.ylabel('Vendas (US$)')
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--')
plt.show()
