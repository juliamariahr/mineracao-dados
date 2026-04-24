def calcular_metricas_sensor(leitura_t1, leitura_t2):
    # Calcula o Delta (variação bruta)
    delta = leitura_t2 - leitura_t1
    
    # Calcula a Evolução Percentual
    evolucao_pct = (delta / leitura_t1) * 100
    
    # Sinaliza se a tendência é de crescimento (1) ou queda (0)
    tendencia = 1 if delta > 0 else 0
    
    print(f"Leitura Inicial: {leitura_t1} | Leitura Atual: {leitura_t2}")
    print(f"Delta: {delta} | Evolução: {evolucao_pct:.2f}% | Crescimento: {bool(tendencia)}")

# Teste do script
calcular_metricas_sensor(150, 185)