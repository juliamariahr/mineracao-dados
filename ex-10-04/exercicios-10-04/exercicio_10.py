# Explicação: Sem normalizar, a diferença de 10 reais no saldo é numericamente desprezível perto de 1 milhão, enquanto a diferença de risco (0.1 para 0.9) é enorme proporcionalmente, mas numericamente pequena (apenas 0.8). A IA focaria no saldo e diria que são iguais.

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.DataFrame({'Saldo': [1000000, 1000010], 'Risco': [0.1, 0.9]})
scaler = MinMaxScaler()
print(scaler.fit_transform(df))
# Agora o Risco varia de 0 a 1, e o Saldo também, mostrando a real diferença.