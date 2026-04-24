from sklearn.ensemble import IsolationForest

servidores = [[20,30], [25, 35], [22, 32], [99, 95], [21, 31]]
modelo = IsolationForest(random_state=0)
modelo.fit(servidores)
preds = modelo.predict(servidores)

print(f"Predições: {preds}")
# O valor -1 significa que o modelo identificou aquela linha como uma anomalia/outlier.