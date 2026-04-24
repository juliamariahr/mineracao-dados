from sklearn.preprocessing import MinMaxScaler
import numpy as np

temps = np.array([[-20], [-10], [0], [20]])
scaler = MinMaxScaler()
res = scaler.fit_transform(temps)
print(res)

# O 0°C virou 0.5. O novo valor 0.0 representa o antigo -20°C (o valor mínimo).
# O zero mudou porque a escala agora é relativa ao intervalo dos dados.