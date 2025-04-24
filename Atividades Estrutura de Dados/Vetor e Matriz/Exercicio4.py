# Programa que calcula a soma das linhas de uma matriz 3x3

# Criando a matriz 3x3 com números decimais simples
matriz = [
    [1.5, 2.3, 3.7],
    [4.2, 5.0, 6.8],
    [7.1, 8.4, 9.2]
]

print("Matriz 3x3:")
for linha in matriz:
    print(linha)

# Calculando as somas
soma_linha1 = matriz[0][0] + matriz[0][1] + matriz[0][2]
soma_linha2 = matriz[1][0] + matriz[1][1] + matriz[1][2]
soma_linha3 = matriz[2][0] + matriz[2][1] + matriz[2][2]

# Mostrando os resultados
print("\nSomas das linhas:")
print(f"Linha 1: {matriz[0]} = {soma_linha1}")
print(f"Linha 2: {matriz[1]} = {soma_linha2}")
print(f"Linha 3: {matriz[2]} = {soma_linha3}")