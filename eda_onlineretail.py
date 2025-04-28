import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('C:/Users/user/Documents/OnlineRetail.csv', encoding='ISO-8859-1')

# Data Cleaning
df = df.dropna(subset=['CustomerID', 'Description'])
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Plot 1: Histogram Quantity (semua data)
plt.figure(figsize=(8,5))
sns.histplot(df['Quantity'], bins=50, kde=True)
plt.title('Distribusi Quantity - Semua Data')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.savefig('histogram_quantity_all.png')
plt.close()

# Plot 2: Histogram Quantity (<500 saja)
plt.figure(figsize=(8,5))
sns.histplot(df[df['Quantity'] < 500]['Quantity'], bins=50, kde=True)
plt.title('Distribusi Quantity - Quantity <500')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.savefig('histogram_quantity_filtered.png')
plt.close()

# Plot 3: Boxplot Unit Price
plt.figure(figsize=(8,5))
sns.boxplot(x=df['UnitPrice'])
plt.title('Boxplot Unit Price')
plt.xlabel('Unit Price')
plt.savefig('boxplot_unitprice.png')
plt.close()

# Plot 4: Scatter Plot Quantity vs UnitPrice
plt.figure(figsize=(8,5))
sns.scatterplot(x='Quantity', y='UnitPrice', data=df)
plt.title('Scatter Plot Quantity vs Unit Price')
plt.xlabel('Quantity')
plt.ylabel('Unit Price')
plt.xlim(0, 1000)
plt.ylim(0, 1000)
plt.savefig('scatter_quantity_unitprice.png')
plt.close()

# Plot 5: Heatmap Korelasi
plt.figure(figsize=(6,4))
corr = df[['Quantity', 'UnitPrice', 'TotalPrice']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Korelasi Quantity, UnitPrice, TotalPrice')
plt.savefig('heatmap_correlation.png')
plt.close()
