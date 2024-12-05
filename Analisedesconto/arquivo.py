import pandas as pd

# Carregar os dados
planilha = pd.read_csv("/home/ianlee/Área de Trabalho/Analisedesconto/amazon.csv")



# Remover o símbolo ₹ e converter para numérico
planilha['actual_price'] = planilha['actual_price'].replace({'₹': '', ',': ''}, regex=True).astype(float)
planilha['discounted_price'] = planilha['discounted_price'].replace({'₹': '', ',': ''}, regex=True).astype(float)

# Verificar valores ausentes (NaN)
print(planilha[['actual_price', 'discounted_price']].isna().sum())

# Substituir valores NaN pela média (evitar FutureWarning)
planilha['actual_price'] = planilha['actual_price'].fillna(planilha['actual_price'].mean())
planilha['discounted_price'] = planilha['discounted_price'].fillna(planilha['discounted_price'].mean())

# Calcular o desconto
planilha['discount'] = planilha['actual_price'] - planilha['discounted_price']

# Exibir as primeiras linhas para verificar os resultados
print(planilha[['product_name', 'actual_price', 'discounted_price', 'discount']].head())

import matplotlib.pyplot as plt

# Criar gráfico de dispersão para mostrar o preço original e o preço com desconto
plt.figure(figsize=(10, 6))
plt.scatter(planilha['actual_price'], planilha['discounted_price'], alpha=0.6, color='blue')

# Adicionar rótulos e título
plt.title('Preço Real vs. Preço com Desconto', fontsize=14)
plt.xlabel('Preço Real (actual_price)', fontsize=12)
plt.ylabel('Preço com Desconto (discounted_price)', fontsize=12)

# Mostrar o gráfico
plt.tight_layout()
plt.show()

