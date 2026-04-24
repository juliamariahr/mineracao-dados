import pandas as pd
import numpy as np

def tratar_nulos_com_indicador(dados):
    # Criando o DataFrame com os dados iniciais
    df = pd.DataFrame(dados, columns=['leitura_sensor'])
    
    # 1. Criar o Indicador de Omissão (Flag de erro)
    # Esta coluna preserva a informação de falha antes de qualquer alteração 
    df['omissao_flag'] = df['leitura_sensor'].isna().astype(int)
    
    # 2. Preencher a lacuna original apenas após criar a flag 
    # Aqui utilizamos a mediana para não distorcer a distribuição dos dados
    mediana = df['leitura_sensor'].median()
    df['leitura_sensor'] = df['leitura_sensor'].fillna(mediana)
    
    return df

# Exemplo de dados com falhas de leitura (NaN)
dados_exemplo = [10.2, np.nan, 10.5, 11.0, np.nan, 10.8]

df_resultado = tratar_nulos_com_indicador(dados_exemplo)
print(df_resultado)