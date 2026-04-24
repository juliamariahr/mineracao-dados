import pandas as pd

def fatiar_turnos_log(lista_horarios):
    # Criando o DataFrame com a coluna de horas (00h às 23h) 
    df = pd.DataFrame(lista_horarios, columns=['hora'])
    
    # Definindo os limites dos blocos (bins) e seus respectivos nomes 
    # 00h às 05h59 -> Madrugada
    # 06h às 17h59 -> Comercial
    # 18h às 23h59 -> Noite
    limites = [0, 6, 18, 24]
    nomes_turnos = ['Madrugada', 'Comercial', 'Noite']
    
    # Aplicando o fatiamento (binning)
    # right=False garante que o limite superior não seja incluído no bloco atual (ex: 18h cai em 'Noite')
    df['turno'] = pd.cut(df['hora'], bins=limites, labels=nomes_turnos, right=False)
    
    return df

# Exemplo de horários extraídos de um log
horarios_log = [2, 7, 10, 15, 19, 23]

df_resultado = fatiar_turnos_log(horarios_log)
print(df_resultado)