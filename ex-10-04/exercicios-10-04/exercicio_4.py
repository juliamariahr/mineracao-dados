import numpy as np
from scipy import stats

medidas = [10, 12, 11, 10, 10000]
z_scores = stats.zscore(medidas)
media = np.mean(medidas)
desvio = np.std(medidas)

print(f"Z-Score do 10000: {z_scores[-1]:.2f}") # Não ultrapassa 3
print(f"Média: {media}")
print(f"Desvio Padrão: {desvio}")
# O desvio padrão ficou tão alto (3995) devido ao 10000 que a distância do 
# valor para a média não atinge 3 sigmas.