import numpy as np
from scipy import stats
from sklearn.preprocessing import MinMaxScaler

producao = np.array([100, 102, 98, 105, 500, 101])
z_scores = np.abs(stats.zscore(producao))

# 1. Remover outlier (500)
dados_limpos = producao[z_scores < 2].reshape(-1, 1)

# 2. Normalizar
scaler = MinMaxScaler()
final = scaler.fit_transform(dados_limpos)
print(final)

# 3. Explicação: É melhor normalizar depois. Se o 500 estivesse lá, ele seria o 1.0 e todos os outros valores (98-105) ficariam "esmagados" próximos de 0.2, fazendo com que variações importantes entre eles desaparecessem na escala.