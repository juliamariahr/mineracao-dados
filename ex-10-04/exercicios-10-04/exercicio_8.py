import pandas as pd
from sklearn.ensemble import IsolationForest

data = {
    'idade': [20, 22, 21, 23, 19, 150],
    'estudo': [10, 12, 11, 15, 8, 5],
    'nota': [8, 7, 9, 8, 6, 2]
}
df = pd.DataFrame(data)

iso = IsolationForest(random_state=0)
df['Outlier'] = iso.fit_predict(df)

# Filtra apenas a anomalia
print(df[df['Outlier'] == -1])