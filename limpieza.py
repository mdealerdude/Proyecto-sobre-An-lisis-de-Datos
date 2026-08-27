import pandas as pd

file_path = "online_retail.csv"

data = pd.read_csv(file_path)

data_cleaned = data.drop_duplicates()
data_cleaned = data_cleaned.dropna(subset=["CustomerID"])
#Valores duplicados antes de limpiarlos
print("Valores duplicados: ", data.duplicated().sum())
#Data limpiada
print("Valores duplicados de data limpiado: ", data_cleaned.duplicated().sum())
print(data_cleaned.head())