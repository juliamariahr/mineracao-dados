from sklearn.ensemble import IsolationForest

# [Nota, Faltas]
dados = [[8, 2], [7, 4], [9, 1], [8, 3], [2, 25], [9, 25]]
modelo = IsolationForest(contamination=0.3, random_state=0)
preds = modelo.fit_predict(dados)

for d, p in zip(dados, preds):
    print(f"Aluno {d}: {'Anomalia' if p == -1 else 'Normal'}")