
valores = [100, 150, 200, 250, 300, 350]
valores_ordenados = sorted(valores)
n = len(valores_ordenados)

mid = n // 2
if n % 2 == 0:
    lower_half = valores_ordenados[:mid]
    upper_half = valores_ordenados[mid:]
else:
    lower_half = valores_ordenados[:mid]
    upper_half = valores_ordenados[mid+1:]

mid_lower = len(lower_half) // 2
if len(lower_half) % 2 == 0:
    q1 = (lower_half[mid_lower - 1] + lower_half[mid_lower]) / 2
else:
    q1 = lower_half[mid_lower]

mid_upper = len(upper_half) // 2
if len(upper_half) % 2 == 0:
    q3 = (upper_half[mid_upper - 1] + upper_half[mid_upper]) / 2
else:
    q3 = upper_half[mid_upper]

print(f"Q1: {q1}")
print(f"Q3: {q3}")
