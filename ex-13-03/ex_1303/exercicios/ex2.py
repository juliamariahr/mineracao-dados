import numpy as np

# Vetor de tempos de processamento
tempos = [12, 15, 14, 13, 16, 12, 14, 150, 13, 15]

# Percentis calculados no exercício 1
q1 = np.percentile(tempos, 25)
q3 = np.percentile(tempos, 75)

# IQR
iqr = q3 - q1

# Limites
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

print(f"Q1 (25%): {q1}")
print(f"Q3 (75%): {q3}")
print(f"IQR: {iqr}")
print(f"Limite Inferior: {limite_inferior}")
print(f"Limite Superior: {limite_superior}")
