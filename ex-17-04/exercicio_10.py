import pandas as pd

def analisar_aceleracao_sensor(leituras):
    # Criando o DataFrame com as leituras do sensor
    df = pd.DataFrame(leituras, columns=['leitura'])
    
    # 1. Calcula a primeira diferença (Velocidade/Delta) 
    df['delta'] = df['leitura'].diff()
    
    # 2. Calcula a diferença entre os deltas (Aceleração/Delta do Delta) 
    df['aceleracao'] = df['delta'].diff()
    
    # 3. Dispara alerta binário (1) se a aceleração for positiva 
    # Isso indica que o ritmo de crescimento está aumentando (tendência exponencial)
    df['alerta_exponencial'] = (df['aceleracao'] > 0).astype(int)
    
    return df

# Exemplo com 5 leituras para observar a evolução dos cálculos
# Note que o crescimento entre os números está aumentando: +5, +10, +15, +25
dados_sensor = [100, 105, 115, 130, 155]

df_resultado = analisar_aceleracao_sensor(dados_sensor)
print(df_resultado)