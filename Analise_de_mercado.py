import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv('Superstore.csv', encoding='latin1')  # Ajuste o caminho do arquivo


# Verificar estrutura dos dados
print(df.head())
print(df.info())

# Tratar dados faltantes (se houver)
df.dropna(inplace=True)

# Converter coluna de data para formato adequado
df['Order Date'] = pd.to_datetime(df['Order Date'])


vendas_por_categoria = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

# Gráfico de barras
plt.figure(figsize=(10, 6))
vendas_por_categoria.plot(kind='bar', color='skyblue')
plt.title('Vendas por Categoria de Produto')
plt.xlabel('Categoria')
plt.ylabel('Vendas (US$)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
plt.show()


lucro_por_subcategoria = df.groupby('Sub-Category')['Profit'].sum().sort_values()

# Gráfico horizontal
plt.figure(figsize=(12, 8))
lucro_por_subcategoria.plot(kind='barh', color='#4CAF50')
plt.title('Lucro por Subcategoria')
plt.xlabel('Lucro (US$)')
plt.ylabel('Subcategoria')
plt.grid(axis='x', linestyle='--')
plt.show()


vendas_mensais = df.resample('M', on='Order Date')['Sales'].sum()

plt.figure(figsize=(12, 6))
vendas_mensais.plot(kind='line', marker='o', color='purple')
plt.title('Vendas Mensais (2015-2018)')
plt.xlabel('Data')
plt.ylabel('Vendas (US$)')
plt.grid(True)
plt.show()


vendas_por_estado = df.groupby('State')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(14, 8))
vendas_por_estado.plot(kind='bar', color='orange')
plt.title('Vendas por Estado')
plt.xlabel('Estado')
plt.ylabel('Vendas (US$)')
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--')
plt.show()