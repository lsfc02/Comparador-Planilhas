import pandas as pd

# Carregar as planilhas
base_inicial = pd.read_csv("BaseInicial.csv", sep=';', encoding="ISO-8859-1")
base_atualizada = pd.read_csv("BaseCompleta.csv", sep=';', encoding="ISO-8859-1")

# Verificar os nomes das colunas
print("Colunas na base inicial:")
print(base_inicial.columns)
print("\nColunas na base atualizada:")
print(base_atualizada.columns)

# Renomear as colunas
base_inicial.rename(columns={'N£mero': 'Número'}, inplace=True)
base_atualizada.rename(columns={'N£mero': 'Número'}, inplace=True)

# Definir o índice para as colunas 'DDD' e 'Número'
base_inicial.set_index(['DDD', 'Número'], inplace=True)
base_atualizada.set_index(['DDD', 'Número'], inplace=True)

# Encontrar números faltantes
faltantes = base_atualizada.index.difference(base_inicial.index)

# Mostrar os números faltantes
print(f"\nNúmeros + DDDs faltando na Base Inicial:\n{faltantes.to_series().to_string(index=False)}")
