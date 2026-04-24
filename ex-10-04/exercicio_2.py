import pandas as pd
import numpy as np
from scipy import stats

vendas = [1200, 1350, 1250, 1300, 13500, 1280]
df = pd.DataFrame(vendas, columns=['vendas'])

# Adiciona coluna z_score
df['z_score'] = stats.zscore(df['vendas'])

# Filtra dados limpos (Z-Score absoluto entre -3 e 3)
df_limpo = df[(df['z_score'] > -3) & (df['z_score'] < 3)]
print(df_limpo)