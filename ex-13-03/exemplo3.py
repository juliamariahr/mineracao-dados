import numpy as np

tempos = [20, 25, 30, 35, 40, 45, 90]

q1 = np.percentile(tempos, 25)
q2 = np.percentile(tempos, 50)
q3 = np.percentile(tempos, 75)

print(f"Q1 = {q1}")
print(f"Q2 = {q2}")
print(f"Q3 = {q3}")

iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

print(f"IQR = {iqr}")
print(f"Limite Inferior = {limite_inferior}")
print(f"Limite Superior = {limite_superior}")


definir_outliers = [x for x in tempos if x < limite_inferior or x > limite_superior]
print(f"Outliers (pelo IQR): {definir_outliers}")


