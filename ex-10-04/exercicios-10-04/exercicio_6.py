import numpy as np
from sklearn.ensemble import IsolationForest

# Dados sintéticos
X = np.random.normal(size=(1000, 2))
outliers = np.random.uniform(low=-10, high=10, size=(50, 2))
X = np.r_[X, outliers]

for cont in [0.05, 0.20]:
    iso = IsolationForest(contamination=cont, random_state=0)
    preds = iso.fit_predict(X)
    print(f"Contamination {cont}: {list(preds).count(-1)} anomalias detectadas.")