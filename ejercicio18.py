def generar_fibonacci(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        siguiente = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(siguiente)
    return fibonacci

print(generar_fibonacci(10))
