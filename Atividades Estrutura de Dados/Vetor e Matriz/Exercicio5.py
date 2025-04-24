# Programa que encontra o maior número em uma matriz 5x5

# Matriz fixa com números positivos e negativos (fácil de entender)
matriz = [
    [12, -5, 8, 0, 20],
    [-3, 15, 7, -10, 4],
    [6, -8, 19, 2, 11],
    [9, 1, -4, 17, 3],
    [-7, 14, 5, -2, 10]
]

print("Matriz 5x5:")
for linha in matriz:
    print(linha)

# Encontrando o maior número
maior = matriz[0][0]  # Começa com o primeiro número

# Verifica cada número da matriz
for linha in matriz:
    for numero in linha:
        if numero > maior:
            maior = numero

print(f"\nO maior elemento da matriz é: {maior}")