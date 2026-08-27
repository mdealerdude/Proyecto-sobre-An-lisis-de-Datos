import pandas as pd

file_path = "online_retail.csv"

data = pd.read_csv(file_path)
# print(data)
# Obtengo información rápida de las columnas
print(data.info())
print("-----------")
#
print(data.head())  # me da los 5 primeros datos
# Estadistica básica
print(data.describe())

# Preguntar por cuales son los valores nulos y sumarlos

print("Valores nulos:\n", data.isnull().sum())

# Calcular la suma de los valores duplicados
print("----------")
print("Valores duplicados: ", data.duplicated().sum())

# Encontrando los valores unicos para cada columna
print("-----------------------")
unique_values = {col: data[col].unique() for col in data.columns}

for col, values in unique_values.items():
    print(f"Columna: {col}")
    print(f"Número de valores únicos: {len(values)}")
    print(f"Valores únicos: {values[:10]}")
    print("-" * 50)
