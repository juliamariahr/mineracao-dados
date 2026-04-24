import pandas as pd

def calcular_rfm(df, data_referencia):
    # Agrupa por cliente e calcula as métricas RFM 
    rfm = df.groupby('id_cliente').agg({
        'data': lambda x: (data_referencia - x.max()).days, # Recência
        'id_cliente': 'count',                             # Frequência
        'valor': 'sum'                                     # Valor Monetário
    }).rename(columns={'data': 'Recencia', 'id_cliente': 'Frequencia', 'valor': 'Valor_Monetario'})
    return rfm

# Exemplo de uso
transacoes = pd.DataFrame({
    'id_cliente': [1, 2, 1, 3],
    'data': pd.to_datetime(['2026-04-01', '2026-04-10', '2026-04-15', '2026-04-16']),
    'valor': [100, 200, 150, 50]
})
print(calcular_rfm(transacoes, pd.to_datetime('2026-04-17')))