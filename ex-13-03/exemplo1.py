import statistics

tempos = [20, 25, 30, 35, 40, 45, 90]

q2 = statistics.median(tempos)

inferior = tempos[:3]
superior = tempos[4:]

q1 = statistics.median(inferior)
q3 = statistics.median(superior)

iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

print(f"Inferior = {inferior}")
print(f"Superior = {superior}")
print(f"Q1 = {q1}")
print(f"Q2 = {q2}")
print(f"Q3 = {q3}")
print(f"IQR = {iqr}")
print(f"Limite Inferior = {limite_inferior}")
print(f"Limite Superior = {limite_superior}")

# 1 - Verificar se no conjunto existe algum outlier (< -5 ou > 75)
# Exemplo_01_1
outliers_1 = [x for x in tempos if x < -5 or x > 75]
print("Outliers (< -5 ou > 75):", outliers_1)

# 2 - Alterar a verificação do conjunto para tornar genérico (para qualquer tamanho)
# Exemplo_01_2
outliers_2 = [x for x in tempos if x < limite_inferior or x > limite_superior]
print("Outliers (genérico pelo IQR):", outliers_2)
