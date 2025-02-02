def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:n]

# Calcular la sucesión de Fibonacci para n=5
n = 5
fibonacci_sequence = fibonacci(n)
print(fibonacci_sequence)  # Resultado: [0, 1, 1, 2, 3]
