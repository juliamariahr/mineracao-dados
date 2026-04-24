# 1
# 200-100/ 500-100 = 100/400 = 0.25
# 2
from sklearn.preprocessing import MinMaxScaler
import numpy as np

pressao = np.array([[100], [200], [500]])
scaler = MinMaxScaler()
print(scaler.fit_transform(pressao)) # Resultado: [[0.], [0.25], [1.]]
