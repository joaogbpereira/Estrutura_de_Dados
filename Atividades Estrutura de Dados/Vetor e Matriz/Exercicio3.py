# Vetor com 10 números positivos
vetor = [5, 8, 12, 3, 7, 9, 11, 4, 6, 10]

# Mostrando o vetor
print("Vetor:", vetor)

# Pedindo o número para buscar
numero = int(input("Digite um número para buscar: "))

# Procurando o número
achou = False
for i in range(10):
    if vetor[i] == numero:
        print(f"O número {numero} está na posição {i}")
        achou = True
        break

if not achou:
    print(f"O número {numero} não está no vetor")