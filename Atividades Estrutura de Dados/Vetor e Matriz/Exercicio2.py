# Criando a matriz com as letras pedidas
matriz = [
    ['a', 'b', 'c', 'd'],
    ['e', 'f', 'g', 'h'],
    ['i', 'j', 'k', 'l'],
    ['m', 'n', 'o', 'p']
]

# Mostrando a matriz
print("Matriz de letras:")
for linha in range(4):
    for coluna in range(4):
        print(matriz[linha][coluna], end=' ')
    print()  # Pula linha após cada linha da matriz