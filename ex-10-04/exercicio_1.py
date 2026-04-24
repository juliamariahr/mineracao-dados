import numpy as np
from scipy import stats

temp = [45.5, 46.0, 45.2, 45.8, 46.1, 98.0, 45.9, 45.3]
z_scores = stats.zscore(temp)

for t, z in zip(temp, z_scores):
    if z > 2.5:
        print(f"Anomalia detectada: {t} (Z-Score: {z:.2f})")