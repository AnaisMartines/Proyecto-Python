def calcular_pi(n):
    suma = 0
    for k in range(1, n + 1):
        suma += ((-1) ** (k + 1)) / (2 * k - 1)
    return 4 * suma

# Calcular π para n=200
n = 200
pi_value = calcular_pi(n)
print(pi_value)  # Resultado: ~3.14
