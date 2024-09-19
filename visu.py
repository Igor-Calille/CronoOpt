import json
import pandas as pd

# Supondo que o JSON esteja em um arquivo chamado 'horario.json'
with open('test.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Converter para DataFrame
df = pd.DataFrame(data['schedule'])

# Exibir as primeiras linhas
print(df)
